import numpy as np
import panel as pn
import holoviews as hv
from bokeh.models import HoverTool
from analytics_framework.reusable_functions.intake_cf import initiate_catalog
hv.extension('bokeh')


class Base:

    def __init__(self):
        self.catalog = initiate_catalog()

    def analysis_twilio_stock(self):
        # reading catalog data
        df_stock_data = self.catalog.twilio_stock_price.read()
        # creating a simple table to display raw data
        simple_table = hv.Table(df_stock_data).opts(width=700)

        # line chart showing the trend of stock prices
        hover_close = HoverTool(tooltips=[('Stock closing price ($)', '$y')])
        hover_open = HoverTool(tooltips=[('Stock opening price ($)', '$y')])

        date_col = np.array(simple_table['date'], dtype=np.datetime64)
        open_ = hv.Curve((date_col, df_stock_data.open),
                         'Date', 'Stock price ($)', label='open').opts(
                          tools=[hover_open])
        close_ = hv.Curve((date_col, df_stock_data.close),
                          'Date', 'Stock price ($)', label='close').opts(
                          tools=[hover_close])
        plot_curve_open_close = (open_ * close_).opts(width=900,
                                                      legend_position='top_left')

        return pn.Column(simple_table, plot_curve_open_close)

    def plot(self):
        view = pn.template.FastListTemplate(
            site="Twilio stock price viz",
            main=[self.analysis_twilio_stock()]
        )
        return view


if __name__ == "__main__":
    obj = Base()
    pn.serve(
        obj.plot(),
        port=5006,
        # NOTE: not a good practice to allow all the traffic, use non-wildcard values to restrict access explicitly
        websocket_origin=['*'],
        autoreload=True,
        start=True,
        location=True,
        )
