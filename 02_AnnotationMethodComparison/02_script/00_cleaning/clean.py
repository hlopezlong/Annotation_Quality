import pandas as pd
import re


# def read_data(dataframe):
#     df = pd.read_csv(dataframe)
#     text = df['text'].values.tolist()
#     aID = df['annotator_ID'].values.tolist()
#     ver = df['version'].values.tolist()
#     agroup = df['annotator_grp'].values.tolist()
#     tID = df['textID'].values.tolist()
#     mlab = df['mult_lab'].values.tolist()
#     slab = df['second_lab'].values.tolist()
#     bin_lab = df['binary_lab'].values.tolist()
#     target = df['target'].values.tolist()
#     return text, aID, ver, agroup, tID, mlab,slab,bin_lab,target

df = pd.read_csv('~/Annotation_Quality/02_AnnotationMethodComparison/01_data/Reannotated_fromState33.csv')

text = df['text'].values.tolist()

def clean(text):
    cleaned_text= []
    for i in text:
        txt = i.strip()
        txt = re.sub(r'http.+', '', txt) #remove urls
        txt = re.sub(r'@.+', '@tag', txt) #replace all @tags with '@tag'
        cleaned_text.append(txt)
    return cleaned_text

df['clean_txt'] = clean(text)

df.to_csv('cleaned_flat1.csv', index=False)
