config.bind("pt", "tab-pin")
config.bind(";w", "hint links spawn --detach mpv --force-window yes {hint-url}")
config.bind(";W", "spawn --detach mpv --force-window yes {url}")
config.bind(
    ";I",
    'hint images spawn --output-messages wget -P "/home/cheese/Pictures/" {hint-url}',
)

# Bindings for normal mode
config.bind("`", "bookmark-add")
config.bind("~", "bookmark-del")

config.bind("M", "hint links spawn mpv {hint-url}")
config.bind("Z", "hint links spawn st -e youtube-dl {hint-url}")
config.bind("t", "cmd-set-text -s :open -t")
config.bind("xb", "config-cycle statusbar.show always never")
config.bind("xt", "config-cycle tabs.show always never")
config.bind(
    "xx",
    "config-cycle statusbar.show always never;; config-cycle tabs.show always never",
)
