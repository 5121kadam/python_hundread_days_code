def add(n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multipy(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
    
operations = {
    "+":add,
    "-":substract,
    "*":multipy,
    "/":divide
}
def calculator():
    print("Welcome to the calculator!")
    should_accumulate = True
    n1 = float(input("What is the first number?\n"))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operaton_symbol = input("pick an operation\n")
        n2 = float(input("What is the next number?\n"))
        ans = (operations[operaton_symbol](n1,n2))
        print(f"{n1} {operaton_symbol} {n2} = {ans}")
        choice = input(f"Type 'y' to calculating with {ans} or type 'n' to stat new calculator\n").lower()
        if choice == 'y':
            n1 = ans
        elif choice == 'n':
            should_accumulate = False
            calculator()
        else:
            print("Invalid input")
            should_accumulate = False
            
calculator()