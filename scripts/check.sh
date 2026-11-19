#!/bin/sh
set -eu
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
