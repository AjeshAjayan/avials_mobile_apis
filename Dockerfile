FROM python:3.7-alpine

RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

COPY requirements.txt /opt/services/djangoapp/src/
RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps linux-headers gcc musl-dev make g++ postgresql-dev && \
    apk add --no-cache jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps
# copy our project code
COPY . /opt/services/djangoapp/src

EXPOSE 8000