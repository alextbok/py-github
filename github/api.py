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
				url_rem = 'users?since=' + str(since)
				return r.Request.get(url_rem, self._auth)
			else:
				return r.Request.get('users', self._auth)

	'''
	if one or more parameters are passed in, update (PATCH) the user:
		https://developer.github.com/v3/users/#update-the-authenticated-user
	else, get (GET) the user:
		https://developer.github.com/v3/users/#get-the-authenticated-user
	'''
	def user(self,
			method='GET', \
			name=None, \
			email=None, \
			blog=None, \
			company=None, \
			location=None, \
			hireable=None, \
			bio=None):
 
		if method is not 'GET' or method is not 'PATCH':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'PATCH\' '
			return

		if method is 'PATCH':
			payload = {}
			args = [arg for arg in locals().items()]
			for arg in args:
					if arg[1] is not None and arg[0] is not 'self' and arg[0] is not 'payload':
						payload[ arg[0] ] = arg[1]
			return r.Request.patch('user', payload, self._auth)
		return r.Request.get('user', self._auth)

	'''
	if method is 'GET':
		https://developer.github.com/v3/repos/#list-your-repositories
	else:
		https://developer.github.com/v3/repos/#create
	'''
	def user_repos(self, \
					method='GET', \
					type=None, \
					sort=None, \
					direction=None, \
					name=None, \
					description=None, \
					homepage=None, \
					private=None, \
					has_issues=None, \
					has_wiki=None, \
					has_downloads=None, \
					team_id=None, \
					auto_init=None, \
					gitignore_template=None, \
					license_template=None):

		if method is not 'GET' or method is not 'POST':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\' '
			return

		payload = {}

		args = [arg for arg in locals().items()]

		for arg in args:
				if arg[1] is not None and arg[0] not in {'self' : 1, 'payload' : 1, 'method' : 1}:
					payload[ arg[0] ] = arg[1]

		if method is 'POST':
			if not name:
				print "ERROR: name is a required parameter wen creating a repository"
				return
			return r.Request.post('user/repos', payload, self._auth)
		return r.Request.get_with_params('user/repos', payload, self._auth) if len(payload) > 0 else r.Request.get('user/repos', self._auth)

	'''
	https://developer.github.com/v3/repos/#list-user-repositories
	'''
	def users_repos(self, \
					username, \
					type=None, \
					sort=None, \
					direction=None):
		payload = {}

		args = [arg for arg in locals().items()]

		for arg in args:
				if arg[1] is not None and arg[0] not in {'self' : 1, 'payload' : 1, 'username' : 1}:
					payload[ arg[0] ] = arg[1]

		url_rem = 'users/' + username + '/repos'

		return r.Request.get_with_params(url_rem, payload, self._auth) if len(payload) > 0 else r.Request.get(url_rem, self._auth)

	'''
	https://developer.github.com/v3/repos/#list-organization-repositories
	'''
	def orgs_repos(self, \
					org, \
					method='GET', \
					_type=None, \
					name=None, \
					description=None, \
					homepage=None, \
					private=None, \
					has_issues=None, \
					has_wiki=None, \
					has_downloads=None, \
					team_id=None, \
					auto_init=None, \
					gitignore_template=None, \
					license_template=None):

		if method is not 'GET' or method is not 'POST':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\' '
			return

		url_rem = 'orgs/' + org + '/repos'

		if method is 'POST':
			payload = {}
			args = [arg for arg in locals().items()]
			for arg in args:
				if arg[1] is not None and arg[0] not in {'self' : 1, 'payload' : 1, 'org' : 1, 'method' : 1, '_type' : 1 }:
					payload[ arg[0] ] = arg[1]
			return r.Request.post(url_rem, payload, self._auth)
		return r.Request.get_with_params(url_rem, { 'type' : _type }, self._auth) if type else r.Request.get(url_rem, self._auth)

	'''
	https://developer.github.com/v3/repos/#list-all-public-repositories
	'''
	def repositories(self, since=None):
			if since:
				url_rem = 'repositores?since=' + str(since)
				return r.Request.get(url_rem, self._auth)
			else:
				return r.Request.get('repositories', self._auth)


	'''
	if method is 'GET':
		https://developer.github.com/v3/repos/#get
	elif method is 'PATCH':
		https://developer.github.com/v3/repos/#edit
	elif method is 'DELETE':
		https://developer.github.com/v3/repos/#delete
	'''
	def repos(self, \
				owner, \
				repo, \
				method='GET', \
				name=None, \
				description=None, \
				homepage=None, \
				private=None, \
				has_issues=None, \
				has_wiki=None, \
				has_downloads=None, \
				default_branch=None):

		if method is not 'GET' or method is not 'PATCH' or method is not 'delete'.upper():
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'PATCH\' or \'DELETE\' '
			return

		url_rem = 'repos/' + owner + '/' + repo

		if method is 'PATCH':
			payload = {}
			args = [arg for arg in locals().items()]
			for arg in args:
				if arg[1] is not None and arg[0] not in {'self' : 1, 'payload' : 1, 'owner' : 1, 'method' : 1, 'repo' : 1 }:
					payload[ arg[0] ] = arg[1]
			return r.Request.patch(url_rem, payload, self._auth)
		else if method is 'delete'.upper():
			return r.Request.delete(url_rem, self._auth)
		return r.Request.get(url_rem, self._auth)

	'''
	https://developer.github.com/v3/repos/#list-contributors
	'''
	def repos_contributors(self, \
							owner, \
							repo, \
							anon=None):
		url_rem = 'repos/' + owner + '/' + repo + '/contributors'
		return r.Request.get_with_params(url_rem, { 'anon' : anon }, self._auth) if anon else r.Request.get(url_rem, self._auth)

	'''
	https://developer.github.com/v3/repos/#list-languages
	'''
	def repos_languages(self, owner, repo):
		url_rem = 'repos/' + owner + '/' + repo + '/languages'
		return r.Request.get(url_rem, self._auth)

	'''
	https://developer.github.com/v3/repos/#list-teams
	'''
	def repos_teams(self, owner, repo):
		url_rem = 'repos/' + owner + '/' + repo + '/teams'
		return r.Request.get(url_rem, self._auth)

	'''
	https://developer.github.com/v3/repos/#list-tags
	'''
	def repos_tags(self, owner, repo):
		url_rem = 'repos/' + owner + '/' + repo + '/tags'
		return r.Request.get(url_rem, self._auth)

	'''
	https://developer.github.com/v3/repos/#list-branches
	'''
	def repos_branches(self, \
						owner, \
						repo,\
						branch=None):
		url_rem = 'repos/' + owner + '/' + repo + '/branches'
		if branch:
			url_rem += '/' + str(branch)
		return r.Request.get(url_rem, self._auth)




