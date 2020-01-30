"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get("github")

    first, last, github = hackbright.get_student_by_github(github)

    rows = hackbright.get_grades_by_github(github)

    project = request.args.get("project")

    if project != None:
        return redirect ("/project")
  
    else:
        html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           rows=rows)
    return html

@app.route("/student-search")
def get_student_form():
    # github = request.args.get("github")

    # student = hackbright.get_student_by_github(github)
    # return student

    return render_template("student_search.html")

@app.route("/students-add")
def student_add_stuff():
    return render_template("create_new.html")

@app.route("/student-add", methods=['POST'])
def student_add():

    first = request.form.get('first')
    last = request.form.get('last')
    github = request.form.get('github')

    hackbright.make_new_student(first, last, github)

    return render_template("student_added.html", github=github, first=first, last=last)

@app.route("/project")
def get_project():
    """Show information about a student."""
    title = request.args.get("project")
    project = hackbright.get_project_by_title(title)
    return render_template("project.html", project=project)
    # first, last, github = hackbright.get_student_by_github(github)

    # rows = hackbright.get_grades_by_github(github)
    # print(rows)
    # html = render_template("student_info.html",
    #                        first=first,
    #                        last=last,
    #                        github=github,
    #                        rows=rows)
    # return html


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
