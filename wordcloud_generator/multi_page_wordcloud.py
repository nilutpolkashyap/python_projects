# Import packages
import wikipedia
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


wiki1 = wikipedia.page('Robot')# Extract the plain text content of the page
wiki2 = wikipedia.page('Artificial Intelligence')
wiki3 = wikipedia.page('Robotics')
wiki4 = wikipedia.page('Robot Operating System')

text1 = wiki1.content# Clean 
text2 = wiki2.content
text3 = wiki3.content
text4 = wiki4.content

text = text1 + text2 + text3 + text4
text = re.sub(r'==.*?==+', '', text)
text = text.replace('\n', '')


# Define a function to plot word cloud
def plot_cloud(wordcloud):
    plt.figure(figsize=(80, 40))
    plt.imshow(wordcloud) 
    plt.axis("off");
    

wordcloud = WordCloud(width = 4500, height = 2000, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate(text)# Plot
plot_cloud(wordcloud)


wordcloud = WordCloud(width = 5000, height = 2000, random_state=1, background_color='black', colormap='Set2', collocations=False, stopwords = STOPWORDS).generate(text)# Plot
plot_cloud(wordcloud)
