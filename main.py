""" My notes and work from the book 'Flask Web Development' by Miguel Grinberg (O’Reilly).
                Copyright 2014 Miguel Grinberg, 978-1-449-3726-2. """


# Flask has two main dependencies.
# The routing, debugging, and Web Server Gateway Interface (WSGI) subsystems come from Werkzeug,
# while template support is provided by Jinja2.

# There is no native support in Flask for accessing databases, validating web forms, authenticating users,
# or other high-level tasks. These and many other key services most web applications need
# are available through extensions that integrate with the core packages.

# All Flask applications must create an application instance.
# The web server passes all requests it receives from clients to this object for handling,
# using a protocol called Web Server Gateway Interface (WSGI).
# The application instance is an object of class Flask,

# Routes and View Functions

# Clients such as web browsers send requests to the web server,
# which sends them to the Flask application instance.
# The application instance needs to know what code needs to run for each URL requested,
# so it keeps a mapping of URLs to Python functions.

# The association between a URL and the function that handles it is called a ROUTE.
# The most convenient way to define a route in a Flask application is
# through the app.route decorator exposed by the application instance,
# which registers the decorated function as a route.

# The portion enclosed in angle brackets is the dynamic part.
# Any URLs that match the static portions will be mapped to the route.
# When the view function is invoked, Flask sends the dynamic component as an argument.

# The dynamic components in routes are STRINGS by default but can also be defined with A TYPE.
# For example, route /user/<int:id> would match only URLs that have an integer in the id dynamic segment.

# Flask supports types int, float, and path for routes.
# The path type also represents a string but DOES NOT CONSIDER slashes as separators,
# instead considers them part of the dynamic component.

# Server Startup

# Once the server starts up, it goes into a loop that waits for requests and services them.
# This loop continues until the application is stopped.
# During development, it is convenient to enable debug mode,
# which among other things activates the debugger and the reloader:
# -> pass the argument debug set to True.