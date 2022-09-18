import datetime as dt
import os
import re
import boto3

def data_cleaning(data):

    regex = r"\"\d.\s"
    test_str = data
    subst = "\""
    dataCleaned = re.sub(regex, subst, test_str, 0, re.MULTILINE)

    return dataCleaned if dataCleaned else 'Failed'


def transfer(data, path, bucket):

    data = data_cleaning(data)

    if data == 'Failed':
        raise Exception("Data cleaning failed")

    INDTimeStamp = dt.datetime.now(dt.timezone(dt.timedelta(hours=5, minutes=30))).strftime("%Y%m%d")
    stock = eval(data)['Meta Data']['Symbol']
 
    S3_connect = boto3.client('s3')
    try:
        S3_connect.put_object(Body=data, Bucket=bucket, Key="{}/{}/Timeseries_{}_{}.json".format(stock,INDTimeStamp, stock, INDTimeStamp))
        return True
    except:
        raise  Exception("File transfer Failed")
    


