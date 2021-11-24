# Create a Person class with 2 instance variables: name and age.
# Let's sort a list of Person objects in ascending order based on their ages.
def insertion_sort(nums):
    for i in range(len(nums)):
        j = i

        # Swap the items on the left if they are bigger
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __repr__(self):
        return str(self.name)


p1 = Person('Aragorn', 4321)
p2 = Person('Gandalf', 8474)
p3 = Person('Frodo', 155)
p4 = Person('Bilbo', 261)
p5 = Person('Sauron', 5324)

p_list = [p1, p2, p3, p4, p5]
insertion_sort(p_list)
print(p_list)
