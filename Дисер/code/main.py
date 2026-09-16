from code.ast_tree.binary_operations.binary_math import BinaryMathOperation
from code.ast_tree.core.context import Context
from code.ast_tree.ast_tree_factory import AstTreeFactory


print(AstTreeFactory.types)
print(AstTreeFactory.build({
    "type": 'binary_math_operation',
    "operator": 'add',
    'left': {
        "type": 'literal',
        'value': 1,
    },
    "right": {
        "type": 'literal',
        'value': 2,
    }
}).eval(Context()))