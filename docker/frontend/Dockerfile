FROM python:3.9-slim

FROM python:3.8-slim

WORKDIR /home
RUN pip install --no-cache-dir --upgrade dash requests

COPY ./frontend/ /home/

CMD ["python", "main.py"]
