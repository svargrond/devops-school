#!/bin/sh -l

echo "$INPUT_USER_VALUE"
echo "$USER_VALUE"
echo "${{ env.USER_VALUE }}"

echo "EXECUTING PYTHON SCRIPT..."
python3 /main.py

echo "ls -lah"
ls -lah

echo "pwd"
pwd

echo "ls -lah /github/workspace"
ls -lah /github/workspace
