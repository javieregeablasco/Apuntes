import boto3
from datetime import datetime, timedelta

# Configuración del cliente
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
client = boto3.client('dynamodb', region_name='us-east-1')

reply_table_name = "Reply"

def delete_table(table_name):
    try:
        table = dynamodb.Table(table_name)
        print(f"Eliminando tabla {table_name}...")
        table.delete()
        table.wait_until_not_exists()
    except client.exceptions.ResourceNotFoundException:
        pass

def create_reply_table():
    print(f"Creando tabla {reply_table_name}...")
    try:
        table = dynamodb.create_table(
            TableName=reply_table_name,
            KeySchema=[
                {'AttributeName': 'Id', 'KeyType': 'HASH'},          # Partition Key
                {'AttributeName': 'ReplyDateTime', 'KeyType': 'RANGE'} # Sort Key
            ],
            AttributeDefinitions=[
                {'AttributeName': 'Id', 'AttributeType': 'S'},
                {'AttributeName': 'ReplyDateTime', 'AttributeType': 'S'},
                {'AttributeName': 'PostedBy', 'AttributeType': 'S'}
            ],
            LocalSecondaryIndexes=[
                {
                    'IndexName': 'PostedBy-Index',
                    'KeySchema': [
                        {'AttributeName': 'Id', 'KeyType': 'HASH'},
                        {'AttributeName': 'PostedBy', 'KeyType': 'RANGE'}
                    ],
                    'Projection': {'ProjectionType': 'KEYS_ONLY'}
                }
            ],
            ProvisionedThroughput={'ReadCapacityUnits': 10, 'WriteCapacityUnits': 5}
        )
        table.wait_until_exists()
        print("Tabla Reply creada.")
    except Exception as e:
        print(f"Error al crear tabla: {e}")

def load_sample_replies():
    table = dynamodb.Table(reply_table_name)
    print(f"Cargando datos en {reply_table_name}...")
    
    # Generar una fecha similar a la de tu ejemplo
    fecha_ejemplo = "2025-09-19T16:30:00.214Z"
    
    # Este es el ítem exacto que tu consulta busca
    item = {
        'Id': 'Amazon DynamoDB#DynamoDB Thread 1',
        'ReplyDateTime': fecha_ejemplo,
        'Message': 'DynamoDB Thread 1 Reply 1 text',
        'PostedBy': 'User A'
    }
    
    try:
        table.put_item(Item=item)
        print(f"Item insertado: {item['Id']}")
    except Exception as e:
        print(f"Error al insertar item: {e}")

def main():
    # 1. Limpieza
    delete_table(reply_table_name)
    
    # 2. Creación
    create_reply_table()
    
    # 3. Carga de datos (Esto es lo que faltaba)
    load_sample_replies()
    
    print("Proceso finalizado.")

if __name__ == "__main__":
    main()