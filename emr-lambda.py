import boto3
conn = boto3.client('emr')
def lambda_handler(event, context):
    cluster_id = conn.run_job_flow(
         Name='Subbu-emr-lambda-test',
         LogUri='s3://<s3 bucket-name>/folder-path',
         ReleaseLabel='emr-5.18.0',
        Applications=[
            {
                'Name': 'Spark'
            },
        ],
        Instances={
            'InstanceGroups': [
                {
                    'Name': "Master",
    				'Market': 'ON_DEMAND',
                    'InstanceRole': 'MASTER',
                    'InstanceType': 'm3.xlarge',
                    'InstanceCount': 1,
                },
                {
                    'Name': "Slave",
                    'Market': 'ON_DEMAND',
                    'InstanceRole': 'CORE',
                    'InstanceType': 'm3.xlarge',
                    'InstanceCount': 2,
                }
            ],
            'Ec2KeyName': '<key-name>',
            'KeepJobFlowAliveWhenNoSteps': True,
            'TerminationProtected': False,
        },
        Steps=[],
    	VisibleToAllUsers=True,
        JobFlowRole='EMR_EC2_DefaultRole',
        ServiceRole='EMR_DefaultRole',
        Tags=[ ],
    )
    print "Starting cluster", cluster_id
