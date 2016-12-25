#!/usr/bin/env bash

die() { echo "$@" && exit 1; }
[[ -n $1 ]] && problem=$1 && shift || die "provide problem number"

basedir=$(dirname $0)
export PYTHONPATH=${basedir}:$PYTHONPATH
solution_file=$(printf "%03d" $(echo $problem|sed s/.py//)).py

[[ -f $basedir/env/bin/activate ]] && source $basedir/env/bin/activate
python $basedir/solutions/$solution_file $@
