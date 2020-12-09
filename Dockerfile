FROM python:3.8-slim

RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app/
COPY . /usr/src/app/

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r config/requirements.txt

CMD ["python", "start.py"]
 
