""""
Delete all workflow run on github
"""
import requests
from dotenv import load_dotenv
from os import environ
load_dotenv()


OWNER = environ.get("OWNER")
REPO = environ.get("REPO")
USERNAME = environ.get("USERNAME")
TOKEN = environ.get("TOKEN")

auth = (USERNAME, TOKEN)

print(f"getting workflow run {REPO}")
runs_url = f'https://api.github.com/repos/{OWNER}/{REPO}/actions/runs'
runs = requests.get(runs_url).json()
print(f"got {runs['total_count']} runs")

for run in runs["workflow_runs"]:
    run_id = run['id']
    delete = requests.delete(f'https://api.github.com/repos/{OWNER}/{REPO}/actions/runs/{run_id}', auth=auth)
    if delete.status_code == 204:
        print(f"Deleted {run_id}")
    else:
        print(f"Failed to delete {run_id}")