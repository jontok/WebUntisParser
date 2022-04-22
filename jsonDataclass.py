from cgitb import enable
from dataclasses import dataclass

from htmlParser import loadWebUntisJson
from urlParser import periods_url,classes_url

my_date = '2022-04-25'
my_school_id = 'K175055'
#2025
course_id = '1646'
school_classes = []
school_periods = []

@dataclass
class Class:
    id: int
    name: str
    # classteacher: str

@dataclass
class SchoolClasses:
    school: int
    course: list

@dataclass
class Period:
    id: int
    name: str
    date: int
    start: int
    end: int
    changed: bool

#[ Classes ]############################################################################
def getSchoolClasses(school_id,base_domain):
    loader = loadWebUntisJson(base_domain,school_id,classes_url(base_domain))
    classes_json = loader['data']['elements']

    for course in classes_json:
        id = course['id']
        name = course['name']
        # teacher = str(course['classteacher']['name'])
        # if teacher is None:
        #     teacher = 'None'
        c = Class(id,name)
        school_classes.append(c)
        
    
    school = SchoolClasses(school_id,school_classes)
    return school


#[ PERIODS ]############################################################################
def getPeriods(base_domain,school_id,class_id,date):
    loader = loadWebUntisJson(
        base_domain,
        school_id,
        periods_url(base_domain,date,class_id)
        )
    period_names = loader['data']['result']['data']['elements']
    periods_json = loader['data']['result']['data']['elementPeriods'][class_id]
    # print(periods_json)

    for period in periods_json:
        id = period['id']
        name_id = period['elements'][1]
        for name_element in period_names:
            if name_id['id'] == name_element['id'] and name_id['type'] == name_element['type']:
                name = name_element['name']
        period_date = period['date']
        start = period['startTime']
        end = period['endTime']
        changed = False
        c = Period(id,name,period_date,start,end,changed)

        c.changed = comparePeriod(c,school_periods)
        school_periods.append(c)
        # print(school_periods)
    
    return school_periods

def comparePeriod(old_p,new_p):
    return False if old_p == new_p else True    

# getSchoolClasses()
# getPeriods()



