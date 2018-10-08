"""
File: awsconsol.py
Author: Rafal Marguzewicz (PGS Software)
Email: rmarguzewicz@pgs-soft.com
Gitlab:
Description: Mangament hooking
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from iam.iam import Iam
from ec2.ec2 import Ec2
from s3.s3 import S3
from elb.elb import Elb
from rds.rds import Rds
from dynamodb.dynamodb import Dynamodb
from migrate import Migrate
from awslambda.awslambda import Lambda

SERVICES: list = ['ec2', 'iam', 's3', 'elb', 'lambda', 'rds', 'migrate', 'dynamodb']

if __name__ == "__main__":
    Arg = ArgumentParser(
        prog='awsconsole.py',
        formatter_class=RawDescriptionHelpFormatter,
        description='''CLI Manager fetures:''',
        epilog='''
examples:
    python3 awsconsole.py ec2 all
    python3 awsconsole.py ec2 all --ebs
    python3 awsconsole.py ec2 all --autoscaling
    python3 awsconsole.py ec2 find -i i-0552e09b7a54fa2cf

    python3 awsconsole.py [rds|elb|lambda] all
    ''')
    Arg.add_argument('service', choices=SERVICES, help="ec2|aim")
    Arg.add_argument('action', help="all|find|...")
    Arg.add_argument('-i', '--id', help="")
    Arg.add_argument('-R', '--running', action='store_true', help="")
    Arg.add_argument('-t', '--tags', action='store_true', help="")
    Arg.add_argument('-u', '--username', help="Username for AIM role")
    Arg.add_argument('-r', '--region_name', help="Username for AIM role")
    Arg.add_argument('-o', '--without_owner', action="store_true", help="Ec2 with owner")
    Arg.add_argument('--autoscaling', action="store_true", help="Search Autoscaling groups (only EC2)")
    Arg.add_argument('--groups', action="store_true", help="Search IAM groups (only IAM")
    Arg.add_argument('--ebs', action="store_true", help="Search EBS Volumes (only service ec2)")
    Arg.add_argument('-p', '--password', help="to IAM")
    Arg.add_argument('--stop', action="store_true", help="Stop one or all instances")
    Arg.add_argument('--start', action="store_true", help="Start one or all instances from query")
    Arg.add_argument('--terminate', action="store_true", help="Terminate one or all EC2 instances")
    Arg.add_argument('--delete', action="store_true", help="Delete RDS, ELB")
    p = Arg.parse_args()

    '''Generate class name by trick locals()[key]'''
    service = locals()[p.service.capitalize()](p)

    if 'service' in p and 'action' in p:
        getattr(service, p.action)()
