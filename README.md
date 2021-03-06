# AWS CRUD Manager
```
usage: awsconsole.py [-h] [-i ID] [-R] [-t] [-u USERNAME] [-r REGION_NAME]
                     [-o] [--ebs] [--autoscaling] [--stop] [--start]
                     [--terminate] [--delete]
                     {ec2,iam,s3,elb,lambda,rds,migrate} action

CLI Manager fetures:

positional arguments:
  {ec2,iam,s3,elb,lambda,rds,migrate}
                        ec2|aim
  action                all|find|...

optional arguments:
  -h, --help            show this help message and exit
  -i ID, --id ID
  -R, --running
  -t, --tags
  -u USERNAME, --username USERNAME
                        Username for AIM role
  -r REGION_NAME, --region_name REGION_NAME
                        Username for AIM role
  -o, --without_owner   Ec2 with owner
  --ebs                 Search EBS Volumes (only service ec2)
  --autoscaling         Search Autoscaling groups (only service ec2)
  --stop                Stop one or all instances
  --start               Start one or all instances from query
  --terminate           Terminate one or all EC2 instances
  --delete              Delete RDS, ELB

examples:
    python3 awsconsole.py ec2 all
    python3 awsconsole.py ec2 all --ebs
    python3 awsconsole.py ec2 all --autoscaling
    python3 awsconsole.py ec2 find -i i-0552e09b7a54fa2cf
    python3 awsconsole.py ec2 find -i i-0552e09b7a54fa2cf --[terminate|start|stop]

    python3 awsconsole.py [rds|elb|lambda] all --delete
```
