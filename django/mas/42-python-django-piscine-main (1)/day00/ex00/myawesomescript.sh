#!/bin/sh

curl -slI $1 | grep -E "Location:|location:" | cut -d ':' -d ' ' -f 2-
