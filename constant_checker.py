import astroid
from astroid import nodes

from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker
from pylint.lint import PyLinter

class ConstantChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'constant-observe'
    priority = -1
    msgs = {
        'C9991': (
            'A constant variable\'s value changes.',
            'constant-value-change',
            'All constants\' value after their initial assignment should stay with the same value.'
        ),
    }
    # options = (
    #     (
    #         'ignore-ints',
    #         {
    #             'default': False, 'type': 'yn', 'metavar' : '<y or n>',
    #             'help': 'Allow returning non-unique integers',
    #         }
    #     ),
    # )

    def __init__(self, linter: PyLinter =None) -> None:
        super(ConstantChecker, self).__init__(linter)
        self._module_variable_dict = {}

    def check_variable_module_level(self, node: nodes.scoped_nodes) -> bool:
        if node == 'Module':
            return True
        return False

    def visit_assign(self, node: nodes.Assign) -> None:
        print('ASSIGNMENT')
        for i in range( len(node.targets) ):
            if self.check_variable_module_level( node.scope().display_type() ):
                if isinstance(node.value, nodes.Const):
                    if node.targets[i].name not in self._module_variable_dict:
                        self._module_variable_dict[node.targets[i].name] = node.value.value
                        return
            if node.targets[i].name in self._module_variable_dict:
                if not isinstance(node.value, nodes.Const):
                    if isinstance(node.value, nodes.BinOp):
                        if node.value.op == '+':
                            value = node.value.left.value + node.value.right.value
                            if self.check_variable_same_value( node.targets[i], value ):
                                continue
                        elif node.value.op == '-':
                            value = node.value.left.value - node.value.right.value
                            if self.check_variable_same_value( node.targets[i], value ):
                                continue
                        elif node.value.op == '*':
                            value = node.value.left.value * node.value.right.value
                            if self.check_variable_same_value( node.targets[i], value ):
                                continue
                        elif node.value.op == '/':
                            value = node.value.left.value / node.value.right.value
                            if self.check_variable_same_value( node.targets[i], value ):
                                continue
                    if isinstance(node.value, nodes.Name):
                        if node.targets[i].name == node.value.name:
                            continue
                    self.add_message('constant-value-change', node=node)
                    return
                elif self.check_variable_same_value( node.targets[i], node.value.value ):
                    continue
                else:
                    self.add_message('constant-value-change', node=node)
                    return

    def leave_assign(self, node: nodes.FunctionDef) -> None:
        return

    def check_variable_same_value(self, node: nodes.NodeNG, value) -> bool:
        if node.name in self._module_variable_dict:
            if self._module_variable_dict[node.name] != value:
                return False
        return True

def register(linter):
    linter.register_checker(ConstantChecker(linter))
