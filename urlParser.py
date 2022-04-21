def session_starter(school_id):
   return f'https://hektor.webuntis.com/WebUntis/?school={school_id}#/basic/timetable'

def periods_url(date):
    return f'https://hektor.webuntis.com/WebUntis/api/public/timetable/weekly/data?elementType=1&elementId=2025&date={date}&formatId=3'

def classes_url():
    return f'https://hektor.webuntis.com/WebUntis/api/public/timetable/weekly/pageconfig?type=1&isMyTimetableSelected=false'