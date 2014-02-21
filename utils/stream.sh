#!/bin/bash

exists () {
    type "$1" >/dev/null 2>/dev/null
}

cd $(dirname $0)

if exists pacat; then
    ./pastream.sh
elif exists sox; then
    ./soxstream.sh
else
    echo "stream.sh: can't stream" >&2
fi

