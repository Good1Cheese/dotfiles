# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

if [ -f ~/.bash_aliases ]; then
. ~/.bash_aliases
fi

# export EDITOR="devour neovide --no-fork"

# export PATH="/home/cheese/.local/share/gem/ruby/3.0.0/bin:$PATH"
export PATH="/root/.local/share/gem/ruby/3.0.0/bin:$PATH"
# Install Ruby Gems to ~/gems
export GEM_HOME="$HOME/gems"
export PATH="$HOME/gems/bin:$PATH"
# Install Ruby Gems to ~/gems
export GEM_HOME="$HOME/gems"
export PATH="$HOME/gems/bin:$PATH"
