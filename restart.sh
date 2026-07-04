#!/bin/bash

cd /root/idaddy_ai || exit 1

./stop.sh

sleep 2

exec ./start.sh
