# -*- coding: utf-8 -*-
"""GenAI Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xpGu4VuytCA5rjTnG-RYrzukeDYoDBki
"""

!pip install transformers pandas

from google.colab import files
uploaded = files.upload()

import pandas as pd

df = pd.read_csv("resumes.csv")
df.head()

from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")



labels = ["Data Science", "Software Development", "HR"]

predicted_categories = []

for resume in df['ResumeText']:
    result = classifier(resume, candidate_labels=labels)
    predicted_categories.append(result['labels'][0])  # Top predicted label

df['Predicted Category'] = predicted_categories
df.to_csv("resume_classified.csv", index=False)

files.download("resume_classified.csv")