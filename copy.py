import os

import boto3

def copy_from_s3(bucketname, localdir=None):
    s3 = boto3.resource('s3')
    if not localdir:
        localdir = bucketname
    bucket = s3.Bucket(bucketname)
    for obj in bucket.objects.all():
        if obj.size > 0:
            destination = os.path.abspath(os.path.join(localdir, obj.key))
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            bucket.download_file(obj.key, destination)
