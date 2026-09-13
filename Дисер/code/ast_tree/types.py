from typing import Generic, TypeVar, Callable

TEnum = TypeVar("TEnum")

class OperatorFuncs(dict[TEnum, tuple[Callable, Callable]], Generic[TEnum]):
    pass

# OPERATORS_FUNCS: Dict[Enum, (callable, callable)] = {
#     UnaryMathOperation.Negate: (torch.neg, lambda x: -x),
#     UnaryMathOperation.Abs: (torch.abs, abs),
#     UnaryMathOperation.Sqrt: (torch.sqrt, math.sqrt),
#     UnaryMathOperation.Sin: (torch.sin, math.sin),
#     UnaryMathOperation.Cos: (torch.cos, math.cos),
#     UnaryMathOperation.Tan: (torch.tan, math.tan),
#     UnaryMathOperation.Exp: (torch.exp, math.exp),
#     UnaryMathOperation.Log: (torch.log, math.log),
#     UnaryMathOperation.Floor: (torch.floor, math.floor),
#     UnaryMathOperation.Ceil: (torch.ceil, math.ceil),
# }
