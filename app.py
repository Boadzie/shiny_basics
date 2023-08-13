from shiny import ui, render, App, reactive


app_ui = ui.div(
 ui.h2("Learning Shiny", class_="text-primary"),
 ui.input_numeric(id="num", label="Number of  Children", value=4),
 ui.output_text_verbatim("result")
)

def server(input, output, session):

    @reactive.Calc
    def square():
        return input.num() ** 2
        

    @output
    @render.text()
    def result():
        return f"{input.num()} squared is: {square()}"
    

app = App(app_ui, server)