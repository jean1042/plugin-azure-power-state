from spaceone.core.manager import BaseManager
from spaceone.inventory.libs.connector import AzureConnector


class AzureManager(BaseManager):
    connector_name = None
    cloud_service_types = []
    response_schema = None
    collected_region_codes = []

    def verify(self, options, secret_data, **kwargs):
        """ Check collector's status.
        """
        connector: AzureConnector = self.locator.get_connector('AzureConnector', secret_data=secret_data)
        connector.verify()

    def collect_power_state(self, params) -> list:
        raise NotImplemented

    def collect_resources(self, params) -> list:
        return self.collect_power_state(params)

    def list_all_resource_groups(self, secret_data):
        connector: AzureConnector = self.locator.get_connector('AzureConnector')
        connector.set_connect(secret_data)

        return connector.list_resource_groups()

