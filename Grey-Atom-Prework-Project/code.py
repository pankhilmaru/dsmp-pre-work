# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio' ]
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

# Concatenate both the strings
new_class = (class_1 + class_2)
print (new_class)


# Append the list
new_class.append('Peter Warden')

# Print updated list
print(new_class)


# Remove the element from the list
new_class.remove('Carla Gentry')

# Print the list
print(new_class)

# Code ends here


# --------------
# Code starts here
courses = {'Math': 65, 'English':70,'History': 80,'French':70,'Science':60}

print(courses)

total = courses['Math']+courses['English']+courses['History']+courses['French']+courses['Science']

print(total)

percentage = (total *100/500)

print(percentage)




# Code ends here


# --------------
# Code starts here
mathematics = {'Geoffrey Hinton': 78,'Andrew Ng': 95,'Sebastian Raschka': 65, 'Yoshua Benijo':50 ,'Hilary Mason': 70, 'Corrina Cortes': 66,'Peter Warden':75}

topper = max(mathematics, key=mathematics.get)

print(topper)




# Code ends here  


# --------------
# Given string
topper = 'andrew ng'


# Code starts here
first_name, last_name = topper.split()

full_name = last_name + " "+ first_name

certificate_name = full_name.upper()

print(certificate_name)


# Code ends here

