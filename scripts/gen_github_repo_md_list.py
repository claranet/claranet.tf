#!/usr/bin/env python

"""
Using github3.py module: https://github3.readthedocs.io/en/latest/index.html#more-examples 
"""

import github3

import os
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

def _get_tofu_registry_url(proj_name):
    proj_url_check = 'https://api.opentofu.org/registry/docs/modules/claranet/{}/azurerm/index.json'.format(proj_name)
    proj_url = 'https://search.opentofu.org/module/claranet/{}/azurerm/latest'.format(proj_name)
    resp = requests.get(proj_url_check)
    if resp.status_code == 200:
        return proj_url
    return None


def gather_repos(organization, no_forks=True):
    all_repos = gh.repositories_by(organization)
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
    repo['registrytofu'] = _get_tofu_registry_url(repo['name'].replace('terraform-aws-', '').replace('terraform-azurerm-', ''))

    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('md_tpl.j2')

    output = template.render(repo=repo)
    print(output)


if __name__ == '__main__':
    gh = github3.login(token=os.environ.get('GITHUB_TOKEN'))

    found_repos = gather_repos('claranet', False)
    for repo in found_repos:
        #if repo['name'].startswith('terraform-aws-') or repo['name'].startswith('terraform-azurerm-'):
        if repo['name'].startswith('terraform-azurerm-'):
            render_tpl(repo)
