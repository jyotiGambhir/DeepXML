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

l = []

with open("original/train_labels.txt") as fp:
        for line in fp:
                line = line.strip().split()
                n = []
                for label in line:
                        try:
                                cluster = label_cluster[label]
                                if cluster not in n:
                                        n.append(cluster)
                        except:
                                continue
                l.append(n)
        fp.close()

with open('train_labels.txt', 'w') as fp:
        for item in l:
                t = " ".join(item) + "\n"
                fp.write(t)
        fp.close()

l = []

with open("original/test_labels.txt") as fp:
        for line in fp:
                line = line.strip().split()
                n = []
                for label in line:
                        try:
                                cluster = label_cluster[label]
                                if cluster not in n:
                                        n.append(cluster)
                        except:
                                continue
                l.append(n)
        fp.close()

with open('test_labels.txt', 'w') as fp:
        for item in l:
                t = " ".join(item) + "\n"
                fp.write(t)
        fp.close()

