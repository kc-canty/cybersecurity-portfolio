# Identity & Access Management Lab
## Microsoft Entra ID (Azure AD) — Joiner / Mover / Leaver (JML)

---

## Objective
Demonstrate core Identity & Access Management (IAM) lifecycle operations by provisioning, modifying, and deprovisioning a user in Microsoft Entra ID using group-based access controls and audit-ready documentation.

---

## Real-World Scenario
An employee joins the organization, later changes roles internally, and eventually exits the company. The IAM team is responsible for provisioning appropriate access, modifying permissions as job responsibilities change, and fully deprovisioning access upon termination to reduce security risk.

---

## Environment & Tools
- Platform: Microsoft Azure
- Identity Provider: Microsoft Entra ID (formerly Azure Active Directory)
- Tenant Type: Azure Free Tier
- Access Model: Group-based access control
- Documentation: Markdown artifacts

---

## Scope of Work
The following IAM lifecycle actions were performed:

### Joiner
- Created a new cloud-only user account in Microsoft Entra ID
- Established security groups to represent role-based access
- Provisioned access by assigning the user to the appropriate security group

### Mover
- Simulated an internal role change by removing the user from one security group
- Granted new access by assigning the user to a different group

### Leaver
- Disabled user sign-in to prevent authentication
- Removed all group memberships to eliminate residual access
- Verified access was fully revoked

---

## Key IAM Concepts Demonstrated
- Identity lifecycle management (Joiner / Mover / Leaver)
- Group-based access control
- Least privilege enforcement
- Access modification without re-creating identities
- Secure deprovisioning practices
- Audit-ready change documentation

---

## Evidence
All screenshots supporting this lab are stored in the `evidence/` folder and named in execution order to demonstrate the complete identity lifecycle.

---

## Artifacts Produced
- `ticket-notes.md` — Simulated IAM ticket documenting access requests, access modifications, and deprovisioning actions
- `findings.md` — Summary of IAM outcomes, risks addressed, and access governance considerations

## Evidence & Validation
All supporting screenshots demonstrating the execution of this lab are stored in the `evidence/` folder.  
Screenshots are named in sequential order to reflect the identity lifecycle from provisioning through deprovisioning.
---

## Outcome
The user account was successfully provisioned, modified, and deprovisioned using Microsoft Entra ID. All access changes were executed using group-based controls, and no residual access remained after account disablement, aligning with enterprise IAM and audit expectations.

---

## Lessons Learned
- Group-based access provides cleaner access control than direct user permissions
- Deprovisioning requires both account disablement and access removal
- Clear documentation is critical for audit and compliance validation
