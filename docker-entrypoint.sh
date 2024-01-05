#!/bin/bash

# python app/bot.py &
python -u app/worker.py &

wait -n

exit $?