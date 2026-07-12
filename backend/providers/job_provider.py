from abc import ABC, abstractmethod


class JobProvider(ABC):

    @abstractmethod
    def search_jobs(
        self,
        keyword: str,
        location: str,
    ):
        pass