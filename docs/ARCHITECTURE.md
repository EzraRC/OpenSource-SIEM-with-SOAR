# Architecture (Wazuh + Shuffle + pfSense)

## Flow
1) **pfSense** and sensors (Suricata/Zeek) send syslog/EVE to **Wazuh Manager**.
2) **Wazuh rules/decoders** normalise and score alerts.
3) **Wazuh integration** (custom-shuffle) forwards high-confidence alerts (JSON) to **Shuffle** webhook.
4) **Shuffle** enriches (VT/WHOIS), decides, and updates **pfSense alias**; creates ticket/Slack message.
5) pfSense logs confirm blocks back into Wazuh → close the loop in Dashboards.

## Secrets & safety
- Keep real IPs/keys out of Git. Use `.env` + GitHub Secrets for CI variables.
- Commit only **sanitised** XML and **redacted** screenshots.
