import unittest

class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from bottlecap.application import main
        app = main()
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.failUnless('tracer' in res.body)