def calc():
  def sum(a, b):
    return a + b

  def sub(a, b):
    return a - b

  def multiply(a, b):
    return a * b

  def division(a, b):
    if b != 0:
        return a / b
    else:
        return "invalid input" 



def main():
    from calc import  sum, sub, multiply, division
    while True:
        x = input("Enter data ")
        if x not in ('sum', 'sub', 'multiply', 'division') :
            print("Invalid input")
            continue
        a=float(input("enter number"))
        b=float(input("enter number"))
        if x == 'sum':
            print(sum(a, b))
        elif x == 'sub':
           print( sub(a, b))
        elif x == 'multiply':
         print( multiply(a, b))
        elif x == 'div':
            print(division(a, b))

       

        y = input("Do you want to perform another operation? (yes/stop): ")
        if y == 'stop':
            print("Exit")
            break

 