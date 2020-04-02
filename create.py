#!/usr/bin/env python
"""
This script renders `index.md.j2` and prints the output,
which should be written to `index.md`.

"""

import pickle
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import urlopen

from github import Github
from jinja2 import Environment, StrictUndefined

TOOLS = (
    "docker-terraform-python",
    "jinjaform",
    "python-terrafile",
    "terraform-datadog-scripts",
    "terraform-wrapper",
)

MODULE_PROVIDERS = {
    "aws": "AWS",
    "azurerm": "Azure",
    "datadog": "Datadog",
    "signalfx": "SignalFx",
}

REGISTRY_API_URL = "https://registry.terraform.io/v1/modules/claranet/{name}/{provider}"
REGISTRY_URL = "https://registry.terraform.io/modules/claranet/{name}/{provider}"


def get_context():
    """
    Returns a context dictionary to use when rendering the template.
    Caches the result in the ".cache" file and uses that file if it exists.

    """

    cache_path = Path(__file__).parent / ".cache"

    if cache_path.exists():
        return pickle.loads(cache_path.read_bytes())

    context = {
        "tools": [],
        "providers": [],
        "modules": defaultdict(list),
    }

    gh = Github()
    organization = gh.get_organization(login="claranet")
    for repo in organization.get_repos():

        if repo.private or repo.fork:
            continue

        if repo.name in TOOLS:
            context["tools"].append(repo)
        else:
            match = re.match(r"(?:terraform|tf)-(.+?)-(.+)", repo.name)
            if match:
                repo_type = match.group(1)
                if repo_type == "provider":
                    context["providers"].append(repo)
                elif (
                    repo_type in MODULE_PROVIDERS
                    or "module" in repo.description.lower()
                ):
                    repo.registry_url = get_registry_url(repo)
                    if repo_type in MODULE_PROVIDERS:
                        provider_title = MODULE_PROVIDERS[repo_type]
                        context["modules"][provider_title].append(repo)
                    else:
                        context["modules"]["Other"].append(repo)
                else:
                    print("SKIPPED:", repo.name, file=sys.stderr)

    cache_path.write_bytes(pickle.dumps(context))
    return context


def get_registry_url(repo):
    """
    Returns the Terraform Registry URL for a repository, if there is one.

    """

    match = re.match(r"(?:terraform|tf)-(.+?)-(.+)", repo.name)
    if match:
        provider = match.group(1)
        name = match.group(2)
        api_url = REGISTRY_API_URL.format(name=name, provider=provider)
        try:
            with urlopen(api_url) as response:
                if response.getcode() == 200:
                    return REGISTRY_URL.format(name=name, provider=provider)
        except HTTPError as error:
            if error.code != 404:
                raise
    return None


env = Environment(
    undefined=StrictUndefined,
    keep_trailing_newline=True,
    extensions=["jinja2.ext.do", "jinja2.ext.loopcontrols"],
)

template_path = Path(__file__).parent / "index.md.j2"
template = env.from_string(template_path.read_text())

rendered = template.render(**get_context())

print(rendered)
