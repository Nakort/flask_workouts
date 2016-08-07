from app.test_base import BaseTestCase

class WorkoutsTests(BaseTestCase):

  def tests_successfull_response(self):
      response = self.client.get("/")
      self.assertTrue(response.status == "200 OK")
