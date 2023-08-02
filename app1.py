# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uw4ZureCS3PZB-pH-xdXh4Issim0w4Bu
"""
!pip install transformers
import streamlit as st
import numpy as np
from transformers import BertTokenizer, BertForSequenceClassification
import torch

st.cache(allow_output_mutation=True)
def get_model():
  tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
  model = BertForSequenceClassification.from_pretrained('Alexcool123/nlp_trained_model')
  return tokenizer, model

tokenizer,model = get_model()

user_input = st.text_area('Print your text for sentiment analysis')
button = st.button('Analyse!')

d = {0: 'Extremely negative',
     1: 'Negative',
     2: 'Neutral',
     3: 'Positive',
     4: 'Extremely positive'

}

if user_input and button:
  test_sample = tokenizer([user_input],padding = True, truncation = True, max_length = 512 , return_tensors = 'pt')
  output = model(**test_sample)
  st.write('Logits:', output.logits)
  y_pred = np.argmax(output.logits.detach().numpy(),axis=1)
  st.write('Prediction: ', d[y_pred[0]])

