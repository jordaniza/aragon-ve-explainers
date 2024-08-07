{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.python3Packages.pylint
    pkgs.python3Packages.manim
    pkgs.python3Packages.pycairo
    pkgs.ffmpeg
    pkgs.pango
  ];
}
