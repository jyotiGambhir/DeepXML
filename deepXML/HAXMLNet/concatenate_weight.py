
import numpy as np

model_name = "FastAttentionXML-Amazon-670K-Tree-0-Level-2"
file_names = ["models/FastAttentionXML-Amazon-670K-Tree-0-Level-2_AttentionWeights.emb.0.weight.npy",
"models/FastAttentionXML-Amazon-670K-Tree-0-Level-2_AttentionWeights.emb.1.weight.npy",
"models/FastAttentionXML-Amazon-670K-Tree-0-Level-2_AttentionWeights.emb.2.weight.npy"]
model_name = "FastAttentionXML-Amazon-670K-Tree-0-Level-3"
file_names = ["models/FastAttentionXML-Amazon-670K-Tree-0-Level-3_AttentionWeights.emb.0.weight.npy",
"models/FastAttentionXML-Amazon-670K-Tree-0-Level-3_AttentionWeights.emb.1.weight.npy",
"models/FastAttentionXML-Amazon-670K-Tree-0-Level-3_AttentionWeights.emb.2.weight.npy"]


'''data = None
for item in range(3):
    file_name = "models/"+file_names[item]
    data = np.concatenate(file_name)
'''

first_file = np.load(file_names[0])
second_file = np.load(file_names[1])
third_file = np.load(file_names[2])

print("First.shape" + str(first_file.shape))
print("Second.shape " + str(second_file.shape))
print("third.shape" + str(third_file.shape))

data = np.concatenate((first_file,second_file))
data = np.concatenate((data,third_file))
print(data.shape)
print(" Location of Saving File " + str("models/Concatenated_" + model_name))
np.save("models/Concatenated_" + model_name,data)

