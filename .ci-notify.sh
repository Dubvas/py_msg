#!/bin/bash

TELEGRAM_BOT_TOKEN=$2
TELEGRAM_USER_ID=$3
TIME="10"
TURL="https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage"

send_msg() {
  curl -s --max-time $TIME -d'parse_mode=HTML' \
    -d "chat_id=$TELEGRAM_USER_ID&disable_web_page_preview=1" \
    -d "text=$1" \
    $TURL #> /dev/null
}

REPOSITORY=$GITHUB_REPOSITORY
BRANCH=$(echo ${GITHUB_REF#refs/heads/})
USER=$GITHUB_ACTOR
SHA=$(echo $GITHUB_SHA | cut -c1-7)
COMMIT_MESSAGE=$4
ACTION_URL="$GITHUB_SERVER_URL/$GITHUB_REPOSITORY/actions/runs/$GITHUB_RUN_ID"

TEXT="<b>github action status:</b> $1%0A%0A<b>Project:</b>  <code>$REPOSITORY</code>%0A<b>Branch:</b>  <code>$BRANCH</code>%0A<b>User:</b>       <code>$USER</code>%0A<b>Commit:</b> <code>$SHA</code>%0A%0A<i>$COMMIT_MESSAGE</i>%0A%0A<b>URL:</b> $ACTION_URL/"

send_msg "$TEXT"