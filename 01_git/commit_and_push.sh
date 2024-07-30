#!/bin/bash
set -e

git config --global user.name 'github-actions'
git config --global user.email 'github-actions@github.com'

if ! git diff --exit-code --quiet README.md; then
  git add README.md
  git commit -m 'Update README'
  git push
fi
