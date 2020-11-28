from os.path import dirname, join
from textx import language, metamodel_from_file, TextXSemanticError, get_location


@language("Robot", "*.robot")
def robot():
    "A language for defining robot behaviour"

    def semantic_check(model, metamodel):
        if model.name == "WrongMode":
            raise TextXSemanticError(
                'The root mode cannot be called "Wrong Mode".', **get_location(model)
            )

    def mode_obj_processor(mode):
        if mode.name[0].islower():
            raise TextXSemanticError(
                f'Mode name "{mode.name}" must be capitalized.', **get_location(mode)
            )

    metamodel = metamodel_from_file(join(dirname(__file__), "robot.tx"))
    metamodel.register_model_processor(semantic_check)
    metamodel.register_obj_processors({"Mode": mode_obj_processor})
    return metamodel
