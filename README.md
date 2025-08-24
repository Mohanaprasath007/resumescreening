# resumescreening
Resume Screening Assistant using  Generative AI

🔹 Project Overview

Recruiters often spend a lot of time screening resumes. This project leverages Zero-Shot Learning to classify resumes into relevant categories such as Data Science, Software Development, or HR, without needing a large labeled training dataset.

By using the facebook/bart-large-mnli model, the system predicts the most suitable category for each resume text, making recruitment faster and smarter.

🔹 Features

Uploads a dataset of resumes (resumes.csv).

Uses HuggingFace Transformers pipeline for zero-shot classification.

Classifies resumes into categories:

Data Science

Software Development

HR

Saves the classified results in resume_classified.csv.

🔹 Tech Stack

Python

HuggingFace Transformers (facebook/bart-large-mnli)

Pandas for data handling

Google Colab for execution
