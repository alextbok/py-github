py-github
=========

Easy to use python wrapper for [GitHub API v3](https://developer.github.com/v3/) that features full functionality for v3.

All **GET** requests are memoized (cached) to help deal with GitHub's rate-limit.

The design choices made were intended to:
- decrease the time it takes to get up and running
- make the library usable without reading documentation
- eliminate dealing with http requests (they are handled by py-github)

Get the code
=============
The code is hosted at https://github.com/alextbok/py-github

Check out the latest version:
```
    $ git clone https://github.com/alextbok/py-github.git
    $ cd py-github
```
**Dependencies**
- [Python Requests](http://docs.python-requests.org/en/latest/)


Using
=========
Access to the API starts with an Api object. Once created, you can make any authenticated (or unauthenticated) call available by the GitHub API. Be sure to sign up for the [GitHub Developer Program](https://developer.github.com/program/)
```
    >>> from github import api
    >>> api_obj = api.Api(<your github username>, <your github password>)
    >>>
    >>> api_obj = api.Api() # or make unauthenticated calls
```
Every function signature directly corresponds to an end point of the GitHubAPI.

Simply replace all forward slashes **/** in the url endpoint with underbars **_**. 

For example, to [list your repositories](https://developer.github.com/v3/repos/#list-your-repositories), the endpoint is https://api.github.com/user/repos. 

To make this call with py-github
```
    >>> from github import api
    >>> api_obj = api.Api(<username>,<password>)
    >>> api_obj.user_repos()
```
You may have noticed that end points sometimes have multiple verb possibilites. 

In this case, use the keyword argument **method** to delineate the type request you want to make. 

The **GET** verb is always the default, so it's unnecessary to include this in the function call.
For example, to [create a new repo](https://developer.github.com/v3/repos/#create), the new signature is
```
    >>> api_obj.user_repos(method='POST', name='foo', description='bar')
```
Any parameters in the **POST** request should be included as keyword arguments.

Arguments that are required by GitHub are also required by py-github (i.e. it will yell at you if you try creating a repo without a name).

The function signatures correspond to the *static* portion of the url. Any variable parts are passed in as arguments, in the order that they appear in the url. 

To [list the contributors of a repository](https://developer.github.com/v3/repos/#list-contributors), the endpoint is **/repos/:owner/:repo/contributors**

To make this call with py-github for **alextbok/py-github**:
```
    >>> api_obj.repos_contributors(alextbok, py-github)
```

**A note on responses**:

Responses are returned as [Python Requests](http://docs.python-requests.org/en/latest/) response objects. To retrieve the header and body of the request
```
    >>> res = api_obj.user_repos()
    >>> res.json()
    >>> res.headers['foo']
```

Functionality
=============
- [Activity](https://developer.github.com/v3/activity/)
- [Gists](https://developer.github.com/v3/gists/)
- [Git Data](https://developer.github.com/v3/git/)
- [Issues](https://developer.github.com/v3/issues/)
- [Miscellaneous](https://developer.github.com/v3/misc/)
- [Organizations](http://developer.github.com/v3/orgs/)
- [Pull Requests](https://developer.github.com/v3/pulls/)
- [Repositories](https://developer.github.com/v3/repos/)
- [Search](https://developer.github.com/v3/search/)
- [Users](https://developer.github.com/v3/users/)

Todo:
-------------
OAuth authorization
