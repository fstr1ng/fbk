FROM python:latest
RUN apt-get update
COPY packages.txt /packages.txt
RUN apt-get install -y $(cat packages.txt | tr '\n' ' ')
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000
CMD python main.py
