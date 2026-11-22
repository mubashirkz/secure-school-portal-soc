# Secure the School Portal — Detection, Response, and Handover

**Client:** Ezitech

**Project:** Secure the School Portal

**Author:** Mubashir Ahmad

**Status:** Task 1 — Lab Setup and Threat Modeling

## 1. Project Overview

This project focuses on securing a fictional school web portal for Bright Future School through practical Security Operations Center (SOC) activities.

The project simulates how a security analyst identifies risks, assesses web application vulnerabilities, monitors suspicious activity, develops detection rules, and responds to security incidents.

The goal is to establish a monitored and controlled testing environment and progressively develop security controls, detection capabilities, incident response procedures, and handover documentation.

## 2. Project Objectives

- Identify security risks affecting authentication and student data access.
- Develop a threat model using the STRIDE methodology.
- Perform controlled web application vulnerability assessments.
- Establish a local lab with a vulnerable web application and SIEM.
- Develop Sigma detection rules for relevant attack techniques.
- Create incident response procedures and conduct a tabletop exercise.
- Document findings, recommendations, and security improvements.

## 3. Project Scope

The fictional Bright Future School portal is the scenario used throughout this project.

Authorized testing environments include:

- PortSwigger Web Security Academy labs.
- The local intentionally vulnerable DVWA application.
- The local Ubuntu and Docker lab environment.
- The locally deployed Elasticsearch service.

Testing against unauthorized production systems, real student data, or third-party infrastructure is outside the approved scope.

Refer to [Rules of Engagement](docs/rules-of-engagement.md) for the complete testing boundaries and restrictions.

## 4. Threat Model

The initial threat model focuses on two important areas:

- User authentication and session management.
- Access to student and teacher information.

The assessment uses STRIDE to identify potential security threats.

**Initial top five risks:**

| Risk | Initial Severity |
|---|---|
| SQL Injection | Critical |
| Broken Authentication | Critical |
| Broken Access Control | Critical |
| Session Hijacking | High |
| Denial of Service | High |

These are preliminary qualitative risk ratings. They will be validated and refined during the vulnerability assessment.

See [Threat Model](threat-model/threat-model.md) for the detailed analysis.

## 5. Lab Architecture

The project uses an Ubuntu virtual machine hosted through Oracle VirtualBox.

The local environment includes:

| Component | Technology |
|---|---|
| Virtualization | Oracle VirtualBox |
| Operating System | Ubuntu 26.04.1 LTS |
| Container Runtime | Docker Engine |
| Vulnerable Web Application | DVWA |
| SIEM Component | Elasticsearch 8.18.0 |
| Container Networking | Docker bridge network |
| Version Control | Git and GitHub |

DVWA and Elasticsearch run