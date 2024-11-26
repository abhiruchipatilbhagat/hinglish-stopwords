# Stopwords Filter

A simple Python library to filter out stopwords from hinglish text. It comes with a predefined list of stopwords and allows users to add custom stopwords.

## Installation

You can install the library using pip:

```bash
pip install hinglish-stopwords
```
Basic Usage
Import and Initialize:
```bash
from hinglish_stopwords.stopwords import StopwordsFilter
```
# Initialize the filter object
```bash
filter = StopwordsFilter()
```
Show Stopwords:
```bash
print(filter.show_stopwords())
```
Filter Text:
```bash
text = "This is an example sentence with stopwords."
filtered_text = filter.filter_text(text)
print(filtered_text)  # Output: "example sentence stopwords."
```
Add Custom Stopwords:
```bash
filter.add_stopwords(["example", "sentence"])
filtered_text = filter.filter_text(text)
print(filtered_text)  # Output: "stopwords."
```
