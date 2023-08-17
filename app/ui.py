from shiny import ui
from app.tailwindcss import tailwind
from app.kpi import total_og, avg_employees, industry_count, X, Y
from shinywidgets import output_widget

app_ui = ui.page_fluid(
    tailwind,
    ui.div(
        ui.h1("Organizations", class_="font-bold text-4xl"),
        class_="bg-white shadow-md text-gray-500 p-3 rounded-md",
    ),
    ui.div(
        ui.span(
            total_og,
            ui.span("Total Number of Organizations", class_="text-md text-green-500 font-medium"),
            class_="shadow-md font-black bg-white flex flex-col gap-2 p-4 rounded-md text-3xl text-gray-500",
        ),
        ui.span(
            avg_employees,
            ui.span("Avg. number of Employees", class_="text-md text-green-500 font-medium"),
            class_="shadow-md font-black bg-white flex flex-col gap-2 p-4 rounded-md text-3xl text-gray-500",
        ),
        ui.span(
            industry_count,
            ui.span("Number of Industries", class_="text-md text-green-500 font-medium"),
            class_="shadow-md font-black bg-white flex flex-col gap-2 p-4 rounded-md text-3xl text-gray-500",
        ),
        class_="grid grid-cols-1 lg:grid-cols-3 gap-2  mt-4 place-content-center",
    ),
    ui.div(
        ui.div(
            ui.input_select(id="x", label="X Variable", choices=[k for k in X.columns], width="100%"),
            ui.input_select(
                id="y",
                label="Y variable",
                choices=[k for k in Y.columns],
                width="100%",
            ),
            class_="col-span-1 bg-white shadow-md w-full p-4",
        ),
        ui.output_ui("plot1", class_="cols-span-2 shadow-md w-full"),
        class_="grid grid-cols-1 lg:grid-cols-3 gap-4 my-4 w-full",
    ),
    ui.div(
        ui.h1("@2023 Learning Shiny", class_="font-light text-lg"),
        class_="bg-white shadow-md text-gray-500 p-3 rounded-md",
    ),
    class_="container mx-auto px-4 py-8 bg-slate-100 w-full",
)
