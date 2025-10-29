from abc import ABC, abstractmethod
import pandas as pd
from typing import Any

class BaseProcessor(ABC):
    def process(self, input_file: str,  output_file:  str ): # cria a classe base e chama os métodos em ordem
        data = self.load_data(input_file)
        data = self.filter_data(data)
        data = self.calculate(data)
        data = self.validate(data)
        self.export_to_xlsx(data, output_file)
        self.report_summary(data)

    def load_data(self, input_file: str):
        try:
            df = pd.read_csv(input_file)
            return df
        except Exception as e:
            raise RuntimeError(f"Failed to load data: {e}")

    @abstractmethod
    def filter_data(self, data :pd.Dataframe) -> pd.DataFrame:
        pass

    @abstractmethod
    def calculate(self, data: pd.DataFrame) -> pd.DataFrame:
        pass

    @abstractmethod
    def validate(self, data: pd.DataFrame) -> pd.DataFrame:
        pass

    @abstractmethod
    def export_to_xlsx(self, data: pd.DataFrame, output_file: str) -> None:
        pass

    # ---------- Optional Hook ----------

    def report_summary(self, data: pd.DataFrame) -> None:
        print(f"✅ Processing completed. Rows processed: {len(data)}")