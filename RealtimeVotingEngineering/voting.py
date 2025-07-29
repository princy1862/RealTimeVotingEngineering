import random
import time
import psycopg2
from confluent_kafka import SerializingProducer
import simplejson as json
from datetime import datetime
import uuid

from main import delivery_report, generate_voter_data

conf = {
    'bootstrap.servers': 'localhost:9092'
}

producer = SerializingProducer(conf)

# def consume_messages():
#     result = []
#     consumer.subscribe(['candidates_topic'])
#     try:
#         while True:
#             msg = consumer.poll(timeout=1.0)
#             if msg is None:
#                 continue
#             elif msg.error():
#                 if msg.error().code() == KafkaError._PARTITION_EOF:
#                     continue
#                 else:
#                     print(msg.error())
#                     break
#             else:
#                 result.append(json.loads(msg.value().decode('utf-8')))
#                 if len(result) == 3:
#                     return result
#
#             # time.sleep(5)
#     except KafkaException as e:
#         print(e)

if __name__ == "__main__":
    conn = psycopg2.connect("host=localhost port = 5432 dbname=voting user=postgres password=postgres")
    cur = conn.cursor()

    # Get candidates from database
    candidates_query = cur.execute(
        """
        SELECT row_to_json(col)
        FROM(
            SELECT * FROM candidates
            ) col;
        """
    )
    candidates = [candidate[0] for candidate in cur.fetchall()]
    
    if len(candidates) == 0:
        raise Exception("No candidates found in the database")
    else:
        print(candidates)

    try:
        vote_count = 0
        while True:
            # Generate a new voter for each vote
            voter_data = generate_voter_data()
            chosen_candidate = random.choice(candidates)
            
            # Create vote record
            vote = voter_data | chosen_candidate | {
                'voting_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'vote': 1
            }

            try:
                print('User {} is voting for candidate: {}'.format(vote['voter_id'], vote['candidate_id']))
                
                # Insert vote into database
                cur.execute("""
                INSERT INTO votes (voter_id, candidate_id, voting_time)
                VALUES (%s, %s, %s)
                """, (vote['voter_id'], vote['candidate_id'], vote['voting_time']))
                conn.commit()

                # Send vote to Kafka
                producer.produce(topic='votes_topic',
                               key=vote['voter_id'],
                               value=json.dumps(vote),
                               on_delivery=delivery_report
                               )
                producer.poll(0)
                
                vote_count += 1
                print(f"Vote #{vote_count} processed successfully")

            except Exception as e:
                print('Error:', e)
                conn.rollback()
            
            # Wait before generating next vote
            time.sleep(2)

    except KeyboardInterrupt:
        print(f"\nVoting stopped. Total votes generated: {vote_count}")
    except Exception as e:
        print('Error:', e)
    finally:
        cur.close()
        conn.close()

