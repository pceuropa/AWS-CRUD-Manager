'''
File: rds.py
Author: Rafal Marguzewicz (PGS Software)
Email: rmarguzewicz@pg-soft.com
Github:
Description: Class contains method neccesairy to manage EC2 instances
'''

import boto3
from helpers.color import yel, alert, red
from aws import Aws
from rds.summary import summary


class Rds(Aws):
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
            client = boto3.client('rds', region_name=region)
            instances = client.describe_db_instances()['DBInstances']
            if instances:
                print(f"{yel(region):30} {len(instances)}")
                for i in instances:
                    arn = i['DBInstanceArn']
                    db_id = i['DBInstanceIdentifier']
                    tags = client.list_tags_for_resource(ResourceName=arn)['TagList']

                    if self.params.delete and not self.have_tag_owner(tags):
                        print(red('drop:'), end='')
                        self.delete(client, db_id)

                    print(f" - {db_id:30} {i['DBInstanceClass']} {i['DBInstanceStatus']} {i['Engine']:10} {i['MasterUsername']} {i['AllocatedStorage']} {alert(self.have_tag_owner(tags))}")

    def find(self, dbname: str='') -> None:
        client = boto3.client('rds', region_name=self.params.region_name)

        if self.params.delete:
            self.delete(client)

        summary(client.describe_db_instances(DBInstanceIdentifier=self.params.id)['DBInstances'][0])

    def delete(self, client, id=None) -> None:
        if id is None:
            id = self.params.id
        return client.delete_db_instance(
            DBInstanceIdentifier=id,
            SkipFinalSnapshot=True,
        )


''' [{
'DBInstanceIdentifier': 'mydbrafalmarguzewicz',
'DBInstanceClass': 'db.t2.micro',
'Engine': 'mariadb',
'DBInstanceStatus': 'creating',
'MasterUsername': 'root',
'DBName': 'dbname',
'AllocatedStorage': 20,
'PreferredBackupWindow': '19:50-20:20',
'BackupRetentionPeriod': 7,
'DBSecurityGroups': [],
'VpcSecurityGroups': [
    {'VpcSecurityGroupId': 'sg-ea26648e', 'Status': 'active'}
],
'DBParameterGroups': [
    {'DBParameterGroupName': 'default.mariadb10.2', 'ParameterApplyStatus': 'in-sync'}
],
'AvailabilityZone': 'ap-southeast-1c',
'DBSubnetGroup': {
    'DBSubnetGroupName': 'default',
    'DBSubnetGroupDescription': 'default',
    'VpcId': 'vpc-45e20621',
    'SubnetGroupStatus': 'Complete',
    'Subnets': [{
        'SubnetIdentifier': 'subnet-a5f1c5e3',
        'SubnetAvailabilityZone': {'Name': 'ap-southeast-1c'}, 'SubnetStatus': 'Active'}, {'SubnetIdentifier': 'subnet-1b71a27f',
        'SubnetAvailabilityZone': {'Name': 'ap-southeast-1a'}, 'SubnetStatus': 'Active'},
        {'SubnetIdentifier': 'subnet-6ccb071a', 'SubnetAvailabilityZone': {'Name': 'ap-southeast-1b'}, 'SubnetStatus':
            'Active'}]}, 'PreferredMaintenanceWindow': 'tue:20:27-tue:20:57', 'PendingModifiedValues':
        {'MasterUserPassword': '****'}, 'MultiAZ': False, 'EngineVersion': '10.2.12', 'AutoMinorVersionUpgrade':
        True, 'ReadReplicaDBInstanceIdentifiers': [], 'LicenseModel': 'general-public-license',
        'OptionGroupMemberships': [{'OptionGroupName': 'default:mariadb-10-2', 'Status': 'in-sync'}],
        'PubliclyAccessible': False, 'StorageType': 'gp2', 'DbInstancePort': 0, 'StorageEncrypted': False,
        'DbiResourceId': 'db-BHRJYWES4ZCU7E5MJW5455ENIM', 'CACertificateIdentifier': 'rds-ca-2015',
        'DomainMemberships': [], 'CopyTagsToSnapshot': True, 'MonitoringInterval': 0, 'DBInstanceArn':
        'arn:aws:rds:ap-southeast-1:890769921003:db:mydbrafalmarguzewicz', 'IAMDatabaseAuthenticationEnabled':
        False, 'PerformanceInsightsEnabled': False}]
'''
