import os
import logging

import boto3

logger = logging.getLogger(__name__)

def copy_from_s3(bucketname, localdir=None, verbose=False):
    s3 = boto3.resource('s3')
    if not localdir:
        localdir = bucketname
    bucket = s3.Bucket(bucketname)
    for obj in bucket.objects.all():
        if obj.size > 0:
            destination = os.path.abspath(os.path.join(localdir, obj.key))
            if os.path.exists(destination):
                if verbose:
                    logger.info('Already downloaded ' + obj.key)
            else:
                os.makedirs(os.path.dirname(destination), exist_ok=True)
                bucket.download_file(obj.key, destination)
                if verbose:
                    logger.info('Downloaded ' + obj.key)
        else:
            if verbose:
                logger.info('Skipped empty ' + obj.key)
