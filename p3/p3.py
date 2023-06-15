import csv

with open("p3.csv") as f:
    csv_file = csv.reader(f)

    # * convert csv file into 2d array
    data = list(csv_file)
    # print(data)
    # output: [['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'], ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'], ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'], ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']]

    # * get the first row of the csv but without the last column
    # [0] -> first row
    # [:-1] -> till last but one row
    specific = data[0][:-1]
    # print(specific)
    # output: ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same']

	# * create 2d array such that -> [['?' * no of columns - 1] * no of columns - 1]
	# no of coulumns - 1 because we excluding last coulumn  
	# no of columns = len(specific)
    general = [["?" for i in range(len(specific))] for j in range(len(specific))]
	# check out list comprehension if you dont understand the above syntax
    # print(general)
    # output: [['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?']]

    for i in data:
        # if last_column of i == YES; then check if any coresponding element of it is not equal to the corresponding element of specific; then set that element specifc and the [j][j]th element oof specific to "?"
        if i[-1] == "Yes":
            for j in range(len(specific)):
                if i[j] != specific[j]:
                    specific[j] = "?"
                    general[j][j] = "?"
                    
		# else check if any coresponding element of it is not equal to the corresponding element of specific; then set the [j][j]th element of general to the jth element of specific; else set it to "?"
        elif i[-1] == "No":
            for j in range(len(specific)):
                if i[j] != specific[j]:
                    general[j][j] = specific[j]
                else:
                    general[j][j] = "?"

        # print("\nStep " + str(data.index(i)+1) + " of Candidate Elimination Algorithm")
        # print(specific)
        # print(general)

	# remove all the unused ['?', '?', '?', '?', '?', '?'] (empty or completely filled question mark arrays) from general
    gh = [] # gh = general Hypothesis
    for i in general:
        for j in i:
            if j != '?':
                gh.append(i)
                break
            
    print("\nFinal Specific hypothesis:\n", specific)
    print("\nFinal General hypothesis:\n", gh)
