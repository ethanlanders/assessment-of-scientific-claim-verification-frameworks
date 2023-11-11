# Project: An Assessment of Scientific Claim Verification Frameworks

Click [here](https://digitalcommons.odu.edu/cgi/viewcontent.cgi?article=1005&context=reu2022_computerscience) to access the final, published slide deck for this project.

## Introduction
- **Objective:** Automate scientific claim verification in response to the growing spread of scientific disinformation.
- **Key Models:** Evaluated the state-of-the-art model, MultiVerS, trained on the SciFact dataset.
- **Scientific Questions:**
  - How well does the SciFact-trained model detect open-domain scientific disinformation?
  - How does the model perform when trained on other datasets for the same purpose?

## Research Goals
1. **Replicate MultiVerS Results:**
   - Successfully replicated the results of the SciFact leaderboard model, MultiVerS.
2. **Create an Open-Domain Scientific Claims Dataset:**
   - Focused on COVID-19 misinformation.
   - Dataset used for testing the model's generalizability.
   - Labeled to assess the model's ability to verify claim accuracy and identify supporting or conflicting sentences.
3. **Analysis of Results:**
   - Utilized precision, recall, and F1 metrics to evaluate the model's performance on different checkpoints.

## How MultiVerS Works
- **Model Components:**
  - Utilized the Long-former model (Beltagy et al., 2020) for encoding claims and context.
  - Multitasked rationale selection and label prediction using Vert5Erini (Pradeep et al., 2021).
- **Training Datasets:**
  - Employed datasets such as SciFact, COVIDFact, HealthVer, and Fever for training.

## Procedures
1. **New Dataset Creation:**
   - Used claims from Snopes.com.
   - 61 instances, each containing a claim and at least one relevant paper (DOI).
   - Open domain, with 18 true claims, 40 false claims, and 3 mixture claims.
2. **Preprocessing:**
   - Tokenized sentences in paper abstracts using NLTK.
   - Generated compatible files in JSON format.
3. **Labeling:**
   - Double independent labeling (with another undergraduate student: Dominik Soos).
   - Achieved a consensus rate of 75%.

## Evaluation Metrics
- **Precision, Recall, and F1 Scores:**
   - Abst (Abstract) and Sent (Sentence) levels.
   - Assessed accuracy of predicted labels on both levels.

## Results
- **Performance Overview:**
   - All versions of MultiVerS performed poorly in detecting disinformation within the new dataset.
   - Checkpoint trained on CovidFact achieved the best abstract_label_only.
   - Sensitivity to data domains highlighted.
- **Future Work:**
   - Identified areas for improvement, emphasizing the model's current reliance on text semantics without background knowledge and inference.
