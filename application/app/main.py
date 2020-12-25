import time
from os import environ as env

import psycopg2
from sanic import Sanic
from sanic.response import text
from sanic.log import logger

app = Sanic("FBK application")
db_config = f"dbname={env['POSTGRES_DB']} user={env['POSTGRES_USER']} password={env['POSTGRES_PASSWORD']} host=postgres"

connection = None
while connection is None:
    try:
        connection = psycopg2.connect(db_config)
        logger.info("Connected to DB server.")
        connection.close()
    except:
        logger.info("Waiting for DB server...")
        time.sleep(1)

with psycopg2.connect(db_config) as connection:
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS post_data (
                            id serial PRIMARY KEY,
                            ts TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                            data text);""")

@app.post("/")
def index(request):
    with psycopg2.connect(db_config) as connection:
        with connection.cursor() as cursor:
            logger.info(request.body)
            cursor.execute("INSERT INTO post_data (data) VALUES (%s);", (request.body.decode(),))
    return text(
        f"Connected to {request.url_for('index')}\n"
        f"{env['POSTGRES_PASSWORD']} {env['POSTGRES_USER']} \n"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, workers=8, access_log=True)
