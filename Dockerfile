FROM arturofc/python-dev-env:latest

COPY requirements.txt /code/
WORKDIR /code

RUN apk --no-cache --update add \
    linux-headers \
    musl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    openssl-dev \
    gcc \
    g++ \
    freetype-dev \
    libpng-dev \
    graphviz

RUN pip install -r requirements.txt

COPY . /code

ENTRYPOINT [ "/bin/bash" ]`