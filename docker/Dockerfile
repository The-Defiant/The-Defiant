FROM python:3.10.5

ARG VERSION=0.1.0
ARG PACKAGE="defiant_backend-${VERSION}-py3-none-any.whl"
WORKDIR /app
COPY dist/ /app/dist/

RUN python -m pip upgrade pip
RUN python -m pip install -e dist/$PACKAGE

