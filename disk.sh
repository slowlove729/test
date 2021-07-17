#! /bin/sh

DISK_LEFT=`df -P | grep -v ^Filesystem | awk '{sum += $4} END { print sum/1024/1024 " GB" }'`

echo "남은 용량 : $DISK_LEFT"
