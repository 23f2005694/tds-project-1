import requests

url = "https://tripterous-mentholated-paloma.ngrok-free.dev/api-endpoint"

data = {
    "email": "student@example.com",
    "secret": "mysecret123",
    "task": "github-user-info-001",
    "round": 1,
    "nonce": "ef56-003",
    "brief": "Create a Bootstrap page with a form #github-user-form that fetches a GitHub username and displays the account creation date in YYYY-MM-DD format inside #github-created-at.",
    "checks": [
        "Repo has MIT license",
        "README.md explains setup",
        "Form renders correctly and fetches GitHub user info"
    ],
    "evaluation_url": "https://webhook.site/e64669ca-0b4b-4bbb-80c6-a037077af5a4",
    "attachments": []
}

resp = requests.post(url, json=data)

print("Status code:", resp.status_code)
try:
    print("JSON response:", resp.json())
except Exception:
    print("Raw response:", resp.text)
