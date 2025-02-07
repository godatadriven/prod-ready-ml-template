#!bin/bash

# Remove all files on the final branch that should not be on the main branch

rm pyproject.toml
rm uv.lock
rm .pre-commit-config.yaml
rm -r app
rm -r cli
rm -r src
rm -r tests
rm -r .github

rm rm-solutions.sh
