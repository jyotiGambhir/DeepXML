import json
with open('mappings.json') as f:
  data = json.load(f)

with open('mappings_test.json') as f1:
  data1  = json.load(f1)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(type(data))
print(len(data))
print(len(data1))
#print(data1)
for key in data1:
  data[key] = data1[key]
print(len(data))

json = json.dumps(data)
f = open("merged_mappings.json","w")
f.write(json)
f.close()
