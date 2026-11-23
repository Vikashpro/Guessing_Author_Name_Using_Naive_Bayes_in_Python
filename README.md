# Guessing Author Name Using Naive Bayes in Python

An early NLP project exploring **authorship attribution**: can simple stylometric and part-of-speech (POS) features tell two authors apart?

## Data

Ten public-domain texts from [Project Gutenberg](https://www.gutenberg.org/):

- **Author 0:** Carey Rockwell (5 texts)
- **Author 1:** Eleanor Hallowell Abbott (5 texts)

## Features

`pos_tag_finals.py` downloads each text, tokenizes it with NLTK, POS-tags it, and extracts 11 features per text:

| # | Feature | # | Feature |
|---|---|---|---|
| 1 | Total characters | 7 | Verb count |
| 2 | Word count (with punctuation tokens) | 8 | Noun count |
| 3 | Word count (without punctuation) | 9 | Pronoun count |
| 4 | Vocabulary size | 10 | Adjective count |
| 5 | Percentage of punctuation | 11 | Adverb count |
| 6 | Lexical density | | |

The resulting feature matrix is saved in `pos_tag_finals_data.dat` (one row per feature, one column per text).

## Classifier

`naive_bayes_machine_learning_challenge.py` loads the feature matrix, shuffles the instances, trains NLTK's `NaiveBayesClassifier` on 70% of them, tests on the remaining 30%, repeats this three times, and prints the average accuracy and the most informative features.

## Files

| File | Purpose |
|---|---|
| `pos_tag_finals.py` | Downloads texts and extracts the feature matrix |
| `pos_tag_finals_data.dat` | Saved feature matrix (11 features × 10 texts) |
| `naive_bayes_machine_learning_challenge.py` | Trains and evaluates the Naive Bayes classifier |

## How to run

The code is written for **Python 2.7**.

```bash
pip install nltk beautifulsoup4 lxml
python -c "import nltk; nltk.download('averaged_perceptron_tagger')"

python pos_tag_finals.py                          # rebuild the feature matrix (optional)
python naive_bayes_machine_learning_challenge.py  # train and evaluate
```

## Known limitations

This was an early learning project, and a later review found several issues:

- **Evaluation setup:** each training instance is a single feature value from one text, not a full text. Because no exact feature value repeats, the classifier effectively falls back on the class prior, so the reported accuracy does not measure true authorship-attribution performance.
- **Vocabulary bug:** `w.lower` is missing parentheses, so the vocabulary size and lexical-density features are not computed correctly.
- **Data:** one of the ten URLs (`22982-readme.txt`) is a Gutenberg readme file, not a novel.
- **Raw counts:** most features are raw counts, which mainly reflect text length rather than writing style.
- **Small dataset:** ten texts are too few for a reliable accuracy estimate.

## Possible improvements

- Treat each text as one instance with all its features.
- Normalize counts by text length (for example, nouns per word).
- Fix the vocabulary bug and replace the readme file with a novel.
- Use Gaussian Naive Bayes with leave-one-out cross-validation.
- Port the code to Python 3.
