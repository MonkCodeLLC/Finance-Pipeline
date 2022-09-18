import json
from module import api
from module import fileCreation
import os

# first test

def lambda_handler(event, context):
    
    try:
        data = api.get_data("MSFT")
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/")
        #fileCreation.create_json(data, path)
        
        return {
        'statusCode': 200,
        'body': json.dumps(data)
        }
    
    except Exception as err:
        return {
            'statusCode': 200,
            'body': json.dumps('File transfer Failed : {}'.format(str(err)))
        }