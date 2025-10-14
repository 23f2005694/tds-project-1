import requests

# Your test data
data = {
    "email": "test@example.com",
    "secret": "i dont have any secret",
    "task": "test-task-789",
    "round": 1,
    "nonce": "nonce-789",
    "brief": "Create a simple HTML page with a heading",
    "checks": ["Page has a heading"],
    "evaluation_url": "https://webhook.site/e64669ca-0b4b-4bbb-80c6-a037077af5a4",  # Change this!
    "attachments": []
}

# Send request
print("📤 Sending request...")
response = requests.post("http://127.0.0.1:8000/api-endpoint", json=data)

print(f"✅ Status: {response.status_code}")
print(f"📨 Response: {response.json()}")