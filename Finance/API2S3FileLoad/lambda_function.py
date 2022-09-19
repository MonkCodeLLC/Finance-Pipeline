import json, os
from module import api, S3

def lambda_handler(event, context):

    try:
        top_stock = {
                        "APPLE": "AAPL",
                        "AMAZON": "AMZN",
                        "GOOGLE": "GOOG",
                        "NETFLIX": "NFLX",
                        "META": "META"
                    }
        bucket = None
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "config/bucket.json"), "r") as f:
            config = json.load(f)
            bucket = config["bucket"]

        for company, stock in top_stock.items():
            data = api.get_data(stock)
            S3.transfer(data, bucket, top_stock)
        
        return {
        'statusCode': 200,
        'Message': 'File transfer Successful'
        }
    
    except Exception as err:
        return {
            'statusCode': 200,
            'body': json.dumps('File transfer Failed : {}'.format(str(err)))
        }