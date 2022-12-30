{ pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/nixos-22.11.tar.gz") {} }:

pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (ps: [
      ps.tkinter
      ps.numpy
      ps.matplotlib
      ps.sympy
    ]))

    pkgs.vim
    pkgs.sqlite
    pkgs.tmux
    pkgs.ganttproject-bin
  ];
}
