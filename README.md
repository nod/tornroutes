# tornroutes

Provides a route decorator for the Tornado framework.

## Installation

This package is available via pip with `pip install tornroutes` for the stable
version.

You can also install the latest source (also usually very stable) by the following:

    pip install -e git+git://github.com/nod/tornroutes.git#egg=tornroutes

## Testing

Pretty well tested.  You can run them with `nosetests` if you have nose
installed.

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

### Simple `generic_route` example

carried over from above, if you have a template at `generic.html` and you want
it to get rendered at a certain uri, do the following:

```python
generic_route('/generic/?', 'generic.html')
```

### Simple `authed_generic_route` example

This one is slightly more involved but still pretty simple.  Most tornado
projects end up defining something like `BaseHandler` that extends
`tornado.web.RequestHandler` and defines methods necessary for authentication.

At it's simplest, this handler would lool like:

```python
class BaseHandler(RequestHandler):
    def get_current_user(self):
        """ do stuff here to authenticate the user """
        return None # NONE MAY PASS
```

Then, to provide authenticated generic routes:

```python
from tornroutes import authed_generic_route

authed_generic_route('/locked', 'some_locked_template.html', BaseHandler)
```

Now, you'll have a uri being answered with a render of
`some_locked_template.html` if the user is authenticated, otherwise, they get
redirected to `settings.login_url`.


