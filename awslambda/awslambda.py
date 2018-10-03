import boto3
from aws import Aws
from helpers.color import yel
from .summary import summary

"""
File: lambda.py
Author: Rafal Marguzewicz
Email: rmarguzewicz@pg-soft.com
Github:
Description: Lambda
"""


class Lambda(Aws):
    ec2 = boto3.client('lambda')
    response_meta_data = None
    functions = None
    """create_user - create user and add to group"""

    def __init__(self, params={}):
        """TODO: to be defined1. """
        super().__init__(params)
        self.functions = self.ec2.list_functions()['Functions']

    def all(self):
        """Create AIM role
        :returns: TODO
        """
        for i in self.regions:
            ec2 = boto3.client('lambda', region_name=i)
            functions = ec2.list_functions()['Functions']
            if functions:
                print(i)
                for i in functions:
                    print(f"{yel(i['FunctionName']):50} {i['LastModified']:.10} | {i['Description']}")

    def find(self):
        """Find one lambda function by name of function
        :returns: One lambda function
        """
        ec2 = boto3.client('lambda', region_name=self.params.region_name)
        response = ec2.get_function(FunctionName=self.params.id)
        return summary(response, region_name=self.params.region_name)

    def tags(self):
        """Create AIM role
        :returns: TODO
        """
        return self.ec2.list_tags(Resource='owner')
