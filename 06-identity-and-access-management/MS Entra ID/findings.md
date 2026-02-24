# IAM Lab Findings — Microsoft Entra ID JML Workflow

---

## Summary
This lab demonstrated a complete identity lifecycle workflow in Microsoft Entra ID, including user provisioning, access modification, and deprovisioning. The exercise reinforced the importance of structured access management and thorough documentation in enterprise IAM environments.

---

## Key Findings

### Identity Lifecycle Management
- User access should be managed through lifecycle events rather than one-off changes.
- Group membership provides a scalable and auditable method for managing permissions.

### Access Governance
- Access changes tied to role transitions (Mover events) reduce the risk of over-permissioning.
- Removing group access is as critical as disabling the account during offboarding.

### Deprovisioning Risks
- Disabling sign-in alone does not fully eliminate access risk.
- Residual group memberships can create latent access exposure if not removed.

### Audit & Compliance Considerations
- Maintaining documentation of access requests and actions supports audit readiness.
- IAM ticket-style documentation provides traceability for access decisions.

---

## Security Impact
The lab highlights how proper IAM practices:
- Reduce unauthorized access risk
- Support least privilege enforcement
- Improve compliance posture in regulated environments

---

## Production Considerations
In a production environment, these actions would typically be:
- Triggered by HR or management requests
- Logged in a ticketing system
- Reviewed during periodic access certifications
- Automated through identity governance tooling where possible
