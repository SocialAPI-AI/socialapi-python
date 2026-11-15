#!/usr/bin/env bash
# Identical in socialapi-go, socialapi-python and socialapi-typescript.
#
# Commits the regenerated SDK to main. When PUBLISH is true and VERSION is set,
# also tags vVERSION and creates a GitHub Release whose notes are the oasdiff
# changelog since the previous tag. Needs GH_TOKEN.
set -euo pipefail

git config user.name "github-actions[bot]"
git config user.email "41898341+github-actions[bot]@users.noreply.github.com"
git add -A
if git diff --cached --quiet; then
  echo "Nothing to commit"
else
  msg="chore: regenerate SDK"
  [ "${PUBLISH:-}" = "true" ] && [ -n "${VERSION:-}" ] && msg="chore: release v$VERSION"
  git commit -qm "$msg"
  git push origin HEAD:main
fi

if [ "${PUBLISH:-}" != "true" ] || [ -z "${VERSION:-}" ]; then
  echo "Not releasing (PUBLISH=${PUBLISH:-unset}, VERSION=${VERSION:-none})"
  exit 0
fi

last=$(git tag -l 'v[0-9]*.[0-9]*.[0-9]*' --sort=-v:refname | head -1)
notes=$(mktemp)
if [ -n "$last" ]; then
  base=$(mktemp)
  git show "$last:openapi.json" >"$base"
  oasdiff changelog "$base" openapi.json >"$notes" || true
fi
[ -s "$notes" ] || echo "Generated from the SocialAPI OpenAPI spec." >"$notes"

git tag -a "v$VERSION" -m "v$VERSION"
git push origin "v$VERSION"
gh release create "v$VERSION" --title "v$VERSION" --notes-file "$notes"
