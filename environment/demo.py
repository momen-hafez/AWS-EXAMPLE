import boto3
s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

data = open('goku.jpg', 'rb')
s3.Bucket('demo-0597529934').put_object(Key='goku.jpg' , Body = data)
