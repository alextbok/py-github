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
	def user(self,
			method='GET', \
			name=None, \
			email=None, \
			blog=None, \
			company=None, \
			location=None, \
			hireable=None, \
			bio=None):
 
		if method is not 'GET' and method is not 'PATCH':
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

	###########
	###REPOS###
	###########

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

		if method is not 'GET' and method is not 'POST':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\' '
			return

		payload = {}

		args = [arg for arg in locals().items()]

		for arg in args:
				if arg[1] is not None and arg[0] not in {'self' : 1, 'payload' : 1, 'method' : 1}:
					payload[ arg[0] ] = arg[1]

		if method is 'POST':
			if name is None:
				print "ERROR: name is a required parameter when creating a repository"
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

		if method is not 'GET' and method is not 'POST':
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

		if method is not 'GET' and method is not 'PATCH' and method is not 'delete'.upper():
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
		elif method is 'delete'.upper():
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
	def notifications(self, \
						method='GET', \
						_all=None, \
						participating=None, \
						since=None, \
						last_read_at=None):

		if method is not 'GET' and method is not 'PUT':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'PUT\' '
			return

		params = {}
		if method is 'PUT':
			return r.Request.put('notifications', { 'last_read_at' : last_read_at }, None, self._auth) if last_read_at is not None else r.Request.put('notifications', None, { 'Content-Length' : None}, self._auth)
		if _all is not None:
			params['all'] = _all
		if participating is not None:
			params['participating'] = participating
		if since is not None:
			params['since'] = since
		return r.Request.get_with_params('notifications', params, self._auth) if len(params) > 0 else r.Request.get('notifications', self._auth)

	'''
	https://developer.github.com/v3/activity/notifications/#list-your-notifications-in-a-repository
	'''
	def repos_notifications(self, \
						owner, \
						repo, \
						_all=None, \
						participating=None, \
						since=None):
		url_rem = 'repos/' + owner + '/' + repo + '/notifications'
		params = {}
		if _all is not None:
			params['all'] = _all
		if participating is not None:
			params['participating'] = participating
		if since is not notifications_threads:
			params['since'] = since
		return r.Request.get_with_params(url_rem, params, self._auth) if len(params) > 0 else r.Request.get(url_rem, self._auth)


	'''
	if method is 'GET':
		https://developer.github.com/v3/activity/notifications/#view-a-single-thread
	else:
		https://developer.github.com/v3/activity/notifications/#mark-a-thread-as-read
	'''
	def notifications_threads(self, \
								id, \
								method='GET'):
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
	def notifications_threads_subscription(self, \
								id, \
								method='GET', \
								subscribed=None, \
								ignored=None):
		if method is not 'GET' and method is not 'PUT' and method is not 'delete'.upper():
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'PUT\' or \'DELETE\''
			return
		url_rem = 'notifications/threads/' + str(id) + '/subscription'
		if method is 'PUT':
			payload = {}
			if subscribed is not None:
				payload['subscribed'] = subscribed
			if ignored is not None:
				payload['ignored'] = ignored
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
	def repos_stargazers(self,owner,repo):
		url_rem = 'repos/' + owner + '/' + repo + '/stargazers'
		return r.Request.get(url_rem, self._auth)

	'''
	https://developer.github.com/v3/activity/starring/#list-repositories-being-starred
	'''
	def users_starred(self, \
						username=None, \
						sort=None, \
						direction=None):
		params = {}
		if sort is not None:
			params['sort'] = sort
		if direction is not None:
			params['direction'] = direction
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
	def user_starred(self, \
			owner, \
			repo, \
			method='GET'):
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
	def repos_subscription(self, \
							owner, \
							repo, \
							method='GET', \
							subscribed=None, \
							ignored=None):
		if method is not 'GET' and method is not 'PUT' and method is not 'delete'.upper():
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'PUT\' or \'DELETE\''
			return
		url_rem = 'repos/' + owner + '/' + repo + '/subscription'
		if method is 'PUT':
			payload = {}
			if subscribed is not None:
				payload['subscribed'] = subscribed
			if ignored is not None:
				payload['ignored'] = ignored
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
		if _id is None:
			if since is not None:
				url_rem += '?since=' + str(since)
			return r.Request.get(url_rem, self._auth) 
		if method is 'GET':
			return r.Request.get(url_rem + str(_id), self._auth)
		if method is 'delete'.upper():
			return r.Request.delete(url_rem + str(_id), self._auth)
		payload = {}
		if files is not None:
			payload['files'] = files
		if description is not None:
			payload['description'] = description
		if method is 'POST':
			if files is None:
				print 'ERROR: files param is required when creating a gist'
				return
			if public is not None:
				payload['public'] = public
			return r.Request.post(url_rem + str(_id), payload, self._auth)
		if content is not None:
			payload['content'] = content
		if filename is not None:
			payload['filename'] = filename
		return r.Request.patch(url_rem + str(_id), payload, self._auth)

	'''
	https://developer.github.com/v3/gists/#list-gist-commits
	'''
	def gists_commits(self, _id):
		return r.Request.get('gists/' + str(_id) + '/commits', self._auth)

	'''
	if method is 'GET':
		https://developer.github.com/v3/gists/#check-if-a-gist-is-starred
	if method is 'PUT':
		https://developer.github.com/v3/gists/#star-a-gist
	if method is 'DELETE':
		https://developer.github.com/v3/gists/#unstar-a-gist
	'''
	def gists_star(self, _id, method='GET'):
		if method is not 'GET' and method is not 'PUT' and method is not 'delete'.upper():
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'PUT\' or \'DELETE\''
			return
		url_rem = 'gists/' + str(_id) + '/star'
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
	def gists_forks(self, _id, method='GET'):
		if method is not 'GET' and method is not 'POST':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\''
			return
		url_rem = 'gists/' + str(_id) + '/forks' 
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
	def gists_comments(self, \
		gist_id, \
		method='GET', \
		body=None, \
		_id=None):
		if method is not in { 'GET' : 1, 'POST' : 1, 'PATCH' : 1, 'delete'.upper() : 1 }:
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\' or \'PATCH\' or \'DELETE\''
			return
		if (method is 'PATCH' or method is 'delete'.upper() ) and (_id is None):
			print 'ERROR: _id is required when editing or deleting a gist comment'
			return
		url_rem = 'gists/' + str(gist_id) + '/comments'
		if method is 'POST' or method is 'PATCH':
			if body is None:
				print 'ERROR: body is a required paramter when creating/editing a gist comment'
				return
			if method is 'POST':
				return r.Requests.post(url_rem, { 'body' : body }, self._auth)
			return r.Requests.patch(url_rem + '/' + str(_id), { 'body' : body }, self._auth)
		if method is 'delete'.upper():
			return r.Requests.delete(url_rem + str(_id))
		return r.Requests.get(url_rem, self._auth) if _id is None else r.Requests.get(url_rem + '/' + str(_id), self._auth) 

	#########
	##BLOBS##
	#########

	'''
	if method is 'GET':
		https://developer.github.com/v3/git/blobs/#get-a-blob
	else:
		https://developer.github.com/v3/git/blobs/#create-a-blob
	'''
	def repos_git_blobs(self, \
						owner, \
						repo, \
						sha, \
						method='GET', \
						content=None, \
						encoding='utf-8'):
		if method is not 'GET' and method is not 'POST':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\''
			return
		url_rem = 'repos/' + owner + '/' + repo + '/git/blobs/' + sha
		if method is 'POST':
			if content is None:
				print 'ERROR: content is required when creating a blob'
				return
			return r.Request.post(url_rem, { 'content' : content, 'encoding' : encoding }, self._auth)
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
	def repos_git_commits(self,
						owner, \
						repo, \
						sha=None, \
						method='GET', \
						message=None, \
						tree=None, \
						parents=None):
		if method is not 'GET' and method is not 'POST':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\''
			return
		url_rem = 'repos/' + owner + '/' + repo + '/git/commits'
		if method is 'POST':
			if message is None or tree is None or parents is None:
				print 'ERROR: message, tree and parents are required when creating a commit'
				return
			payload = { 'message' : message, 'tree' : tree, 'parents' : parents }
			return r.Request.post(url_rem, payload, self._auth)
		if sha is None:
			print 'ERROR: sha is required to get a commit'
			return
		return r.Request.get(url_rem + '/' + sha, self._auth)

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
	def repos_git_refs(self,
					owner, \
					repo, \
					ref=None, \
					method='GET', \
					_ref=None, \
					sha = None, \
					force=None):
		if method is not in { 'GET' : 1, 'POST' : 1, 'PATCH' : 1, 'delete'.upper() : 1 }:
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\' or \'PATCH\' or \'DELETE\''
			return
		url_rem = 'repos/' + owner + '/' + repo + '/git/refs'
		if method is 'PATCH':
			return r.Request.patch(url_rem + '/' + ref, { 'sha' : sha, 'force' : force }, self._auth)
		if method is 'POST':
			return r.Request.post(url_rem, { 'ref' : _ref, 'sha' : sha }, self._auth)
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
	def repos_get_tags(self, \
						owner, \
						repo, \
						sha=None, \
						method='GET', \
						tag=None, \
						message=None, \
						_object=None, \
						_type=None, \
						tagger=None):
		if method is not 'GET' and method is not 'POST':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\''
			return
		url_rem = 'repos/' + owner + '/' + repo + '/git/tags'
		if method is 'POST:'
			payload = { 'tag' : tag, 'message' : message, 'object' : _object, 'type' : _type, 'tagger' : tagger }
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
	def repos_git_trees(self, \
						owner, \
						repo, \
						sha=None, \
						method='GET', \
						recursive=False, \
						tree=None, \
						base_tree=None):
		if method is not 'GET' and method is not 'POST':
			print 'ERROR: invalid method parameter:' + str(method)
			print 'method must be \'GET\' (default) or \'POST\''
			return
		url_rem = 'repos/' + owner + '/' + repo + '/git/trees'
		if method is 'POST':
			if tree is None:
				print 'ERROR: tree parameter is required when creating a tree'
				return
			return r.Request.post(url_rem, { 'tree' : tree, 'base_tree' : base_tree }, self._auth)
		return r.Request.get(url_rem + '/' + sha + '?recursive=1', self._auth) if recursive else r.Request.get(url_rem + '/' + sha, self._auth)



