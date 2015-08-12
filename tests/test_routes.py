
import os.path
import sys
import unittest

import tornado.web
from tornado.testing import AsyncHTTPTestCase

# make sure we get our local tornroutes before anything else
sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path

from tornroutes import (
    route, route_redirect,
    generic_route, authed_generic_route
    )

# NOTE - right now, the route_redirect function is not tested.


class RouteTests(unittest.TestCase):

    def setUp(self):
        route._routes = [] # reach in and ensure this is clean
        @route('/xyz')
        class XyzFake(object):
            pass

        route_redirect('/redir_elsewhere', '/abc')

        @route('/abc', name='abc')
        class AbcFake(object):
            pass

        route_redirect('/other_redir', '/abc', name='other')


    def test_num_routes(self):
        self.assertTrue( len(route.get_routes()) == 4 ) # 2 routes + 2 redir

    def test_routes_ordering(self):
        # our third handler's url route should be '/abc'
        self.assertTrue( route.get_routes()[2].reverse() == '/abc' )

    def test_routes_name(self):
        # our first handler's url route should be '/xyz'
        t = tornado.web.Application(route.get_routes(), {})
        self.assertTrue( t.reverse_url('abc') )
        self.assertTrue( t.reverse_url('other') )


class ParameterizedRouteTests(AsyncHTTPTestCase):

    def get_app(self):
        return tornado.web.Application(route.get_routes())

    @classmethod
    def setUpClass(cls):
        route._routes = []

        @route(r'/redirect/(?P<param>\w+)', name='param')
        class ParamRedirectHandler(tornado.web.RequestHandler):
            def get(self, param):
                self.redirect(self.reverse_url(param))

        @route('/abc', name='abc')
        class AbcFake(object):
            pass

    def test_param_passed(self):
        response = self.fetch('/redirect/abc', follow_redirects=False)
        assert response.code == 302, "Parameter passed through to handler"


class GenericRouteTests(unittest.TestCase):

    def setUp(self):
        route._routes = [] # clean things out just in case

    def test_generic_routes_default_handler(self):
        generic_route('/something', 'some_template.html')
        assert len(route.get_routes()) == 1


class BogonAuthedHandler(tornado.web.RequestHandler):
    """
    used in testing authed_generic_route(...)
    """
    def get_current_user(self):
        return None


class TestGenericRoute(AsyncHTTPTestCase):

    def get_app(self):
        return tornado.web.Application(
            route.get_routes(),
            template_path = os.path.dirname(__file__),
            login_url = '/faked_for_authed_generic',
            )

    @classmethod
    def setUpClass(cls):
        route._routes = []

        # must be done here prior to get_app being called
        generic_route('/generic', 'generic_1.html')
        generic_route('/other', 'generic_2.html')
        authed_generic_route('/locked', 'generic_1.html', BogonAuthedHandler)

    def test_authed_generic(self):
        response = self.fetch('/locked', follow_redirects=False)
        assert response.code == 302, "Didn't redirect to login page"

    def test_generic_render(self):
        generic_1 = open(
            os.path.join( os.path.dirname(__file__), 'generic_1.html')
            ).read()
        generic_2 = open(
            os.path.join( os.path.dirname(__file__), 'generic_2.html')
            ).read()

        response = self.fetch('/generic')
        assert bytearray(generic_1.strip(), encoding='utf-8') == response.body.strip()
        assert response.code == 200

        response = self.fetch('/other')
        assert bytearray(generic_2.strip(), encoding='utf-8') == response.body.strip()
        assert response.code == 200


