ARG BUILD_FROM
FROM $BUILD_FROM

COPY roon-extension-deep-harmony /
COPY readme.html /
COPY dh.sh /
COPY run.sh /
RUN chmod a+x /run.sh
CMD [ "/run.sh" ]