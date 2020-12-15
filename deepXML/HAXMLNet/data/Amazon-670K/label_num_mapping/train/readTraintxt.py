import readline
import copy
all_words = []
with open("train.txt", "r") as f:
    data = f.readlines()
    for line in data:
        words = line.split()
        temp = copy.deepcopy(words[0])
        all_words.append(temp)

print(all_words)

with open("onlyTrainLabels.txt", "w") as file1: 
    # Writing data to a file 
    # file1.write("Hello \n") 
    for elem in all_words:
        file1.writelines(elem)
        file1.writelines("\n") 

