# scripts/github.py
import requests
from Nebula.models import Project

#name  description url language stargazers_count(stars)
def _get_github_data():
    r = requests.get('https://api.github.com/users/H0R4T1U/repos')
    try:
        r.raise_for_status()
        return r.json()
    except:
        return None

def update_github_data():
    json = _get_github_data()
    if json is not None:
        delete_old_github_data(json)
        for p in json:
            name = p['name']
            description = p['description']
            url = p['html_url']
            language = p['language']
            stars = p['stargazers_count']
            m = Project(name=name,description=description,url=url,language=language,stars=stars)
            projects = Project.objects.all()
            if not projects.filter(name=m.name).exists():
                m.save()
            else:
                Project.objects.filter(name=m.name).update(description=description,url=url,language=language,stars=stars)

def delete_old_github_data(json):

    
    names = list(map(lambda x:x['name'],json)) #array of names from json req
    projects = Project.objects.all()
    for p in projects:
        if p.name not in names:
            Project.objects.filter(name=p.name).delete()
