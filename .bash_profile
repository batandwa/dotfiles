# Start a screen as soon as you login
if [ -z "$STY" ]; then /usr/bin/screen -dRRS $USER; fi