#!/usr/bin/env python
import boto3
from datetime import datetime
from datetime import timedelta
import time


def initialize_client():
    client = boto3.client(
        'cloudwatch',
        aws_access_key_id='AKIA5D4WV7YYGCSZZTOQ',
        aws_secret_access_key='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',
        region_name='sa-east-1'
    )

    return client


def request_metric(client):
    response = client.get_metric_statistics(
        Namespace='AWS/EC2',
        Period=120,
        StartTime=datetime.utcnow() - timedelta(seconds=600),
        EndTime=datetime.utcnow(),
        MetricName='CPUUtilization',
        Statistics=['Average'],
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': 'i-02caee88b06a9ca34'
            }
        ],
    )

    return response


def request_metricNI(client):
    response_ni = client.get_metric_statistics(
        Namespace='AWS/EC2',
        Period=120,
        StartTime=datetime.utcnow() - timedelta(seconds=600),
        EndTime=datetime.utcnow(),
        MetricName='NetworkIn',
        Statistics=['Average'],
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': 'i-02caee88b06a9ca34'
            }
        ],
    )

    return response_ni


def request_metricNO(client):
    response_no = client.get_metric_statistics(
        Namespace='AWS/EC2',
        Period=120,
        StartTime=datetime.utcnow() - timedelta(seconds=600),
        EndTime=datetime.utcnow(),
        MetricName='NetworkOut',
        Statistics=['Average'],
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': 'i-02caee88b06a9ca34'
            }
        ],
    )

    return response_no


def main():
    while True:
        time.sleep(10),
        client = initialize_client()

        response = request_metric(client)
        response_ni = request_metricNI(client)
        response_no = request_metricNO(client)

        with open('static/saidadocw.json', 'w+') as arquivo:
            [print(response, file=arquivo)]
            [print(response_ni, file=arquivo)]
            [print(response_no, file=arquivo)]


main()
