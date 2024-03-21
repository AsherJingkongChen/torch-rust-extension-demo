#! /usr/bin/env python3

"""
Development

## Usage

1.
```shell
./scripts/dev.py
```

2.
```shell
python3 scripts/dev.py
```
"""


def dev():
    from subprocess import run
    from util_env import Env

    python = Env().data.executable

    run([python, "-m", "maturin", "develop", "--skip-install"], check=True)
    run([python], check=True)


if __name__ == "__main__":
    dev()
