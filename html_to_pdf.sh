#!/bin/sh

chromium --headless --disable-gpu --no-margins --print-to-pdf-no-header --print-to-pdf="$1" $2
