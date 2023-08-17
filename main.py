from shiny import App
from app.ui import app_ui
from app.app_server import server

app = App(app_ui, server)
