# scripts/github.py
import requests
from Nebula.models import Project

#name  description url language stargazers_count(stars)
def run():
    pass

'''
                                                                ADD TO DATABASE.

    for p in r.json():
        name = p['name']
        description = p['description']
        url = p['html_url']
        language = p['language']
        stars = p['stargazers_count']
        m = Project(name=name,description=description,url=url,language=language,stars=stars)
        projects = Project.objects.all()
        if not projects.filter(name=m.name).exists():
            m.save()
'''
'''
                                                                DELETE FROM DATABASE
    r = requests.get('https://api.github.com/users/H0R4T1U/repos').json()
    names = list(map(lambda x:x['name'],r)) #array of names from json req
    projects = Project.objects.all()
    for p in projects:
        if p.name not in names:
            Project.objects.filter(name=p.name).delete()
'''