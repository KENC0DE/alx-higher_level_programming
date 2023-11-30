#!/bin/bash
# displays the size of the body of the response
curl -s -w "%{size_download}" -X GET "$1"
