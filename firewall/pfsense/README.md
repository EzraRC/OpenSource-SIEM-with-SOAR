# pfSense notes

- Export sanitized XML at **Diagnostics → Backup & Restore** and store here.
- Set up **Syslog**: Status → System Logs → Settings → Remote Logging Options → send to Wazuh manager (UDP/514).
- For SOAR containment:
  - Use the **pfSense API** package (preferred) _or_ SSH with `pfctl`.
  - Maintain a dedicated alias (e.g., `SOAR_BLOCKLIST`) that Shuffle updates.
