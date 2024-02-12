set fish ~/.config/fish
set functions ~/.config/fish/functions

set -x VISUAL nvim
set -x EDITOR nvim

source $fish/aliases.fish
source $fish/keymaps.fish

source $functions/nvim_cfg_switcher.fish
source $functions/br.fish
source $functions/lfcd.fish
