#Configurations blended from https://towardsdatascience.com/how-to-easily-make-beautiful-wordclouds-in-python-55789102f6f5#

#Instructions
#Take your word document and save it as a PDF and place it in the same file as the python script and or alter the path.  Ensure that you change the file name to match your file
#Sometimes it will take multiple times with complex word documents and formatting.

from stop_words import get_stop_words
import stylecloud

#Insert the additional stop words here#
stop_words = get_stop_words('english')
stop_words.append('Officer')
stop_words.append('Marine')
stop_words.append('Corps')
stop_words.append('Marines')
stop_words.append('Can')
stop_words.append('S')
stop_words.append('can')
stop_words.append('Officers')
##stop_words.append('RS')
##stop_words.append('Detachment')
##stop_words.append('Challenge')
##stop_words.append('Sgt')
##stop_words.append('Can')


#Website to choose the design of the cloud https://fontawesome.com/icons?d=gallery&p=2&m=free#

#Can remove palette command below to use default colors.  Chose pallete from https://jiffyclub.github.io/palettable/

#palette='colorbrewer.diverging.RdBu_11'


stylecloud.gen_stylecloud(file_path='Talent.txt', icon_name= "fas fa-cloud", palette='colorbrewer.diverging.RdBu_11', custom_stopwords=stop_words) #Icon name is where you can go to the above website to change the style of the word cloud
