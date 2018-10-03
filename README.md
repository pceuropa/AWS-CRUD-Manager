# AWS CRUD Manager
CLI Manager fetures:

Query:
- all - find all resources
- find - find one resources
    
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

    python3 awsconsole.py [rds|elb|lambda] all
```
 
[AWS Watchdog lambda](https://ap-southeast-2.console.aws.amazon.com/lambda/home?region=ap-southeast-2#/functions/aws-watchdog?tab=graph) live in [Australia Sydney (ap-southeast-2)](https://ap-southeast-1.console.aws.amazon.com/lambda/home?region=ap-southeast-2#/functions)

Warning!!!
To test - run aplication in test mode. If you need test lambda function add to Environment variables Key: TESTMODE Value: 1
The default tests are on [Pacyfic (ap-southeast-1)](https://ap-southeast-1.console.aws.amazon.com/ec2/v2/home?region=ap-southeast-1#Instances:sort=instanceId) where there is not much resources.
Watchdog can terminate all resourses in all regions  for this important is test application in testmode.

Run testmode
```bash
export TESTMODE=1
```
or 
```bash
./test.sh
```

## Directory structure
      deploy-aws-lambda.sh  deploy code to AWS lambda
      lambda_config.json    data config used by Aws lambda. File is create after use deploy-aws-lambda.sh
      main.py               main file with handler()
      policy.json           IAM policy used in AWS lambda
      tests.sh              Lanuch automatic tests. Add env variable


## Requirements
- Python 3.6+
- boto3
- inotifywait (to test.sh)


## Easy deployment
Default region: ap-southeast-2
Script shoud be executable
```bash
chmod +x deploy-aws-lambda.sh
```

```bash
./deploy-aws-lambda.sh
Action: [C]reate/[U]pdate/[R]ead/[D]elete lambda function ? [c/r/u/d] c
Start process update lambda function...
Zip requirements packages? [y/N] n
Update lamba function? [y/N] y
updating: main.py (deflated 37%)
    "FunctionName": "aws-watchdog",
```

## Tests
Test.sh file add environment variable TESTMODE
```bash
./tests.sh
```

## Know problems
1. is have autoscaling group
