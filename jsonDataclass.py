from dataclasses import dataclass

from htmlParser import loadWebUntisJson
from urlParser import periods_url,classes_url

@dataclass
class Class:
    id: int
    name: str

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
    room: int

@dataclass
class Timetable:
    school_id: str
    class_id: int
    date: str
    periods: list

#[ Classes ]############################################################################
def getSchoolClasses(school_id,base_domain):
    school_classes = []
    loader = loadWebUntisJson(base_domain,school_id,classes_url(base_domain))
    classes_json = loader['data']['elements']

    for course in classes_json:
        id = course['id']
        name = course['name']
        c = Class(id,name)
        school_classes.append(c)
        
    
    school = SchoolClasses(school_id,school_classes)
    return school


#[ PERIODS ]############################################################################
def getPeriods(base_domain,school_id,class_id,date):
    school_periods = []

    loader = loadWebUntisJson(
        base_domain,
        school_id,
        periods_url(base_domain,date,class_id)
        )
    period_names = loader['data']['result']['data']['elements']
    periods_json = loader['data']['result']['data']['elementPeriods'][class_id]

    for period in periods_json:
        changed = False
        id = period['id']
        name_id = period['elements'][1]
        for name_element in period_names:
            if name_id['id'] == name_element['id'] and name_id['type'] == name_element['type']:
                name = name_element['name']
            if name_id['state'] == "SUBSTITUTED":
                changed = True
        room_id = period['elements'][2]
        for room_element in period_names:
            if room_id['id'] == room_element['id'] and room_id['type'] == room_element['type']:
                room = room_element['name']
            changed = False
            if room_id['state'] == "SUBSTITUTED":
                changed = True
        period_date = period['date']
        start = period['startTime']
        end = period['endTime']
        
        c = Period(id,name,period_date,start,end,changed,room)
        school_periods.append(c)
        
    timetable = Timetable(school_id,class_id,date,school_periods)
    return timetable

def comparePeriod(old_p,new_p):
    return False if old_p == new_p else True    




