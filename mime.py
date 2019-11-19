import boto3
from messenger.application.config import cfg

if __name__ == '__main__':
    session = boto3.Session()
    s3_client = session.client(service_name=cfg['service_name'],
                               endpoint_url=cfg['service_url'],
                               aws_access_key_id=cfg['AWS_AK'],
                               aws_secret_access_key=cfg['AWS_SK']
                               )
    s3_client.put_object(Bucket='atom', Key='325', Body='a_gridin_try')
