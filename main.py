from controller import Controller
from view import View
from model import PressureStatistics

if __name__ == "__main__":
    model = PressureStatistics()
    view = View(model=model)
    controller = Controller(view=view, model=model)
    try:
        controller.run()
    finally:
        model.save()
