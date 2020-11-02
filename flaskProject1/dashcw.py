import time
import dash
import dash_html_components as html
from dash.dependencies import Input, Output, State
import boto3
from datetime import datetime
from datetime import timedelta
import pandas as pd


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

app = dash.Dash()
app.layout = html.Div(
    [
        html.Button("PC WYLLIS", id="button_3"),
        html.Button("PC MARCUS", id="button_4"),
        html.Div(children="CPU", id="CPU"),
        html.Div(children="NET IN", id="NET IN"),
        html.Div(children="NET OUT", id="NET OUT"),
    ]
)


@app.callback(
    Output("CPU", "children"),
    [Input("button_3", "n_clicks")])
def first_callback(a):
    while True:
        time.sleep( 5 )
        client = initialize_client()
        response = request_metric( client )
        dfa = pd.DataFrame( response['Datapoints'] )
        return "MÉDIA CPU", dfa["Average"].values[0], " ", dfa["Unit"].values[0]


@app.callback(
    Output( "NET IN", "children" ),
    [Input( "button_3", "n_clicks" )] )
def second_callback(b):
    while True:
        time.sleep( 5 )
        client = initialize_client()
        response_ni = request_metricNI( client )
        dfb = pd.DataFrame(response_ni['Datapoints'])
        return "MÉDIA INTERNET IN",dfb["Average"].values[0], " ", dfb["Unit"].values[0]


@app.callback(
    Output( "NET OUT", "children" ),
    [Input( "button_3", "n_clicks" )] )
def third_callback(c):
    while True:
        time.sleep( 5 )
        client = initialize_client()
        response_no= request_metricNO(client)
        df = pd.DataFrame( response_no['Datapoints'] )
        return "MÉDIA INTERNET OUT", df["Average"].values[0], " ", df["Unit"].values[0]


if __name__ == '__main__':
    app.run_server( debug=True, port=8055 )
