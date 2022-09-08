import intake
from dagster import get_dagster_logger, job, op, Output, graph
from analytics_framework import INTAKE_LOC

from dagster.utils.log import get_dagster_logger
logger = get_dagster_logger()

catalog_path = INTAKE_LOC.joinpath("catalog_entry.yml")

@op
def read_stock_price_data():
    catalog = intake.open_catalog(catalog_path)
    df_raw = catalog.twilio_stock_price.read()
    logger.info(f"Raw dataset first 05 rows: {df_raw.head(5)}")
    logger.info(f"Shape of the data loaded: {df_raw.shape}")
    return df_raw


@op
def rolling_average(df_raw):
    simple_rolling_avg = df_raw['close'].rolling(30).mean() # rolling avg for 30 days
    logger.info(f"Simple stock closing price rolling avg for 300 days: {simple_rolling_avg}")


@op
def statistical_info(df_raw):
    logger.info(f"Stock price statistical info", df_raw.describe())


@job
def compute():
    df_raw = read_stock_price_data()
    result_simple_rolling_avg = rolling_average(df_raw)
    result_statistical_value = statistical_info(df_raw)


if __name__ == "__main__":
    result = compute.execute_in_process()
