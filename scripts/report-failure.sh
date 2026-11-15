#!/usr/bin/env bash
# Identical in socialapi-go, socialapi-python and socialapi-typescript.
# Opens one regeneration-failed issue, or comments on the open one. Needs GH_TOKEN.
set -euo pipefail
run="$GITHUB_SERVER_URL/$GITHUB_REPOSITORY/actions/runs/$GITHUB_RUN_ID"
open=$(gh issue list --label regeneration-failed --state open --json number -q '.[0].number')
if [ -n "$open" ]; then
  gh issue comment "$open" --body "Failed again: $run"
else
  gh label create regeneration-failed --color B60205 --force
  gh issue create --title "SDK regeneration failed" --label regeneration-failed \
    --body "The release workflow failed and nothing was published: $run"
fi
