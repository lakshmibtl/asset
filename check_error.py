import urllib.request
import urllib.error

url = "http://127.0.0.1:8000/login/"
try:
    response = urllib.request.urlopen(url)
    print(f"Status code: {response.getcode()}")
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code}")
    print(e.read().decode('utf-8')[:1000])
except Exception as e:
    print(f"Error: {e}")
