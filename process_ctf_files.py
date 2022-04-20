import subprocess
import json
import argparse
import os

YEAR = 2022
MONTH = 'APR'
RUN = 513464

MAX_WORKERS = 4

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--slice", type=int)
args = parser.parse_args()

files_list = json.load(open('alien_filelist.json', 'r'))

JOBS = len(files_list) // MAX_WORKERS

START = args.slice * JOBS
END = (args.slice + 1) * JOBS

print(f'Worker {args.slice} ready to process slice from {START} TO {END-1}')

os.makedirs('./data', exist_ok=True)
os.makedirs('./output', exist_ok=True)

for part,file in files_list[START:END]:
	name = file.split('.')[0].split('_')
	json_dirname = f'{name[3]}_{name[4]}'
	print(json_dirname)
	path_in = f'alien:///alice/data/{YEAR}/{MONTH}/{RUN}/raw/{part}/{file}'
	path_out = f'file://data/{file}'
	subprocess.run(["alien.py", "cp", path_in, path_out], stdout=subprocess.PIPE)
	subprocess.run([f'./process.sh ./data/{file} ./output/{json_dirname}'], shell=True)
	os.remove(f'./data/{file}')
