FROM python:latest
COPY ./app /app
RUN pip install sanic
WORKDIR /app
CMD python main.py
