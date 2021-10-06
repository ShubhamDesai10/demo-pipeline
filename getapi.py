import boto3

def getApiURL():
    clientObj = boto3.client('apigateway')


    jsonObj = clientObj.get_rest_apis(limit=10)

    for x in jsonObj['items']:
        if x['name'] == "lambda-api":
            global id
            id = x['id']

    api_url = "https://{}.execute-api.us-east-2.amazonaws.com/v0/lambda".format(id)
    return api_url



