#!/usr/bin/python

from github import requests
from github import simplejson as json
import memoized

'''
Makes (un)authenticated calls to the GitHub API
Calls are memoized to help with rate-limit
'''

GITHUB_API_BASE_URL = 'https://api.github.com/'

class Request():

	'''
	GET
	Memoized so repeated requests with the same arguments don't eat away at our precious rate-limit
	'''
	@staticmethod
	@memoized.Memoized
	def get(url_remainder, auth=None):
		url = GITHUB_API_BASE_URL + url_remainder
		return requests.get(url, auth=auth) if auth else requests.get(url)

	@staticmethod
	def post(url_remainder, data, auth=None):
		url = GITHUB_API_BASE_URL + url_remainder
		return requests.post(url, data=json.dumps(data), auth=auth) if auth else requests.post(url, data=data)

	@staticmethod
	def patch(url_remainder, data, auth=None):
		url = GITHUB_API_BASE_URL + url_remainder
		return requests.post(url, data=json.dumps(data), auth=auth) if auth else requests.post(url, data=data)


