from ArrayStack import ArrayStack


def postfix_calculator():
    # helper function
    symbols = ["+", "-", "*", "/"]

    def calculate(items, variable):
        stack = ArrayStack()

        # creates stack
        for i in range(len(items)):
            # pushes int and float values onto stack
            try:
                if isinstance(float(items[i]), float):
                    stack.push(int(items[i]))
            except ValueError:
                if items[i] not in symbols:
                    stack.push(variable[items[i]])

            # calculates items in stack
                else:
                    x = stack.pop()
                    y = stack.pop()
                    if items[i] == "+":
                        stack.push(y + x)
                    elif items[i] == "-":
                        stack.push(y - x)
                    elif items[i] == "*":
                        stack.push(y * x)
                    elif items[i] == "/":
                        stack.push(y / x)

        ans = stack.pop()
        return ans

    # activation
    expression = input("--> ")
    variable = {}

    # continue when user doesn't input done()
    while expression != "done()":
        items = expression.split(" ")

        # checks for valid response
        valid_res = True
        for elem in items:

            # considers extra spaces
            if (elem.isnumeric() == False) and (elem != " ") and (elem not in symbols):
                valid_res = False

            # considers variable and equal sign
            if (elem.isalpha() == True) or (elem == "="):
                valid_res = True

            # considers negative value(s)
            if (elem.isnumeric() == False) and (elem != " ") and (elem not in symbols):
                try:
                    valid_res = True
                except ValueError:
                    valid_res = False

        # continue when response is valid
        if valid_res is True:

            # checks for assignment expression
            if len(items) > 2 and items[1] == "=":
                ans = calculate(items[2:], variable)
                variable[items[0]] = ans
                print(items[0])

            # otherwise it is an arithmetic expression
            else:
                ans = calculate(items, variable)
                print(ans)

        expression = input("--> ")
