FROM python:3.9

WORKDIR /code

COPY . .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
ENTRYPOINT ["python3", "-u", "server.py"]