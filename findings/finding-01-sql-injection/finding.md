# Finding 01: SQL Injection

## 1. Vulnerability Overview

| Field | Details |
|---|---|
| Finding ID | F-01 |
| Vulnerability | SQL Injection |
| Affected Application | DVWA |
| Affected Module | SQL Injection |
| Security Level | Low |
| Severity | High |
| OWASP Mapping | A03:2021 – Injection |
| Status | Confirmed |

## 2. Description

The application accepts user input through the User ID field and appears to process that input unsafely in a database query.

During testing, a crafted SQL condition altered the query behavior and caused multiple database records to be returned.

## 3. Testing Evidence

### Normal Input

Input:
`1`

Observed response:
- ID: 1
- First name: admin
- Surname: admin

### Injection Test

Input:
`1' OR '1'='1`

Observed response:
- admin admin
- Gordon Brown
- Hack Me
- Pablo Picasso
- Bob Smith

Five records were returned instead of the single record observed during the baseline test.

## 4. Reproduction Steps

1. Log in to the DVWA application.
2. Set the DVWA security level to Low.
3. Open the SQL Injection module.
4. Enter `1` in the User ID field and submit.
5. Record the normal response.
6. Enter `1' OR '1'='1` and submit.
7. Observe the additional database records.

## 5. Security Impact

An attacker may exploit this weakness to retrieve database records beyond the intended access.

Depending on the database query and application permissions, further database exposure or manipulation may be possible.

## 6. Root Cause

The observed behavior is consistent with unsafe handling of user-controlled input in an SQL query.

The underlying source code has not yet been inspected, so the exact vulnerable implementation remains unverified.

## 7. Recommended Remediation

- Use parameterized SQL queries or prepared statements.
- Avoid constructing SQL queries through string concatenation.
- Validate user input on the server side.
- Apply least-privilege database permissions.
- Avoid exposing unnecessary database errors or records.

## 8. Evidence

The following evidence is included in the repository:

- `evidence/finding-01-sql-injection/SQL Injection - Evidence.PNG`
  - Screenshot showing the SQL injection input and returned records.
- `evidence/finding-01-sql-injection/poc-execution.txt`
  - Successful Python PoC execution output.
- `poc/sql_injection_poc.py`
  - Automated PoC that authenticates to DVWA using its login CSRF token and tests the SQL injection condition.

## 9. Conclusion

SQL Injection was successfully demonstrated in the authorized DVWA lab at Low security level.

The crafted input caused five database records to be returned, confirming that the application does not safely handle this test input.

This finding will help guide future detection engineering and security remediation tasks.
