#!/bin/sh

if [ -d 'dist' ] ; then
    rm -rf dist
fi

if [ -d 'site' ] ; then
    rm -rf site
fi

if [ -d 'htmlcov' ] ; then
    rm -rf htmlcov
fi

if [ -d 'aioworker.egg-info' ] ; then
    rm -rf aioworker.egg-info
fi

# delete python cache
find . -iname '*.pyc' -delete
find . -iname '__pycache__' -delete
