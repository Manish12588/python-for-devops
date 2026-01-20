import boto3

def get_connections(service_name):
    return boto3.client(service_name)   #Making a connection to the amazon client service

def s3_bucket_lists(client_name):
    response = client_name.list_buckets()
    for bucket in response['Buckets']:  #Get the name of each bucket.
     print(f'  {bucket["Name"]}')

def create_s3_bucket(client_name,bucket_name):
    response = client_name.create_bucket(
      Bucket=bucket_name)
    if response["ResponseMetadata"]["HTTPStatusCode"]==200:
      print(f"Bucket '{bucket_name}' is created successfully.")
    else:
      print("Error in creating bucket.")

def delete_s3_bucket(client_name,bukcetname):
   response = client_name.delete_bucket(Bucket=bukcetname)
   if response["ResponseMetadata"]["HTTPStatusCode"]==200:
      print(f"Bucket '{bukcetname}' is deleted successfully.")
   else:
      print("Error in deleting bucket.")

def show_regions(ec2_client):
   response = ec2_client.describe_regions()

s3 = get_connections("s3")   #Creating a connection
print ("Fetching the list of bucket before creating new bucket: ") 
s3_bucket_lists(s3)
create_s3_bucket(s3, "learning-test-kumar") #Creating new bucket
print ("Fetching the list of bucket after creating new bucket: ") 
s3_bucket_lists(s3)
delete_s3_bucket(s3, "learning-test-kumar") #Deleting bucket
print ("Fetching the list of bucket after deleting bucket: ") 
s3_bucket_lists(s3)

"""
def showing_all_bucket_list_in_one_function():
    s3_client = boto3.client("s3")

    response = s3_client.list_buckets()

    print(type(response))
    print(response)  #Tp get all the bucket list

    print('Existing buckets:')
    for bucket in response['Buckets']:  #Get the name of each bucket.
        print(f'  {bucket["Name"]}')

"""


