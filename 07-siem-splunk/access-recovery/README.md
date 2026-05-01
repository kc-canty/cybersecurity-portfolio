# Splunk SOC Analyst Labs (Beginner Portfolio)

## Overview
This repository contains hands-on labs I completed while learning Splunk and SOC analyst fundamentals. 

The focus of these labs is not just using Splunk, but troubleshooting issues, analyzing logs, and building basic detection logic in a realistic way.

---

## Labs Included

### Lab 1: Splunk Access Recovery
- Troubleshot port conflicts (8000, 8089)
- Reset admin credentials using configuration files
- Restored access to Splunk web interface

📁 `lab-1-access-recovery/`

---

### Lab 2: Failed Login Detection (Event ID 4625)
- Ingested Windows Security Logs
- Identified failed login attempts
- Built basic SPL queries to detect brute-force patterns

📁 `lab-2-failed-login-detection/`

---

### Lab 3: Basic Alerting
- Created alerts based on failed login thresholds
- Configured Splunk to trigger alerts on suspicious activity
- Observed alert behavior in real time

📁 `lab-3-basic-alerting/`

---

## Tools Used
- Splunk Enterprise
- Windows Event Logs
- PowerShell
- SPL (Search Processing Language)

---

## What I’m Working On Next
- Dashboard creation
- Correlation searches
- More advanced detection use cases
- Expanding into SIEM + SOC workflows

---

## Notes
I am still early in my learning, so these labs reflect a beginner perspective. My goal is to build real skills through hands-on work and document the process clearly.
