from app import app

@app.route('/')
def index():
    return 'Discover Your Trip'
