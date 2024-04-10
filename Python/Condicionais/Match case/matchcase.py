# Match case example: 

values = [1, "hello", False, 1.0]

for v in values:
    match v:
        case str():
            print(f"{v} é uma string")
        case int():
            print(f"{v} é um integer")
        case float():
            print(f"{v} é um float")
        case bool():
            print(f"{v} é um boolean")
        case _: 
            print(f"{v} é do tipo: {type(v)}!")
