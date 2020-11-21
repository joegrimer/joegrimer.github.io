#!/bin/bash

LAST_FILE="test"
PARENT="test"
for i in {1..999}
  do
  python3 "$LAST_FILE.py"
  if [ $? -gt 0 ] ; then
    echo Failed
    LAST_FILE="$PARENT" # i.e. go back
  else
    echo succeeded
    PARENT="$LAST_FILE"
    LAST_FILE="$LAST_FILE""n"
  fi
done
echo "last file:$LAST_FILE"
echo "parent:$PARENT"
