rec_file = open("sillyRec.txt", 'r')

rec_file = rec_file.readlines()
line_number = 1
for line in rec_file:
    if line_number % 2 == 1:
        print(line)


