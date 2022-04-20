import subprocess
import json

YEAR = 2022
MONTH = 'APR'
RUN = 513464

parts_list = [1710, 1720, 1730, 1740, 1800]

files_list = []

for p in parts_list:
	path = f'/alice/data/{YEAR}/{MONTH}/{RUN}/raw/{p}'
	res = subprocess.run(["alien.py", "ls", path], stdout=subprocess.PIPE)
	files = res.stdout.decode('ascii').split('\n')
	for f in files:
		if len(f) > 0:
			files_list.append([p, f])

with open('alien_filelist.json', 'w') as f:
	f.write(json.dumps(files_list))

print(f'NUM FILES IN DIRECTORY: {len(files_list)}')
