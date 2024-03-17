import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def analyze_research_papers(papers):
    """
    Analyzes research papers in the project's domain to extract insights, trends, and findings.
    
    Parameters:
    papers (list): List of research paper URLs or file paths.
    
    Returns:
    dict: A dictionary containing the extracted insights, trends, and findings.
    """
    
    # Initialize variables
    insights = []
    trends = []
    findings = []
    
    # Load stopwords and lemmatizer
    nltk.download('stopwords')
    nltk.download('wordnet')
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    
    # Iterate through each paper
    for paper in papers:
        # Retrieve paper content
        if paper.startswith('http'):
            response = requests.get(paper)
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.get_text()
        else:
            with open(paper, 'r') as file:
                content = file.read()
        
        # Tokenize and preprocess text
        tokens = nltk.word_tokenize(content)
        tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens if token.isalpha()]
        filtered_tokens = [token for token in tokens if token not in stop_words]
        
        # Create TF-IDF vectorizer
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(filtered_tokens)
        
        # Perform K-means clustering
        num_clusters = 3
        kmeans = KMeans(n_clusters=num_clusters)
        kmeans.fit(tfidf_matrix)
        
        # Extract insights, trends, and findings
        for i, cluster in enumerate(kmeans.labels_):
            if cluster == 0:
                insights.append(content[tfidf_matrix[:, i].argmax()])
            elif cluster == 1:
                trends.append(content[tfidf_matrix[:, i].argmax()])
            else:
                findings.append(content[tfidf_matrix[:, i].argmax()])
    
    # Return results
    return {
        'insights': insights,
        'trends': trends,
        'findings': findings
    }
