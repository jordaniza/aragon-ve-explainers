# Aragon: wtf is ve?

This is a collection of scenes using the manim library that illustrate:
    - VE tokenomics
    - Gauges
    - Reward mechanisms

## Usage

Manim is not an easy library to install across multiple systems - so we have isolated system and python dependencies into a single shell.nix file. Simply ensure `nix shell` is installed and run:

```sh
nix-shell
```

To start an isolated environment.

To render a scene, just run:

```sh
manim scenes/MY_SCENE.py
```

where `MY_SCENE` should be replaced by your scene.

