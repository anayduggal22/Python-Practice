import requests

def safe_call(url):
    try:
        r = requests.get(url, timeout= 10)

        r.raise_for_status() #Which will cause exception

        return r.json()

    except r.exceptions.Timeout:
        print("Timed Out")
        return None
    
    except r.exceptions.HTTPError as e:
        print(f"HTTP Erro: {e}")
        return None
    except r.exceptions.ConnectionError:
        print(f"No Internet")
        return None

data = safe_call("https://jsonplaceholder.typicode.com/users/1")
if data:
    print("Got:", data["name"])

# Test bad URL
data = safe_call("https://jsonplaceholder.typicode.com/users/9999")
if data is None:
    print("Failed gracefully — no crash")
    