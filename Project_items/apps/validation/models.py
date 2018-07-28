from __future__ import unicode_literals

from django.db import models
from datetime import date
import datetime
import bcrypt
import re

# Create your models here.
class UserAction(models.Manager):
    def newUser(self, POST_data):
        NAME_REGEX = re.compile(r'^[a-zA-Z]{3,}$')
        USERNAME_REGEX = re.compile(r'^[a-zA-Z]{3,}$')
        DATE_REGEX = re.compile(r'^[0-9]{2}/[0-9]{2}/[0-9]{4}')
        PW_REGEX = re.compile(r'^.{8,}$')
        message = []
        if self.filter(username=POST_data['username']):
            message.append(' Account already exist')
        if not NAME_REGEX.match(POST_data['first_name']):
            message.append(' Name should be atleast three characters and letters only')
        if not USERNAME_REGEX.match(POST_data['username']):
            message.append(' Invalid username')
        if not DATE_REGEX.match(POST_data['date_hired']):
            message.append('Please verify the date format entered (must be mm/dd/yyyy)')
        else:
            hired = POST_data['date_hired'].split('/')
            try:
                dateHired = datetime.date(int(hired[2]),int(hired[0]),int(hired[1]))
            except ValueError:
                message.append('Date entered is not a valid one ')
            else:
                if not dateHired <= datetime.datetime.today().date():
                    message.append(' Date hired should be in the past')
        if not PW_REGEX.match(POST_data['pw']):
            message.append('Password must be 8 or more charaters')
        if not POST_data['pw'] == POST_data['pwConf']:
            message.append(' Passwords do not match')
        if message:
            return message, False
        else:
            hash = bcrypt.hashpw(POST_data['pw'].encode(), bcrypt.gensalt())
            newUser = self.create(first_name=POST_data['first_name'], username=POST_data['username'], hire_date=dateHired, password=hash)
            return newUser, True
    def validateUser(self, POST_data):
        message = []
        if POST_data['username']:
            username = POST_data['username']
            checkUser = self.filter(username=username)
            if not checkUser:
                message.append(' User account not present')
                return message, False
            elif bcrypt.hashpw(POST_data['pw'].encode(), checkUser[0].password.encode()) == checkUser[0].password:
                    return checkUser[0], True
            else:
                message.append(' Incorrect password')
                return message, False
        else:
            message.append(' Please enter username')
            return message, False
class User(models.Model):
    first_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    hire_date = models.DateField(blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = UserAction()