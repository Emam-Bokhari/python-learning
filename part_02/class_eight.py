# map function

numbers=[1,12,13,15,17,19]

result=map(lambda n:n*2,numbers)

print(list(result))

# filter function
person_counts=[1,2,3,6,11,111,12,15,16]

def is_even(numbers):
    return numbers % 2==0

result=filter(is_even,person_counts)

print(list(result))

