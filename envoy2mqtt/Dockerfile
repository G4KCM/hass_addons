ARG BUILD_FROM=hassioaddons/base:7.1.0
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apk add --no-cache python3 py3-requests py3-pip py3-paho-mqtt

COPY envoy.py /
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
