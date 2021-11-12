from abc import ABC, abstractmethod
from typing import List


class Importer(ABC):
    """
    Abstract importer class
    """

    @classmethod
    def _check_file_ext(cls, file_path: str, allowed_ext: str):
        _, file_ext = file_path.lower().split(".", -1)
        if file_ext != allowed_ext:
            raise ValueError("Arquivo inválido")

    @abstractmethod
    def import_data(self, file_path: str) -> List[dict]:
        """
        Signature for import_data method
        """
        return NotImplemented
