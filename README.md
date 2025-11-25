# cybersecurity-portfolio
A unified cybersecurity portfolio showcasing hands-on SOC analysis, IAM workflows, vulnerability research, and security-aligned Salesforce automation. Designed to demonstrate real-world problem-solving, technical depth, and the readiness expected of top early-career talent.


# Keith C. Canty — Cybersecurity & Salesforce Portfolio

Welcome to my cybersecurity portfolio. This repository is a living collection of beginner-friendly but employer-ready labs that show how I think, investigate, and document security work.

I built this to support roles like **SOC Analyst**, **Threat Hunter (Jr)**, **IAM Analyst**, **Vulnerability Analyst**, and **Security-minded Salesforce Admin/Analyst**.

---

## How This Portfolio Is Organized

Each top-level folder represents a **focus area**.  
Each lab inside that area contains:

- `lab-notes.md` — what I did, why I did it, and what I found  
- `screenshots/` — key steps and proof of work  
- `artifacts/` — exports, logs, reports, code, or configs

### 1. `soc-analyst/`

Labs that show log analysis, detection, and basic threat hunting.

Example labs:
- `windows-event-logs-bruteforce/`  
  - Simulated brute-force logon failures in a Windows lab  
  - Analyzed Event ID 4625/4624 in Event Viewer  
  - Documented findings and mapped activity to the MITRE ATT&CK framework

- `network-monitoring-mitre/`  
  - Captured network traffic during benign and suspicious activity  
  - Identified patterns that could indicate scanning or lateral movement  
  - Tied observations back to MITRE techniques and potential detections

### 2. `iam/`

Labs focused on **who has access to what**, and whether that access is appropriate.

Example labs:
- `linux-rbac-sudo-review/`  
  - Reviewed local Linux user accounts, groups, and `sudo` privileges  
  - Applied least-privilege principles and documented an access review  
  - Explained how this maps to IAM and real-world change control

- `salesforce-access-review/`  
  - Performed a mock access review using Salesforce profiles and permission sets  
  - Identified over-privileged users and recommended adjustments  
  - Documented before/after access in the context of compliance and risk

### 3. `vulnerability-management/`

Labs that demonstrate basic vulnerability discovery, triage, and remediation planning.

Example labs:
- `nessus-essentials-webscan/`  
  - Scanned a small target (e.g., vulnerable VM or test web app) with Nessus Essentials  
  - Categorized findings by severity and business impact  
  - Wrote remediation recommendations prioritized by risk

### 4. `python/`

Small scripts to automate or speed up common analyst tasks.

Example labs:
- `failed-login-log-parser/`  
  - Python script that parses auth logs (e.g., Windows or Linux)  
  - Counts failed logons by username/IP and highlights brute-force patterns

- `api-log-anomaly-counter/`  
  - Simple Python analyzer for HTTP/API logs  
  - Surfaces unusual status codes or spikes in requests to specific endpoints

### 5. `salesforce-security/`

Labs that combine my Salesforce background with security principles.

Example labs:
- `field-level-security-lab/`  
  - Configured Salesforce field-level security and profiles for least privilege  
  - Demonstrated how changing profile/permission set design reduces data exposure

- `login-history-monitoring/`  
  - Exported and analyzed Salesforce login history (e.g. by location, time, outcome)  
  - Highlighted suspicious patterns (multiple failures, unusual IPs or times)  
  - Proposed simple monitoring rules and follow-up actions

---

## 🧠 What This Portfolio Shows About Me

- I **document like an analyst**: clear steps, screenshots, findings, and next actions  
- I can **bridge IT, security, and business tools like Salesforce**  
- I am comfortable working with:
  - Windows Event Viewer and basic log analysis  
  - Linux user/group management and `sudo` reviews  
  - Vulnerability scanning concepts and risk-based remediation  
  - Basic Python scripting to support analyst workflows  

I am still early in my cybersecurity career, but I built this portfolio to show that I can learn quickly, think like a defender, and communicate clearly with both technical and non-technical stakeholders.

---

## How to Navigate This Repo

- Start with the folder that matches the role you’re hiring for:
  - **SOC / Threat Hunter** → `soc-analyst/`
  - **IAM / Access Governance** → `iam/`
  - **Vulnerability / Risk** → `vulnerability-management/`
  - **Python-oriented roles** → `python/`
  - **Salesforce-security / hybrid roles** → `salesforce-security/`
- Open any `lab-notes.md` to see:
  - The scenario
  - The tools/commands used
  - Screenshots (linked from `/screenshots`)
  - Key findings and recommendations

If you’d like a guided walk-through of any lab, I’m happy to talk through my approach in more detail.
