"""
File: migrate.py
Author: Rafal Marguzewicz (PGS Software)
Email: rmarguzewicz@pgs-soft.com
Github:
Description: God to AWS
"""

import boto3
from aws import Aws
from uuid import uuid1


class Migrate(Aws):

    uuid = 'z' + str(uuid1())[:8]

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

    def all(self):
        self.ec2()
        self.rds()
        self.elb()
        self.auto_scaling_group()
        self.ebs()

    def client(self, client_name):
        return boto3.client(client_name, region_name=self.region_name)

    def availability_zones(self) -> list:
        client = self.client('ec2')
        response = client.describe_availability_zones()
        return [i['ZoneName'] for i in response['AvailabilityZones']]

    def ec2(self) -> boto3:
        """Print all instances
        :returns: list
        """
        print(self.params.region_name)
        ec2 = boto3.resource('ec2', region_name=self.region_name)

        return ec2.create_instances(
            ImageId='ami-0c5199d385b432989',
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                    {
                        'ResourceType': 'instance',
                        'Tags': [
                            {'Key': 'name', 'Value': 'rmarguzewicz'},
                        ]
                    },
            ]
        )

    def ebs(self):
        ec2 = boto3.resource('ec2', region_name=self.region_name)
        zones = self.availability_zones()
        print(zones)
        return ec2.create_volume(
            AvailabilityZone=zones[0],
            Encrypted=False,
            Size=20,
            # SnapshotId='string',
            VolumeType='standard',  # |'io1'|'gp2'|'sc1'|'st1',
            DryRun=False,
        )
# 'ResourceType': 'customer-gateway'|'dedicated-host'|'dhcp-options'|'image'|'instance'|'internet-gateway'|'network-acl'|'network-interface'|'reserved-instances'|'route-table'|'snapshot'|'spot-instances-request'|'subnet'|'security-group'|'volume'|'vpc'|'vpn-connection'|'vpn-gateway',

    def rds(self):
        client = boto3.client('rds', region_name=self.region_name)
        return client.create_db_instance(
            DBName='DBName',
            DBInstanceIdentifier=self.uuid,
            AllocatedStorage=20,
            DBInstanceClass='db.t2.micro',
            Engine='mariadb',
            MasterUsername='root',
            MasterUserPassword='123456789asdfsdfsfjpoiewur',
            Tags=[
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
        )

    def elb(self):
        client = boto3.client('elb', region_name=self.region_name)
        return client.create_load_balancer(
            LoadBalancerName=self.uuid,
            Listeners=[
                {
                    'Protocol': 'HTTP',
                    'LoadBalancerPort': 80,
                    'InstancePort': 80,
                },
            ],
            AvailabilityZones=['ap-southeast-1a', ],
            # SecurityGroups=[ 'string', ],
            # Scheme='string',
            # Tags=[ { 'Key': 'string', 'Value': 'string' }, ]
        )

    def auto_scaling_group(self):
        client = boto3.client('autoscaling', region_name=self.region_name)
        return client.create_auto_scaling_group(
            AutoScalingGroupName=self.uuid,
            LaunchConfigurationName='launch-configuration-to-autoscaling-rm',
            MinSize=2,
            MaxSize=2,
            AvailabilityZones=['ap-southeast-1a', ],
            # LoadBalancerNames=[ 'string', ],
            # TargetGroupARNs=[ 'string', ],
            # HealthCheckType='string',
            # HealthCheckGracePeriod=123,
            # PlacementGroup='string',
            # VPCZoneIdentifier='string',
            # TerminationPolicies=[ 'string', ],
            # NewInstancesProtectedFromScaleIn=True|False,
            Tags=[
                {'Key': 'string', 'Value': 'string', 'PropagateAtLaunch': True},
            ],
            # ServiceLinkedRoleARN='string'
        )
