from bs4 import BeautifulSoup
import urllib
count = 0
urls_high_priority = []
ids_final = []
urls_covered =[]
urls_low_priority = []
urls_all = []
f = open('C:/Users/Entigence09/Desktop/abc.txt','w')
def func(url):
    try:
        print url
        ur = urllib.urlopen(url)
        soup = BeautifulSoup(ur.read())
        items = soup.findAll('a')
    except:
        return
    for item in items:
        link = item.get('href')
        if link not in urls_all:
            urls_all.append(link)
            decide(link)
    for link in urls_high_priority:
        if link not in urls_covered:
            urls_covered.append(link)
            func("https://vimeo.com"+link)
    for link in urls_low_priority:
        if link not in urls_covered:
            urls_covered.append(link)
            func("https://vimeo.com"+link)
    return

def decide(link):
    try:
        splitted_link = link.split('/')
        if 'help' in splitted_link[1] or 'javascript:' in link:
            return
        if len(splitted_link)>1 and splitted_link[1]!='' and 'www.' not in link:
            if ':' in splitted_link[-1]:
                urls_high_priority.append(link)
                return
            try:
                if 'user' in splitted_link[1] or int(splitted_link[1]) :
                    if splitted_link[1] not in ids_final:
                        ids_final.append(splitted_link[1])
                        f.write(splitted_link[1] +"\n")
                        print '@@@@@@@@@@@@@@@@@  '+str(len(ids_final))+'  @@@@@@@@@@@@@@@@@@@@@@'
                        return
            except:
                urls_low_priority.append(link)
                return
    except:
        return
        
func("https://vimeo.com/") 
        #OR
#func("https://vimeo.com/categories/art/videos/")
