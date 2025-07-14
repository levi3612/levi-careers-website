from flask import Flask, render_template

app = Flask(__name__)

SKILLS = [
  {
    'id': 1,
    'title': 'IoT Development',
    'location': 'Remote',
    'salary': 'Php 100,000'
  },
  {
    'id': 2,
    'title': 'Network Engineer',
    'location': 'Polangui',
    'salary': 'Php 150,000'
  },
  {
    'id': 3,
    'title': 'Data Scientist',
    'location': 'Pasig',
    'salary': 'Php 20,000'
  },
  {
    'id': 1,
    'title': 'AI Engineer',
    'location': 'Remote',
    'salary': 'Php 200,000'
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html',
                        skills=SKILLS)

@app.route('/api/skils')
def list_skills():
  jsonify(SKILLS)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')