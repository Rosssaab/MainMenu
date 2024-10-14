from flask import Flask, render_template, redirect
from waitress import serve

app = Flask(__name__)

# Define your port mappings here
PORT_MAPPINGS = {
    'MainMenu': 8080,
    'BookSearch': 8081,
    'SongSearch': 8082,
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
        return redirect(f"http://mywebstuff.co.uk:{PORT_MAPPINGS[app_name]}")
    return f"No application named {app_name} found.", 404

if __name__ == '__main__':
    from waitress import serve
    print("Starting server on http://localhost:8080")
    serve(app, host='0.0.0.0', port=8080)
