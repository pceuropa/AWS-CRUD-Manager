from helpers.color import gre, red, yel, cyan, grey


def summary(response, region_name='eu-west-1'):
    code = response['Code']
    r = response['ResponseMetadata']
    c = response['Configuration']

    try:
        print("\nFunctionName: {0}\n \tRegoin: {1}\tDesc: {2}".format(
            yel(c['FunctionName']),
            yel(region_name),
            c['Description'],
        ))
        print("\tRuntime: {0}\tRole: {1}".format(
            gre(c['Runtime']),
            cyan(c['Role'])
        ))

        print("\tHandler: {0}\t \tCodeSize: {1}\tTimeout: {2}\t MemorySize: {3}\t FunctionArn: {4}".format(
            cyan(c['Handler']),
            gre(c['CodeSize']),
            red(c['Timeout']),
            red(c['MemorySize']),
            cyan(c['FunctionArn'])
        ))

        print("\tLastModified: {0}\t \tVersion: {1}\t CodeSha256: {2}".format(
            cyan(c['LastModified']),
            gre(c['Version']),
            cyan(c['CodeSha256']),
        ))

        print("\tResponseMetadata:\n \t\tHTTPStatusCode: {0}\tRetryAttempts: {1}\tRequestId: {2}".format(
            red(r['HTTPStatusCode']),
            cyan(r['RetryAttempts']),
            cyan(r['RequestId']),
        ))

        print("\t\tHTTPHeaders:\n \t\t\tdate: {0}\n\t\t\tcontent-type: {1}\tcontent-length: {2}\tconnection: {3}\n\t\t\tx-amz-requestid: {4}".format(
            cyan(r['HTTPHeaders']['date']),
            cyan(r['HTTPHeaders']['content-type']),
            cyan(r['HTTPHeaders']['content-length']),
            cyan(r['HTTPHeaders']['connection']),
            cyan(r['HTTPHeaders']['x-amzn-requestid']),
        ))

    except Exception as e:
        print(e)

    try:
        print("\tVPC:\n \t\tSubnetIds: {0}\tSecurityGroudIds: {1}\tVpcId: {2}".format(
            cyan(c['VpcConfig']['SubnetIds']),
            cyan(c['VpcConfig']['SecurityGroupIds']),
            cyan(c['VpcConfig']['VpcId']),
        ))
    except Exception as e:
        pass

    try:
        print("\tEnvironment Variables: {0}".format(
            cyan(c['Environment']['Variables']),
        ))

        print("\tTracingConfig: {0}\t RevisionId: {1}".format(
            cyan(c['TracingConfig']),
            cyan(c['RevisionId']),
        ))
    except Exception as e:
        pass

    try:
        print("\tRepositoryType: {0}\n\tLocation: {1}".format(
            cyan(code['RepositoryType']),
            grey(code['Location'])
        ))

    except Exception as e:
        pass
