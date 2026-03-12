from abc import ABC, abstractmethod

import pandas as pd


class BaseLoader(ABC):
    """
    Abstract base class for all data loaders.
    """

    @abstractmethod
    def load(self) -> pd.DataFrame:
        """
        Load raw data and return a DataFrame.
        """
        pass
