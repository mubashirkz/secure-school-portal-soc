# Rules of Engagement (RoE)

## Project Information

| Item | Details |
|---|---|
| Project | Secure the School Portal |
| Client | Ezitech |
| Target Organization | Bright Future School (Fictional) |
| Security Role | SOC Analyst |
| Document | Rules of Engagement |
| Version | 1.0 |

## 1. Purpose

The purpose of these Rules of Engagement is to establish the authorized scope, boundaries, and limitations for security testing activities conducted during the Secure the School Portal project.

The objective is to identify security weaknesses, understand potential attack paths, and improve the security of the school's portal.

## 2. Authorized Scope

The following targets are authorized for this project:

- PortSwigger Web Security Academy practice labs.
- A deliberately vulnerable web application running inside our isolated local lab environment.
- Local SIEM components used for monitoring and analyzing security events.
- Simulated attacks against the locally hosted application.

The Bright Future School portal is a fictional system created for educational and security testing purposes.

## 3. Out-of-Scope Activities

The following activities are strictly prohibited:

- Testing real school websites or production systems without explicit written authorization.
- Attacking third-party websites or infrastructure.
- Conducting denial-of-service (DoS) attacks.
- Accessing real users' accounts or personal information.
- Attempting to bypass security controls on systems outside the authorized scope.
- Performing social engineering against real individuals.
- Modifying or deleting data on unauthorized systems.

## 4. Testing Rules

All security testing must follow these rules:

1. Perform testing only against explicitly authorized targets.
2. Use PortSwigger Web Security Academy for controlled web security exercises.
3. Keep the vulnerable application inside an isolated local lab.
4. Use fictional accounts and test data.
5. Document testing activities and their results.
6. Avoid activities that could affect external systems or real users.
7. Stop testing immediately if unexpected access to real systems or sensitive information occurs.

## 5. Testing Environment

The project uses a local lab environment hosted inside Oracle VirtualBox.

The implemented environment consists of:

- Oracle VirtualBox for virtualization.
- Ubuntu 26.04.1 LTS as the lab operating system.
- Docker Engine for running isolated application and SIEM containers.
- DVWA as the intentionally vulnerable web application.
- Elasticsearch 8.18.0 as the local SIEM component.
- Docker bridge network `school-portal-lab` for container communication.
- VS Code for development and documentation.
- Git and GitHub for version control.

The DVWA and Elasticsearch services are published only on the Ubuntu VM's localhost interface. They are not intentionally exposed to the external network.

Elasticsearch authentication and TLS are temporarily disabled for local lab development. The service must remain restricted to the controlled testing environment.

## 6. Evidence Collection

Security testing evidence may include:

- Application screenshots.
- Relevant application and security logs.
- HTTP request and response samples from authorized labs.
- SIEM alerts and detection results.
- Documentation of identified vulnerabilities.

Evidence must not contain real personal information, passwords, API keys, or other sensitive credentials.

## 7. Incident and Stop Conditions

Testing must stop if:

- Activity affects a system outside the authorized scope.
- Unexpected access to sensitive information occurs.
- The lab environment becomes unstable.
- Testing causes unintended disruption.

Any unexpected security event must be documented and reviewed before testing resumes.

## 8. Authorization Statement

This document defines the intended testing boundaries for this educational project.

Only PortSwigger Web Security Academy practice labs and explicitly controlled local lab assets are included in the authorized testing scope.

No testing against real Bright Future School infrastructure or other third-party production systems is authorized by this document.

---

**Document Owner:** Mubashir Ahmad  
**Project:** Secure the School Portal  
**Client:** Ezitech  
**Version:** 1.0