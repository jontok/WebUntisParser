def session_starter(base_domain: str,school_id: int) -> str:
   return f'https://{base_domain}/WebUntis/?school={school_id}#/basic/timetable'

def periods_url(base_domain: str,date: str,course_id: int) -> str:
    return f'https://{base_domain}/WebUntis/api/public/timetable/weekly/data?elementType=1&elementId={course_id}&date={date}&formatId=3'

def classes_url(base_domain: str) ->str:
    return f'https://{base_domain}/WebUntis/api/public/timetable/weekly/pageconfig?type=1&isMyTimetableSelected=false'