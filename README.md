py-github
=========

Easy to use python wrapper for [GitHub API v3](https://developer.github.com/v3/).
Features full functionality for v3.
All GET requests are memoized (cached) to help deal with GitHub's rate-limit.

The design choices made were intended to:
- decrease the time it takes to get up and running
- make the library usable without reading documentation
- eliminate dealing with http requests (they are handled by py-github)

Get the code
=============
The code is hosted at https://github.com/alextbok/py-github

Check out the latest development version::
    $ git clone git://github.com/alextbok/py-github.git
    $ cd py-github

Dependencies
- [Python Requests](http://docs.python-requests.org/en/latest/)


Using
=========
Access to the API starts with an Api object. Once created, you can make any authenticated (or unauthenticated) call available by the GitHub API. Be sure to sign up for the [GitHub Developer Program](https://developer.github.com/program/)
::
    >>> from github import api
    >>> api_obj = api.Api(<your github username>, <your github password>)
Every function signature directly corresponds to an end point of the GitHubAPI.
Simply replace all forward slashes '/' in the url endpoint with underbars '_'. 
For example, to [list your repositories](https://developer.github.com/v3/repos/#list-your-repositories), the endpoint is https://api.github.com/user/repos. 
To make this call with py-github
```
    >>> from github import api
    >>> api_obj = api.Api(<username>,<password>)
    >>> api`_obj.user_`repos()
```
You may have noticed that end points sometimes have multiple verb possibilites. In this case, use the keyword argument
'method' to delineate the request you want to make. The 'GET' verb is always the default, so it's unnecessary to include this in the function call.
For example, to [create a new repo](https://developer.github.com/v3/repos/#create), the new signature is::
    >>> api`_obj.user_`repos(method='POST', name='foo', description='bar')
Any parameters in the 'POST' request should be included as keyword arguments. Arguments that are required by GitHub are also required by py-github (i.e. it will yell at you if you try creating a repo without a name).

The function signatures correspond to the *static* portion of the url. Any variable parts are passed in as arguments, in the order that they appear in the url. 
For example, to [list the contributors of a repository](https://developer.github.com/v3/repos/#list-contributors), the url is https://api.github.com/repos/:owner/:repo/contributors
To make this call with py-github for alextbok/py-github:
    >>> api`_obj.repos_`contributors(alextbok, py-github)

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

TODO:
-------------
OAuth authorization
