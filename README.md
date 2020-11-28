# robot-dsl
![textX pipeline](https://github.com/JnxF/robot-dsl/workflows/textX%20pipeline/badge.svg)
[![GitHub stars](https://img.shields.io/github/stars/JnxF/robot-dsl.svg)](https://GitHub.com/JnxF/robot-dsl/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/JnxF/robot-dsl.svg)](https://GitHub.com/JnxF/robot-dsl/network/)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/JnxF/robot-dsl.svg)](https://github.com/JnxF/robot-dsl)
[![GitHub contributors](https://img.shields.io/github/contributors/JnxF/robot-dsl.svg)](https://GitHub.com/JnxF/robot-dsl/graphs/contributors/)
[![GitHub license](http://img.shields.io/github/license/JnxF/robot-dsl.svg)](https://github.com/JnxF/robot-dsl/blob/master/LICENSE)

Toy robot DSL implemented in textX

## Installation

This DSL requires [textX](https://textx.github.io/textX/stable/).

```bash
pip install textX
pip install .
```

## Usage
Using directly the `textx` command:
```bash
textx generate example.robot --target dot
dot -Tpng -O example.dot
open example.dot.png
```

From Python 3:
```python
from textx import metamodel_from_file
robot_meta = metamodel_from_file('tx_robot/robot.tx')
example_robot_model = robot_meta.model_from_file('example.robot')
example_robot_model.name
```

VS Code extension:
* Install the [textX](https://github.com/textX/textX-LS) extension on VS Code.
* Open the root folder of the repository: `code .`
* Right click to `setup.py` and _Install textX project_.
* Browse any `*.robot` file.

## License
[MIT](https://choosealicense.com/licenses/mit/)