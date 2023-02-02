#!/bin/bash

pip install -r requirements.txt

chmod u+x ./main.py 
mkdir -p $HOME/.local/bin
cp ./main.py $HOME/.local/bin/pns

echo make sure that $HOME/.local/bin is in our PATH