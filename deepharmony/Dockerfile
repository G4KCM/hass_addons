ARG BUILD_FROM
FROM $BUILD_FROM

COPY roon-extension-deep-harmony /addons/deepharmony/
COPY readme.html /addons/deepharmony/
COPY run.sh /
RUN chmod 777 /addons/deepharmony/roon-extension-deep-harmony
RUN chmod a+x /run.sh

CMD [ "./run.sh" ]