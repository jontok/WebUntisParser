# WebUntisParser
HTML Parser for WebUntis Timetables This is an Flask API which provides a JSON output from any open WebUntis Timetable.


## Dependencies
```
pip install Flask
pip intstall flask-cors
pip install requests-html
```

## How To Run
Clone The repo and change your directory in to it. `cd WebUnitisParser`

Install all dependencies and export FLASK env Variable `export FLASK_APP=serve` then run `flask run`

## Usage
GO to your WebUntis timetable and copy the following parts:

Variable | Explenation
--- | ---
base_domain | `<something>.webuntis.com` 
school_id | `WebUntis/?school=<school_id>#/`<br>copy only the school id

### Classes
Get all the Classes of your School.

```
https://localhost:5000/periods/<base_domain>/<school_id>
```

### Timetable

```
https://localhost:5000/periods/<base_domain>/<school_id>/<class_id>/<date>
```