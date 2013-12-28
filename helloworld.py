import webapp2
import cgi
import codecs
import logging
import re

form="""
<form method="post">
    <textarea name="text">%(user_input)s</textarea>
	<input type="submit">
</form>
"""
form_user_signup="""
<!DOCTYPE html>

<html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="%(username)s">
          </td>
          <td class="error">
            %(err_username)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="">
          </td>
          <td class="error">
            %(err_pw)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="">
          </td>
          <td class="error">
            %(err_pw_nomatch)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value="">
          </td>
          <td class="error">
            
          </td>
        </tr>
      </table>

      <input type="submit">
    </form>
  </body>

</html>
"""
text = ""
class UserSignupHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(form_user_signup %{"username":"", "email":"", "error_username":"", "error_no_password":"", "error_password_not_match":"", "error_email":""})
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Hello, Udacity!")	
class Rot13Handler(webapp2.RequestHandler):
	
	"""
	def rot13_string(self):
		# This function does not escape html.
		return map(self.rot13_char, self.text)
		
	def rot13_char(self, c):
		if (c >= 'a' and c <= 'z'):
			return ( ( c - 'a' + 13) % 26 ) + 'a'
		elif (c >='A' and c <= 'Z'):
			return ( ( c - 'A' + 13) % 26 ) + 'A'
		else:
			return c
	"""
	def get(self):		
		self.response.out.write(form % {"user_input": cgi.escape ( codecs.encode(text, "rot_13") )})
	
	def post(self):
		text = self.request.get("text")
		text = codecs.encode(text, "rot_13")
		# logging.info ("text = %s"%text)
		self.response.out.write(form % {"user_input": cgi.escape ( text )})
		
application = webapp2.WSGIApplication([
    ('/', MainPage), ('/Rot13', Rot13Handler), ('/UserSignup', UserSignupHandler),
], debug=True)