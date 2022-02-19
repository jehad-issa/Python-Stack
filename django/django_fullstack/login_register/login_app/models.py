from django.db import models
import re


class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors["first_name"] = " first name should be at least 3 characters long"
        if len(postData['last_name']) < 3:
            errors["last_name"] = "last name description should be at least 3 characters long"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):              
            errors['email'] = "Invalid email address!"
        # PASWORD_REGEX = re.compile(r'^[a-zA-Z0-9]$')
        # if not PASWORD_REGEX.match(postData['password']):              
            # errors['password'] = "they should contanning only character and number!"
        if postData['password'] != postData['confirm_pw']:
            errors['matching_pass'] = "the given password do not match"   

        if len(postData['password']) < 8:
            errors["password"] = "password description should be at least 8 characters"   
        if len(postData['confirm_pw']) < 8:
            errors["confirm_pw"] = "password description should be at least 8 characters"     
        return errors

    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):              
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors["password"] = "password description should be at least 8 characters"
        return errors




class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()