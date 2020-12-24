FROM python:latest
RUN apt update
COPY packages.txt /packages.txt
RUN apt install -y $(cat packages.txt | tr '\n' ' ')
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000
CMD python main.py
