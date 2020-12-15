# File Sharing 

Currently all files relevant are present in : /share1/prakash.nath/ on ADA system and given proper rights to copy the contents. 

Drive Link For Attention Weight and Score : https://drive.google.com/open?id=1MQPfrf3yiufJxHC3qsH-Ts3cu9fHzdST
It contains the images of Network Structure. 

# Reading Network Structure of a Model and Steps for Getting Attention Weights :

<br />
1. Run AttentionXML / FastAttentionXML on the dataset from scripts folder.
<br />
2. After execution completes , models will be saved in "./models" folder for respective dataset. 
<br />
3. Configure "readmodel.py" for the model file of which network structure is to be obtained . 
<br />
4. Configure the "readmodel.py" to read specific model -> attributes if to be saved  ( set model_name param to file/model name you want to get the Network structure ).
<br />
5. Execute the "readmodel.py".
<br />
6. Structure will be printed on console with respective network structure details and saving is done ( if not commenetd for saving the models for respective attribute ).
<br />
7. If the network structure contains attributes like "AttentionWeights.emb.0.weight.npy" , then it shows the respective model is ran on distributed GPU's. Hence we need to concatenate such type of weights.
<br />
8. Keep "concatenate_weight.py" parellel to "./models" folder ( from copying from "./AttentionXML/HAXMLNet/concatenate_weight.py" to parellel to "./models" folder.
<br />
9. Provide the file names inside lists named <b>"file_names"</b> which ever you want to concatenate. Program will load through and concatenate them.
<br />

10. You will get concatenated models as a result prefix with "Concatenate_" as "Concatenate_nameofmodel" and saved in respective folder where script is ran. On ADA currently the files as an example is "Concatenated_FastAttentionXML-Amazon-670K-Tree-0-Level-3.npy" present in "/share1/prakash.nath/All_Fast_XML_Details_Amazon_670K/models/Concatenated_FastAttentionXML-Amazon-670K-Tree-0-Level-3.npy". Dimension of the file is ( 667317,1024 ). ( Corresponding Image is on Google drive in "Network Structure Folder/Concatenated_Attention_Weight_Dimension.jpg") 

<br />
	
# HAXMLNet

Navigate to Current directory as  ./AttentionXML/HAXMLNet
<br />
Preprocessing : 
<br />
<br />
	1. Create Mapping & Reverse Mapping .
<br />
	2. Run create_cluster_label.py
<br />
<br />
<br />
There are two parts for this section : 
<br />
1) Configuration for HAXMLNet G Part : 
<br />
	a. Download the Dataset from respective Dataset URL.
<br />
	b. Create the folder with dataset name like "Amazon-670K" in data folder. New path will be ./HAXMLNET/data/Amazon-670K.
<br />
	c. Place the dataset into folder ./HAXMLNET/data/Amazon-670K. 
<br />
	d. Go to folder "./HAXMLNET/data/Amazon-670K" . Create a folder named "original".
<br />
	e. Copy "test_labels.txt" and "train_labels.txt" in original folder.
<br />
	f. Remove all .npy files from "./HAXMLNET/data/Amazon-670K" if any
<br />
	g. Remove "label_binariser" file if any.  
<br />
	h. Run modify_label_G.py.
<br />
	i. "train_labels.txt" and "test_labels.txt" will be produced.
<br />
	h. Create folder named "HAXML_NET_G" inside Amazon-670K folder. and copy above files to this folder.
<br />
	j. Train the model by running "scripts/run_amazon_fast.sh" 
<br />
	k. Post Successfull run do following steps:
<br />
		Create folder AttentionXML/models/HAXMLNet_G_Amazon-670K/ <br>
		Move all the models and .npy file inside it <br>
		Create folder AttentionXML/results/HAXMLNet_G_Amazon-670K/ <br>
		Move all .npy files inside it  <br>
	
<br />
<br />
<br />

2) Configuration for HAXMLNet L Part :
<br />
	a. Keeping all the points explained in above steps from 1 (a) - 1 (g).  
<br />
	b Run modify_label_L.py.
<br />
	i. "train_labels.txt" and "test_labels.txt" will be produced in ./HAXMLNet/data/Amazon-670K.
<br />
	h. Create folder named "HAXML_NET_L" and copy above files to this folder.
<br />
	j. Train the model by running "scripts/run_amazon_fast.sh" 
<br />
	k. Post Successfull run create a backup for reference of below folder:
<br/>
	   	Create folder AttentionXML/models/HAXMLNet_L_Amazon-670K/ <br>
		Move all the models and .npy file inside it <br>
		Create folder AttentionXML/results/HAXMLNet_L_Amazon-670K/ <br>
		Move all .npy files inside it  <br>
<br />
<br />
<br />

3) Combining both parts : 
<br />
	a. Execute ./deepxml/compute_score_HAXML.py
<br />
	b. It produces the labels output in ./results folder named "{dataset}_labels"
<br />
	c. It produces the scores output in ./results folder named "{dataset}_scores"

<br />

4) Evaluating Results : 
<br />
	a. Execute ./deepxml/evaluation_metrics.py. 
<br />
	b. Obtain the Results for different metric like precision and Distributive Cumulative Gain.  
<br />
<br />
---------------------------------------------------------------------------------------


