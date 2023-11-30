#!/bin/bash
# displays the body of the response
curl -sH "email: test@gmail.com" -H "subject: I will always be here for PLD" -X POST "$1"
