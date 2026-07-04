#!/bin/bash

echo "Stopping IDaddy AI..."

pkill -f "uvicorn backend.main:app --host 0.0.0.0 --port 8001"

sleep 2

echo "Done."
