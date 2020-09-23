from app import app

# @app.route('/<name>')
# def greet(name):
    # return f"Hello {name}!"
@app.route('/')
def index():
    return "Now Paul has access to the internet.  The CodeClan instructors knew what they were doing but did they TRULY understand what they had done?..."