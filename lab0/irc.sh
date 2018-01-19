#!/bin/sh
# Copyright 2014 Vivien Didelot <vivien@didelot.org>
# Licensed under the terms of the GNU GPL v3, or any later version.

NICK=guesswho
SERVER=irc.freenode.net
PORT=6667
CHAN="#iitpkd"

{
  # join channel and say hi
  cat << IRC
NICK $NICK
nc $SERVER $PORT
USER irccat 8 x : irccat
JOIN $CHAN
PRIVMSG $CHAN :message  
IRC

  echo QUIT
} | nc $SERVER $PORT | while read line ; do
  case "$line" in
    *PRIVMSG\ $CHAN\ :*) echo "$line" | cut -d: -f3- ;;
    #*) echo "[IGNORE] $line" >&2 ;;
  esac
done
