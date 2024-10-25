import intake
from pandas import DataFrame
from dagster import asset, Definitions
from analytics_framework import INTAKE_LOC

catalog_path = INTAKE_LOC.joinpath("catalog_entry.yml")
catalog = intake.open_catalog(catalog_path)

@asset
def simple_rolling_average():
    df_raw = catalog.twilio_stock_price.read()
    SRA = df_raw['close'].rolling(window=30).mean() # rolling avg for 30 days
    return SRA


@asset
def exponential_rolling_average():
    df_raw = catalog.twilio_stock_price.read()
    ERA = df_raw['close'].ewm(span=30, adjust=False).mean()
    return ERA


outcome = Definitions(assets=[simple_rolling_average, exponential_rolling_average])
