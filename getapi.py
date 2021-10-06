import boto3
from requests.models import Response

def getApiURL():
    clientObj = boto3.client('apigateway')


    jsonObj = clientObj.get_rest_apis()

    for x in jsonObj['items']:
        if x['name'] == "lambda-api":
            global id
            id = x['id']

    api_url = "https://{}.execute-api.us-east-2.amazonaws.com/v0/hello".format(id)
    return api_url

def deleteApi():
    clientObj = boto3.client('cloudformation')
    clientObj.delete_stack(StackName='Hello-App')


