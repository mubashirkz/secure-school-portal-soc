# School Portal SOC Lab Environment

## 1. Overview

This directory documents the local security testing environment developed for the Secure the School Portal project.

The lab provides an intentionally vulnerable web application and a local Elasticsearch service for security monitoring and future detection engineering exercises.

All testing is restricted to authorized lab systems and approved training environments.

## 2. Lab Architecture

The environment runs inside an Ubuntu virtual machine hosted by Oracle VirtualBox.

| Component | Technology | Purpose |
|---|---|---|
| Virtualization | Oracle VirtualBox | Isolated Linux environment |
| Operating System | Ubuntu 26.04.1 LTS | Lab host |
| Container Runtime | Docker Engine | Runs lab services |
| Vulnerable Application | DVWA | Web security testing |
| SIEM Component | Elasticsearch 8.18.0 | Security event storage and search |
| Container Networking | Docker bridge network | Internal communication |

## 3. Network Configuration

The Docker bridge network is named `school-portal-lab`.

| Component | Container IP | Host Port |
|---|---|---|
| DVWA | 172.18.0.2 | 127.0.0.1:8080 |
| Elasticsearch | 172.18.0.3 | 127.0.0.1:9200 |
| Docker Gateway | 172.18.0.1 | N/A |

Both containers are connected to the same Docker network.

Container-to-container communication was verified by sending an HTTP request from Elasticsearch to DVWA using the Docker hostname `dvwa`. DVWA returned HTTP 302, redirecting the request to its login page.

**Network isolation limitation:** The Docker bridge network provides connectivity between the lab containers but does not block outbound internet access. Published service ports are restricted to the Ubuntu VM's loopback interface. The lab should only be used for authorized testing, and the vulnerable application must not be exposed to public or untrusted networks.

**Security note:** Both published application ports are bound to the Ubuntu VM's loopback interface. The Docker bridge network is not configured as internal-only (`Internal: false`).

## 4. Resource Configuration

The Ubuntu VM has 4 GB of allocated RAM and 4 virtual CPUs.

A 2 GB swap file was configured and enabled persistently through `/etc/fstab`.

Elasticsearch uses the following initial resource settings:

- JVM heap: 512 MB
- Container memory limit: 1,500 MB
- Deployment mode: Single-node

These conservative settings were selected to reduce memory pressure on the VM.

## 5. Security Controls

- DVWA runs as an intentionally vulnerable application for controlled testing.
- DVWA is published on `127.0.0.1:8080`.
- Elasticsearch is published on `127.0.0.1:9200`.
- Both services use a dedicated Docker bridge network.
- No production school systems or real student information are used.
- Elasticsearch security is temporarily disabled for local development and testing.
- The lab is not intended for production deployment.

## 6. Verification Evidence

The following checks were completed successfully:

| Verification | Result |
|---|---|
| Docker Engine operational | PASS |
| DVWA container running | PASS |
| Elasticsearch container running | PASS |
| Elasticsearch HTTP API responding | PASS |
| Docker network membership verified | PASS |
| Container-to-container HTTP connectivity | PASS |
| Localhost-only port bindings verified | PASS |
| Persistent swap configuration verified | PASS |

### Useful Verification Commands

```bash
sudo docker ps
sudo docker compose ps
sudo docker network inspect school-portal-lab
sudo docker stats --no-stream
curl http://127.0.0.1:9200
sudo swapon --show
free -h
```

## 7. Current Limitations

- DVWA is intentionally configured with a low security level for controlled vulnerability assessment.
- Elasticsearch is running without built-in authentication and TLS; it must remain restricted to the local lab.
- DVWA log ingestion into Elasticsearch has not yet been configured.
- Kibana has not yet been deployed.
- Detection rules and incident response workflows will be developed in subsequent project tasks.

## 8. Conclusion

The local lab infrastructure is operational. DVWA and Elasticsearch are running as separate Docker containers and have verified network connectivity.

This environment provides the foundation for the upcoming vulnerability assessment, security detection engineering, and incident response exercises.