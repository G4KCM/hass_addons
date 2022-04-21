ARG BUILD_FROM
FROM $BUILD_FROM

COPY roon-extension-deep-harmony /
COPY readme.html /
COPY run.sh /
RUN chmod 777 /roon-extension-deep-harmony
RUN chmod a+x /run.sh

CMD [ "./run.sh" ]