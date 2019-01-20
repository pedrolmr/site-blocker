import time
from datetime import datetime as dt

hosts_path_windows = r"C:\Windows\System32\drivers\etc\hosts"
hosts_path_unix = "/etc/hosts"
host_dir = "hosts"

links = [
    'www.blogger.com',
    'blogger.com'
]
redirect = "127.0.0.1"
start_time = 10
end_time = 23

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, start_time) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_time):
        with open(host_dir, 'r+') as file:
            content = file.read()
            for link in links:
                if link in content:
                    pass
                else:
                    file.write(redirect + " " + link + "\n")
        print('working...')
    else:
        print('app is resting')
    time.sleep(1)
