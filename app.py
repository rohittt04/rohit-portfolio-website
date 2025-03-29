from flask import Flask, render_template

app = Flask(__name__)

SKILLS = [
    {
        "title": "Python",
        "about": "Experienced in web development and scripting.",
        "exp": "3 years"
    },
    {
        "title": "JavaScript",
        "about": "Proficient in front-end and back-end development.",
        "exp": "2 years"
    },
    {
        "title": "HTML/CSS",
        "about": "Skilled in creating responsive and visually appealing web pages.",
        "exp": "4 years"
    },
    {
        "title": "JAVA",
        "about": "Skilled in creating responsive and visually appealing applications.",
        "exp": "1 years"
    }
]



@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/skill')
def skill():
    return render_template('skill.html', skills = SKILLS )

@app.route('/form')
def form():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

