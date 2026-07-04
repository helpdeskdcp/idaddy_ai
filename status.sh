#!/bin/bash

unset VIRTUAL_ENV
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
hash -r

cd /root/idaddy_ai || exit 1

source /root/idaddy_ai/venv/bin/activate

echo "========== IDaddy AI Status =========="
echo "Project : $(pwd)"
echo "Python  : $(which python)"
echo "VENV    : $VIRTUAL_ENV"

echo
echo "Git Branch:"
git branch --show-current

echo
echo "Git Status:"
git status --short

echo
echo "Uvicorn:"
pgrep -af "uvicorn backend.main:app" || echo "Not Running"

echo
echo "Health:"
curl -s http://127.0.0.1:8001/health || echo "API Not Running"

echo
echo "======================================"
