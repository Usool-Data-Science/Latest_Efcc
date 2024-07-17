FROM python:3.10.14-alpine3.20

WORKDIR /usr/src/app

EXPOSE 5000

ENV APP_SECRET_KEY='758f68bd91c339321ea21540b206bcab'

COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#RUN python sample_data.py

# Set the entrypoint to use the virtual environment's python
CMD ["python", "-m", "api.v1.app"]
