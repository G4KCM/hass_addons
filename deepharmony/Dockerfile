ARG BUILD_FROM=hassioaddons/base:7.1.0
FROM $BUILD_FROM

ENV LANG C.UTF-8

COPY roon-extension-deep-harmony /data/
COPY readme.html /data/
COPY run.sh /data/
RUN chmod a+x /data/roon-extension-deep-harmony
RUN chmod a+x /data/run.sh

WORKDIR /data
CMD [ "./run.sh" ]