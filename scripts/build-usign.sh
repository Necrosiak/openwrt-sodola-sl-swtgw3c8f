#!/usr/bin/env bash
set -euo pipefail
build=${1:?build directory required}
mkdir -p "$build"
git -C "$build" init -q
git -C "$build" remote add origin https://git.openwrt.org/project/usign.git
git -C "$build" fetch --depth=1 origin c4c72b1b07945ee192361dc751291a7c98d6adcd
git -C "$build" checkout --detach FETCH_HEAD
cmake -S "$build" -B "$build/out" -DUSE_LIBUBOX=OFF
cmake --build "$build/out" -j2
