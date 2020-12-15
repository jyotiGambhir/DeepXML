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

wrd_idx = load_data("./label_num_mapping/merged_mappings_rev.json")
idx_wrd = load_data("./label_num_mapping/merged_mappings.json")
label_cluster = load_data("label_cluster.json")
cluster_label = load_data("cluster_label.json")

max_neg_labels = 1

l = []

with open("./original/train_labels.txt") as fp:
    for line in fp:
        line = line.strip().split()
        l.append(line)

cnt = 0

with open("./HAXML_NET_G/train_labels.txt") as fp:
    for line in fp:
        line = line.strip().split()
        # n = []
        neg = max_neg_labels
        for cluster_id in line:
            try:
                for label in cluster_label[cluster_id]:
                    if label not in l[cnt] and neg>0:
                        l[cnt].append(label)
                        neg -= 1
            except:
                continue
        # l.append(n)
        cnt += 1
    fp.close()

with open('train_labels.txt', 'w') as fp:
    for item in l:
        t = " ".join(item) + "\n"
        fp.write(t)
    fp.close()


l = []
cnt = 0
max_neg_labels = 1

with open("./original/test_labels.txt") as fp:
    for line in fp:
        line = line.strip().split()
        l.append(line)

with open("./HAXML_NET_G/test_labels.txt") as fp:
    for line in fp:
        line = line.strip().split()
        neg = max_neg_labels
        for cluster_id in line:
            try:
                for label in cluster_label[cluster_id]:
                    if label not in l[cnt] and neg > 0:
                        l[cnt].append(label)
                        neg -= 1
            except:
                continue
        cnt += 1
    fp.close()

with open('test_labels.txt','w') as fp:
    for item in l:
        t = " ".join(item) + "\n"
        fp.write(t)
    fp.close()

