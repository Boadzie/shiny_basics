from shiny import ui, render, App 


app_ui = ui.div(
 ui.h2("Learning Shiny", class_="text-primary"),
 ui.input_numeric(id="num", label="Number of  Children", value=4),
 ui.output_text_verbatim("result")
)

def server(input, output, session):
    @output
    @render.text()
    def result():
        return f"The Number times 2 is: {input.num() * 2}"
    

app = App(app_ui, server)