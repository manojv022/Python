#!/bin/bash
THRESHOLD=80
usage=$(df / | grep / | awk '{ print $5 }' | sed 's/%//g')
if [ $usage -gt $THRESHOLD ]; then
  echo "Disk space critical: $usage%" | mail -s "Disk Alert" admin@example.com
fi
