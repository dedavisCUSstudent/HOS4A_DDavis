#Let's use the del method
motorcycle = ['Honda', 'yamaha', 'suzuki']
del motorcycle[1]
print(motorcycle)

#Let's explore the pop method
motorcycles = ['Honda', 'Yamaha', 'Suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
first_owned = motorcycles.pop(0)
print("The first owned motorcycle is a" , first_owned)

#Let's try the remove method
motorcycles = ['Honda', 'Yamaha', 'Suzuki']
motorcycles.remove('Suzuki')
print(motorcycles)