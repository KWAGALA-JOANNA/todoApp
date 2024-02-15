from flask import Flask, render_template, request, redirect, url_for

tasks =[]


#app instance from the flask class

app = Flask(__name__, template_folder=('templates'))


@app.route("/")
def home():
    # whenever we create new tasks fromthe back nd we have to render them on the user interface by passing the variable
# within the render template

    return render_template('index.html', tasks=tasks)
@app.route('/add' , methods=['POST', 'GET'])
# when creating new content we use the post method behind the scenes
def create_new_task():
    task = request.form.get('task')
    tasks.append(task)
    return redirect(url_for('home'))

# # creating the update
@app.route("/update/<int:index>", methods=['POST', 'GET'])
def update_task(index):
    if request.method == 'POST':
        new_task = request.form.get('task')
        tasks[index] = new_task
        return redirect(url_for('home'))
    else:
        return render_template('update.html', index=index, task=tasks[index])
    

# working with a method that enables us to delete a particular task from the UI
@app.route('/delete/<int:index>')
def delete_task(index):
    # checking whether its within the range of the task lists
    if 0<= index < len(tasks):
        del tasks[index]
    return redirect(url_for('home'))

    


if __name__ ==' __main__':
    app.run(debug=True)
    




