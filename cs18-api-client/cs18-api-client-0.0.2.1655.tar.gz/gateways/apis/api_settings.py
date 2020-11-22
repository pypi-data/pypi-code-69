from typing import List

from gateways.apis.api_base_class import ApiBase


class ApiSettings(ApiBase):
    def cloud_providers(self):
        return self.build_route("settings/cloudproviders")

    def cloud_accounts(self):
        return self.build_route("settings/cloudaccounts")

    def compute_services(self):
        return self.build_route("settings/cloudaccounts/computeservices")

    def status(self):
        return self.build_route("settings/status")

    def azure_cloud_accounts(self):
        return self.build_route("settings/cloudaccounts/azure")

    def aws_cloud_accounts(self):
        return self.build_route("settings/cloudaccounts/aws")

    def add_compute_service_aks(self):
        return self.build_route("settings/cloudaccounts/azure/computeservices/aks")

    def add_compute_service_aws_k8s_unmanaged(self):
        return self.build_route("settings/cloudaccounts/aws/computeservices/k8s_unmanaged")

    def aws_template(self):
        return self.build_route("settings/cloudaccounts/aws/template")

    def space_roles(self):
        return self.build_route("settings/spaceroles")

    def account_roles(self):
        return self.build_route("settings/accountroles")

    def verify_cloud_account(self):
        return self.build_route("settings/cloudaccounts/verify")

    def add_repository_by_token(self):
        return self.build_route("settings/repositories/bytoken")

    def add_github_repository(self):
        return self.build_route("settings/repositories/github")

    def add_bitbucket_repository(self):
        return self.build_route("settings/repositories/bitbucket")

    def repositories(self):
        return self.build_route("settings/repositories")

    def repository(self, name: str):
        return self.build_route(f"settings/repositories/{name}")

    def k8s_agent_deployment_yaml(self, cloud_account_name: str, compute_service_name: str, agent_namespace: str,
                                  sandbox_namespaces: str):
        return self.build_route("settings/cloudaccounts/computeservices/k8s/agent-deployment-yaml"
                                "?cloudAccount={cloud_account_name}"
                                "&computeService={compute_service_name}"
                                "&agentNamespace={agent_namespace}"
                                "&sandboxNamespaces={sandbox_namespaces}"
                                .format(**locals()))
