#!/usr/bin/python

import request as r


'''
GitHub API object
'''

class Api(object):

	'''
	Instantiate with github authentication info. If the authenticated user
	has signed up for the github developer program, then the rate-limit for
	api calls is 5000/hour. Otherwise, for an unauthenticated user, it is 60/hour.
	'''
	def __init__(self, \
				username=None, \
				password=None):
		if username and password:
			self._auth = (username, password)
		else:
			self._auth = None

	'''
	https://developer.github.com/v3/users/
	'''
	def users(self, username=None, since=None):
		#https://developer.github.com/v3/users/#get-a-single-user
		if username:
			return r.Request.get( ('users/' + username), self._auth)
		#https://developer.github.com/v3/users/#get-all-users
		else:
			if since:
				since_param = 'users?since=' + str(since)
				return r.Request.get(since_param, self._auth)
			else:
				return r.Request.get('users', self._auth)

	'''
	if one or more parameters are passed in, update (PATCH) the user:
		https://developer.github.com/v3/users/#update-the-authenticated-user
	else, get (GET) the user:
		https://developer.github.com/v3/users/#get-the-authenticated-user
	'''
	def user(self, 
			name=None, \
			email=None, \
			blog=None, \
			company=None, \
			location=None, \
			hireable=None, \
			bio=None):
 
		payload = {}

		args = [arg for arg in locals().items()]

		for arg in args:
				if arg[1] is not None and arg[0] is not 'self' and arg[0] is not 'payload':
					payload[ arg[0] ] = arg[1]

		return r.Request.patch('user', payload, self._auth) if len(payload) > 0 else r.Request.get('user', self._auth)






