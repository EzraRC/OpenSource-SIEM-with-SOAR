# 🛡️ Open Source SIEM with SOAR

An open source Security Information and Event Management (SIEM) platform with integrated Security Orchestration, Automation and Response (SOAR), and firewall automation.  
This project combines **Wazuh All-in-One**, **Shuffle SOAR**, and **pfSense** to provide a lightweight but production-style SOC environment for detection, enrichment, and automated response.

---

## 🚀 Project Overview

**Components:**
- **[Wazuh AIO](https://wazuh.com/):** Open source SIEM built on the Elastic Stack, used for log collection, threat detection, and alerting.
- **[Shuffle SOAR](https://shuffler.io/):** Automation platform for handling alerts, enrichment, and response playbooks.
- **[pfSense](https://www.pfsense.org/):** Open source firewall used for network visibility and automated blocking of malicious hosts.

**Key Features:**
- Centralised log collection and monitoring.
- Custom Wazuh integration to forward selected alerts to Shuffle via webhook.
- Shuffle playbooks for enrichment (e.g., VirusTotal) and automated actions.
- pfSense firewall alias management for automated blocking of malicious IPs.
- GitHub CI workflows to validate playbooks and configs.

---

## 🏗️ Architecture

```
    [ pfSense Firewall ] --------> [ Wazuh SIEM ]
                                         |
                                         v
                                 [ Shuffle SOAR ]
                                         |
                           (Enrichment & Automated Actions)
                                         |
                                         v
                              [ pfSense API / Blocklist ]
```

---

## 📂 Repository Layout

```
├── wazuh/                  # Wazuh rules, decoders, ossec.conf snippets
├── integrations/           # Custom Wazuh → Shuffle webhook integration
├── playbooks/shuffle/      # Example Shuffle SOAR playbooks (JSON)
├── firewall/pfsense/       # Notes, sanitised XML backups, API usage
├── docs/                   # Architecture docs, screenshots
├── scripts/                # Helper scripts (bootstrap Shuffle, etc.)
└── .github/workflows/      # GitHub Actions for validation
```

---

## ⚙️ Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/EzraRC/OpenSource-SIEM-with-SOAR.git
cd OpenSource-SIEM-with-SOAR
```

### 2. Deploy Wazuh AIO
- Import the official [Wazuh AIO OVA](https://documentation.wazuh.com/current/installation-guide/wazuh-indexer/virtual-machine.html)  
  **or** install via Docker:
  ```bash
  curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh
  bash wazuh-install.sh -a
  ```
- Apply example configs from `wazuh/config/`.
- Copy `integrations/shuffle-webhook/custom-shuffle.py` into `/var/ossec/integrations/custom-shuffle/`.

### 3. Spin up Shuffle
```bash
./scripts/bootstrap.sh
# Access UI: https://localhost:3443
```
- Create a Webhook trigger.
- Import `playbooks/shuffle/example_enrich_block.json`.
- Add your VirusTotal, Slack, and pfSense credentials.

### 4. Configure pfSense
- Enable syslog → point to Wazuh manager (`UDP/514`).
- Install **pfSense API** package.
- Create an alias (e.g., `SOAR_BLOCKLIST`) for automated blocking.
