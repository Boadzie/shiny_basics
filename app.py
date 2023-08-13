from shiny import ui, render, App, reactive


app_ui = ui.div(
 ui.h2("Learning Shiny", class_="text-primary"),
 ui.input_numeric(id="num", label="Number of  Children", value=4),
 ui.input_action_button("compute", "Compute Square"),
 ui.output_text_verbatim("result")
)

def server(input, output, session):
    @output
    @render.text
    @reactive.event(input.compute)
    def result():
        return f"{input.num()} squared is: {input.num() ** 2}"
    

app = App(app_ui, server)