# DELETE all workflow run 
### Run
First get your token via [Github Token provider](https://github.com/settings/tokens)
<br>
Then change .env file as you need it should be like this 
```dotenv
OWNER=owner
REPO=repo
USERNAME=username
TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
Then run these command on your Terminal/Console
```bash
# Install requirements
pip install -r requirements.txt
# Run script
python3 main.py
```

### End points
##### GET runs
```dotenv
https://api.github.com/repos/{OWNER}/{REPO}/actions/runs
```
##### DELETE runs 
```dotenv
https://api.github.com/repos/{OWNER}/{REPO}/actions/runs/{run_id}
```