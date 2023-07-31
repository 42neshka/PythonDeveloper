class Numbers:
    def __init__(self):
        self.list = []

    def add_number(self, n):
        self.list.append(n)

    def get_even(self):
        even = []
        for c in self.list:
            if c % 2 == 0:
                even.append(c)
        return even

    def get_odd(self):
        odd = []
        for c in self.list:
            if c % 2 == 1:
                odd.append(c)
        return odd
    
numbers = Numbers()

numbers.add_number(1)
numbers.add_number(2)
numbers.add_number(3)
numbers.add_number(4)

even = numbers.get_even()
odd = numbers.get_odd()
print(numbers.get_even())
print(numbers.get_odd())

even.append(None)
odd.append(None)
print(numbers.get_even())
print(numbers.get_odd())