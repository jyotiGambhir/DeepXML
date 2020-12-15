import numpy as np
import pandas as pd
import json
from tqdm import tqdm

def save_data(filename,data):
    with open(filename, 'w') as fp:
        json.dump(data, fp, indent=4, sort_keys=True)

def load_data(filename):
    with open(filename, 'r') as fp:
        data = json.load(fp)
    return data

group_score = np.load("/home/prakash.nath/AttentionXML/results/HAXML_NET_G_EUR-LEX/AttentionXML-EUR-Lex-Ensemble-scores.npy")
group_id = np.load("/home/prakash.nath/AttentionXML/results/HAXML_NET_G_EUR-LEX/AttentionXML-EUR-Lex-Ensemble-labels.npy")

label_score = np.load("/home/prakash.nath/AttentionXML/results/HAXML_NET_L_EUR-LEX/AttentionXML-EUR-Lex-Ensemble-scores.npy")
label_id = np.load("/home/prakash.nath/AttentionXML/results/HAXML_NET_L_EUR-LEX/AttentionXML-EUR-Lex-Ensemble-labels.npy")

group_label = load_data("/home/prakash.nath/AttentionXML/data/EUR-Lex/cluster_label.json")

labels_pred = []
labels_score = []

topk_groups = 15
topk_labels = 20

for i in tqdm(range((group_score.shape)[0])):
	lp, ls = [], []
	top_groups = group_id[i,:topk_groups]
	top_groups_scores = group_score[i,:topk_groups]

	for j in range((top_groups.shape)[0]):
		#print(top_groups[j])
		label_list = group_label[top_groups[j]]
		for label in label_list:
			score = 0.0
			for k in range((label_id[i].shape)[0]):
				if label_id[i,k] == label:
					score = label_score[i,k]
					break
			if score != 0.0:
				lp.append(label)
				ls.append(score * top_groups_scores[j])

	temp_dict = {}
	for j in range(len(lp)):
		temp_dict[ls[j]] = lp[j]

	lp, ls = [], []
	cnt = 0

	for j in sorted(temp_dict,reverse=True):	
		lp.append(temp_dict[j])
		ls.append(str(j))
		cnt += 1
		if cnt == topk_labels:
			break
			
	labels_pred.append(lp)
	labels_score.append(ls)


with open('/home/prakash.nath/AttentionXML/results/EUR-Lex_labels_1024', 'w') as fp:
    for item in labels_pred:
        t = " ".join(item) + "\n"
        fp.write(t)
    fp.close()

#print(labels_score)

with open('/home/prakash.nath/AttentionXML/results/EUR-Lex_score_1024', 'w') as fp:
    for item in labels_score:
        t = " ".join(item) + "\n"
        fp.write(t)
    fp.close()


