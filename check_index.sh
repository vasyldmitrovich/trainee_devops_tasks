#!/bin/bash

# Check that file index.html is in repo
if [ -f index.html ]; then
  echo "index.html exists"
  exit 0
else
  echo "index.html does not exist"
  exit 1
fi
