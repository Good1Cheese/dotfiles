#!/usr/bin/env bash

# dmenu_run improved
# command ending with '!', is started in the terminal.

test -s "$HOME"/.dmenurc && . "$HOME"/.dmenurc

cmd="$(dmenu_path | dmenu "$@")"

case $cmd in
    *\!) "${TERMINAL:-alacritty}" -e "${cmd%?}" & ;;
    *)   "${cmd}" & ;;
esac
