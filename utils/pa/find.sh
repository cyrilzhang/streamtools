#!/bin/bash

# find.sh: list devices
pactl list | grep Name: | awk '{print $2}'