import datetime as dt, json, boto3, re


def data_cleaning(data, top_stock):

    regex = r"\"\d.\s"
    test_str = data
    subst = "\""
    dataCleaned = re.sub(regex, subst, test_str, 0, re.MULTILINE)

    dataCleaned = json.loads(dataCleaned)
    dataCleaned["Meta Data"]["Company Name"] =  list(top_stock.keys())[list(top_stock.values()).index(dataCleaned["Meta Data"]["Symbol"])]
    dataCleaned = json.dumps(dataCleaned, indent=4)

    return dataCleaned if dataCleaned else 'Failed'


def transfer(data, bucket, top_stock):

    data = data_cleaning(data, top_stock)

    if data == 'Failed':
        raise Exception("Data cleaning failed")

    INDTimeStamp = dt.datetime.now(dt.timezone(dt.timedelta(hours=5, minutes=30))).strftime("%Y%m%d")
    stock = eval(data)['Meta Data']['Symbol']
    company = eval(data)['Meta Data']['Company Name']
 
    S3_connect = boto3.client('s3')
    try:
        S3_connect.put_object(Body=data, Bucket=bucket, Key="{}/{}/Timeseries_{}_{}.json".format(company,INDTimeStamp, stock, INDTimeStamp))
        return True
    except:
        raise  Exception("File transfer Failed")
    


