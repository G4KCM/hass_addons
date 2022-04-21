#!/bin/sh
if [  ! -d /addons/roon-extension-deep-harmony ]; then
    mkdir /addons/roon-extension-deep-harmony
    cp dh.sh /addons/roon-extension-deep-harmony/
    chmod a+x /addons/roon-extension-deep-harmony/dh.sh
    cp roon-extension-deep-harmony /addons/roon-extension-deep-harmony/
    chmod a+x /addons/roon-extension-deep-harmony/roon-extension-deep-harmony
    cp readme.html /addons/roon-extension-deep-harmony/
fi
cd /addons/roon-extension-deep-harmony
./dh.sh