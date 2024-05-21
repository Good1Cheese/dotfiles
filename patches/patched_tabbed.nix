with import <nixpkgs> { };

(tabbed.overrideAttrs (oldAttrs: rec {
  patches = [
    /home/cheese/dotfiles/patches/p-tabbed/cwd.diff
    /home/cheese/dotfiles/patches/p-tabbed/autohide-20.diff
    /home/cheese/dotfiles/patches/p-tabbed/keyrelease-20.diff
    /home/cheese/dotfiles/patches/p-tabbed/hidetabs-20.diff
  ];
}))
