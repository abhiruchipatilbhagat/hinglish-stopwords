from hinglish_stopwords.stopwords import StopwordsFilter

# Create a filter object
filter = StopwordsFilter()

# Show stopwords
print(filter.show_stopwords())

# Filter stopwords from text
text = "This is an example sentence with stopwords."
filtered_text = filter.filter_text(text)
print(filtered_text)
