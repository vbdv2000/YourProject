#!/bin/bash
if [ "$PROD" != 1 ]; then
    # Dev mode
    echo "Running Dev"
    python -u -Xfrozen_modules=off \
        -m debugpy --listen 0.0.0.0:5678 \
        -m uvicorn --reload \
            --host 0.0.0.0 --port 8000 \
            --workers 1 \
            YourProject.main:app
else
    # PROD
    echo "Running Production Server"
    python -u -Xfrozen_modules=off \
        -m uvicorn \
            --host 0.0.0.0 --port 8000 \
            --workers 1 \
            YourProject.main:app
fi