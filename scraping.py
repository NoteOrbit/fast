import requests, traceback, json

all_items = []
user = 2593236
stack = "stackoverflow.com"
qa = "questions" # or answers


page = 1
while 1:
	u = f"https://api.stackexchange.com/2.2/users/{user}/{qa}?site={stack}&page={page}&pagesize=100"
	j = requests.get(u).json()
	if j:

		all_items += j["items"]

		if not j['has_more']:
			print("No more Pages")
			break
		elif not j['quota_remaining']:
			print("No Quota Remaining ")
			break
	else:
		print("No Questions")
		break

	page+=1


if all_items:
	print(f"How many {qa}? ", len(all_items))
	# save questions/answers to file
	with open(f"{user}_{qa}_{stack}.json", "w") as f:
		f.write(json.dumps(all_items))