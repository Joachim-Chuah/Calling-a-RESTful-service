import requests
import time

def fetch_quote(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Success: {response.json()}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    base_url = "http://quoters:8080"
    endpoints = ["/api/random", "/api/", "/api/1", "/api/2"]
    
    time.sleep(10)
    
    for endpoint in endpoints:
        fetch_quote(f"{base_url}{endpoint}")
