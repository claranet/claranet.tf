#!/usr/bin/env python

"""
Original gist: https://gist.github.com/ralphbean/5733076
Print all of the clone-urls for a GitHub organization.
It requires the pygithub3 module, which you can install like this::
    $ sudo yum -y install python-virtualenv
    $ mkdir scratch
    $ cd scratch
    $ virtualenv my-virtualenv
    $ source my-virtualenv/bin/activate
    $ pip install pygithub3
Usage example::
    $ python list-all-repos.py
Advanced usage.  This will actually clone all the repos for a
GitHub organization or user::
    $ for url in $(python list-all-repos.py); do git clone $url; done
"""

import pygithub3
import requests
from jinja2 import Environment, FileSystemLoader

gh = None


def _get_tfregistry_url(proj_name):
    proj_url_check = 'https://registry.terraform.io/v1/modules/claranet/{}'.format(proj_name)
    proj_url = 'https://registry.terraform.io/modules/claranet/{}'.format(proj_name)
    resp = requests.get(proj_url_check)
    if resp.status_code == 200:
        return proj_url
    return None


def gather_repos(organization, no_forks=True):
    all_repos = gh.repos.list(user=organization).all()
    for repo in all_repos:

        # Don't print the urls for repos that are forks.
        if no_forks and repo.fork:
            continue

        yield {
            'name': repo.name,
            'url': repo.html_url,
            'desc': repo.description,
            'is_fork': repo.fork,
        }


def render_tpl(repo):
    repo['registry'] = _get_tfregistry_url(repo['name'].replace('terraform-aws-', '').replace('terraform-azurerm-', ''))

    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('md_tpl.j2')

    output = template.render(repo=repo)
    print(output)


if __name__ == '__main__':
    gh = pygithub3.Github()

    found_repos = gather_repos('claranet', False)
    for repo in found_repos:
        if repo['name'].startswith('terraform-aws-') or repo['name'].startswith('terraform-azurerm-'):
            render_tpl(repo)
