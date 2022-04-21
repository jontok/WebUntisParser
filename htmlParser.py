import requests
import json
from urlParser import session_starter



from requests_html import HTMLSession

def loadWebUntisJson(school,urlparser):
    school_id = school
    try:
        session = HTMLSession()
        session.get(session_starter(school_id))
        response_api_classes = session.get(urlparser)
        json_data =  json.loads(response_api_classes.html.text)
        return json_data

    except requests.exceptions.RequestException as e:
        return e

    

