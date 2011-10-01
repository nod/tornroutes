# tornroutes

Provides a route decorator for the Tornado framework.

## Installation

Just place this directory in your python path or run the following:

    sudo python setup.py install

## Testing

There are tests written.  Run them with nosetests.

## Usage

The best source of information is the comments in tornroutes/__init__.py.

Here's a simple example.

    import tornado.web
    from tornroutes import route

    @route('/blah')
    class SomeHandler(tornado.web.RequestHandler):
        pass

    t = tornado.web.Application(route.get_routes(), {'some app': 'settings'}


