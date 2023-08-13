from shiny import ui, render, App, reactive
from tailwindcss import tailwind
import polars as pl

df = pl.scan_csv("organizations-2000000.csv")

app_ui = ui.page_fluid(
    ui.div(
        ui.h2("Learning Shiny & Friends", class_="text-4xl my-2"),
        ui.div(
            ui.input_text("country", "", width="40%", placeholder="Search Country"),
            ui.input_action_button("search", "Search"),
            class_="flex items-center space-x-4",
        ),
    ),
    ui.div(ui.output_table("tablex"), class_="mt-4 font-bold"),
    class_="container mx-auto px-4 py-4",
)


def server(input, output, session):
    @reactive.Calc
    def get_country():
        if input.country():
            c = df.filter(pl.col("Country") == f"{input.country().capitalize()}").limit(1000000).collect()
            return c

    @output
    @render.table
    @reactive.event(input.search)
    def tablex():
        return get_country()


app = App(app_ui, server)
