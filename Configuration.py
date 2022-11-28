from dataclasses import dataclass
from typing import List


@dataclass
class Configuration:
    """Defines the class for a Configuration-Object.
       It is instantiated through reading the configuration-file."""

    def __init__(self):
        self.name: str = "null"
        self.note: str = "null"
        self.id: str = "null"
        self.list_of_alt_labels: List[str] = []
        self.required: str = "null"
        self.required_element: str = "null"
        self.wordcount: str = "null"
        self.internal_norm_vocabulary: str = "null"
        self.external_norm_vocabulary: str = "null"
        self.lod: str = "null"
        self.coordinate: str = "null"
        self.date: str = "null"
        self.empty_string: str = "null"
