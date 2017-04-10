import json
import urllib
import urllib2

url = "https://contact.plaid.com/jobs"
values = {
  "name": "Tiju Mathew George",
  "position": "Software Engineer-New Grad",
  "email": "tiju.m.george@gmail.com",
  "resume": "tijugeorge.github.io/CV/Resume.pdf",
  "coverletter": "tijugeorge.github.io/coverletter/CoverLetter.pdf",
  "github": "github.com/tijugeorge",
  "twitter": "@tiju_george",
  "website": "tijugeorge.github.io"
}

req = urllib2.Request(url, json.dumps(values), headers={'Content-type': 'application/json', 'Accept': 'application/json'})
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
