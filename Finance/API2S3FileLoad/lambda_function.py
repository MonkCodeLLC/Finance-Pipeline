import json, os
from module import api, S3

def lambda_handler(event, context):

    try:
        top_stock = {
                        "APPLE INC": "AAPL",
                        "MICROSOFT CORPORATION": "MSFT",
                        "ALPHABET INC": "GOOG",
                        "AMAZON.COM INC": "AMZN",
                        "TESLA INC": "TSLA",
                        "BERKSHIRE HATHAWAY INC": "BRK-A",
                        "UNITEDHEALTH GROUP INC": "UNH",
                        "JOHNSON & JOHNSON": "JNJ",
                        "VISA INC": "V",
                        "META INC": "META"
                    }

        data = api.get_data(top_stock["MICROSOFT CORPORATION"])
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/")

        bucket = None
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "config/bucket.json"), "r") as f:
            config = json.load(f)
            bucket = config["bucket"]

        S3.transfer(data, path, bucket, top_stock)
        
        return {
        'statusCode': 200,
        'body': json.dumps('File transfer Successful')
        }
    
    except Exception as err:
        return {
            'statusCode': 200,
            'body': json.dumps('File transfer Failed : {}'.format(str(err)))
        }