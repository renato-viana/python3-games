# tuple

p1_tuple = ('Renato', 31)
p2 = ('Ana', 31)
p3 = ('Pietra', 31)

people_list = [p1_tuple, p2, p3]

people_dictionary = {'Renato': 31, 'Ana': 25}

print(p1_tuple)
print(people_list)
print(people_dictionary)

inteiros = [1, 3, 4, 5, 7, 8, 9, 10]
pares = [x for x in inteiros if x % 2 == 0]

print(pares)

file = open('words.txt', 'r')
  words = []

   for line in file:
        line = line.strip()
        words.append(line)

    file.close()
