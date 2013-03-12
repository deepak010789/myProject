from myProject.Premiere.models import VimeoBasicModel
from django.shortcuts import render
from bs4 import BeautifulSoup
import urllib

def home(request):
    return render(request,'index.html',{})

def search(request):
    lines = [line.strip() for line in open('C:/Users/Entigence09/Desktop/abc.txt', 'r')]
    for value in lines:
        print value
        create_user(request, value)
    return render(request,'index.html',{})

def create_user(request, user_id):
    try:
        if 'user' not in user_id:
            ur = urllib.urlopen("http://vimeo.com/api/v2/video/"+user_id+".xml")
            soup = BeautifulSoup(ur.read())
            user_id = soup.find('user_id').string
        
        ur = urllib.urlopen("http://vimeo.com/api/v2/"+user_id+"/info.xml")
        soup = BeautifulSoup(ur.read())
        name = soup.find('display_name').string
        paying = soup.find('is_plus').string
        url = soup.find('profile_url').string
        video = soup.find('total_videos_uploaded').string
        
        objmodel = VimeoBasicModel()
        setattr(objmodel, 'user_id', user_id)
        setattr(objmodel, 'name', name)
        setattr(objmodel, 'url', url)
        setattr(objmodel, 'paying', paying)
        setattr(objmodel, 'staffpicks', False)
        setattr(objmodel, 'video', video)
        
        objmodel.save()
        print '--------------saved---------'
        return
    except:
        return
