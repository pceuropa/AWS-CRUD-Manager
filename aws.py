"""
File: aws.py
Author: Rafal Marguzewicz (PGS Software)
Email: rmarguzewicz@pgs-soft.com
Gitlab:

Description: Coore super class for class services AWS
    ami_filter = [
        {"Name": "platform", 'Values': ["windows"]},
        {"Name": "virtualization-type", 'Values': ["hvm"]},
        {"Name": "image-type", 'Values': ["machine"]},
        {"Name": "architecture", 'Values': ["x86_64"]},
        {"Name": "state", 'Values': ["available"]},
        {'Name': 'tag:stop', 'Values': ['false'] },
        {"Name": "is-public", 'Values': ['false']},
        {'Name': 'instance-state-name', 'Values': ['running'] },
    ]
    ami_owners = ['amazon']
"""

from typing import TypeVar
import logging
from os import environ

StrNone = TypeVar('SN', str, None)
AnyStr = TypeVar('AnyStr', bytes, str)

log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())
log.setLevel(logging.INFO)


class Aws(object):
    """Command line app to manage AWS PGS Sandox """
    f = {
        'running': {'Name': 'instance-state-name', 'Values': ['running']},
        "dont_stop": {'Name': 'tag:stop', 'Values': ['false']},
        "without_owner": {'Name': 'tag:Owner', 'Values': ['*']}
    }
    filters = []
    # defaul region where you work
    region_name = 'ap-southeast-1'
    regions = [
        'sa-east-1',
        'ca-central-1',
        'eu-west-3', 'eu-west-2', 'eu-west-1', 'eu-central-1',
        'ap-south-1', 'ap-northeast-2', 'ap-northeast-1', 'ap-southeast-1', 'ap-southeast-2',
        'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2'
    ]
# region to tests https://ap-southeast-1.console.aws.amazon.com/ec2/v2/home?region=ap-southeast-1
    if environ.get('TESTMODE'):
        regions = [
            'ap-southeast-1',
        ]
        print('TESTMODE on')

    def __init__(self, params={}):
        """Preconfiguring filters """
        # from file settings (maybe in future)
        # from command line
        if params is not None:
            self.params = params

            if self.params.region_name:
                self.region_name = self.params.region_name
                self.regions = [self.region_name]
            else:
                self.params.region_name = self.region_name

            if params.running:
                self.filters.append(self.f['running'])

            if params.without_owner:
                self.filters.append(self.f['without_owner'])

            if params.tags:
                self.filters.append(self.f['dont_stop'])

    def set_filter(self, **kwargs):
        """factory filters """
        filters = []
        options = {'running': False, 'dont_stop': False}
        options.update(kwargs)

        if options['running']:
            filters.append(self.f['running'])

        if options['dont_stop']:
            filters.append(self.f['dont_stop'])

        return filters

    def have_tag(self, dictionary: dict, tag_key: str) -> StrNone:
        """Search owner by tag value
        :instance: ec2.Instance
        :tag_key: str Tag Key ex. owner, stop
        :returns: StrNone Onwer name
        """
        tags = (tag_key.capitalize(), tag_key.lower())
        if dictionary is not None:
            dict_with_owner_key = [tag for tag in dictionary if tag["Key"] in tags]
            if dict_with_owner_key:
                return dict_with_owner_key[0]['Value']
        return None

    def have_tag_owner(self, tags: dict) -> StrNone:
        return self.have_tag(tags, 'owner')

    def have_tag_stop(self, tags: dict) -> StrNone:
        return self.have_tag(tags, 'stop')
