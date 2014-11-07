#!/bin/bash

# Easy screen clear
alias cls=clear

# Prepare MP3 and OGG files for Amarok tagging
# alias a_amarok_afttagger='find . -iname "*.ogg" -o -iname "*.mp3" -exec amarok_afttagger -qv {} \;'
alias a_amarok_afttagger='find . -iname \*.ogg -o -iname \*.wma -o -iname \*.mp3 -exec amarok_afttagger -qv {} \;'

alias ls="ls -F"
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Find entry in history list
alias histfind='history | grep $@'

# Ignore case and search only for the 
alias locate='locate --ignore-case --basename'