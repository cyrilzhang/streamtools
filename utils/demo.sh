#!/bin/bash
./utils/stream.sh | python -m streamtools.demos.$1 ${@:2}
