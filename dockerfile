FROM ubuntu

WORKDIR /usr/src/app

COPY . .

RUN apt-get update && apt-get install -y python3-pip

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "api.v1.app"]