#!/bin/sh
[ ! -d "/addons/deepharmony" ] && mkdir /addons/deepharmony
if [ -f "/roon-extension-deep-harmony" ]; then
    mv ./roon-extension-deep-harmony /addons/deepharmony
fi
if [ -f "/readme.html" ]; then
    mv ./readme.html /addons/deepharmony
fi
cd /addons/deepharmony || exit
until env DEBUG="*" ./roon-extension-deep-harmony; do
    echo "roon-extension-deep-harmony terminated with exit code $?.  Restarting.." >&2
    if [ -f ./roon-extension-deep-harmony.old ]; then
        rm ./roon-extension-deep-harmony.old
    fi
    if [ -f ./downloads/roon-extension-deep-harmony ]; then
        mv ./roon-extension-deep-harmony ./roon-extension-deep-harmony.old
        mv ./downloads/roon-extension-deep-harmony ./roon-extension-deep-harmony
        chmod 777 ./roon-extension-deep-harmony
        rm ./readme.html
        mv ./downloads/readme.html ./readme.html
    fi
    sleep 1
done
