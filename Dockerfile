# Use the official Debian image as a base
FROM python:3.8-buster

# Install dependencies
RUN apt-get update && apt-get install -y \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libsasl2-dev \
    libldap2-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    libjpeg-dev \
    libpq-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    libfreetype6-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip3 install pip setuptools wheel Cython==3.0.0a10
RUN pip3 install gevent==20.9.0 --no-build-isolation
RUN pip3 install -r requirements.txt

COPY . .

RUN mkdir /usr/src/app/config

EXPOSE 8069

# Run the application
CMD ["python3", "./odoo-bin", "-i", "base", "--config=/usr/src/app/config/odoo.conf"]