from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# our index route will handle rendering our form

@app.route('/')
def find_count():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return render_template('index.html')
    # return redirect('/show', str(counter=session['visits']))
@app.route('/clear')
def clear():
    session.clear()	
    return redirect('/')

@app.route('/add')
def add2():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)
