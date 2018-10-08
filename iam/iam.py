import boto3
from aws import Aws
from helpers.color import gre, red, alert, cyan
from datetime import datetime

"""
File: aim.py
Author: Rafal Marguzewicz
Email: rmarguzewicz@pg-soft.com
Github:
Description: Class contains method neccesairy to manage AIM roles
"""


class Iam(Aws):
    iam = boto3.resource('iam')
    """create_user - create user and add to group"""

    def __init__(self, params: dict):
        super().__init__(params)

    def create(self):
        """Create AIM role
        :returns: TODO
        """
        try:
            user = self.aim.create_user(
                UserName=self.params.username,
            )
            print(user)
        except Exception as e:
            print(red("Please enter username -u --username"))

    def delete_user(self):
        """Delete AIM role
        :returns: TODO
        """
        try:
            response = self.iam.User(name=self.params.username).delete()
            print(response)
        except Exception as e:
            print(red("Please enter correct username -u --username"))

    def all(self):
        if self.params.groups:
            self.groups()
        else:
            self.users()
        print("groups or users command")

    def find(self):
        """Default find user (optionaly role)
        :returns: TODO

        """
        pass

    def groups(self):
        """List IAM groups
        :returns: list
        """
        iam = boto3.client('iam')
        try:
            for i in iam.list_groups()['Groups']:
                print(f"{i['GroupName']:20} {i['Arn']}")

        except Exception as e:
            raise e

    def delete_profile(self):
        if self.params.id:
            login_profile = self.iam.LoginProfile(self.params.id)
            return login_profile.delete()

    def create_profile(self):
        if self.params.id:
            login_profile = self.iam.LoginProfile(self.params.id)
            return login_profile.create(
                Password=self.params.password,
                PasswordResetRequired=False
            )
        else:
            print("awsconsol.py iam create_profile -i [user_name]")

    def users(self):
        """List users
        :returns: list
        """
        iam = boto3.resource('iam')
        try:
            iam_users = iam.users.all()
        except Exception as e:
            raise e

        print(f"{cyan('name'):29} {cyan('last login')} {cyan('console')} {cyan('groups')}")
        for iam_user in iam_users:
            last = iam_user.password_last_used
            if isinstance(last, datetime):
                last = last.strftime("%Y-%m-%d")
            groups = ','.join([group.name for group in iam_user.groups.all()])

            print(f"{iam_user.name:20} {alert(last, False):20} {self.isPasswordEnabled(iam_user.name)} {groups}")

    def isPasswordEnabled(self, user: str) -> bool:
        login_profile = self.iam.LoginProfile(user)
        try:
            login_profile.create_date
            return red('True')
        except Exception as e:
            return gre('False')
