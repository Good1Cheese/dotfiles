#
# ~/.bash_profile
#

if [ -z "$DISPLAY" ] && [ "$XDG_VTNR" = 1 ]; then
  exec startx
fi

export XMODIFIERS=fcitx
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx

[[ -f ~/.bashrc ]] && . ~/.bashrc
