import boto3


clientObj = boto3.client('apigateway')


jsonObj = clientObj.get_rest_apis(limit=10)


for x in jsonObj['items']:
    if x['name'] == "lambda-api":
        print(x['id'])

