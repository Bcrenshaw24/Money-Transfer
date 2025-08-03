from unittest import case
import pika
import json
from FraudEngine import FraudEngine

def callback(ch, method, properties, body):
    data = json.loads(body)
    engine = FraudEngine(data["ip_address"])
    # Prepare features for prediction (convert booleans if needed)
    features = {
        "amount": data["amount"],
        "source_balance": data["source_balance"],
        "source_monthly_sent": data["source_monthly_sent"],
        "source_monthly_limit": data["source_monthly_limit"],
        "average_transaction_amount_30d": data["average_transaction_amount_30d"],
        "transaction_count_24h": data["transaction_count_24h"],
        "login_count_24h": data["login_count_24h"],
        "geo_distance_km": data["geo_distance_km"],
        "hour_of_day": data["hour_of_day"],
        "day_of_week": data["day_of_week"],
        "source_account_age_days": data["source_account_age_days"],
        "destination_account_age_days": data["destination_account_age_days"],
        "amount_over_avg_ratio": data["amount_over_avg_ratio"],
        "amount_pct_of_balance": data["amount_pct_of_balance"],
        "amount_pct_of_limit": data["amount_pct_of_limit"],
        "last_login_ip_same": int(data["last_login_ip_same"]),
        "known_device": int(data["known_device"])
    }
    result = engine.predict_transaction(features)
    print(f"Transaction {data['transaction_id']} fraud prediction: {result}")

    match result: 
        case 1:
            print(f"Transaction {data['transaction_id']} is likely fraudulent.")
            queue_name = 'fraud'
        case 0:
            print(f"Transaction {data['transaction_id']} is likely not fraudulent.")
            queue_name = 'non_fraud'
        case _:
            print(f"Transaction {data['transaction_id']} prediction is inconclusive.")
            queue_name = 'unknown'

   
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=json.dumps(data)
    )

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        port=5672,
        credentials=pika.PlainCredentials('username', 'password')
    )
)
channel = connection.channel()
channel.queue_declare(queue='fraud_queue')

channel.basic_consume(queue='fraud_queue', on_message_callback=callback, auto_ack=True)
print('Waiting for messages...')
channel.start_consuming()