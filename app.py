from shiny import ui, render, App, reactive
from tailwindcss import tailwind

app_ui = ui.page_fluid(
 ui.div(
    tailwind,
    ui.h2("Learning Shiny", class_="text-4xl my-2"),
    ui.input_numeric(id="num", label="", value=4),
    ui.input_action_button("compute", "Compute Square"),
 ),
ui.div(
    ui.output_text_verbatim("result"),
    class_="mt-4 font-bold"
),
class_="container mx-auto px-4 py-4"
)

def server(input, output, session):
    @output
    @render.text
    @reactive.event(input.compute)
    def result():
        return f"{input.num()} squared is: {input.num() ** 2}"
    

app = App(app_ui, server)