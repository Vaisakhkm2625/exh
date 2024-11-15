sleep 5
xclip -o -selection clipboard >/tmp/cliptypetext
ydotool type --delay 250 --file /tmp/cliptypetext
