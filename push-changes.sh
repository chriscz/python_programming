#!/bin/bash
cp -r website/output/* .
git add --all .
git commit -a -m "update"
