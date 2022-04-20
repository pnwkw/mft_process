from pathlib import Path
import json
import shutil

YEAR = 2022
MONTH = 'APR'
RUN = 513464

hit_list = []

files_list = json.load(open('alien_filelist.json', 'r'))

filedict = {}

for part, file in files_list:
	filedict[file] = part

pathlist = Path('output').rglob('*.json')
for path in pathlist:
	tracks = json.load(open(path, 'r'))

	if tracks['trackCount'] > 0:
		print(f'TRACKS: {tracks["trackCount"]} -> {str(path)}')
		ctf = f'o2_ctf_run00{RUN}_{path.parts[-2]}.root'
		hit_list.append(f'/alice/data/{YEAR}/{MONTH}/{RUN}/raw/{filedict[ctf]}/{ctf}')
		shutil.copy2(path, f'./jsons/{path.parts[-1]}')

with open('hits.json', 'w') as f:
	f.write(json.dumps(hit_list))

print(f'TOTAL: {len(hit_list)} CTFs')
