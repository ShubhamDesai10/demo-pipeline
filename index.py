def handler(event, context):
            response = {
              'isBase64Encoded': False,
              'statusCode': 200,
              'headers': {},
              'multiValueHeaders': {},
              'body': 'Hello, World! Happy to see you'
            }
            return response
