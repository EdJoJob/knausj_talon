tag: terminal
and tag: user.cli
-
edit: "vi "
search: "rg "
file: "fd "

kill all:
  key(ctrl-c)
rerun search:
  key(ctrl-r)
rerun <user.text>:
  key(ctrl-r)
run last:
  key(up)
  key(enter)
suspend:
  key(ctrl-z)
resume:
  insert("fg")
  key(enter)
