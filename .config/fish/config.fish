# atuin init fish | source
# set -x HISTFILE $HOME/.local/share/fish/fish_history | atuin import fish

eval "$(direnv hook fish)"

set fish ~/.config/fish
set functions ~/.config/fish/functions

fish_add_path ~/.local/share/gem/ruby/3.1.0/bin

# any-nix-shell fish --info-right | source

set -x VISUAL nvim
set -x EDITOR devour neovide --no-fork
# set -x EDITOR nvim

set -x XMODIFIERS fcitx
set -x GTK_IM_MODULE fcitx
set -x QT_IM_MODULE fcitx

set -x CM_SELECTIONS "clipboard"
set -x CM_DEBUG 1
set -x CM_OUTPUT_DEBUG 0
set -x CM_MAX_CLIPS 10

set -x DIRENV_LOG_FORMAT ""

source $fish/aliases.fish
source $fish/keymaps.fish

source $functions/greeting.fish
source $functions/xorg_on_startup.fish
source $functions/nvim_cfg_switcher.fish
source $functions/lfcd.fish
source $functions/yy.fish
