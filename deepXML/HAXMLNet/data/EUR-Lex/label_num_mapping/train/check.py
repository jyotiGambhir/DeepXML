import json
with open('mappings.json') as f:
  data = json.load(f)

tlist = []
with open("onlyTestLabelsnpy.txt") as f1:
  for x in f1:
  	tlist.append(x)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
#print(type(data))
#print(len(data))

#print(len(tlist))
#print(tlist[0])
dkeys = data.keys()
print(type(dkeys))
#print(data[0])

for elem in tlist:
	print(type(elem))
	words = elem.split(",")
	for w in words:
		print(type(w) , w)
		tempvar = w
		tempvar = tempvar.replace("'","")
		tempvar = tempvar.replace("[","")
		tempvar = tempvar.replace("]","")
		tempvar = tempvar.replace("\n","")
		tempvar = tempvar.replace(" ","")
		print("tempvar is -->",tempvar)	
		if(tempvar in data.keys()):
			pass
		else:
			print("not present ",tempvar)
			exit(0)
#print(data1)
#for key in data1:
#  data[key] = data1[key]
print(len(data))

#json = json.dumps(data)
#f = open("merged_mappings.json","w")
#f.write(json)
#f.close()
