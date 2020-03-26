<!-- TOC -->

- [Tools](#tools)
  - [tfwrapper](#tfwrapper)
- [Providers](#providers)
  - [Cloud-Deploy](#cloud-deploy)
  - [Gitlab](#gitlab)
  - [Azure DevOps](#azure-devops)
- [Modules](#modules)
  - [AWS](#aws)
  - [Azure](#azure)
  - [Datadog](#datadog)
  - [SignalFx](#signalfx)

<!-- /TOC -->

# Tools

## tfwrapper
[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://github.com/claranet/terraform-wrapper)

`tfwrapper` is a python wrapper for Terraform which aims to simplify Terraform usage and enforce best practices.

# Providers

## Cloud-Deploy
[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://github.com/claranet/terraform-provider-cloud-deploy)

Terraform Provider that manages Claranet Cloud Deploy (Ghost) applications.

## Gitlab
[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://github.com/claranet/terraform-provider-gitlab)

Fork of the official Gitlab provider with Claranet's contributions and improvements.

## Azure DevOps
[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://github.com/claranet/terraform-provider-azuredevops)

Fork of the official Azure DevOps provider with Claranet's contributions and improvements.

# Modules

## AWS

{% include_relative tf-modules-aws.md %}

## Azure

{% include_relative tf-modules-azure.md %}

## Datadog

{% include_relative tf-modules-datadog.md %}

## SignalFx

{% include_relative tf-modules-signalfx.md %}
