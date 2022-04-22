# domain = "https://kephiso.webuntis.com/WebUntis/?school=GWS+Villingen#/basic/timetable"

# domain

# base_domain1 = "kephiso.webuntis.com"
# base_domain = "hektor.webuntis.com"
def session_starter(base_domain,school_id):
   return f'https://{base_domain}/WebUntis/?school={school_id}#/basic/timetable'

def periods_url(base_domain,date,course_id):
    return f'https://{base_domain}/WebUntis/api/public/timetable/weekly/data?elementType=1&elementId={course_id}&date={date}&formatId=3'

def classes_url(base_domain):
    return f'https://{base_domain}/WebUntis/api/public/timetable/weekly/pageconfig?type=1&isMyTimetableSelected=false'