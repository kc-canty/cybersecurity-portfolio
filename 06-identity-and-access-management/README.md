# Active Directory Lab 01  
## User Provisioning, Password Resets & Account Lockouts

### Objective
Simulate common help desk identity and access management tasks using Active Directory, including:
- Creating a domain user
- Resetting a password
- Triggering and resolving an account lockout
- Verifying activity through Event Viewer

This lab reflects real-world Tier 1 / Tier 2 help desk workflows and introduces IAM fundamentals.

---

## Tools Used
- Windows Server (Domain Controller)
- Active Directory Users and Computers (ADUC)
- Windows 10/11 Client (domain-joined)
- Event Viewer

---

## Lab Tasks (ADHD-Friendly Checklist)

### Step 1: Verify Domain Controller
- Confirm Windows Server is promoted to a Domain Controller
- Verify domain name (ex: corp.local)

Evidence:
- Screenshot of Server Manager → AD DS installed

---

### Step 2: Create a Test User
- Open **Active Directory Users and Computers**
- Create user:
  - Username: `jdoe`
  - Temporary password
  - Force password change at next login
 Evidence:
- User object properties showing username and enabled status

---

### Step 3: Simulate Password Reset
- Reset `jdoe` password from ADUC
- Set a known password

Evidence:
- Password reset confirmation window

---

### Step 4: Trigger Account Lockout
- Attempt multiple failed logins as `jdoe` from client machine
- Exceed lockout threshold

 Evidence:
- ADUC showing account locked
- Client login error message

---

### Step 5: Unlock Account
- Unlock `jdoe` from ADUC
- Reset password again if needed

📸 Evidence:
- Account properties showing unlocked status

---

### Step 6: Review Security Logs
- Open Event Viewer on Domain Controller
- Identify:
  - Failed logon events (4625)
  - Successful logon events (4624)
  - Account lockout events

 Evidence:
- Event Viewer logs with Event IDs visible

---

## Why This Lab Matters
- Demonstrates real help desk IAM responsibilities
- Shows troubleshooting, not just configuration
- Builds foundation for SOC and IAM analyst roles
