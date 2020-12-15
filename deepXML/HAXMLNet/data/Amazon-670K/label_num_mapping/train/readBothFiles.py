import copy
all_list = []
with open("onlyTrainLabels.txt") as textfile1, open("onlyTrainLabelsnpy.txt") as textfile2: 
    for x, y in zip(textfile1, textfile2):
        x = x.strip()
        y = y.strip()
        strn =  "{0}\t{1}".format(x, y)
        temp = copy.deepcopy(strn)
        all_list.append(temp)
        # print("{0}\t{1}".format(x, y))
print(len(all_list))
print(all_list[2])
with open("list_mappings.txt", 'w') as file1: 
    for i in range(0,len(all_list)):
        file1.write(all_list[i])
        file1.write("\n")
