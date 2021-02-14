FROM python:3.7-slim

RUN apt-get update

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . .

CMD ["gunicorn", "flaskr:create_app()", "-b", "0.0.0.0:5000", "-w", "3"]
