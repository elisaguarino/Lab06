import flet as ft

from model.model import Autonoleggio
from UI.view import View
from UI.controller import Controller
from UI.alert import AlertManager
'''
DA ESEGUIRE
'''

def main(page: ft.Page):
    my_model = Autonoleggio("Polito Rent", "Alessandro Visconti")
    my_view = View(page)
    alert_manager = AlertManager(page)
    my_controller = Controller(my_view, my_model, alert_manager)
    my_view.set_controller(my_controller)
    my_view.load_interface()


ft.app(target=main)
