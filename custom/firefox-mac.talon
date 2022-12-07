os: mac
app: firefox
-
# Self-signed SSL
accept warning:
    key(tab space)
    sleep(100ms)
    key(tab tab tab space)

new child: key(cmd-y)
new sib: key(cmd-shift-y)

toggle dark: key(alt-shift-a)
toggle global dark: key(alt-shift-d)
