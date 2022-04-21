#!/bin/sh
until env DEBUG="*" ./data/roon-extension-deep-harmony; do
    echo "roon-extension-deep-harmony terminated with exit code $?.  Restarting.." >&2
    if [ -f ./data/roon-extension-deep-harmony.old ]; then
        rm ./data/roon-extension-deep-harmony.old
    fi
    if [ -f ./data/downloads/roon-extension-deep-harmony ]; then
        mv ./data/roon-extension-deep-harmony ./data/roon-extension-deep-harmony.old
        mv ./data/downloads/roon-extension-deep-harmony ./data/roon-extension-deep-harmony
        chmod 777 ./data/roon-extension-deep-harmony
        rm ./data/readme.html
        mv ./data/downloads/readme.html ./readme.html
    fi
    sleep 1
done
