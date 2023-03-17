import json
import boto3

from app.model import write_to_db


def lambda_handler(event, context):
    operation = event['httpMethod']

    if operation != 'GET':
        return {"error": f"Método não suportado: {operation}"}

    payload = event['queryStringParameters']
    bucket_name = payload.get('bucket_name')
    object_key = payload.get('object_key')

    try:
        s3 = boto3.client('s3')
        obj = s3.get_object(Bucket=bucket_name, Key=object_key)
        file_content = obj['Body'].read().decode('utf-8').splitlines()
        success = write_to_db(file_content)
        message = 'Sucesso ao inserir dados no banco!' if success else 'Falha ao inserir dados no banco!'
        response_body = {'message': message}
        response_headers = {'Content-Type': 'application/json'}

        return {
            'statusCode': 200 if success else 400,
            'body': json.dumps(response_body),
            'headers': response_headers
        }

    except Exception as e:
        print(f"Erro ao obter o objeto {object_key} do bucket {bucket_name}. Verifique se eles existem e se a função está na mesma região do bucket.")
        raise e
