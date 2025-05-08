from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete_task(index):
    try:
        tasks.pop(index)
    except IndexError:
        pass
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
