FROM httpd:2.4

RUN apt-get update \
    && apt install -y python3 python3-pip python3-venv

RUN apt-get install -y libapr1 libapr1-dev
RUN apt install -y libapache2-mod-wsgi-py3

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
RUN pip install mod-wsgi-httpd
COPY src/requirements.txt .
RUN pip install -r requirements.txt
RUN echo 'Include conf/extra/wsgi.conf' >> /usr/local/apache2/conf/httpd.conf
COPY wsgi.conf /usr/local/apache2/conf/extra/wsgi.conf
COPY src/ /app/