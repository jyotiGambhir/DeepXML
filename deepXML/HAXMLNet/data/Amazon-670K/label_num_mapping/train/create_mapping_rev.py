import json
all_words = []
all_dict = {}
with open("list_mappings.txt", "r") as f:
    data = f.readlines()
    for line in data:
        words = line.split("\t")
        print(type(words[0]) , type(words[1]))
        print(words[0])
        words[1] = words[1].replace("'","")
        words[1] = words[1].replace("[","")
        words[1] = words[1].replace("]","")
        words[1] = words[1].replace("\n","")
        print(words[1])
        part1 = words[0].split(",")
        print(part1)
        part2 = words[1].split(", ")
        print(part2)
        for i in range(0,len(part1)):
            all_dict[part2[i]] = part1[i]
       
print(all_dict)
json = json.dumps(all_dict)
f = open("mappings_rev.json","w")
f.write(json)
f.close()
