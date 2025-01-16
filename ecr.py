import boto3

# Initialize the ECR client
ecr_client = boto3.client('ecr')

ecr_client = boto3.client('ecr', region_name='us-east-1')  # Replace 'us-east-1' with your desired region

ecr_client = boto3.client('ecr', region_name='your-region')


# Define the repository name
repository_name = "my-cloud-native-repo"

# Create the repository
response = ecr_client.create_repository(repositoryName=repository_name)

# Extract the repository URI from the response
repository_uri = response['repository']['repositoryUri']
print(repository_uri)
