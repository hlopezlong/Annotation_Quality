import pandas as pd

#Load data sets

orig = pd.read_csv('random_sample_20k_rows_randomstate33.csv')#random state 33 data
reanno = pd.read_csv('Reannotated_fromState33.csv')

#Adding text ids
otext = orig['comment_text'].values.tolist()
textid = orig['id'].values.tolist()
retext = reanno['text'].values.tolist()

##Finding IDs from  Original file

def find_id(orig, new, ids):
    id_list = []
    for i in new:
        if i in orig:
            id = ids[i]
        else:
            id = noid
    id_list.append(id)
    return id_list

reanno['text_ID'] = find_id(otext,retext,textid)

#Creating binary labels
multi = reanno['mult_lab'].values.tolist()

def bin_label(label_list):
    bin = []
    positive = ['H', 'O', 'I', 'E']
    for i in label_list:
        if i == 'NEI':
            lab = 'NEI'
        elif i in positive:
            lab = 1
        else:
            lab = 0
        bin.append(lab)
    return bin

reanno['binary_lab'] = bin_label(multi)

#Exporting data
reanno.to_csv('reannotated_202303.csv')
