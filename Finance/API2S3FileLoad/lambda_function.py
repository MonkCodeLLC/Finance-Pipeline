import json, os
from module import api, S3

def lambda_handler(event, context):

    try:
        top_stock = {
                        'Apple':'AAPL',
                        'Microsoft':'MSFT',
                        'Google':'GOOG',
                        'Amazon':'AMZN',
                        'Tesla':'TSLA',
                        '':'BRK-A',
                        '':'UNH',
                        '':'JNJ',
                        '':'V',
                        '':'META'
                    }

        data = api.get_data("MSFT")
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/")

        bucket = None
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "config/bucket.json"), "r") as f:
            config = json.load(f)
            bucket = config["bucket"]

        S3.transfer(data, path, bucket)
        
        return {
        'statusCode': 200,
        'body': json.dumps('File transfer Successful')
        }
    
    except Exception as err:
        return {
            'statusCode': 200,
            'body': json.dumps('File transfer Failed : {}'.format(str(err)))
        }