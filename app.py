from flask import Flask, render_template, redirect
from waitress import serve

app = Flask(__name__)

# Define your port mappings here
PORT_MAPPINGS = {
    'app1': 8081,
    'app2': 8082,
    'app3': 8083,
}

# Keep your existing routes here
@app.route('/')
def index():
    return render_template('index.html')  # Or whatever your main page route is

# Add any other existing routes from your MainMenu-80 project here

# Add the new routing functionality
@app.route('/<app_name>')
def redirect_to_app(app_name):
    if app_name in PORT_MAPPINGS:
        return redirect(f"http://localhost:{PORT_MAPPINGS[app_name]}")
    return f"No application named {app_name} found.", 404

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=80)
