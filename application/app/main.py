from os import environ as env

from sanic import Sanic
from sanic.response import text

app = Sanic("endpoint")

@app.get("/")
def index(request):
    return text(
        f"{request.remote_addr} connected to {request.url_for('index')}\n"
        f"Forwarded: {request.forwarded}\n"
        f"{env['POSTGRES_PASSWORD']} {env['POSTGRES_USER']} \n"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, workers=8, access_log=True)
