# Architecture Decision Record (ADR)

## ADR-001: Selection of Lab Environment and SIEM

**Project:** Secure the School Portal  
**Client:** Ezitech  
**Author:** Mubashir Ahmad  
**Status:** Accepted  
**Date:** 20 November 2026

## 1. Context

The Secure the School Portal project requires an isolated lab environment containing a deliberately vulnerable web application and a local Security Information and Event Management (SIEM) solution.

The environment must support vulnerability assessment, security event collection, detection engineering, and incident response.

The selected technologies must also operate within the available hardware resources.

The host machine has 16 GB of physical RAM. The Ubuntu virtual machine has been allocated 4 GB of RAM and 4 virtual CPUs.

During implementation, memory usage was monitored and resource allocations were adjusted to maintain system stability.

## 2. Architecture Decisions

The following technologies have been selected:

| Component | Selected Technology | Purpose |
|---|---|---|
| Virtualization | Oracle VirtualBox | Isolated lab environment |
| Operating System | Ubuntu 26.04.1 LTS | Lab operating system |
| Container Runtime | Docker Engine | Running isolated lab services |
| Vulnerable Application | DVWA | Web security testing |
| SIEM | Elastic Stack (initially Elasticsearch) | Security event storage and analysis |
| Container Networking | Docker bridge network | Communication between lab services |
| Documentation | Markdown | Technical documentation |
| Version Control | Git and GitHub | Source control and collaboration |

## 3. Why VirtualBox?

VirtualBox was selected to provide an isolated virtual environment for security testing.

**Advantages:**
- Runs a separate operating system without replacing Windows.
- Supports isolated networking configurations.
- Allows snapshots and recovery.
- Provides a controlled environment for security experiments.

**Trade-off:**

Virtual machines consume additional RAM, CPU, and disk resources. Resource allocation must therefore be managed carefully.

## 4. Why DVWA?

Damn Vulnerable Web Application (DVWA) was selected as the deliberately vulnerable web application.

DVWA is deployed inside a Docker container running within the Ubuntu virtual machine.

**Advantages:**
- Provides practical web application security exercises.
- Supports testing of common vulnerabilities.
- Allows controlled vulnerability assessment.
- Helps generate security events for future SIEM monitoring.

**Trade-off:**

DVWA is intentionally insecure and must remain inside the controlled lab environment. It must never be exposed publicly.

The application is currently configured at Low security level for controlled testing.

## 5. Why Elastic Stack Instead of Wazuh?

Elastic Stack was selected as the SIEM solution.

The primary reason is familiarity with Elasticsearch, log ingestion, and security dashboards from previous SOC projects.

Continuing with Elastic allows more time to be spent on detection engineering, security analysis, and incident response instead of learning a completely new SIEM platform.

**Advantages of Elastic Stack:**
- Powerful log ingestion and search capabilities.
- Flexible data analysis.
- Kibana dashboards and visualizations.
- Integration with security monitoring workflows.
- Existing familiarity with Elasticsearch from previous projects.

**Why not Wazuh?**

Wazuh provides integrated endpoint monitoring, security detection, and centralized management.

However, selecting Wazuh would introduce additional learning and configuration requirements for this project.

Since the primary objective is to develop detection rules and incident response capabilities, Elastic is the preferred choice.

**Implementation note:**

Elasticsearch 8.18.0 has been deployed successfully as a single-node service. Kibana and application log ingestion have not yet been implemented and remain future integration activities.

## 6. Architecture Trade-offs

| Decision | Benefit | Trade-off |
|---|---|---|
| VirtualBox | Isolated testing environment | Consumes host resources |
| Ubuntu | Flexible Linux environment | Requires Linux administration |
| Docker | Repeatable and manageable deployments | Requires container administration |
| DVWA | Practical vulnerability testing | Must remain securely isolated |
| Elastic Stack | Flexible log analysis and dashboards | Higher resource consumption and configuration effort |
| Local SIEM | Full control over lab data | Requires manual setup and maintenance |
| Localhost-only port binding | Limits access to the VM's local services | Remote access requires additional configuration |

