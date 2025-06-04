

def static_routes(app):

    # This is probably only necessary for local instances;
    app.static("/favicon.ico", "src/www/static/favicon.ico", resource_type='file', name="favicon")

    ## Demonstrating static endpoints:
    # app.static("/static1/", "src3/static/static1/", resource_type='dir', name="static1")
      # So this doesn't work; it appears that resource_type='dir' doesn't really do anything;
      # If you want to list the directory, then gotta do, directory_view=True;
      # 'dir' never needs to be set explicitly, according to AI; maybe some legacy stuff; not sure;
      # The only use here is if you want to set resource_type='file' which I do below;
    app.static("/static1/", "src/www/static/static1/index2.html", resource_type='file', name="static1")
      # http://127.0.0.1:8000/static1/
      # This is simlar to index='index.html'; but in this case, index2.html above is the
       # only file that this endpoint can route to; any other file will error;
      # Doing index.html as below gives you more flexibility;
    app.static("/static2/", "src/www/static/static2/", directory_view=True, name="static2")
      # http://127.0.0.1:8000/static2/
      # Creates directory listing with default html styling;
      # apparently there's ways to custome the styling;
    app.static("/static3/", "src/www/static/static3/", index="index.html", name="static3")
      # http://127.0.0.1:8000/static3/
      # http://127.0.0.1:8000/static3/file4.html
      # http://127.0.0.1:8000/static3/index2.html
      # http://127.0.0.1:8000/static3/dir1/readme.html
      # This prints index.html by defeault when you go to /static3/ endpoint;
      # However, unlike the static1 example above, you can also route to any file in the directory;
      # If you don't point to a specific directory, defaults to index.html;

    # // 2025-05-16 Fri 13:37
    # Can't remember where I got the code for doing static directories?
    # Found this:
    # https://sanic.readthedocs.io/en/latest/sanic/api/app.html#sanic.app.Sanic.static
    #


#------------------------------------------

# Alternatives:

# # static_config.py
# STATIC_ROUTES = [
#     {
#         "uri": "/static2/",
#         "file_or_directory": "src/www/static/static2/",
#         "kwargs": {"directory_view": True, "name": "static2"}
#     },
#     {
#         "uri": "/static3/",
#         "file_or_directory": "src/www/static/static3/",
#         "kwargs": {"index": "index.html", "name": "static3"}
#     }
# ]

# # json
# [
#     {
#         "uri": "/static2/",
#         "file_or_directory": "src/www/static/static2/",
#         "kwargs": {"directory_view": true, "name": "static2"}
#     },
#     {
#         "uri": "/static3/",
#         "file_or_directory": "src/www/static/static3/",
#         "kwargs": {"index": "index.html", "name": "static3"}
#     }
# ]


# # Load from Python dict
# from static_config import STATIC_ROUTES
# for route in STATIC_ROUTES:
#     app.static(route["uri"], route["file_or_directory"], **route["kwargs"])

# # Or load from JSON
# import json
# with open("static_routes.json") as f:
#     static_routes = json.load(f)
#     for route in static_routes:
#         app.static(**route)  # Unpack the entire route dict
