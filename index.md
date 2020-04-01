- [Tools](#tools)
  - [docker-terraform-python](#docker-terraform-python)
  - [jinjaform](#jinjaform)
  - [python-terrafile](#python-terrafile)
  - [terraform-datadog-scripts](#terraform-datadog-scripts)
  - [terraform-wrapper](#terraform-wrapper)
- [Providers](#providers)
  - [clouddeploy](#terraform-provider-clouddeploy)
- [Modules](#modules)
  - [AWS](#aws)
  - [Azure](#azure)
  - [Datadog](#datadog)
  - [Other](#other)
  - [SignalFx](#signalfx)

# Tools

## [docker-terraform-python](https://api.github.com/repos/claranet/docker-terraform-python)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/docker-terraform-python)

A version of the terraform:light Docker container that also includes Python and awscli.

## [jinjaform](https://api.github.com/repos/claranet/jinjaform)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/jinjaform)

Terraform wrapper with Jinja2 templates

## [python-terrafile](https://api.github.com/repos/claranet/python-terrafile)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/python-terrafile)

Manages external Terraform modules

## [terraform-datadog-scripts](https://api.github.com/repos/claranet/terraform-datadog-scripts)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-datadog-scripts)

 Scripts used for datadog terraform modules for CI and compliant purpose.

## [terraform-wrapper](https://api.github.com/repos/claranet/terraform-wrapper)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-wrapper)

Claranet France Terraform Wrapper

# Providers

## [terraform-provider-clouddeploy](https://api.github.com/repos/claranet/terraform-provider-clouddeploy)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-provider-clouddeploy)

Cloud Deploy - Terraform provider

# Modules

## AWS

### [terraform-aws-alb-cloudwatch-logs-json](https://api.github.com/repos/claranet/terraform-aws-alb-cloudwatch-logs-json)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-aws-alb-cloudwatch-logs-json) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/alb-cloudwatch-logs-json/aws)

Terraform module for shipping AWS ALB logs to CloudWatch Logs in JSON format

### [terraform-aws-asg-instance-alarms](https://api.github.com/repos/claranet/terraform-aws-asg-instance-alarms)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-aws-asg-instance-alarms) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/asg-instance-alarms/aws)

Manages CloudWatch Alarms for EC2 Instances in ASGs

### [terraform-aws-asg-instance-replacement](https://api.github.com/repos/claranet/terraform-aws-asg-instance-replacement)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-aws-asg-instance-replacement) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/asg-instance-replacement/aws)

Terraform module for AWS ASG instance replacement

### [terraform-aws-aurora](https://api.github.com/repos/claranet/terraform-aws-aurora)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-aws-aurora) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/aurora/aws)

Terraform module for creating and managing Amazon Aurora clusters

### [terraform-aws-cloudwatch-slack](https://api.github.com/repos/claranet/terraform-aws-cloudwatch-slack)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-aws-cloudwatch-slack) 

Terraform module for sending CloudWatch Alarm events to Slack

### [terraform-aws-eipattach](https://api.github.com/repos/claranet/terraform-aws-eipattach)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-aws-eipattach) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/eipattach/aws)

Automatically attach Elastic IPs to instances

### [terraform-aws-fargate-service](https://api.github.com/repos/claranet/terraform-aws-fargate-service)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-aws-fargate-service) 

Terraform module for creating a Fargate service that can be updated with a Lambda function call

### [terraform-aws-lambda](https://api.github.com/repos/claranet/terraform-aws-lambda)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-aws-lambda) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/lambda/aws)

Terraform module for AWS Lambda functions

### [terraform-aws-lets-encrypt](https://api.github.com/repos/claranet/terraform-aws-lets-encrypt)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-aws-lets-encrypt) 

Terraform module for creating Let's Encrypt certificates with AWS Lambda and Route 53

### [terraform-aws-packer-cleanup](https://api.github.com/repos/claranet/terraform-aws-packer-cleanup)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-aws-packer-cleanup) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/packer-cleanup/aws)

Terraform module to clean up Packer AWS resources

### [terraform-aws-s3-yum-repo](https://api.github.com/repos/claranet/terraform-aws-s3-yum-repo)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-aws-s3-yum-repo) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/s3-yum-repo/aws)

Manages a YUM repository in an S3 bucket

### [terraform-aws-ssh-keys](https://api.github.com/repos/claranet/terraform-aws-ssh-keys)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-aws-ssh-keys) 

Terraform module for managing SSH keys

### [terraform-aws-ssm-patch-management](https://api.github.com/repos/claranet/terraform-aws-ssm-patch-management)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-aws-ssm-patch-management) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/ssm-patch-management/aws)

Terraform module for AWS SSM Patch Management

### [terraform-aws-vpc-modules](https://api.github.com/repos/claranet/terraform-aws-vpc-modules)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-aws-vpc-modules) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/vpc-modules/aws)

Terraform modules for AWS VPC management

## Azure

### [terraform-azurerm-acr](https://api.github.com/repos/claranet/terraform-azurerm-acr)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-acr) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/acr/azurerm)

Terraform module for Azure Container Registry

### [terraform-azurerm-aks](https://api.github.com/repos/claranet/terraform-azurerm-aks)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-aks) 

Terraform module composition (feature) for Azure Kubernetes Service

### [terraform-azurerm-alerting](https://api.github.com/repos/claranet/terraform-azurerm-alerting)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-alerting) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/alerting/azurerm)

Terraform module for Azure Alerting

### [terraform-azurerm-app-gateway](https://api.github.com/repos/claranet/terraform-azurerm-app-gateway)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-app-gateway) 

Terraform module for Azure Application Gateway

### [terraform-azurerm-app-service-plan](https://api.github.com/repos/claranet/terraform-azurerm-app-service-plan)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-app-service-plan) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/app-service-plan/azurerm)

Terraform module composition (feature) for Azure App Service Plan

### [terraform-azurerm-app-service-web](https://api.github.com/repos/claranet/terraform-azurerm-app-service-web)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-app-service-web) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/app-service-web/azurerm)

Terraform module composition (feature) for Azure App Service Web

### [terraform-azurerm-bastion-vm](https://api.github.com/repos/claranet/terraform-azurerm-bastion-vm)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-bastion-vm) 

Terraform module for a bastion (Jump Host) via a Linux VM

### [terraform-azurerm-dashboard](https://api.github.com/repos/claranet/terraform-azurerm-dashboard)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-dashboard) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/dashboard/azurerm)

Terraform module for Azure Dashboard

### [terraform-azurerm-db-mysql](https://api.github.com/repos/claranet/terraform-azurerm-db-mysql)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-db-mysql) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/db-mysql/azurerm)

Terraform module composition (feature) for Azure MySQL Database

### [terraform-azurerm-db-postgresql](https://api.github.com/repos/claranet/terraform-azurerm-db-postgresql)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-db-postgresql) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/db-postgresql/azurerm)

Terraform module composition (feature) for Azure PostGreSQL Database

### [terraform-azurerm-db-sql](https://api.github.com/repos/claranet/terraform-azurerm-db-sql)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-db-sql) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/db-sql/azurerm)

Terraform module composition (feature) for Azure SQL Database (SQLServer based)

### [terraform-azurerm-eventhub](https://api.github.com/repos/claranet/terraform-azurerm-eventhub)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-eventhub) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/eventhub/azurerm)

Terraform module for Azure Eventhub

### [terraform-azurerm-function-app-single](https://api.github.com/repos/claranet/terraform-azurerm-function-app-single)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-function-app-single) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/function-app-single/azurerm)

Terraform module for Azure Function App V2

### [terraform-azurerm-function-app-with-plan](https://api.github.com/repos/claranet/terraform-azurerm-function-app-with-plan)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-function-app-with-plan) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/function-app-with-plan/azurerm)

Terraform module for Azure Function App V2 with App Service Plan

### [terraform-azurerm-global-services](https://api.github.com/repos/claranet/terraform-azurerm-global-services)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-global-services) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/global-services/azurerm)

Terraform module composition (feature) for Global (cross Subscriptions) Azure Services

### [terraform-azurerm-keyvault](https://api.github.com/repos/claranet/terraform-azurerm-keyvault)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-keyvault) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/keyvault/azurerm)

Terraform module composition (feature) for Azure KeyVault

### [terraform-azurerm-linux-vm](https://api.github.com/repos/claranet/terraform-azurerm-linux-vm)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-linux-vm) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/linux-vm/azurerm)

 Terraform module composition (feature) for ARM Linux Virtual Machine (VM)

### [terraform-azurerm-nsg](https://api.github.com/repos/claranet/terraform-azurerm-nsg)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-nsg) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/nsg/azurerm)

Terraform module for Azure Network Security Group

### [terraform-azurerm-policy](https://api.github.com/repos/claranet/terraform-azurerm-policy)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-policy) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/policy/azurerm)

Terraform module for Azure Policy

### [terraform-azurerm-redis](https://api.github.com/repos/claranet/terraform-azurerm-redis)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-redis) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/redis/azurerm)

Terraform module for Azure Redis

### [terraform-azurerm-regions](https://api.github.com/repos/claranet/terraform-azurerm-regions)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-regions) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/regions/azurerm)

Terraform module to handle Azure Regions

### [terraform-azurerm-rg](https://api.github.com/repos/claranet/terraform-azurerm-rg)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-rg) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/rg/azurerm)

Terraform module for Azure Resource Group

### [terraform-azurerm-route-table](https://api.github.com/repos/claranet/terraform-azurerm-route-table)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-route-table) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/route-table/azurerm)

Terraform module for Azure route table

### [terraform-azurerm-run-common](https://api.github.com/repos/claranet/terraform-azurerm-run-common)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-run-common) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/run-common/azurerm)

Terraform module composition (feature) to setup Claranet MSP Azure common tools

### [terraform-azurerm-run-iaas](https://api.github.com/repos/claranet/terraform-azurerm-run-iaas)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-run-iaas) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/run-iaas/azurerm)

Terraform module composition (feature) to setup Claranet MSP Azure IaaS/VM tools

### [terraform-azurerm-search-service](https://api.github.com/repos/claranet/terraform-azurerm-search-service)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-search-service) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/search-service/azurerm)

Terraform module for Azure Search Service

### [terraform-azurerm-service-bus](https://api.github.com/repos/claranet/terraform-azurerm-service-bus)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-service-bus) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/service-bus/azurerm)

Terraform module for Azure Service bus

### [terraform-azurerm-storage-sas-token](https://api.github.com/repos/claranet/terraform-azurerm-storage-sas-token)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-storage-sas-token) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/storage-sas-token/azurerm)

Terraform module for Azure Storage SAS Token access

### [terraform-azurerm-subnet](https://api.github.com/repos/claranet/terraform-azurerm-subnet)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-subnet) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/subnet/azurerm)

Terraform module for Azure virtual networks subnets

### [terraform-azurerm-support](https://api.github.com/repos/claranet/terraform-azurerm-support)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-support) 

Terraform module for Support (bastion zone)

### [terraform-azurerm-tagging](https://api.github.com/repos/claranet/terraform-azurerm-tagging)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-tagging) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/tagging/azurerm)

Terraform module for Resources Tagging

### [terraform-azurerm-vm-backup](https://api.github.com/repos/claranet/terraform-azurerm-vm-backup)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-vm-backup) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/vm-backup/azurerm)

Terraform module to enable Azure Backup policy on Azure VM

### [terraform-azurerm-vm-logs](https://api.github.com/repos/claranet/terraform-azurerm-vm-logs)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-vm-logs) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/vm-logs/azurerm)

Terraform module to enable Diagnostics and Logs on Azure VM

### [terraform-azurerm-vnet](https://api.github.com/repos/claranet/terraform-azurerm-vnet)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-vnet) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/vnet/azurerm)

Terraform module for Azure Virtual Network (vnet)

### [terraform-azurerm-vnet-peering](https://api.github.com/repos/claranet/terraform-azurerm-vnet-peering)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-vnet-peering) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/vnet-peering/azurerm)

Terraform module for Azure virtual networks peering

### [terraform-azurerm-vpn](https://api.github.com/repos/claranet/terraform-azurerm-vpn)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-vpn) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/vpn/azurerm)

Terraform module for Azure VPN stack (Gateway, Route table)

### [terraform-azurerm-windows-vm](https://api.github.com/repos/claranet/terraform-azurerm-windows-vm)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-azurerm-windows-vm) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/windows-vm/azurerm)

Terraform module composition (feature) for ARM Windows Virtual Machine (VM)

## Datadog

### [terraform-datadog-integrations](https://api.github.com/repos/claranet/terraform-datadog-integrations)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-datadog-integrations) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/integrations/datadog)

Manage Datadog integrations with terraform dedicated modules.

### [terraform-datadog-monitors](https://api.github.com/repos/claranet/terraform-datadog-monitors)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-datadog-monitors) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/monitors/datadog)

Manage Datadog monitors with terraform dedicated modules.

## Other

### [terraform-path-hash](https://api.github.com/repos/claranet/terraform-path-hash)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-path-hash) 

Terraform module for hashing the contents of a path

### [terraform-write-files](https://api.github.com/repos/claranet/terraform-write-files)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-write-files) 

Terraform module that creates files during the plan phase

## SignalFx

### [terraform-signalfx-dashboards](https://api.github.com/repos/claranet/terraform-signalfx-dashboards)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-signalfx-dashboards) 

Collection of terraform modules for SignalFX dashboards.

### [terraform-signalfx-detectors](https://api.github.com/repos/claranet/terraform-signalfx-detectors)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-signalfx-detectors) 

Collection of terraform modules for SignalFX detectors.

### [terraform-signalfx-integrations](https://api.github.com/repos/claranet/terraform-signalfx-integrations)

[![github](https://img.shields.io/badge/source-github-black.svg?style=flat-square&logo=github)](https://api.github.com/repos/claranet/terraform-signalfx-integrations) [![registry](https://img.shields.io/badge/terraform-registry-623CE4.svg?style=flat-square&logo=terraform)](https://registry.terraform.io/modules/claranet/integrations/signalfx)

Collection of terraform modules for SignalFX integrations.

