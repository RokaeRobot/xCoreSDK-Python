#!/usr/bin/env bash
set -euo pipefail

VERSION="${1:?Usage: $0 <version>}"
OUTPUT_DIR="${2:-dist}"
PY_TAG="py38"

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$ROOT/$OUTPUT_DIR"

LINUX_DIR="rokae_SDK_linux_v${VERSION}_${PY_TAG}"
WIN_DIR="rokae_SDK_win_v${VERSION}_${PY_TAG}"

pack_targz() {
    local name="$1" dir="$2"
    if [[ ! -d "$ROOT/$dir/lib" ]]; then
        echo "WARNING: Skipping missing path: $dir/lib" >&2
        return 0
    fi
    local tar_path="$ROOT/$OUTPUT_DIR/$name"
    rm -f "$tar_path"
    tar -czf "$tar_path" -C "$ROOT" "$dir/lib"
    echo "Created $tar_path"
}

pack_zip() {
    local name="$1" dir="$2"
    if [[ ! -d "$ROOT/$dir/lib" ]]; then
        echo "WARNING: Skipping missing path: $dir/lib" >&2
        return 0
    fi
    local zip_path="$ROOT/$OUTPUT_DIR/$name"
    rm -f "$zip_path"
    (cd "$ROOT" && zip -rq "$zip_path" "$dir/lib")
    echo "Created $zip_path"
}

pack_targz "xCoreSDK-Python-${VERSION}-linux-${PY_TAG}.tar.gz" "$LINUX_DIR"
pack_zip "xCoreSDK-Python-${VERSION}-win-${PY_TAG}.zip" "$WIN_DIR"

echo ""
echo "Done. Upload $OUTPUT_DIR/* to GitHub Release v${VERSION}"
