#!/usr/bin/python

from github import collections, functools

'''
Decorator that caches a function's return value each time it is called so if it is
called later with the same arguments, the cached value is returned, instead of
reevaluating the function
'''
class Memoized(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        return self.func.__doc__
    def __get__(self, obj, objtype):
        return functools.partial(self.__call__, obj)