from flask import Flask, render_template, redirect
from waitress import serve
import os

app = Flask(__name__)

# Define your port mappings here
PORT_MAPPINGS = {
    'MainMenu': 8080,
    'BookSearch': 8081,
    'SongSearch': 8082,
    'FilmSearch': 8083,
    'DvlaSearch': 8084,
    'BookStore': 8085
}

# Get the directory of the current script (app.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Go up one level to the parent directory
parent_dir = os.path.dirname(current_dir)

# Define the path for the visitor count file
COUNTER_FILE = os.path.join(parent_dir, 'visitor.txt')

def get_visitor_count():
    if not os.path.exists(COUNTER_FILE):
        return 0
    with open(COUNTER_FILE, 'r') as f:
        return int(f.read() or 0)

def increment_visitor_count():
    count = get_visitor_count() + 1
    with open(COUNTER_FILE, 'w') as f:
        f.write(str(count))
    return count

@app.route('/')
def index():
    visitor_count = increment_visitor_count()
    return render_template('index.html', visitor_count=visitor_count)  # Or whatever your main page route is

# Add any other existing routes from your MainMenu-80 project here

# Add the new routing functionality
@app.route('/<app_name>')
def redirect_to_app(app_name):
    if app_name in PORT_MAPPINGS:
        return redirect(f"http://mywebstuff.co.uk:{PORT_MAPPINGS[app_name]}")
    return f"No application named {app_name} found.", 404

if __name__ == '__main__':
    print("Starting server on http://localhost:8080")
    serve(app, host='0.0.0.0', port=8080)
