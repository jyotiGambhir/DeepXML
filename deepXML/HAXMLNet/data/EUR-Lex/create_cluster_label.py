import numpy as np
import pandas as pd
import json

def save_data(filename,data):
    with open(filename, 'w') as fp:
        json.dump(data, fp, indent=4, sort_keys=True)

def load_data(filename):
    with open(filename, 'r') as fp:
        data = json.load(fp)
    return data

a = np.load("FastAttentionXML-EUR-Lex-Tree-0-cluster-Level-8.npy")
wrd_idx = load_data("./label_num_mapping/merged_mappings_rev.json")
idx_wrd = load_data("./label_num_mapping/merged_mappings.json")
prefix = "group"
clust_label = {}
label_clust = {}

for key in idx_wrd:
	print(key,end=",")
print("")
h = 0
for i in range(len(a)):
	cluster_name = prefix+str(i)
	clust_label[cluster_name] = []
	#print(a[i])
	print(i)
	for j in a[i]:
	#	print(j)
	#	print(type(j))
		j = str(j)
		try:
			clust_label[cluster_name].append(idx_wrd[j])
			label_clust[idx_wrd[j]] = cluster_name
		except:
			h += 1
			continue

save_data("cluster_label.json",clust_label)
save_data("label_cluster.json",label_clust)
print(h)
