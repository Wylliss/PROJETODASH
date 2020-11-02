#!/usr/bin/env python
import json
from pprint import pprint

import boto3
from datetime import datetime
from datetime import timedelta
import time
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
from dash.exceptions import PreventUpdate
import dash_table
import plotly.express as px


def initialize_client():
    client = boto3.client(
        'cloudwatch',
        aws_access_key_id='AKIA5D4WV7YYBVO3TD4E',
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
        time.sleep(5),
        client = initialize_client()

        response = request_metric(client)
        response_ni = request_metricNI(client)
        response_no = request_metricNO(client)

        pf = pd.DataFrame(response['Datapoints'])
        print(pf)

        pfni = pd.DataFrame(response_ni['Datapoints'])
        print(pfni)

        pfno = pd.DataFrame(response_no['Datapoints'])
        print(pfno)


main()
