from django.shortcuts import render

class Responce:
  def __init__(self, status, message, data):
    self.status = status
    self.message = message
    self.data = data
  
  def fname(arg):
    pass