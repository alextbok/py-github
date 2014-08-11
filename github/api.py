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
	def __init__(self, username=None, password=None):
		if username is not None and password is not None:
			self._auth = (username, password)
		else:
			self._auth = None

	###########
	###USERS###
	###########

	'''
	if username:
		https://developer.github.com/v3/users/#get-a-single-user
	else:
		https://developer.github.com/v3/users/#get-all-users
	'''
	def users(self, username=None, since=None):
		if username is not None:
			return r.Request.get( ('users/' + username), self._auth)
		else:
			if since is not None:
				return r.Request.get( ('users?since=' + str(since)), self._auth)
			else:
				return r.Request.get('users', self._auth)

	'''
	if method is 'GET':
		https://developer.github.com/v3/users/#get-the-authenticated-user
	else:
		https://developer.github.com/v3/users/#update-the-authenticated-user
	'''
	def user(self, method='GET', **kwargs):
 
		if method is not 'GET' and method is not 'PATCH':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'PATCH\' '
			return

		if method is 'PATCH':
			payload = {}
			for arg in kwargs:
				payload[arg] = kwargs[arg]
			return r.Request.patch('user', payload, self._auth)
		return r.Request.get('user', self._auth)

	###########
	###REPOS###
	###########

	'''
	if method is 'GET':
		https://developer.github.com/v3/repos/#list-your-repositories
	else:
		https://developer.github.com/v3/repos/#create
	'''
	def user_repos(self, method='GET', **kwargs):

		if method is not 'GET' and method is not 'POST':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\' '
			return

		payload = {}
		for arg in kwargs:
			payload[arg] = kwargs[arg]

		if method is 'POST':
			if name is None:
				print "ERROR: name is a required parameter when creating a repository"
				return
			return r.Request.post('user/repos', payload, self._auth)
		return r.Request.get_with_params('user/repos', payload, self._auth) if len(payload) > 0 else r.Request.get('user/repos', self._auth)

	'''
	https://developer.github.com/v3/repos/#list-user-repositories
	'''
	def users_repos(self, username, **kwargs):

		payload = {}
		for arg in kwargs:
			payload[arg] = kwargs[arg]

		url_rem = 'users/' + username + '/repos'
		return r.Request.get_with_params(url_rem, payload, self._auth) if len(payload) > 0 else r.Request.get(url_rem, self._auth)

	'''
	https://developer.github.com/v3/repos/#list-organization-repositories
	'''
	def orgs_repos(self, org, method='GET', **kwargs):

		if method is not 'GET' and method is not 'POST':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\' '
			return

		url_rem = 'orgs/' + org + '/repos'

		if method is 'POST':
			payload = {}
			for arg in kwargs:
				payload[arg] = kwargs[arg]
			return r.Request.post(url_rem, payload, self._auth)
		return r.Request.get_with_params(url_rem, { 'type' : _type }, self._auth) if type else r.Request.get(url_rem, self._auth)

	'''
	https://developer.github.com/v3/repos/#list-all-public-repositories
	'''
	def repositories(self, since=None):
			if since is not None:
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
	def repos(self, owner, repo, method='GET', **kwargs):

		if method is not 'GET' and method is not 'PATCH' and method is not 'delete'.upper():
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'PATCH\' or \'DELETE\' '
			return

		url_rem = 'repos/' + owner + '/' + repo

		if method is 'PATCH':
			payload = {}
			for arg in kwargs:
				payload[arg] = kwargs[arg]
			return r.Request.patch(url_rem, payload, self._auth)
		elif method is 'delete'.upper():
			return r.Request.delete(url_rem, self._auth)
		return r.Request.get(url_rem, self._auth)

	'''
	https://developer.github.com/v3/repos/#list-contributors
	'''
	def repos_contributors(self, owner, repo, **kwargs):
		payload = {}
		for arg in kwargs:
			payload[arg] = kwargs[arg]
		url_rem = 'repos/' + owner + '/' + repo + '/contributors'
		return r.Request.get_with_params(url_rem, payload, self._auth) if anon else r.Request.get(url_rem, self._auth)

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
	def repos_branches(self, owner, repo, branch=None):
		url_rem = 'repos/' + owner + '/' + repo + '/branches'
		if branch is not None:
			url_rem += '/' + str(branch)
		return r.Request.get(url_rem, self._auth)

	###########
	##EVENTS###
	###########

	'''
	https://developer.github.com/v3/activity/events/#list-public-events
	'''
	def events(self):
		return r.Request.get('events', self._auth)

	'''
	https://developer.github.com/v3/activity/events/#list-repository-events
	'''
	def repos_events(self, owner, repo):
		url_rem = 'events/' + owner + '/' + repo + '/events'
		return r.Request.get(url_rem, self._auth)

	'''
	https://developer.github.com/v3/activity/events/#list-issue-events-for-a-repository
	'''
	def repos_issues_events(self, owner, repo):
		url_rem = 'events/' + owner + '/' + repo + '/issues/events'
		return r.Request.get(url_rem, self._auth)

	'''
	https://developer.github.com/v3/activity/events/#list-public-events-for-a-network-of-repositories
	'''
	def networks_events(self, owner, repo):
		url_rem = 'networks/' + owner + '/' + repo + '/events'
		return r.Request.get(url_rem, self._auth)

	'''
	https://developer.github.com/v3/activity/events/#list-public-events-for-an-organization
	'''
	def orgs_events(self, org):
		url_rem = 'orgs/' + org + '/events'
		return r.Request.get(url_rem, self._auth)


	'''
	https://developer.github.com/v3/activity/events/#list-events-that-a-user-has-received
	'''
	def user_received_events(self, user):
		url_rem = 'users/' + user + '/received_events'
		return r.Request.get(url_rem, self._auth)		

	'''
	https://developer.github.com/v3/activity/events/#list-public-events-that-a-user-has-received
	'''
	def user_received_events_public(self, user):
		url_rem = 'users/' + user + '/received_events/public'
		return r.Request.get(url_rem, self._auth)		

	'''
	https://developer.github.com/v3/activity/events/#list-events-for-an-organization
	'''
	def users_events_orgs(self, user, org):
		url_rem = 'users/' + user + '/events/orgs/' + org
		return r.Request.get(url_rem, self._auth)

	###########
	###FEEDS###
	###########

	def feeds(self):
		return r.Request.get('feeds', self._auth)

	#################
	##NOTIFICATIONS##
	#################

	'''
	if method is 'GET':
		https://developer.github.com/v3/activity/notifications/#list-your-notifications
	else:
		https://developer.github.com/v3/activity/notifications/#mark-as-read
	'''
	def notifications(self, method='GET', **kwargs):

		if method is not 'GET' and method is not 'PUT':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'PUT\' '
			return

		payload = {}
		for arg in kwargs:
			payload[arg] = kwargs[arg]
		if method is 'PUT':
			return r.Request.put('notifications', payload, None, self._auth) if len(payload) > 0 else r.Request.put('notifications', None, { 'Content-Length' : None}, self._auth)
		return r.Request.get_with_params('notifications', payload, self._auth) if len(payload) > 0 else r.Request.get('notifications', self._auth)

	'''
	https://developer.github.com/v3/activity/notifications/#list-your-notifications-in-a-repository
	'''
	def repos_notifications(self, owner, repo, **kwargs):
		url_rem = 'repos/' + owner + '/' + repo + '/notifications'
		params = {}
		for arg in kwargs:
			params[arg] = kwargs[arg]
		return r.Request.get_with_params(url_rem, params, self._auth) if len(params) > 0 else r.Request.get(url_rem, self._auth)


	'''
	if method is 'GET':
		https://developer.github.com/v3/activity/notifications/#view-a-single-thread
	else:
		https://developer.github.com/v3/activity/notifications/#mark-a-thread-as-read
	'''
	def notifications_threads(self, id, method='GET'):
		if method is not 'GET' and method is not 'PATCH':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'PATCH\' '
			return
		if method is 'PATCH':
			return r.Request.patch('notifications/threads/' + str(id), self._auth)
		return r.Request.get('notifications/threads/' + str(id), self._auth)

	'''
	if method is 'GET':
		https://developer.github.com/v3/activity/notifications/#get-a-thread-subscription
	elif method is 'PUT':
		https://developer.github.com/v3/activity/notifications/#set-a-thread-subscription
	elif method is 'DELETE':
		https://developer.github.com/v3/activity/notifications/#delete-a-thread-subscription
	'''
	def notifications_threads_subscription(self, id, method='GET', **kwargs):
		if method is not 'GET' and method is not 'PUT' and method is not 'delete'.upper():
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'PUT\' or \'DELETE\''
			return
		url_rem = 'notifications/threads/' + str(id) + '/subscription'
		if method is 'PUT':
			payload = {}
			for arg in kwargs:
				payload[arg] = kwargs[arg]
			return r.Request.put(url_rem, payload, None, self._auth) if len(payload) > 0 else r.Request.put(url_rem, None, { 'Content-Length' : 0 }, self._auth)
		if method is 'delete'.upper():
			return r.Request.delete(url_rem, self._auth)
		return r.Request.get(url_rem, self._auth)


	##############
	###STARRING###
	##############

	'''
	https://developer.github.com/v3/activity/starring/#list-stargazers
	'''
	def repos_stargazers(self, owner, repo):
		url_rem = 'repos/' + owner + '/' + repo + '/stargazers'
		return r.Request.get(url_rem, self._auth)

	'''
	https://developer.github.com/v3/activity/starring/#list-repositories-being-starred
	'''
	def users_starred(self, username=None, **kwargs):
		params = {}
		for arg in kwargs:
			params[arg] = kwargs[arg]
		if username is not None:
			return r.Request.get_with_params('users/' + username + '/starred', params, self._auth) if len(params) > 0 else r.Request.get('users/' + username + '/starred', self._auth)
		return r.Request.get_with_params('users/starred', params, self._auth) if len(params) > 0 else r.Request.get('users/starred', self._auth)

	'''
	if method is 'GET':
		https://developer.github.com/v3/activity/starring/#check-if-you-are-starring-a-repository
	elif method is 'PUT':
		https://developer.github.com/v3/activity/starring/#star-a-repository
	elif method is DELETE:
		https://developer.github.com/v3/activity/starring/#unstar-a-repository
	'''
	def user_starred(self, owner, repo, method='GET'):
		if method is not 'GET' and method is not 'delete'.upper() and method is not 'PUT':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'DELETE\' or \'PUT\''
			return
		url_rem = 'user/starred/' + owner + '/' + repo
		if method is 'PUT':
			return r.Request.put(url_rem, None, { 'Content-Length' : 0 }, self._auth)
		if method is 'delete'.upper():
			return r.Request.delete(url_rem, self._auth)
		return r.Request.get(url_rem, self._auth)

	##############
	###WATCHING###
	##############

	'''
	https://developer.github.com/v3/activity/watching/#list-watchers
	'''
	def repos_subscribers(self, owner, repo):
		url_rem = 'repos/' + owner + '/' + repo + '/subscribers'
		return r.Request.get(url_rem, self.auth)

	'''
	https://developer.github.com/v3/activity/watching/#list-repositories-being-watched
	'''
	def users_subscriptions(self, user):
		url_rem = 'users/' + user + '/subscriptions'
		return r.Request.get(url_rem, self.auth)

	'''
	https://developer.github.com/v3/activity/watching/#list-repositories-being-watched
	'''
	def user_subscriptions(self):
		return r.Request.get('user/subscriptions', self.auth)

	'''
	https://developer.github.com/v3/activity/watching/#get-a-repository-subscription
	'''
	def repos_subscription(self, owner, repo, method='GET', **kwargs):
		if method is not 'GET' and method is not 'PUT' and method is not 'delete'.upper():
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'PUT\' or \'DELETE\''
			return
		url_rem = 'repos/' + owner + '/' + repo + '/subscription'
		if method is 'PUT':
			payload = {}
			for arg in kwargs:
				payload[arg] = kwargs[arg]
			return r.Request.put(url_rem, payload, None, self._auth) if len(payload) > 0 else r.Request.put(url_rem, None, { 'Content-Length' : 0 }, self._auth)
		if method is 'delete'.upper():
			return r.Request.delete(url_rem, self._auth)
		return r.Request.get(url_rem, self._auth)

	###########
	###GISTS###
	###########

	'''
	https://developer.github.com/v3/gists/#list-gists
	'''		
	def users_gists(self, user, since=None):
		url_rem = 'user/' + user + '/gists'
		if since is not None:
			url_rem += '?since=' + str(since)
		return r.Request.get(url_rem, self._auth) 

	def gists_public(self, user, since=None):
		url_rem = 'gists/public'
		if since is not None:
			url_rem += '?since=' + str(since)
		return r.Request.get(url_rem, self._auth) 

	def gists_starred(self, user, since=None):
		url_rem = 'gists/starred'
		if since is not None:
			url_rem += '?since=' + str(since)
		return r.Request.get(url_rem, self._auth) 

	'''
	if id is None:
		https://developer.github.com/v3/gists/#list-gists
	if id is not None and method is 'GET':
		https://developer.github.com/v3/gists/#get-a-single-gist
	if method is 'POST':
		https://developer.github.com/v3/gists/#create-a-gist
	if method is 'PATCH':
		https://developer.github.com/v3/gists/#edit-a-gist
	if method is 'DELETE':
		https://developer.github.com/v3/gists/#delete-a-gist
	'''
	def gists(self, \
				user, \
				method='GET', \
				_id=None, \
				since=None, \
				files=None, \
				description=None, \
				public=None, \
				content=None, \
				filename=None):
		if method not in { 'GET' : 1, 'POST' : 1, 'PATCH' : 1, 'delete'.upper() : 1 }:
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\' or \'PATCH\''
			return
		url_rem = 'gists'
		if 'id' not in kwargs:
			if since in kwargs:
				url_rem += '?since=' + str(kwargs['since'])
			return r.Request.get(url_rem, self._auth) 
		if method is 'GET':
			return r.Request.get(url_rem + str(kwargs['id']), self._auth)
		if method is 'delete'.upper():
			return r.Request.delete(url_rem + str(kwargs['id']), self._auth)
		payload = {}
		for arg in kwargs:
			if arg is not 'id':
				payload[arg] = kwargs[arg]
		if method is 'POST':
			if 'files' not in kwargs:
				print 'ERROR: files param is required when creating a gist'
				return
			return r.Request.post(url_rem + str(kwargs['id']), payload, self._auth)
		return r.Request.patch(url_rem + str(kwargs['id']), payload, self._auth)

	'''
	https://developer.github.com/v3/gists/#list-gist-commits
	'''
	def gists_commits(self, id):
		return r.Request.get('gists/' + str(id) + '/commits', self._auth)

	'''
	if method is 'GET':
		https://developer.github.com/v3/gists/#check-if-a-gist-is-starred
	if method is 'PUT':
		https://developer.github.com/v3/gists/#star-a-gist
	if method is 'DELETE':
		https://developer.github.com/v3/gists/#unstar-a-gist
	'''
	def gists_star(self, id, method='GET'):
		if method is not 'GET' and method is not 'PUT' and method is not 'delete'.upper():
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'PUT\' or \'DELETE\''
			return
		url_rem = 'gists/' + str(id) + '/star'
		if method is 'PUT':
			return r.Request.put(url_rem, None, { 'Content-Length' : 0 }, self._auth)
		if method is 'delete'.upper():
			return r.Request.delete(url_rem, self._auth)
		return r.Request.get(url_rem, self._auth)

	'''
	if method is 'GET':
		https://developer.github.com/v3/gists/#list-gist-forks
	else:
		https://developer.github.com/v3/gists/#fork-a-gist
	'''
	def gists_forks(self, id, method='GET'):
		if method is not 'GET' and method is not 'POST':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\''
			return
		url_rem = 'gists/' + str(id) + '/forks' 
		payload = {}
		if method is 'POST':
			return r.Request.post(url_rem, payload, self._auth)
		return r.Request.get(url_rem, self._auth)

	'''
	if method is 'GET':
		if id:
			https://developer.github.com/v3/gists/comments/#get-a-single-comment
		else:
			https://developer.github.com/v3/gists/comments/#list-comments-on-a-gist
	elif method is 'POST':
		https://developer.github.com/v3/gists/comments/#create-a-comment
	elif method is 'PATCH':
		https://developer.github.com/v3/gists/comments/#edit-a-comment
	elif method is 'DELETE':
		https://developer.github.com/v3/gists/comments/#delete-a-comment
	'''
	def gists_comments(self, gist_id, method='GET', **kwargs):
		if method is not in { 'GET' : 1, 'POST' : 1, 'PATCH' : 1, 'delete'.upper() : 1 }:
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\' or \'PATCH\' or \'DELETE\''
			return
		if (method is 'PATCH' or method is 'delete'.upper() ) and ('id' not in kwargs):
			print 'ERROR: _id is required when editing or deleting a gist comment'
			return
		url_rem = 'gists/' + str(gist_id) + '/comments'
		if method is 'POST' or method is 'PATCH':
			if body not in 'kwargs':
				print 'ERROR: body is a required paramter when creating/editing a gist comment'
				return
			if method is 'POST':
				return r.Requests.post(url_rem, { 'body' : body }, self._auth)
			return r.Requests.patch(url_rem + '/' + str(kwargs['id']), { 'body' : body }, self._auth)
		if method is 'delete'.upper():
			return r.Requests.delete(url_rem + str(kwargs['id']))
		return r.Requests.get(url_rem, self._auth) if 'id' not in kwargs else r.Requests.get(url_rem + '/' + str(kwargs['id']), self._auth) 

	#########
	##BLOBS##
	#########

	'''
	if method is 'GET':
		https://developer.github.com/v3/git/blobs/#get-a-blob
	else:
		https://developer.github.com/v3/git/blobs/#create-a-blob
	'''
	def repos_git_blobs(self, owner, repo, sha, **kwargs):
		if method is not 'GET' and method is not 'POST':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\''
			return
		url_rem = 'repos/' + owner + '/' + repo + '/git/blobs/' + sha
		if method is 'POST':
			if 'content' not in kwargs:
				print 'ERROR: content is required when creating a blob'
				return
			payload = {}
			for arg in kwargs:
				payload[arg] = kwargs[arg]
			return r.Request.post(url_rem, payload, self._auth)
		return r.Request.get(url_rem, self._auth)

	#########
	#COMMITS#
	#########

	'''
	if method is 'GET':
		https://developer.github.com/v3/git/commits/#get-a-commit
	else:
		https://developer.github.com/v3/git/commits/#create-a-commit
	'''
	def repos_git_commits(self, owner, repo, sha=None, method='GET', **kwargs):
		if method is not 'GET' and method is not 'POST':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\''
			return
		url_rem = 'repos/' + owner + '/' + repo + '/git/commits'
		if method is 'POST':
			if 'message' not in kwargs or 'tree' not in kwargs or 'parents' not in kwargs:
				print 'ERROR: message, tree and parents are required when creating a commit'
				return
			payload = {}
			for arg in kwargs:
				payload[arg] = kwargs[arg]
			return r.Request.post(url_rem, payload, self._auth)
		if 'sha' not in kwargs:
			print 'ERROR: sha is required to get a commit'
			return
		return r.Request.get(url_rem + '/' + kwargs['sha'], self._auth)

	############
	#REFERENCES#
	############

	'''
	if method is 'GET':
		if refs is not None:
			https://developer.github.com/v3/git/refs/#get-a-reference
		else: 
			https://developer.github.com/v3/git/refs/#get-all-references
	if method is 'POST':
		https://developer.github.com/v3/git/refs/#create-a-reference
	if method is 'PATCH':
		https://developer.github.com/v3/git/refs/#update-a-reference
	if method is 'DELTE':
		https://developer.github.com/v3/git/refs/#delete-a-reference
	'''
	def repos_git_refs(self, owner, repo, ref=None, method='GET', **kwargs):
		if method is not in { 'GET' : 1, 'POST' : 1, 'PATCH' : 1, 'delete'.upper() : 1 }:
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\' or \'PATCH\' or \'DELETE\''
			return
		url_rem = 'repos/' + owner + '/' + repo + '/git/refs'
		payload = {}
		for arg in kwargs:
			payload[arg] = kwargs[arg]
		if method is 'PATCH':
			return r.Request.patch(url_rem + '/' + ref, payload, self._auth)
		if method is 'POST':
			return r.Request.post(url_rem, payload, self._auth)
		if method is 'delete'.upper():
			return r.Request.delete(url_rem + '/' + ref, self._auth)
		return r.Request.get(url_rem, self._auth) if ref is None else r.Request.get(url_rem + '/' + ref, self._auth)

	########
	##TAGS##
	########

	'''
	if method is 'GET':
		https://developer.github.com/v3/git/tags/#get-a-tag
	else:
		https://developer.github.com/v3/git/tags/#create-a-tag-object
	'''
	def repos_get_tags(self, owner, repo, sha=None, method='GET', **kwargs):
		if method is not 'GET' and method is not 'POST':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\''
			return
		url_rem = 'repos/' + owner + '/' + repo + '/git/tags'
		if method is 'POST:'
			payload = {}
			for arg in kwargs:
				payload[arg] = kwargs[arg]
			return r.Request.post(url_rem, payload, self._auth)
		return r.Request.get(url_rem + '/' + sha, self._auth)

	#########
	##TREES##
	#########

	'''
	if method is 'GET':
		https://developer.github.com/v3/git/trees/#get-a-tree
	else:
		https://developer.github.com/v3/git/trees/#create-a-tree
	'''
	def repos_git_trees(self, owner, repo, sha=None, method='GET', **kwargs):
		if method is not 'GET' and method is not 'POST':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\''
			return
		url_rem = 'repos/' + owner + '/' + repo + '/git/trees'
		if method is 'POST':
			if 'tree' not in kwargs:
				print 'ERROR: tree parameter is required when creating a tree'
				return
			payload = {}
			for arg in kwargs:
				payload[arg] = kwargs[arg]
			return r.Request.post(url_rem, payload, self._auth)
		return r.Request.get(url_rem + '/' + sha + '?recursive=1', self._auth) if 'recursive' in kwargs else r.Request.get(url_rem + '/' + sha, self._auth)

	##########	
	##ISSUES##
	##########

	'''
	https://developer.github.com/v3/issues/#list-issues
	'''
	def issues(self):
		return r.Request.get('issues', self._auth)

	def user_issues(self):
		return r.Request.get('user/issues', self._auth)

	def org_issues(self, org, **kwargs):
		params = {}
		for arg in kwargs:
			params[arg] = kwargs[arg]
		return r.Request.get_with_params('orgs/' + org + '/issues', params, self._auth)

	'''
	if method is 'GET':
		if number:
			https://developer.github.com/v3/issues/#get-a-single-issue
		https://developer.github.com/v3/issues/#list-issues-for-a-repository
	elif method is 'POST':
		https://developer.github.com/v3/issues/#create-an-issue
	elif method is 'PATCH':
		https://developer.github.com/v3/issues/#edit-an-issue
	'''
	def repos_issues(self, owner, repo, number=None, method='GET', **kwargs):
		if method not in { 'GET' : 1, 'POST' : 1, 'PATCH' : 1 }:
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\' or \'PATCH\''
			return
		url_rem = 'repos/' + owner + '/'  + repo + '/issues'
		if method is 'GET':
			return r.Request.get(url_rem, self._auth) if number is None else r.Request.get(url_rem + '/' + str(number), self._auth)
		payload = {}
		for arg in kwargs:
			payload[arg] = kwargs[arg]
		if method is 'POST':
			if 'title' not in kwargs:
				print 'ERROR: title is required when creating an issue'
				return
			return r.Request.post(url_rem, payload, self._auth)
		return r.Request.patch(url_rem + '/' + str(number), payload, self._auth)

	###########
	#ASSIGNEES#
	###########

	'''
	if 'assignees':
		https://developer.github.com/v3/issues/assignees/#list-assignees
	else:
		https://developer.github.com/v3/issues/assignees/#check-assignee
	'''
	def repos_assignees(self, owner, repo, assignee=None):
		url_rem = 'repos/' + owner + '/'  + repo + '/assignees'
		return r.Request.get(url_rem + '/' + assignee, self._auth) if assignee is not None else r.Request.get(url_rem, self._auth)


	##########
	#COMMENTS#
	##########

	'''
	if method is 'GET':
		https://developer.github.com/v3/issues/comments/#list-comments-on-an-issue
		https://developer.github.com/v3/issues/comments/#list-comments-in-a-repository
		https://developer.github.com/v3/issues/comments/#get-a-single-comment
	if method is 'POST':
		https://developer.github.com/v3/issues/comments/#create-a-comment
	if method is 'PATCH':
		https://developer.github.com/v3/issues/comments/#edit-a-comment
	if method is 'DELETE':
		https://developer.github.com/v3/issues/comments/#delete-a-comment
	'''
	def repos_issues_comments(self, owner, repo, number=None, id=None, **kwargs):
		if method not in { 'GET' : 1, 'POST' : 1, 'PATCH' : 1, 'delete'.upper() : 1 }:
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\' or \'PATCH\' or \'DELETE\' '
			return
		url_rem = 'repos/' + owner + '/'  + repo + '/issues'
		if method is 'GET':
			return r.Request.get(url_rem + '/' + str(number) + '/comments', self._auth) if number is not None else r.Request.get(url_rem + '/comments', self._auth)
		if method is 'delete'.upper():
			return r.Request.delete(url_rem + '/comments/' + str(id), self._auth)
		payload = {}
		for arg in kwargs:
			payload[arg] = kwargs[arg]
		if 'body' not in kwargs:
			print 'ERROR: body is required when creating/editing an issue comment'
			return
		if method is 'POST':
			return r.Request.post(url_rem + '/' + str(number) + '/comments', payload, self._auth)
		if method is 'PATCH':
			return r.Request.patch(url_rem + '/comments/' + str(id), payload, self._auth)

	##########
	##EVENTS##
	##########

	'''
	if issue_number is not None:
		https://developer.github.com/v3/issues/events/#list-events-for-an-issue
	if id is not None:
		https://developer.github.com/v3/issues/events/#get-a-single-event
	else:
		https://developer.github.com/v3/issues/events/#list-events-for-a-repository
	'''
	def repos_issues_events(self, owner, repo, issue_number=None, id=None):
		url_rem = 'repos/' + owner + '/'  + repo + '/issues'
		if issue_number is not None:
			return r.Request.get(url_rem + '/' + issue_number + '/events', self._auth)
		if id is not None:
			return r.Request.get(url_rem + '/events/' + str(id), self._auth)
		return r.Request.get(url_rem + '/events', self._auth)

	##########
	##LABELS##
	##########

	'''
	https://developer.github.com/v3/issues/labels/
	'''
	def repos_labels(self, owner, repo, number=None, name=None, method='GET', **kwargs):
		if method not in { 'GET' : 1, 'POST' : 1, 'PATCH' : 1, 'delete'.upper() : 1 }:
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\' or \'PATCH\' or \'DELETE\' '
			return
		url_rem = 'repos/' + owner + '/'  + repo + '/labels'
		if method is 'GET':
			return r.Request.get(url_rem, self._auth) is name is None else r.Request.get(url_rem + '/' + name, self._auth)
		if method is 'delete'.upper():
			return r.Request.delete(url_rem + '/' + name, self._auth)
		payload = {}
		for arg in kwargs:
			payload[arg] = kwargs[arg]
		if 'name' not in kwargs or 'color' not in kwargs:
			print 'ERROR: name and color required to create or edit a label'
			return
		if method is 'POST':
			return r.Request.post(url_rem, payload, self._auth)
		return r.Request.patch(url_rem + '/' + name, payload, self._auth)

	def repos_issues_labels(self, owner, repo, number, name=None, method='GET', **kwargs):
		if method not in { 'GET' : 1, 'POST' : 1, 'PUT' : 1, 'delete'.upper() : 1 }:
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\' or \'PUT\' or \'DELETE\' '
			return	
		url_rem = 'repos/' + owner + '/' + repo + '/issues/' + str(number) + '/labels'
		if method is 'POST':
			return r.Request.post(url_rem, args, self._auth)
		if method is 'PUT':
			payload = {}
			for arg in kwargs:
				payload[arg] = kwargs[arg]
			return r.Request.post(url_rem, data=payload, auth=self._auth)
		if method is 'delete'.upper():
			return r.Request.delete(url_rem, self._auth) if name is None else r.Request.delete(url_rem + '/' + name, self._auth)
		return r.Request.get(url_rem, self._auth)

	'''
	https://developer.github.com/v3/issues/labels/#get-labels-for-every-issue-in-a-milestone
	'''
	def repos_milestones_labels(self):
		url_rem = 'repos/' + owner + '/' + repo + '/milestones/' + str(number) + '/labels'
		return r.Request.get(url_rem, self._auth)

	############
	#MILESTONES#
	############

	'''
	if method is 'GET':
		if number is None:
			https://developer.github.com/v3/issues/milestones/#list-milestones-for-a-repository
		https://developer.github.com/v3/issues/milestones/#get-a-single-milestone
	if method is 'POST':
		https://developer.github.com/v3/issues/milestones/#create-a-milestone
	if method is 'PATCH':
		https://developer.github.com/v3/issues/milestones/#edit-a-milestone
	if method is 'DELETE':
		https://developer.github.com/v3/issues/milestones/#delete-a-milestone
	'''
	def repos_milestones(self, owner, repo, number=None, method='GET', **kwargs):
		if method not in { 'GET' : 1, 'POST' : 1, 'PATCH' : 1, 'delete'.upper() : 1 }:
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\' or \'PATCH\' or \'DELETE\' '
			return
		url_rem = 'repos/' + owner + '/' + repo + '/milestones'
		payload = {}
		for arg in kwargs:
			payload[arg] = kwargs[arg]
		if method is 'POST':
			if 'title' not in kwargs:
				print 'ERROR: title is required when creating a milestone'
				return
			return r.Request.post(url_rem, payload, self._auth)
		if method is 'PATCH':
			return r.Request.patch(url_rem + '/' + str(number), payload, self._auth)
		if method is 'delete'.upper():
			return r.Request.delete(url_rem + '/' + str(number), self._auth)
		if number is not None:
			return r.Request.get_with_params(url_rem + '/' + str(number), self._auth)
		return r.Request.get(url_rem, payload, self._auth)

	###############
	#MISCELLANEOUS#
	###############

	'''
	https://developer.github.com/v3/emojis/#emojis
	'''
	def emojis(self):
		return r.Request.get('emojis', self._auth)

	'''
	https://developer.github.com/v3/gitignore/
	'''
	def gitignore_templates(self):
		return r.Request.get('gitignore/templates', self._auth)

	'''
	https://developer.github.com/v3/markdown/#render-an-arbitrary-markdown-document
	'''
	def markdown(self, **kwargs):
		if 'text' not in kwargs:
			print 'ERROR: text required when rendering a mardown document'
			return
		payload = {}
		for arg in kwargs:
			payload[arg] = kwargs[arg]
		return r.Request.post('markdown', payload, self._auth)

	'''
	https://developer.github.com/v3/markdown/#render-a-markdown-document-in-raw-mode
	'''
	def markdown_raw(self, **kwargs):
		payload = {}
		for arg in kwargs:
			payload[arg] = kwargs[arg]
		return r.Request.post('markdown/raw', payload, self._auth)

	'''
	https://developer.github.com/v3/meta/
	'''
	def meta(self, **kwargs):
		params = {}
		for arg in kwargs:
			params[arg] = kwargs[arg]
		return r.Request.get('meta', self._auth) if len(kwargs) < 0 else r.Request.get_with_params('meta', params, self._auth)

	'''
	https://developer.github.com/v3/rate_limit/#get-your-current-rate-limit-status
	'''
	def rate_limit(self):
		return r.Request.get('rate_limit', self._auth)
























