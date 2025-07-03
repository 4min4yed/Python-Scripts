import requests
ip=input('What ip re you scanning?')
http = "http"
https = "https"
ports = [1, 80, 111, 443, 3128, 5212, 5555, 7000, 8006]
print('ports to be scanned:', ports)
prtcls = [http, https]

for i in ports:
    for j in prtcls:
        url = f"{j}://{ip}:{i}"
        try:
            r = requests.get(url, timeout=3)
            print(url, "OK")
        except requests.exceptions.Timeout:
            print(url, "Timed out")
        except requests.exceptions.ConnectionError:
            print(url, "Connection error")
        except requests.exceptions.RequestException as e:
            print(url, "Request failed:", e)
