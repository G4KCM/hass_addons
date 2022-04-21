ARG BUILD_FROM
FROM $BUILD_FROM

COPY roon-extension-deep-harmony /share/roon-extension-deep-harmony/
COPY readme.html /share/roon-extension-deep-harmony/
COPY run.sh /
RUN chmod 777 /share/roon-extension-deep-harmony/roon-extension-deep-harmony
RUN chmod a+x /run.sh

CMD [ "./run.sh" ]