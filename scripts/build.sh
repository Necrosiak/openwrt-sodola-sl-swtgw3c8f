#!/usr/bin/env bash
set -euo pipefail
root=$(cd -- "$(dirname -- "$0")/.." && pwd)
build=${1:-"$root/build"}
shift || true
python3 "$root/scripts/prepare.py" "$build" "$@"
cd "$build"
make -j"${JOBS:-2}" download
make -j"${JOBS:-2}" || make -j1 V=s
