#!/usr/bin/env bash
# Regenerates src/socialapi from openapi.json. The generator replaces the whole
# package directory, so hand-written modules live in extras/ and are copied in.
set -euo pipefail
cd "$(dirname "$0")/.."
uvx --from openapi-python-client==0.30.0 --with ruff==0.14.5 openapi-python-client generate \
  --path openapi.json --config openapi-python-client.yaml --custom-template-path templates --meta none \
  --output-path src/socialapi --overwrite
cp extras/*.py src/socialapi/
touch src/socialapi/py.typed
