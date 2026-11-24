# Finding 02: Local File Inclusion (LFI)

## 1. Vulnerability Overview

| Field | Details |
|---|---|
| Finding ID | F-02 |
| Vulnerability | Local File Inclusion (LFI) |
| Affected Application | DVWA |
| Affected Module | File Inclusion |
| Security Level | Low |
| Severity | High (provisional) |
| OWASP Mapping | A03:2021 – Injection |
| CWE | CWE-98 – Improper Control of Filename for Include/Require Statement in PHP Program |
| Status | Confirmed |

## 2. Description

The File Inclusion module accepts a filename through the `page` URL parameter.

During testing, the application accepted a local system-file path instead of restricting access to the intended PHP pages. The application displayed the contents of `/etc/hostname`, confirming that a local file outside the intended application pages could be read.

## 3. Testing Evidence

**Normal request:**

`/vulnerabilities/fi/?page=file1.php`

Observed response:
- Welcome message displayed.
- Username displayed as admin.
- Client IP address displayed.

**LFI test request:**

`/vulnerabilities/fi/?page=/etc/hostname`

Observed response:

`75cdb21db70e`

The displayed value matched the DVWA container hostname.

## 4. Reproduction Steps

1. Log in to the authorized DVWA lab.
2. Set the DVWA security level to Low.
3. Open the File Inclusion module.
4. Confirm that the normal `file1.php` page loads.
5. Replace the `page` parameter with `/etc/hostname`.
6. Observe the hostname displayed in the response.

## 5. Security Impact

An attacker may read local files accessible to the web server process.

Depending on file permissions and application configuration, this could expose application configuration, system information, or sensitive data.

The current test confirms access to `/etc/hostname` only. Access to credentials or other sensitive files has not been demonstrated.

## 6. Root Cause

The Low-security source code assigns the user-controlled `page` parameter directly to `$file` without input validation.

The application does not restrict the requested path to an approved set of files at this security level.

## 7. Recommended Remediation

- Use a strict allowlist of permitted page identifiers.
- Avoid passing user-controlled paths directly to file inclusion functions.
- Resolve permitted files from a fixed application directory.
- Reject path traversal and unexpected file paths.
- Apply least-privilege permissions to the web server process.

## 8. Evidence

- `evidence/finding-02-lfi/Finding-02-LFI-Evidence.PNG`

The screenshot shows the `/etc/hostname` test and the returned hostname.

## 9. Conclusion

Local File Inclusion was successfully demonstrated in the authorized DVWA lab at Low security level.

The application displayed the contents of `/etc/hostname` through the `page` parameter, confirming that local file access was not adequately restricted.