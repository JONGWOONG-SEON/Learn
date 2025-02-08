#!/bin/sh

python ./Sync_Server.py &
sleep 2
python ./Sync_Client_Sleep.py &
sleep 1
python ./Sync_Client_NonSleep.py &
