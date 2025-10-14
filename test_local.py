import requests
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()

# Get your secret from .env
USER_SECRET = os.getenv("USER_SECRET")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")

print("=" * 60)
print("🧪 TESTING LLM CODE DEPLOYMENT PROJECT")
print("=" * 60)

# Test data
test_payload = {
    "email": "test@example.com",
    "secret": USER_SECRET,
    "task": f"test-task-{int(time.time())}",  # Unique task name
    "round": 1,
    "nonce": f"nonce-{int(time.time())}",
    "brief": "Create a simple HTML page with a heading 'Test Page' and a paragraph saying 'This is a test.'",
    "checks": [
        "Page has a heading",
        "Page has a paragraph",
        "HTML is valid"
    ],
    "evaluation_url": "https://postman-echo.com/post",  # Test URL that echoes back
    "attachments": []
}

print("\n📋 Test Configuration:")
print(f"   GitHub Username: {GITHUB_USERNAME}")
print(f"   Task ID: {test_payload['task']}")
print(f"   Secret: {'✓ Loaded' if USER_SECRET else '✗ Missing'}")

# Step 1: Check if server is running
print("\n1️⃣  Checking if server is running...")
try:
    response = requests.get("http://127.0.0.1:8000/docs", timeout=5)
    if response.status_code == 200:
        print("   ✅ Server is running!")
    else:
        print("   ⚠️  Server responded but with unexpected status")
except requests.exceptions.ConnectionError:
    print("   ❌ Server is NOT running!")
    print("   👉 Run: uvicorn app.main:app --reload")
    exit(1)
except Exception as e:
    print(f"   ❌ Error: {e}")
    exit(1)

# Step 2: Send test request
print("\n2️⃣  Sending test request to /api-endpoint...")
try:
    response = requests.post(
        "http://127.0.0.1:8000/api-endpoint",
        json=test_payload,
        timeout=10
    )
    
    print(f"   Status Code: {response.status_code}")
    print(f"   Response: {response.json()}")
    
    if response.status_code == 200:
        print("   ✅ Request accepted!")
    else:
        print("   ❌ Request failed!")
        exit(1)
        
except Exception as e:
    print(f"   ❌ Error sending request: {e}")
    exit(1)

# Step 3: Wait for background processing
print("\n3️⃣  Waiting for background processing (30 seconds)...")
print("   (Watch the server terminal for logs)")
for i in range(30, 0, -5):
    print(f"   ⏱️  {i} seconds remaining...")
    time.sleep(5)

# Step 4: Check if repo was created
print("\n4️⃣  Verifying GitHub repo creation...")
repo_url = f"https://github.com/{GITHUB_USERNAME}/{test_payload['task']}"
print(f"   Expected repo: {repo_url}")

try:
    response = requests.get(repo_url, timeout=10)
    if response.status_code == 200:
        print("   ✅ Repository created successfully!")
    else:
        print("   ⚠️  Repository not found (might need more time)")
except Exception as e:
    print(f"   ⚠️  Could not verify repo: {e}")

# Step 5: Check GitHub Pages
print("\n5️⃣  Checking GitHub Pages...")
pages_url = f"https://{GITHUB_USERNAME}.github.io/{test_payload['task']}/"
print(f"   Expected URL: {pages_url}")
print("   ⏱️  Waiting 10 seconds for Pages to deploy...")
time.sleep(10)

try:
    response = requests.get(pages_url, timeout=10)
    if response.status_code == 200:
        print("   ✅ GitHub Pages is live!")
        print(f"   🌐 Visit: {pages_url}")
    else:
        print("   ⚠️  Pages not ready yet (can take 1-2 minutes)")
except Exception as e:
    print(f"   ⚠️  Pages not accessible yet: {e}")

# Summary
print("\n" + "=" * 60)
print("📊 TEST SUMMARY")
print("=" * 60)
print(f"✅ Server is running")
print(f"✅ API endpoint accepts requests")
print(f"🔗 Check your repo: {repo_url}")
print(f"🌐 Check your page: {pages_url}")
print("\n💡 TIP: GitHub Pages can take 1-2 minutes to become available")
print("=" * 60)