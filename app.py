from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/publications')
def publications():
    return render_template('publications.html')

@app.route('/awards')
def awards():
    return render_template('awards.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/membership')
def membership():
    return render_template('membership.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/presentations')
def presentations():
    return render_template('presentations.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
