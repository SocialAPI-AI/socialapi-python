#!/usr/bin/env bash
# Identical in socialapi-go, socialapi-python and socialapi-typescript.
#
# Usage: scripts/next-version.sh <first-version> <package path>...
# Prints the version to release, or nothing when the package paths match the
# last release tag. The bump comes from oasdiff on the spec at that tag:
# a breaking change bumps minor before 1.0 (major after), anything else patch.
set -euo pipefail
first=$1; shift

git add -A -- "$@" # so new, untracked generated files count as changes
last=$(git tag -l 'v[0-9]*.[0-9]*.[0-9]*' --sort=-v:refname | head -1)
# No tag, or a tag from before generation (no spec in it): first generated release.
if [ -z "$last" ] || ! git cat-file -e "$last:openapi.json" 2>/dev/null; then
  echo "$first"
  exit 0
fi
if git diff --cached --quiet "$last" -- "$@"; then
  exit 0
fi

IFS=. read -r major minor patch <<<"${last#v}"
base=$(mktemp)
git show "$last:openapi.json" >"$base"
if oasdiff breaking "$base" openapi.json --fail-on ERR >/dev/null; then
  echo "$major.$minor.$((patch + 1))"
elif [ "$major" -ge 1 ]; then
  echo "$((major + 1)).0.0"
else
  echo "$major.$((minor + 1)).0"
fi
