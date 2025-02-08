#!/bin/sh

python ./Async_Server.py &

sleep 2

python ./Async_Client_Sleep.py & 
sleep 1
python ./Async_Client_NonSleep.py &
