import pandas as pd
from ingestion.base.base_loader import BaseLoader
from ingestion.utils.normalization import normalize_company_name

HUGGINGFACE_URL = "https://huggingface.co/datasets/seemasaharann/fortune1000-dataset/resolve/main/train.csv"


class Fortune1000Loader(BaseLoader):
    """
    Loader for the Fortune 1000 dataset from Hugging Face.
    Downloads CSV, normalizes company names, and returns DataFrame.
    """

    def __init__(self, url: str = HUGGINGFACE_URL):
        self.url = url

    def load(self) -> pd.DataFrame:
        """
        Download Fortune 1000 CSV, normalize company names, and return a DataFrame.
        """
        df = pd.read_csv(self.url)

        # normalize company names
        if "Company" in df.columns:
            df["normalized_name"] = df["Company"].apply(normalize_company_name)
        else:
            df["normalized_name"] = df.iloc[:, 0].apply(normalize_company_name)

        return df
