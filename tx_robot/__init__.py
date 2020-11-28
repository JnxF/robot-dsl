from os.path import dirname, join
from textx import language, metamodel_from_file

@language("Robot", "*.robot")
def robot():
    "A language for defining robot behaviour"
    return metamodel_from_file(join(dirname(__file__), "robot.tx"))
