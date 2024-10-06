from transformers import pipeline

# Function to fetch and clean the article
import bs4 as bs
import urllib.request

def fetch_article(url):
    # Scraping the article from the given URL
    scraped_data = urllib.request.urlopen(url)
    article = scraped_data.read()

    # Parsing the article
    parsed_article = bs.BeautifulSoup(article, 'lxml')
    
    # Finding all paragraphs
    paragraphs = parsed_article.find_all('p')
    
    # Combine the paragraphs into a single text
    article_text = ""
    for p in paragraphs:
        article_text += p.text
    
    return article_text

# URL of the article to summarize
url = "https://www.bbc.com/news/world-10621633"

# Fetch the article
article_text = fetch_article(url)

# Initialize the Hugging Face summarization pipeline
summarizer = pipeline("summarization")

# Perform abstractive summarization
summary = summarizer(article_text, max_length=150, min_length=40, do_sample=False)

# Print the summary
print("Summarized Article: \n", summary[0]['summary_text'])