## 7. Resource Management

The host machine has 16 GB of physical RAM.

The Ubuntu virtual machine has the following configuration:

- Allocated RAM: 4 GB.
- Virtual CPUs: 4.
- Swap file: 2 GB, activated persistently through `/etc/fstab`.

To reduce memory pressure, Elasticsearch was deployed using a conservative configuration.

**Actual Elasticsearch configuration:**

- Version: 8.18.0.
- Deployment mode: Single-node.
- JVM heap: 512 MB (`-Xms512m -Xmx512m`).
- Docker container memory limit: 1,500 MB.
- HTTP API port: 9200.
- Port binding: `127.0.0.1:9200`.

DVWA runs in a separate Docker container and uses approximately 96 MiB of memory during the observed resource check.

The Elasticsearch JVM heap is part of the container's memory consumption, not an additional allocation.

The initial deployment uses a smaller heap than originally planned because the Ubuntu VM has approximately 3.3 GiB of usable memory and must also run the operating system and DVWA.

Memory and performance will continue to be monitored as additional services are introduced.

## 8. Security Considerations

The lab environment follows these security principles:

1. Keep vulnerable applications isolated.
2. Use fictional accounts and test data.
3. Avoid exposing vulnerable services to public networks.
4. Restrict access to administrative interfaces.
5. Collect relevant application and security logs.
6. Use controlled testing targets only.
7. Document security configuration and changes.
8. Keep vulnerable services bound to localhost where appropriate.

**Implemented network controls:**

- A dedicated Docker bridge network named `school-portal-lab` connects DVWA and Elasticsearch.
- DVWA is published on `127.0.0.1:8080`.
- Elasticsearch is published on `127.0.0.1:9200`.
- Container-to-container communication has been verified.

**Important security limitation:**

The Docker bridge network is not configured as internal-only. Both services are bound to the Ubuntu VM's loopback interface, but this does not mean the containers have no external network access.

Elasticsearch's built-in security has temporarily been disabled using `xpack.security.enabled=false` to simplify local development and testing.

Therefore, Elasticsearch must remain restricted to the isolated lab environment. Authentication and TLS must be addressed before any production or broader network deployment.

## 9. Implementation and Validation

The following implementation activities have been completed:

| Activity | Result |
|---|---|
| Ubuntu virtual machine setup | Completed |
| Docker Engine installation | Completed |
| Docker bridge network creation | Completed |
| DVWA deployment | Completed |
| Elasticsearch 8.18.0 deployment | Completed |
| Persistent swap configuration | Completed |
| Elasticsearch HTTP API verification | Successful |
| Docker network connectivity verification | Successful |
| Container-to-container HTTP test | Successful |
| Localhost-only port binding verification | Successful |

Elasticsearch successfully returned its cluster information through its HTTP API.

A connectivity test from the Elasticsearch container to DVWA using the Docker hostname `dvwa` returned HTTP 302, confirming successful container-to-container communication.

Application log ingestion into Elasticsearch, Kibana deployment, and detection engineering remain future implementation activities.

## 10. Final Decision

VirtualBox with Ubuntu, Docker, DVWA, and Elasticsearch 8.18.0 has been selected for the initial lab deployment. Kibana and application log ingestion will be added during subsequent implementation tasks as the project architecture.

Elastic Stack was chosen because of previous experience with Elasticsearch, log ingestion, and dashboard development.

This decision reduces unnecessary learning overhead and allows greater focus on the core SOC objectives of detection engineering, security monitoring, and incident response.

The initial lab infrastructure has been successfully deployed and validated.

Resource allocations were adjusted during implementation to accommodate the available VM memory. The current configuration uses a 512 MB Elasticsearch JVM heap and a persistent 2 GB swap file.

The architecture will continue to evolve as the project progresses through vulnerability assessment, detection engineering, incident response, and final handover.

---

**Decision Owner:** Mubashir Ahmad  
**Project:** Secure the School Portal  
**Client:** Ezitech  
**ADR:** 001  
**Status:** Accepted