import pandas as pd
from ingestion.base.base_loader import BaseLoader
from ingestion.utils.normalization import normalize_company_name

SP500_URL = "https://datahub.io/core/s-and-p-500-companies/_r/-/data/constituents.csv"


class SP500Loader(BaseLoader):
    """
    Loader for S&P 500 companies dataset.
    """

    def __init__(self, url: str = SP500_URL):
        self.url = url

    def load(self) -> pd.DataFrame:
        """
        Download and load the S&P 500 CSV, normalize company names,
        and return DataFrame.
        """
        df = pd.read_csv(self.url)
        df["normalized_name"] = df["Security"].apply(normalize_company_name)
        return df
