#Configurations blended from https://towardsdatascience.com/how-to-easily-make-beautiful-wordclouds-in-python-55789102f6f5#

from stop_words import get_stop_words

#Insert the additional stop words here#
stop_words = get_stop_words('english')
stop_words.append('MRO')
stop_words.append('Marine')
stop_words.append('Concurs')
stop_words.append('Marines')
stop_words.append('Peer')
stop_words.append('Concur')
stop_words.append('Peers')
stop_words.append('Continue')
stop_words.append('RS')
stop_words.append('Detachment')
stop_words.append('Challenge')
stop_words.append('Sgt')
stop_words.append('Can')
import stylecloud

#Website to choose the design of the cloud https://fontawesome.com/icons?d=gallery&p=2&m=free#


stylecloud.gen_stylecloud(file_path='comments.txt', icon_name= "fas fa-cloud", custom_stopwords=stop_words)
