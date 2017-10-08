import pickle
from collections import Counter
from wordcloud.wordcloud import WordCloud
from parser import split_individual

def make_cloud():
    print("Generating word cloud...")
    authors,dates,contents,bigstring = split_individual("archive.pkl")
    def rainbow_color_func(word, font_size, position, orientation, random_state=None,
                        **kwargs):
        
        return "hsl(hue,100%,50%)".replace("hue",str(int(position[1] / 1000 * 360)))
    
    wc=WordCloud(width=2000,height=2000,color_func=rainbow_color_func,stopwords=None,collocations=False)
    wc.generate(bigstring)
    wc.to_file("wordcloud-rainbow.png")
    wc=WordCloud(width=2000,height=2000,stopwords=None)
    wc.generate(bigstring)
    wc.to_file("wordcloud-standard.png")
    
    
    wc.generate_from_frequencies(Counter(authors))
    wc.to_file("wordcloud-rainbow-authors.png")
    wc=WordCloud(width=2000,height=2000,stopwords=None)
    wc.generate_from_frequencies(Counter(authors))
    wc.to_file("wordcloud-standard-authors.png")