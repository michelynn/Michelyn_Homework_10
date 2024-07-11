import fibonacci

class main:
    def __init__(self, input_number):
        self.input_number = input_number

    def get_number(self):
        return self.input_number

    def run_fib(self):
        result = fibonacci.calculate(self.input_number)
        return result

user_input = int(input("enter your desired number of fibonacci: "))
my_class = main(user_input)
my_class.get_number()
fibonacci_result = my_class.run_fib() 
print(fibonacci_result)