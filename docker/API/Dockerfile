FROM python:3.8-slim

WORKDIR /home
COPY ./requirements.txt /home/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /home/

WORKDIR /home/fastapi
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]