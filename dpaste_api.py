import requests
import re


class dpaste_interface:

    def __init__(self, content, syntax=None, title=None, poster=None,
                 expiry=7):
        self.content = content
        self.syntax = syntax
        self.title = title
        self.poster = poster
        self.expiry = expiry

    def create_headers(self):
        """Creates header for HTTP POST request.

        If any field is None, dpaste API ignores it."""
        headers = {'content': self.content,
                   'syntax': self.syntax,
                   'title': self.title,
                   'poster': self.poster,
                   'expiry': self.expiry}
        return headers

    def get_expiry(self, string):
        """Gets expiration date from passed-in header.

        Should probably find a more graceful regex."""
        r = re.compile(r'expires=.{29}')
        expiry = r.search(string).group().split(sep='=')[1]
        return expiry

    def post(self):
        """Posts to dpaste using requests module, gets the URL and expiration
        back, then returns both as a tuple.

        May edit to have it set variables on the object instead so they can be
        called -- would just need return statement to be deleted.
        """
        url = 'http://dpaste.com/api/v2/'
        headers = self.create_headers()
        p = requests.post(url, data=headers)
        self.paste_url = p.text.strip()
        self.expires = self.get_expiry(p.headers['Set-Cookie'])
        return self.paste_url, self.expires
