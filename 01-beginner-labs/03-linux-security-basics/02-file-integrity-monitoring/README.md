# Findings – Linux Authentication Log Analysis

## Overview
This analysis reviews authentication-related activity observed in the Linux authentication log (`/var/log/auth.log`). The goal was to identify suspicious login behavior, assess potential security risks, and document findings in a manner consistent with entry-level SOC and system administration investigations.

---

## Key Observations

### Invalid User Attempts
- An invalid user account named **"fakeuser"** attempted to authenticate via SSH.
- Source IP address: **127.0.0.1 (loopback)**.
- Invalid user attempts often indicate **username enumeration** or probing for valid accounts.

### Failed Password Attempts
- Multiple failed SSH password attempts were recorded for the invalid user **"fakeuser"**.
- Authentication attempts were rejected by the system.
- No successful login was observed.

---

## Behavioral Analysis
- The repeated pattern of invalid user attempts followed by failed password attempts is consistent with **brute-force credential guessing behavior**.
- Although the source IP was local (loopback), the activity **accurately simulates real-world external probing and attack patterns**.
- No evidence of privilege escalation or account compromise was detected.

---

## MITRE ATT&CK Mapping
The observed behavior aligns with the following MITRE ATT&CK techniques:

- **T1110 – Brute Force**
- **T1078 – Valid Accounts** (attempted but unsuccessful)
- **T1059 – Command and Scripting Interpreter** (SSH-related interactions)

---

## Impact Assessment
If this activity originated from an external source, it could indicate:
- Username enumeration
- Credential stuffing attempts
- Early-stage reconnaissance prior to a larger attack

In this case, system controls successfully prevented unauthorized access.

---

## Analyst Notes
- Repeated invalid user and failed password attempts are common early indicators of unauthorized access attempts.
- These events should be monitored closely, especially if originating from external IP addresses.
- Proper logging and alerting are critical for early detection.

---

## Recommendations
To reduce the risk of successful brute-force or enumeration attacks:

- Enable **fail2ban** to automatically block repeated failed login attempts
- Disable **root login over SSH**
- Enforce **strong password policies**
- Transition to **SSH key-based authentication only**
- Monitor authentication logs regularly or forward them to a SIEM

---

## Conclusion
This investigation identified simulated brute-force behavior targeting SSH authentication. While no compromise occurred, the activity reflects common real-world attack techniques and highlights the importance of proactive monitoring and hardening of authentication services.
