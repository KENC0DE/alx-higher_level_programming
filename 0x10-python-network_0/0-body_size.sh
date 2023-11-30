#!/usr/bin/bash
curl -s -w "%{size_download}" -X GET "$1"
