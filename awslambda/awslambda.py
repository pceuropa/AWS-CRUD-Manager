from boto3 import client
from aws import Aws, StrNone
from helpers.color import yel
from .summary import summary

"""
File: lambda.py
Author: Rafal Marguzewicz
Email: info@pceuropa.net
Github:
Description: Lambda
"""


class Lambda(Aws):
    response_meta_data = None
    functions = None
    """create_user - create user and add to group"""

    def __init__(self, params={}):
        """TODO: to be defined1. """
        super().__init__(params)
        self.cl = client('lambda', region_name=self.params.region_name)

    def have_tag_owner(self, tags: dict={}) -> StrNone:

        if 'owner' in tags:
            return tags['owner']

        if 'Owner' in tags:
            return tags['Owner']

        return None

    def all(self):
        """Create AIM role
        :returns: TODO
        """
        for region in self.regions:
            cl = client('lambda', region_name=region)
            functions = cl.list_functions()['Functions']

            if functions:
                print('\n', region)
                for i in functions:
                    response = cl.get_function(FunctionName=i['FunctionName'])

                    if self.params.delete:
                        try:
                            if not self.have_tag_owner(response['Tags']):
                                self.delete(i['FunctionName'])
                        except KeyError as e:
                            self.delete(i['FunctionName'])

                    try:
                        print(f"{yel(i['FunctionName']):50} {i['LastModified']:.10} {self.have_tag_owner(response['Tags'])} | {i['Description']}")
                    except Exception as e:
                        print(f"{yel(i['FunctionName']):50} {i['LastModified']:.10} {i['Description']}")

    def find(self):
        """Find one lambda function by name of function
        :returns: One lambda function
        """
        response = self.cl.get_function(FunctionName=self.params.id)
        if self.params.delete:
            self.delete(self.params.id)
        return summary(response, region_name=self.params.region_name)

    def delete(self, function_name: str):
        """Delete AWS lambda
        :function_name: lambda name function
        :returns: TODO
        """
        return self.cl.delete_function(
            FunctionName=function_name,
        )

    def tags(self):
        """Create AIM role
        :returns: TODO
        """
        return self.cl.list_tags(Resource='owner')
