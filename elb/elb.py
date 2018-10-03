'''
File: elb.py
Author: Rafal Marguzewicz (PGS Software)
Email: rmarguzewicz@pg-soft.com
Github:
Description: Class contains method neccesairy to manage Clasic Load Balancer
'''

import boto3
from helpers.color import red
from aws import Aws


class Elb(Aws):
    settings = {}  # file config
    params = {}  # command line params

    """ List method: """

    def __init__(self, params):
        """TODO: to be defined1. """
        super().__init__(params)

    def all(self) -> None:
        """Print all instances, can terminate all instance withou tag "owner"
            instance keys:
                .id,
                .instance_type
                .state
                .tags
        :returns: list
        """

        for region in self.regions:
            client = boto3.client('elb', region_name=region)
            balancers = client.describe_load_balancers()['LoadBalancerDescriptions']

            if balancers:
                print(region)
                for e in balancers:

                    tags = client.describe_tags(LoadBalancerNames=[e['LoadBalancerName']])
                    tags = tags['TagDescriptions'][0]['Tags']

                    if self.params.delete and not self.have_tag_owner(tags):
                        print(red('delete:'), end='')
                        self.delete(e['LoadBalancerName'], client)

                    print(f"{e['LoadBalancerName']} {e['Scheme']} {e['AvailabilityZones']}")

    def find(self) -> None:
        client = boto3.client('elb', region_name=self.params.region_name)
        load_balancer_id = self.params.id
        balancer = client.describe_load_balancers(LoadBalancerNames=[load_balancer_id])['LoadBalancerDescriptions'][0]

        if self.params.delete:
            self.delete(load_balancer_id, client)

        print(f"{balancer['LoadBalancerName']} {balancer['Scheme']}")

    def delete(self, load_balancer_name: str, client) -> None:
        return client.delete_load_balancer(
            LoadBalancerName=load_balancer_name
        )
