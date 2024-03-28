set fish ~/.config/fish
set functions ~/.config/fish/functions

# fish_add_path /home/cheese/.local/share/gem/ruby/3.0.0/bin
fish_add_path /root/.local/share/gem/ruby/3.0.0/bin/

set -x VISUAL nvim
set -x EDITOR nvim

set -x CM_SELECTIONS "clipboard"
set -x CM_DEBUG 1
set -x CM_OUTPUT_DEBUG 0
set -x CM_MAX_CLIPS 10

source $fish/aliases.fish
source $fish/keymaps.fish

source $functions/nvim_cfg_switcher.fish
source $functions/br.fish
source $functions/lfcd.fish
