from backend.providers.arbeitnow_provider import ArbeitNowProvider
from backend.providers.remotive_provider import RemotiveProvider


class JobProviderFactory:

    def __init__(self):

        self.providers = [
            RemotiveProvider(),
            ArbeitNowProvider(),
        ]

    def get_all(self):

        return self.providers