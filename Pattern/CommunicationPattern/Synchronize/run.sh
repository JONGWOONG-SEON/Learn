#!/bin/sh

python ./Sync_Server.py &

python ./Sync_Client_Sleep.py
python ./Sync_Client_NonSleep.py
