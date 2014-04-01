#!/bin/bash

# demo.sh: run demo in library
python -m streamtools.demos.$1 ${@:2}
