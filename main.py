import configparser

from controller import Controller
from controller_cl import ControllerCL
from view import View
from model import PressureStatistics

if __name__ == "__main__":
    model = PressureStatistics()
    view = View(model=model)

    config = configparser.ConfigParser()
    config.read('config.ini')
    interface_type = config['interface']['type']
    if interface_type == "cli":
    	controller = ControllerCL(view=view, model=model)
    elif interface_type == "interactive":
    	controller = Controller(view=view, model=model)
    try:
        controller.run()
    finally:
        model.save()
