from dataclasses import dataclass
from htmlParser import loadWebUntisJson
from urlParser import periods_url,classes_url

date = '2022-04-25'
school_id = 'K175055'
school_classes = []

@dataclass
class Class:
    id: int
    name: str
    classteacher: str

@dataclass
class SchoolClasses:
    school: int
    course: list

@dataclass
class Periods:
    id: int
    date: str
    start: int
    end: int

def getSchoolClasses():
    classes_json = loadWebUntisJson(school_id,classes_url())['data']['elements']

    for i,course in enumerate(classes_json):
        id = course['id']
        name = course['name']
        teacher = str(course['classteacher']['name'])
        if teacher is None:
            teacher = 'None'
        c = Class(id,name,teacher)
        school_classes.append(c)
        print(c)





    school = SchoolClasses(school_id,school_classes)
    print(school)

getSchoolClasses()




