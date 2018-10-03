from helpers.color import gre, red, yel, cyan


def summary(i, region_name: str=''):
    print(f"DBInstanceIdentifier: {yel(i['DBInstanceIdentifier'])}, DBInstanceClass: {i['DBInstanceClass']}, Engine: {i['Engine']}, DBInstanceStatus: {i['DBInstanceStatus']}")
    print(f"MasterUsername: {i['MasterUsername']}, 'AllocatedStorage': {i['AllocatedStorage']}")
    print(f"DBParameterGroups: {i['DBParameterGroups']}")


'''
'PreferredBackupWindow': '19:50-20:20',
'BackupRetentionPeriod': 7,
'DBSecurityGroups': [],
'VpcSecurityGroups': [
    {'VpcSecurityGroupId': 'sg-ea26648e', 'Status': 'active'kj
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
