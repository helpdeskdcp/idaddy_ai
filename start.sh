#!/bin/bash

unset VIRTUAL_ENV
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
hash -r

cd /root/idaddy_ai || exit 1

source /root/idaddy_ai/venv/bin/activate

if pgrep -f "uvicorn backend.main:app" >/dev/null; then
    echo "IDaddy AI is already running."
    ./status.sh
    exit 0
fi

echo "=================================="
echo "IDaddy AI Starting..."
echo "=================================="
echo "Project : $(pwd)"
echo "Python  : $(which python)"
echo "VENV    : $VIRTUAL_ENV"
echo "=================================="

exec uvicorn backend.main:app \
    --host 0.0.0.0 \
    --port 8001 \
    --reload
