ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache libstdc++
RUN apk add libc6-compat gcompat

COPY readme.html /
COPY roon-extension-deep-harmony /
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]