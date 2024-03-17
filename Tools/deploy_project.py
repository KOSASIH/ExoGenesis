import boto3

def deploy_project(project_name, region, bucket_name, zip_file_path):
    # Create an S3 client
    s3 = boto3.client('s3', region_name=region)

    # Upload the zip file to the S3 bucket
    s3.upload_file(zip_file_path, bucket_name, project_name + '.zip')

    # Create an Elastic Beanstalk client
    eb = boto3.client('elasticbeanstalk', region_name=region)

    # Create an application version
    response = eb.create_application_version(
        ApplicationName=project_name,
        VersionLabel=project_name + '-' + '1.0',
        SourceBundle={
            'S3Bucket': bucket_name,
            'S3Key': project_name + '.zip'
        }
    )

    # Deploy the application version
    response = eb.update_environment(
        ApplicationName=project_name,
        EnvironmentName=project_name + '-env',
        VersionLabel=project_name + '-' + '1.0'
    )

    print("Project deployed successfully.")
