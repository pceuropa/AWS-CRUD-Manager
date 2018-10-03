import boto3
from aws import Aws
# from helpers.color import gre, red, yel
from .s3inspector import main

"""
File: aim.py
Author: Rafal Marguzewicz
Email: rmarguzewicz@pg-soft.com
Gitlab:
Description: Class contains method neccesairy to manage AIM roles
"""


class S3(Aws):
    ec2 = boto3.resource('s3')
    """create_user - create user and add to group"""

    def __init__(self, params={}):
        """TODO: to be defined1. """
        super().__init__(params)

    def inspect(self):
        """Create AIM role
        :returns: TODO
        """
        main()
