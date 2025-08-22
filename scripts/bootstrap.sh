#!/usr/bin/env bash
set -euo pipefail
echo "Starting Shuffle locally..."
docker compose up -d
echo "Now: create a Webhook in Shuffle and paste its URL into wazuh/config/ossec.conf"
