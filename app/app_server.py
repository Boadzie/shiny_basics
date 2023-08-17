from shiny import ui, render, App, reactive
import polars as pl
import app.kpi as kpi
from lets_plot import *
from lets_plot.mapping import as_discrete
import lets_plot as lp

df = (
    pl.scan_csv("app/organizations-2000000.csv")
    .filter(pl.col("Country").is_in(["Ghana", "Nigeria", "Kenya"]))
    .with_columns(pl.col("Founded").cast(pl.Date))
).collect()
# print(df.head())


def server(input, output, session):
    @output(id="plot1")
    @render.ui
    def plot1():
        x = input.x()
        y = input.y()
        if x and y:
            fig = (
                ggplot(
                    df.sample(1000),
                    aes(x=f"{x}", y=f"{y}"),
                )
                + geom_bar(
                    stat="identity",
                    show_legend=False,
                )
                + labs(
                    title="Employees distribution across Company, Country and Industry",
                    subtitle="Data from Kaggle",
                )
                + theme(
                    title=element_text(face="bold"),
                )
                + ggsize(height=600, width=970)
            )
            phtml = lp._kbridge._generate_static_html_page(fig.as_dict(), iframe=True)
            return ui.HTML(phtml)
