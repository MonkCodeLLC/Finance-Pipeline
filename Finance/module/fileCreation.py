import datetime as dt
import os
import re

def data_cleaning(data):

    regex = r"\"\d.\s"
    test_str = data
    subst = "\""
    dataCleaned = re.sub(regex, subst, test_str, 0, re.MULTILINE)

    return dataCleaned if dataCleaned else 'Failed'


def create_json(data, path):

    data = data_cleaning(data)

    if data == 'Failed':
        print("Data cleaning failed")
        return False

    INDTimeStamp = dt.datetime.now(dt.timezone(dt.timedelta(hours=5, minutes=30))).strftime("%Y%m%d")
    stock = eval(data)['Meta Data']['Symbol']
 
    with open(os.path.join(path,"Timeseries_{}_{}.json".format(stock,INDTimeStamp)), "w") as f:
        f.write(data)