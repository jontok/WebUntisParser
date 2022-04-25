from dataclasses import dataclass

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