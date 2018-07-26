from google.appengine.ext import ndb


class Movie(ndb.Model):
    title = ndb.StringProperty(required=True)
    media_type = ndb.StringProperty(required=True, default="movie")
    runtime = ndb.IntegerProperty(required=False)
    rating = ndb.StringProperty(required=False)





class Person(ndb.Model):
    fname = ndb.StringProperty(required=True)
    lname = ndb.StringProperty(required=False)
    occupation = ndb.StringProperty(required=False)
    age = ndb.IntegerProperty(required=True, default=15)
    skills = [] #THings that are in here are stringProperties
    connections = []

    # def __init__(self, fname, lname, occupation, age):
    #     self.fname = fname
    #     self.lname = lname
    #     self.occupation = occupation
    #     self.age = age

    def addSkill(skill=ndb.StringProperty(required=True)):
        skills.append(skill)


class Company(ndb.Model):
    company_name = ndb.StringProperty(required=True)
    location = ndb.StringProperty(required=False)
    description = ndb.StringProperty(required=True)
    employees = []

    # def __init__(self, name, loc, desc):
    #     self.company_name = name
    #     self.location = loc
    #     self.description = desc

    def addEmployee(emp):
        employees.append(emp)


class College(ndb.Model):
    college_name = ndb.StringProperty(required=True)
    class_size = ndb.IntegerProperty(required=True)
    alumni = [] #this is a list of other Persons
    location = ndb.StringProperty(required=True)
