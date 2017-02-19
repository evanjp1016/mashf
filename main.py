#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import logging
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET")
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render())


class ExhibitsHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET")
        template = JINJA_ENVIRONMENT.get_template('templates/exhibits.html')
        self.response.write(template.render())


class HistoryHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET")
        template = JINJA_ENVIRONMENT.get_template('templates/history.html')
        self.response.write(template.render())

class InducteesHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET")
        template = JINJA_ENVIRONMENT.get_template('templates/inductees.html')
        self.response.write(template.render())

class Inductees1987Handler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET")
        template = JINJA_ENVIRONMENT.get_template('templates/inductees-1987.html')
        self.response.write(template.render())

class Inductees1988Handler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET")
        template = JINJA_ENVIRONMENT.get_template('templates/inductees-1988.html')
        self.response.write(template.render())

class Inductees1989Handler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET")
        template = JINJA_ENVIRONMENT.get_template('templates/inductees-1989.html')
        self.response.write(template.render())

class Inductees1990Handler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET")
        template = JINJA_ENVIRONMENT.get_template('templates/inductees-1990.html')
        self.response.write(template.render())

class DistiguishedServiceHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET")
        template = JINJA_ENVIRONMENT.get_template('templates/distinguished-service.html')
        self.response.write(template.render())

class ScholarAthleteHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET")
        template = JINJA_ENVIRONMENT.get_template('templates/scholar-athlete.html')
        self.response.write(template.render())

class CeremonyHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET")
        template = JINJA_ENVIRONMENT.get_template('templates/ceremony.html')
        self.response.write(template.render())

class NewsHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET")
        template = JINJA_ENVIRONMENT.get_template('templates/news.html')
        self.response.write(template.render())        

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/home', MainHandler),
    ('/exhibits', ExhibitsHandler),
    ('/history', HistoryHandler),
    ('/inductees', InducteesHandler),
    ('/inductees-1987', Inductees1987Handler),
    ('/inductees-1988', Inductees1988Handler),
    ('/inductees-1989', Inductees1989Handler),
    ('/inductees-1990', Inductees1990Handler),
    ('/distinguished-service', DistiguishedServiceHandler),
    ('/scholar-athlete', ScholarAthleteHandler),
    ('/ceremony', CeremonyHandler),
    ('/news', NewsHandler)
], debug=True)