# List creation 
prime_list = [3,5,7,11,13,17,19]

# Adding an element to the list
prime_list.append(21)

#Removing an element from the list
prime_list.remove(3)

#Modifying an element in the list
prime_list[6] = 23

print("Updated list:" ,prime_list)

#Creating a dictionary

car_dict = {'brand':'volkswagon', 'name':'virtus', 'type':'sedan'}

#adding 
car_dict['engine'] = 'turbo'

#removing
del car_dict ['type']

#modifying
car_dict['name'] = 'taigun'

print("updated dictionary:" ,car_dict)

#Creating a Set

even_set = {2,4,6,8,10}

#adding an element
even_set.add(12)

#removing an element 
even_set.remove(2)

#Modifying an element 
even_set.discard(4)
even_set.add(14)

print("updated set is:" , even_set)

