# !/bin/sh

python ./RequestResponse_Server.py &

for ((i=1; i<=5; i++));
do
    echo "[sh 실행] :" $i
    python ./RequestResponse_Client.py
done