# Get information from GitHub API with the username:
import requests

def get_user_info(username):
    url = "https://api.github.com/users/{}".format(username)
    response = requests.request("GET", url)
    return response.json()

def get_followers_info(username):
	url = "https://api.github.com/users/{}/followers".format(username)
	params = {'per_page': 100}
	response = requests.request("GET", url, params=params)
	return response.json()