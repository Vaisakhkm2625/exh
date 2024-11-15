sleep 5
xclip -o -selection clipboard >/tmp/cliptypetext
xdotool type --delay 250 --file /tmp/cliptypetext
