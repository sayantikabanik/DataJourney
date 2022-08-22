import numpy as np
import panel as pn
import matplotlib.pyplot as plt
import hvplot.pandas
import holoviews as hv
from holoviews import opts,dim
from bokeh.models import HoverTool
hv.extension('bokeh')

class Base:

    def __init__(self):
        catalog = catalog_init()

    def line_chart_twilio_stock(self):
