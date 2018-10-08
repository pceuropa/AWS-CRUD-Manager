"""
Summary

Description: Class contains method neccesairy to manage EC2 instances
File: ec2.py
Author: Rafal Marguzewicz (PGS Software)
Email: rmarguzewicz@pgs-soft.com
Github:
"""

import boto3
from helpers.color import yel, alert, red, gre
from helpers.date import difference
from aws import Aws, log
from ec2.summary import summary


class Ec2(Aws):

    """ List method:
        all - list instances with possibly filters and can stop or terminate instances
        clean - imporve rule : all instance without tag owner - terminate, running without tag stop - stop
            0 : pending
            16 : running
            32 : shutting-down
            48 : terminated
            64 : stopping
            80 : stopped
    """

    def __init__(self, params={}):
        """TODO: to be defined1. """
        super().__init__(params)

    def migrate(self):
        self.create(self)

    def create(self) -> boto3:
        """Print all instances
        :returns: list
        """
        print(self.params.region_name)
        ec2 = boto3.resource('ec2', region_name=self.regions[0])

        return ec2.create_instances(
            ImageId='ami-0c5199d385b432989',
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                    {
                        'ResourceType': 'instance',
                        'Tags': [
                            {'Key': 'owner', 'Value': 'rmarguzewicz'},
                            {'Key': 'name', 'Value': 'rmarguzewicz'},
                        ]
                    },
            ]
        )

    def all(self) -> None:
        """Print all instances, can terminate all instance withou tag "owner"
            instance keys:
                .id,
                .instance_type
                .state
                .tags
        :returns: list
        """

        if self.params.ebs:
            self.ebs()
        elif self.params.autoscaling:
            self.autoscaling()
        else:
            self.instances()

    def instances(self) -> None:
        for region in self.regions:
            ec2 = boto3.resource('ec2', region_name=region)
            instances = [instance for instance in ec2.instances.filter(Filters=self.filters)]

            if len(instances):
                print(yel(region))
                for i in instances:
                    subnet = i.subnet

                    if self.params.terminate and not self.have_tag_owner(i.tags) and i.state['Code'] != 48:
                        i.terminate()

                    try:
                        state_name = self.state_name(i)
                        print(f"{i.id} {i.instance_type} {state_name}{'':5} {alert(self.have_tag_owner(i.tags)):25} {i.launch_time:%Y-%m-%d} {subnet.vpc_id} {subnet.id}")
                    except Exception as e:
                        print(f"{i.id} {i.instance_type} {state_name} {'':3}{alert(self.have_tag_owner(i.tags)):25}")

    def ebs(self) -> None:

        for region in self.regions:
            ec2 = boto3.resource('ec2', region_name=region)
            volumes = [v for v in ec2.volumes.filter(Filters=self.filters)]  # if you want to list out only attached volumes

            if volumes:
                print(yel(region))
                for v in volumes:

                    if self.params.delete and not self.have_tag_owner(v.tags):
                        v.delete()

                    print(f"{v.id} {v.size} {v.state} {alert(self.have_tag_owner(v.tags))}")

    def autoscaling(self) -> None:
        """Print all autoscaling group in all regions
        :returns: list
        """
        for region in self.regions:
            client = boto3.client('autoscaling', region_name=region)
            groups = client.describe_auto_scaling_groups()

            autoscaling = groups['AutoScalingGroups']
            if autoscaling:
                print(yel(region))

                for group in autoscaling:
                    groupname = group['AutoScalingGroupName']
                    print(f"{group['MinSize']}/{red(group['MaxSize'], group['MaxSize'])} {gre(groupname)} {group['LoadBalancerNames']} {group['AvailabilityZones']} {group['Tags']}")

                    stop = self.have_tag(group['Tags'], 'stop')

                    if self.params.delete and not self.have_tag(group['Tags'], 'owner'):
                        log.info(f"Terminate {groupname}")
                        response = client.delete_auto_scaling_group(
                            AutoScalingGroupName=groupname,
                            ForceDelete=True
                        )
                        print(response)

                    if not stop:
                        pass

    def state_name(self, i):
        state = i.state['Name']

        if i.state['Code'] == 16:  # not terminated
            state = yel(state)

        if i.state['Code'] != 48:  # not terminated
            state += str(difference(i.launch_time))

        return state

    def find(self) -> str:
        instance = self.get_instance()
        self._action(instance)
        return summary(instance, self.params.region_name)

    def _action(self, instance) -> None:

        if self.params.terminate:
            instance.terminate()

        if self.params.start:
            instance.start()

        if self.params.stop:
            instance.stop()

    def get_instance(self) -> boto3:
        """Get instace by id
        :id: str id of instance (i-04922d66b1a9111f5)
        :returns: ec2.Instance(i-xx)
        """
        if self.params.id:
            ec2 = boto3.resource('ec2', region_name=self.params.region_name)
            return ec2.Instance(self.params.id)

    def clean(self) -> None:
        """TODO
        """
        log.info('stopping ec2 instances')

        for reg in self.regions:
            ec2 = boto3.resource('ec2', region_name=reg)
            instances = [instance for instance in ec2.instances.filter(Filters=[self.f['running']])]

            if len(instances):
                print(reg)
                for instance in instances:

                    if not self.have_tag_owner(instance.tags):
                        instance.terminate()
                        log.info(f"terminate {instance.id}")
                        continue

                    if not self.have_tag_stop(instance.tags):
                        try:
                            instance.stop()
                            log.info(f"stop {instance.id}")
                        except Exception as e:
                            print(e)
