import json
import base64
from server.rebus_solver import solve

def handler(event, context):

    rebus = base64.b64decode(event['body']).decode('utf-8')
    
    answer = solve(rebus)

    return {
        'statusCode': 200,
        'body': json.dumps({
            "rebus":rebus,
            "answer": answer
        })
    }