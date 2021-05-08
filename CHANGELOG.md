# CHANGELOG

## v3.0.0 (2021-05-08)

* Updates entire library to be compliant with the new `v2` API (endpoints, HTTP methods, etc)
* The return value of any method is now the `Response` object instead of `json`, now you can retrieve the `status_code` or other details of the response
* Build requests via a `Client` now providing your email and api_key
* Added optional `base_url` and `timeout` options to client
* Module names are now plural
* The Client now checks if an email and api_key is provided and raises an error if not
* Removed `utils` module (pretty print)
* Added unit tests

## v2.2.0 (2021-02-20)

* Adds timeout on HTTP requests 
* Adds try/except block arround HTTP requests
* Changes internal function name from `response` to `_make_http_request`

## v2.1.0 (2021-02-05)

* Changed all classmethods to staticmethods
* Added user-agent to requests (closes #4)
* Linting and formatting changes
* Switched from Pylint to Flake8
* Added GitHub Actions

## v2.0.0 (2020-04-17)

* Updated naming scheme of all classes and functions to match other client libraries (breaking change)

## v1.0.0 (2020-04-04)

* Initial release
* Added all methods for customers, tickets, inventory, and locations
* Added examples and documentation
