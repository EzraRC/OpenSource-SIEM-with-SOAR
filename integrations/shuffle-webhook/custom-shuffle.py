#!/usr/bin/env python3
"""
Wazuh custom integration to forward alerts to a Shuffle Webhook.
Place on Wazuh manager under /var/ossec/integrations/custom-shuffle
and reference via <integration><name>custom-shuffle</name> in ossec.conf.
"""
import sys, json, urllib.request

def main():
    data = sys.stdin.read()  # Wazuh pipes alert JSON on stdin
    alert = json.loads(data) if data else {}
    # Prefer hook_url from ossec.conf <integration><hook_url>, else env/arg
    hook_url = "http://localhost:3001/api/v1/hooks/CHANGE_ME"
    if len(sys.argv) > 1:
        hook_url = sys.argv[1]
    try:
        req = urllib.request.Request(hook_url, data=json.dumps(alert).encode("utf-8"),
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            print("Posted to Shuffle:", resp.status)
    except Exception as e:
        print("Shuffle post failed:", e, file=sys.stderr)

if __name__ == "__main__":
    main()
