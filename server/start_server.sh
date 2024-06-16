#!/bin/sh

# check if ../.env has been sourced or not
if [ -z $SYSTEM_PROTOCOL ];then
	echo -e "\n\n\ncustomize and source ../.env before starting this script to have a working configuration\n\n\n"
fi

# Use FLASK_DEBUG=True if needed

FLASK_APP="$(dirname "$(readlink -f "$0")")"/standalone.py python3 -m flask run --host 0.0.0.0 $(if [ -n "$FLASK_PORT" ];then echo --port "$FLASK_PORT"; fi) --with-threads
