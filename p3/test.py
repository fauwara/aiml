import csv

with open('p3.csv') as f:
	csv_file = csv.reader(f)

	data = list(csv_file)

	specific = data[0][:-1]
	general = [["?" for _ in range(len(specific))] for _ in range(len(specific))]

	for i in range(len(data)):
		if data[i][-1] == "Yes":
			for j in range(len(specific)):
				if data[i][j] != specific[j]:
					specific[j] = "?"
					general[j][j] = "?"
			
		else:
			for j in range(len(specific)):
				if data[i][j] != specific[j]:
					general[j][j] = specific[j]
				else:
					general[j][j] = "?"

	print(specific)
	print(general)