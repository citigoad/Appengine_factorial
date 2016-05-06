#!/usr/bin/env python
import time
import webapp2
from google.appengine.api import memcache
from google.appengine.api import users
def factorial(n):
    n = int(n)
    cfac=memcache.get(str(n))
    if cfac != None:
      return cfac
    if n == 0:
      return 1
    else:
        r= (n * factorial(n-1))
        memcache.set(str(n),r)
        return r 
class MainPage(webapp2.RequestHandler):
  def get(self):
    user=users.get_current_user()
    if user:
      self.response.out.write('<html><h1>Welcome '+user.nickname())
      self.response.out.write('<h1>Factorial of \'n\'</h1>')
      
  
      self.response.out.write('<form method="get">')
      self.response.out.write('<input name="n" type="text">')
      self.response.out.write('<input type="submit" name="submit"></br>')
      if 'f' in self.request.GET.keys():
        memcache.flush_all()
      if 'n' in self.request.GET.keys():
        self.response.out.write(str(factorial(self.request.GET['n'])))
      self.response.out.write('<a href="'+users.create_logout_url('/'))
      self.response.out.write('"style="color: #555; background: #ffc; margin-left: 600px">signout</a>')
      
    else:
      self.response.out.write('<a href="'+users.create_login_url('/'))
      self.response.out.write('">Login</a>')
app = webapp2.WSGIApplication([
  ('/', MainPage)
], debug=True)
