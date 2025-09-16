import re
from pydantic import BaseModel


class Temperature(BaseModel):
    value: int


class DewPoint(BaseModel):
    value: int


def parse(message: str):
    conditions = []
    stack = ""
    for lookahead in message + "=":
        print(stack)
        if re.search("M[0-9]{2}$", stack):
            value = -int(stack[-2:])
            if conditions and isinstance(conditions[-1], Temperature):
                conditions.append(DewPoint(value=value))
                stack = stack[:-3]
            elif lookahead == "/":
                conditions.append(Temperature(value=value))
                stack = stack[:-3]
        elif re.search("[0-9]{2}$", stack):
            value = int(stack[-2:])
            if conditions and isinstance(conditions[-1], Temperature):
                conditions.append(DewPoint(value=value))
                stack = stack[:-2]
            elif lookahead == "/":
                conditions.append(Temperature(value=value))
                stack = stack[:-2]

        stack += lookahead
    return conditions


def main():
    print("Hello from lr1!")


if __name__ == "__main__":
    main()
