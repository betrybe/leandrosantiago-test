from abc import ABC, abstractmethod
from os.path import exists
from typing import List


class Importer(ABC):
    """
    Abstract importer class
    """

    @abstractmethod
    def import_data(self, file_path: str) -> List[dict]:
        """
        Signature for import_data method
        """
        return NotImplemented
