# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps
# pylint: disable=line-too-long, too-many-lines

helps['appservice plan create'] = """
type: command
short-summary: Create an app service plan.
examples:
  - name: Create a basic app service plan.
    text: >
        az appservice plan create -g MyResourceGroup -n MyPlan
  - name: Create a standard app service plan with with four Linux workers.
    text: >
        az appservice plan create -g MyResourceGroup -n MyPlan \\
            --is-linux --number-of-workers 4 --sku S1
  - name: Create an app service plan for app service environment.
    text: >
        az appservice plan create -g MyResourceGroup -n MyPlan \\
            --app-service-environment MyAppServiceEnvironment --sku I1
  - name: Create an app service plan for a kubernetes environment.
    text: >
        az appservice plan create -g MyResourceGroup -n MyPlan \\
            --kube-environment MyKubeEnvironment --kube-sku ANY
"""

helps['appservice plan update'] = """
type: command
short-summary: Update an app service plan. See https://docs.microsoft.com/azure/app-service/app-service-plan-manage#move-an-app-to-another-app-service-plan to learn more
examples:
  - name: Update an app service plan. (autogenerated)
    text: az appservice plan update --name MyAppServicePlan --resource-group MyResourceGroup --sku F1
    crafted: true
  - name: Update a kubernetes app service plan.
    text: >
        az appservice plan update --name MyAppServicePlan --resource-group MyResourceGroup \\
            --kube-sku Standard_DS2_v2 --number-of-workers 3
"""

helps['appservice kube'] = """
    type: group
    short-summary: Manage Kubernetes Environments
"""

helps['appservice kube create'] = """
    type: command
    short-summary: Create a Kubernetes Environment.
    examples:
    - name: Create Kubernetes Environment with default values.
      text: |
          az appservice kube create -n MyKubeEnvironment -g MyResourceGroup \\
              --client-id MyServicePrincipalClientId \\
              --client-secret MyServicePrincipalClientSecret
"""

helps['appservice kube update'] = """
    type: command
    short-summary: Update a Kubernetes Environment.
    examples:
    - name: Update the Kubernetes Environment's Log Analytics workspace ID.
      text: |
          az appservice kube update -n MyKubeEnvironment -g MyResourceGroup \\
              --workspace-id MyLogAnalyticsWorkspaceResourceId
"""

helps['appservice kube show'] = """
    type: command
    short-summary: Show the details of a kubernetes environment.
    examples:
    - name: Show the details of a Kubernetes Environment.
      text: |
          az appservice kube show -n MyKubeEnvironment -g MyResourceGroup
"""

helps['appservice kube list'] = """
    type: command
    short-summary: List kubernetes environments by subscription or resource group.
    examples:
    - name: List Kubernetes Environments by subscription.
      text: |
          az appservice kube list
    - name: List Kubernetes Environments by resource group.
      text: |
          az appservice kube list -g MyResourceGroup
"""

helps['appservice kube delete'] = """
    type: command
    short-summary: Delete kubernetes environment.
    examples:
    - name: Delete Kubernetes Environment.
      text: az appservice kube delete -g MyResourceGroup -n MyKubeEnvironment
"""

helps['appservice kube wait'] = """
    type: command
    short-summary: Wait for a Kubernetes Environment to reach a desired state.
    examples:
    - name: Wait for a Kubernetes Environment to be provisioned, polling every 60 seconds.
      text: |
          az appservice kube wait -g MyResourceGroup -n MyKubeEnvironment \\
              --created --interval 60
"""

helps['webapp up'] = """
type: command
short-summary: >
    Create a webapp and deploy code from a local workspace to the app. The command is required to run from the folder
    where the code is present. Current support includes Node, Python, .NET Core and ASP.NET. Node,
    Python apps are created as Linux apps. .Net Core, ASP.NET, and static HTML apps are created as Windows apps.
    Append the html flag to deploy as a static HTML app.
examples:
  - name: View the details of the app that will be created, without actually running the operation
    text: >
        az webapp up -n MyUniqueAppName --dryrun
  - name: Create a web app with the default configuration, by running the command from the folder where the code to deployed exists.
    text: >
        az webapp up -n MyUniqueAppName -l locationName
  - name: Create a web app in a specific region, by running the command from the folder where the code to deployed exists.
    text: >
        az webapp up -n MyUniqueAppName -l locationName
  - name: Deploy new code to an app that was originally created using the same command
    text: >
        az webapp up -n MyUniqueAppName -l locationName
  - name: Create a web app and enable log streaming after the deployment operation is complete. This will enable the default configuration required to enable log streaming.
    text: >
        az webapp up -n MyUniqueAppName --logs
  - name: Create a web app and deploy as a static HTML app.
    text: >
        az webapp up -n MyUniqueAppName --html
"""
