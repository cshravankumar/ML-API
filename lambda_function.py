import json
from scorer import calculate_score
from pre_treatment import treat_input


def lambda_handler(event, context):
    if event == {}:
        # In case the input is json
        #event = event['params']['querystring']
        event = "inside first function"
    else:
        # in case input is urlencoded
        #event = event['form']
        print(event)
        #event = {x.split('=')[0]: x.split('=')[1] for x in event.split("&")}

    treated_event = treat_input(event)
    score = calculate_score(treated_event)

    # build response
    r = score
   
    status_code = 200
    response = {
        #"isBase64Encoded": False,
        #"headers": {"Content-Type": "application/json"},
        #"statusCode": status_code,
        "body": json.dumps(r)
    }
    
    #response = event
    
    #return response
    return response
    
    raise Exception('the sky is falling!')