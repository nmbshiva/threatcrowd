#python3

import requests
import json
import sys
from datetime import datetime

if len(sys.argv) < 2:
	sys.exit("[!] Error! No domain specified!\n")

f=open(sys.argv[1]+'.txt', 'w')
log=open('log.txt', 'w')
i=datetime.now()

print("\nQuerying threatcrowd to find list of subdomains\n")
print("[+] Started at {0}".format(i.strftime("%H:%M:%S %d/%m/%Y")))
print("[+] Querying domain {0}, please wait.\n".format(sys.argv[1]))

try:
	
	result=requests.get("http://www.threatcrowd.org/searchApi/v2/domain/report/", \
	params={"domain": sys.argv[1]})
	data=json.loads(result.text)
	print("[+] Written to file {0}.txt.".format(sys.argv[1]))
	urls=json.loads(result.text)
	print("[+] Subdomains found:\n")
	for url in urls["subdomains"]:
		print("	-> {0}".format(url))
		f.write(url + "\n")
	print("\n")
	log.write("\n<!-- "+ i.strftime("%H:%M:%S %d/%m/%Y") +" -->\n")
	log.write(json.dumps(data, indent=4, sort_keys=True))
	log.write("\n")
	f.close()
	log.close()

except Exception as e:
	print(e)
	f.close()
	sys.exit(0)
