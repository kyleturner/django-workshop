from django.test import TestCase
from django.utils import simplejson

class SimpleTest(TestCase):

    fixtures = ['test_data.json']
    
    def test_teams_exists_in_response(self):
        params = {}
        response = self.client.get('/api/teams/', params, content_type="application/json")
        json = simplejson.loads(response.content)
        
        self.assertTrue('teams' in json, "'teams' key should exist in JSON response.")
        
    def test_two_teams_returned_in_response(self):
        response = self.client.get('/api/teams/', {} , content_type="application/json")
        json = simplejson.loads(response.content)
        teams = json['teams']
        self.assertEquals(2, len(teams), "There should be 2 teams")
        
    