from app import app

@app.route('/')
def index():
    return 'Discover Your Trip'

@app.before_request
def before_request():
    pass
