ARG BUILD_FROM
FROM $BUILD_FROM

COPY roon-extension-deep-harmony /
COPY readme.html /
RUN chmod a+x /run.sh
CMD [ "/run.sh" ]