#%%
#%%
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

html = urllib.request.urlopen('https://www.geeksforgeeks.org/grep-command-in-unixlinux/?ref=leftbar-rightbar').read()
print(text_from_html(html))
    
file = open("text_file.txt", "r")
contents = text_from_html.read()
soup = BeautifulSoup(contents, 'html.parser')
  
f = open("test1.txt", "w")
  
# traverse paragraphs from soup
for data in soup.find_all("p"):
    sum = data.get_text()
    f.writelines(sum)
  
f.close()                           