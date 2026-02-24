# IAM Access Ticket – User Lifecycle Management

## Request Details
- Request Type: User Provisioning / Access Modification / Deprovisioning
- Request Source: Human Resources (Simulated)
- System: Microsoft Entra ID
- Environment: Azure Free Tenant (Lab)

## User Impacted
- Name: Luke Johnson
- Account Type: Cloud-only user

## Access Requirements
- Initial access to Finance-related resources
- Subsequent access modification to Reporting resources
- Full access removal upon termination

## Actions Taken

### Joiner
- Created a new cloud-only user account in Microsoft Entra ID.
- Provisioned access by assigning the user to the `Finance-Users` security group.

### Mover
- Removed user from `Finance Users` group.
- Assigned user to `Reporting Users` security group to reflect role change.

### Leaver
- Disabled user sign-in to prevent authentication.
- Removed all group memberships to eliminate residual access.

## Access Control Model
- Access managed through group-based controls rather than direct user permissions.
- Group membership used to enforce role-based access control (RBAC).

## Outcome
User access was successfully provisioned, modified, and deprovisioned in alignment with IAM best practices. No residual access remained following account disablement.

## Notes
In a production environment, these actions would be initiated through an approved HR or management request and documented within a centralized ticketing system to support audit and compliance requirements.
