# tornroutes

Provides a route decorator for the Tornado framework.

## Installation

Just place this directory in your python path or run the following:

	`sudo python setup.py install`

or

	`pip install -e git+git://github.com/nod/tornroutes.git#egg=tornroutes`

## Testing

There are tests written.  Run them with nosetests.

## Usage

The best source of information is the comments in tornroutes/__init__.py.


### Here's a simple example.

    ```python
    import tornado.web
    from tornroutes import route

    @route('/blah')
    class SomeHandler(tornado.web.RequestHandler):
        pass

    t = tornado.web.Application(route.get_routes(), {'some app': 'settings'}
    ```

### Simple generic_route example

carried over from above, if you have a template at `generic.html` and you want
it to get rendered at a certain uri, do the following:

    ```python
    generic_route('/generic/?', 'generic.html')
    ```

