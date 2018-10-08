"""
Summary

Description: Class contains method neccesairy to manage EC2 instances
File: ec2.py
Author: Rafal Marguzewicz (PGS Software)
Email: rmarguzewicz@pgs-soft.com
Github:
"""

from boto3 import resource, client
from aws import Aws


class Dynamodb(Aws):

    """ List method: """

    def __init__(self, params={}):
        """TODO: to be defined1. """
        super().__init__(params)

    def migrate(self):
        self.create(self)

    def create(self) -> None:
        """Print all instances
        :returns: list
        """
        dynamodb = resource('dynamodb', region_name=self.region_name)

        dynamodb.create_table(
            TableName='krypto',
            KeySchema=[
                {
                    'AttributeName': 'username',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'last_name',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'username',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'last_name',
                    'AttributeType': 'S'
                },

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

    def all(self) -> dict:
        print(self.region_name)
        dynamodb = client('dynamodb', region_name=self.region_name)
        response = dynamodb.list_tables()
        print(response)
