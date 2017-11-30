#!/bin/bash

cd $(dirname $0)
SRC_DIR=src
SRC_FILE=$SRC_DIR/main.py

function clean () {
 echo "TODO implement this command"
}

function run () {
  python $SRC_FILE
}

function watch () {
  run &
  while true
  do
    FORMAT=$(echo -e "\033[1;33m%w%f\033[0m written at $(date +'%r')")
    inotifywait -qre close_write --format "$FORMAT" $SRC_DIR
    pkill -SIGKILL -xf "python $SRC_FILE"
    run &
  done
}


if ! [ ${VIRTUAL_ENV} ]
then
  echo WARNING: virtualenv not sourced
  exit 1
fi
if [[ `type -t $1` == 'function' ]]
then
  $1
else
  echo "usage: clean | run | watch"
fi
