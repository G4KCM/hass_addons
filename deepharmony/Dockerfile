ARG BUILD_FROM
FROM $BUILD_FROM

RUN mkdir -p /addons/roon-extension-deep-harmony
COPY roon-extension-deep-harmony /addons/roon-extension-deep-harmony/
COPY readme.html /addons/roon-extension-deep-harmony/
COPY run.sh /
RUN chmod 777 /addons/roon-extension-deep-harmony/roon-extension-deep-harmony
RUN chmod a+x /run.sh

CMD [ "./run.sh" ]