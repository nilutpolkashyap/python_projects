import wikipedia
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

wiki = wikipedia.page('Robot')# Extract the plain text content of the page
text = wiki.content# Clean text
text = re.sub(r'==.*?==+', '', text)
text = text.replace('\n', '')

# Define a function to plot word cloud
def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(80, 40))
    plt.imshow(wordcloud) 
    plt.axis("off");
    
wordcloud = WordCloud(width = 4500, height = 2000, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate(text)
plot_cloud(wordcloud)
