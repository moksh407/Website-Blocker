import time
from datetime import datetime as dt

# r is used to avoid escape sequences in the dir name
# or we can use 2 \\ instead of r.
hosts_path_windows=r"C:\Windows\System32\drivers\etc\hosts"
hosts_path_Linux_mac=r'/etc/hosts'
redirect='127.0.0.1'
website_list=['www.facebook.com','facebook.com']

while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,0,0) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,2,0):
		
		with open(hosts_path_Linux_mac,'r+') as file:
			content=file.read()
			print('working hours...')
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect+' '+website+'\n')
	
	else:
		
		with open(hosts_path_Linux_mac,'r+') as file:
			content=file.readlines()
			file.seek(0)
			print('Play hours...')
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()
	time.sleep(1)