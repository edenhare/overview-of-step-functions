import json
import random

def lambda_handler(event, context):
    
    print(json.dumps(event, indent=2))
    # TODO implement
    random.seed()
    number = random.randint(0,1)
    if number == 0:
        status = 200
        text = "ok"
    else:
        status = 400
        text = "bad"
        
    first = event['body']['first']
    second = event['body']['second']
    
    body = {
        "text": text,
        "first": first,
        "second": second,
    }
    
    return {
        'statusCode': status,
        'body': body
    }
    