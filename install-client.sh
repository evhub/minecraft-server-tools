#!/usr/bin/env sh
git pull
py -3 -m pip install -Ue .
py -3 -m minecraft_server_tools.install_client
