#!/bin/sh -Cue


. ../../lib/dot.sh

for CHROME_PROFILE in $CHROME_PROFILES; do

    cat <<EOT | tee "$HOME/.local/share/applications/chrome-$CHROME_PROFILE.desktop"
[Desktop Entry]
Version=1.0
Name=Chrome (${CHROME_PROFILE})
GenericName=Chrome (${CHROME_PROFILE})
Exec=/usr/bin/google-chrome-stable --user-data-dir=.config/google-chrome-$CHROME_PROFILE --class=C$CHROME_PROFILE
StartupNotify=true
Terminal=false
Icon=google-chrome
Type=Application
Categories=Network;WebBrowser;
MimeType=text/html;text/xml;application/xhtml_xml;image/webp;x-scheme-handler/http;x-scheme-handler/https;x-scheme-handler/ftp;
X-MultipleArgs=false
Actions=NewWindow;Incognito;TempProfile;
StartupWMClass=C$CHROME_PROFILE

EOT

done

echo ">>> Chrome profiles created"