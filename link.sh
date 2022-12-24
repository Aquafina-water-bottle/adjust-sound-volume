#!/usr/bin/env bash

# script taken from anki-connect

plugin_name=AdjustSoundVolume
plugin_path_linux=~/.local/share/Anki2/addons21
plugin_path_mac=~/Library/Application\ Support/Anki2/addons21

if [ -d "$plugin_path_linux" ]; then
    ln -s -f $(pwd) $plugin_path_linux/$plugin_name
fi

if [ -d "$plugin_path_mac" ]; then
    ln -s -f $(pwd) $plugin_path_mac/$plugin_name
fi

