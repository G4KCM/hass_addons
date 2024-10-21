ARG BUILD_FROM
FROM ${BUILD_FROM}

ENV LANG C.UTF-8

RUN apk add --no-cache python3
RUN pip install "paho-mqtt==1.6.1"
COPY comfort2.py /
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
