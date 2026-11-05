#!/usr/bin/env bash
# Lesson 29: the smallest honest backup for the course stack.
# Backs up: the Postgres database, the n8n data volume (files and
# the encryption key material in .n8n config), into a dated folder.
# NOT covered, deliberately, so you must decide them: off-site copy,
# retention, and restore rehearsals. An untested backup is a rumour.
set -euo pipefail

STAMP=$(date +%Y%m%d-%H%M)
DEST="${1:-./backups/$STAMP}"
mkdir -p "$DEST"

echo "Dumping database..."
docker compose exec -T db pg_dump -U "$DB_USER" "$DB_NAME" > "$DEST/db.sql"

echo "Archiving n8n data volume..."
docker run --rm -v ai-automation-with-n8n_n8n_data:/data:ro \
  -v "$PWD/${DEST#./}":/backup alpine \
  tar czf /backup/n8n_data.tar.gz -C /data .

echo "Backup written to $DEST"
echo "Now: copy it off this machine, and rehearse a restore quarterly."
