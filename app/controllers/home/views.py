from . import home


@home.route('/')
def home_page():
	return "Hello World - NEW"