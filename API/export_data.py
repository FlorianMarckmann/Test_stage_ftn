from github import Github
import json

data = {}
data['issue'] = []

# using an access token
g = Github("1f18903ceb60ae44d01e00afdea0b2a125e02f9b")

repo = g.get_repo("PyGithub/PyGithub")
open_issues = repo.get_issues(state='open')
open('./API/data_issues.json', 'w').close()
for issue in open_issues:
	data['issue'].append({'title': issue.title, 'number': issue.number})

with open('./API/data_issues.json', 'aw') as f:
	json.dump(data, f, indent = 4, sort_keys=True)
	print(">> Data exported")
		
