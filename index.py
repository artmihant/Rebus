import json
import base64
from main import solve
from solvers import ten_adic_rebus_solver

def handler(event, context):
    """ Это функция для яндекс-облака """

    rebus = base64.b64decode(event['body']).decode('utf-8')
    
    answer = solve(rebus, ten_adic_rebus_solver)

    return {
        'statusCode': 200,
        'body': json.dumps({
            "rebus":rebus,
            "answer": answer
        })
    }