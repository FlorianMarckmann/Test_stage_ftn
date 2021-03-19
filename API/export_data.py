from github import Github
import json

data = {}
data['issue'] = []

# using an access token
g = Github("69f7f9a521e3acf1fae10a2363acacc59d3c6a7a")

repo = g.get_repo("PyGithub/PyGithub")
open_issues = repo.get_issues(state='open')
open('./API/data_issues.json', 'w').close()
for issue in open_issues:
	data['issue'].append({'title': issue.title, 'number': issue.number})

with open('./API/data_issues.json', 'aw') as f:
	json.dump(data, f, indent = 4, sort_keys=True)
	print(">> Data exported")
		
