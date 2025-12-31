# Findings — Lab 01: AD Domain Join + Password Reset + Account Lockout Triage

## What I built
- Created a basic Active Directory domain controller (new forest).
- Created an OU and a domain user account in ADUC.
- Joined a Windows client machine to the domain.
- Logged into the domain using the created user account.

## What I simulated (real Help Desk tickets)
1) Domain join workflow:
   - Client DNS must point to the Domain Controller for a domain join to succeed.
2) Account lockout scenario:
   - Multiple failed login attempts caused the domain account to lock.
3) Access restoration:
   - I unlocked the account in ADUC and confirmed the user could authenticate again.
4) Evidence-driven triage:
   - I validated the issue and recovery steps using Domain Controller security logs.

## Key troubleshooting takeaways
- If a domain join fails, verify:
  - DNS on the client points to the DC
  - Network connectivity between client and DC
- If a user is locked out:
  - Confirm lockout / failures in Event Viewer on the DC
  - Unlock the account and/or reset password in ADUC
  - Validate login success on the client after remediation

## Why this matters for Help Desk / Service Desk
This lab demonstrates core, high-frequency work:
- provisioning users, assisting with access issues
- resolving lockouts quickly
- joining machines to the domain
- documenting steps and confirming resolution with evidence
