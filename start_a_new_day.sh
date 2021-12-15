#!/bin/env bash
LAST_DAY=$(fd "day" --type directory --max-depth=1 | sort | tail -1 | tr -d -c 0-9)
echo "----- most recent day is $LAST_DAY"
TEMP=$(( LAST_DAY + 1 )) 

if [[ $TEMP -le 10 ]]; then
    NEW_DAY="day_0${TEMP}"
else
    NEW_DAY="day_${TEMP}"
fi

echo "----- going to create folder for $NEW_DAY"
mkdir "$NEW_DAY"
cp -R template/* "$NEW_DAY/"

echo "----- new folder created"
echo "----- renaming the files with $NEW_DAY"
fd -g '*NEW*' -E "template" | while read -r LINE; do
    NEW_PATH=$(echo "$LINE" | sed "s/NEW/03/")
    mv "$LINE" "$NEW_PATH"
done
