from flask import Flask, render_template, redirect, request, flash

from shorter import Shortener

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

shr = Shortener() 


@app.route('/', methods=('GET', 'POST'))
def hello():
    if request.method == "POST":
        url = request.form['title']

        message = shr.put_code_from_url(url)

        if not url:
            flash('URL is required')
    return render_template('index.html', message=message)

@app.route('/<name>', methods=["GET"])
def url_return(name):
    url = shr.get_url_from_code(name)
    
    if (not url.startswith("http")):
        url = f"https://{url}"
    print(url)
    
    return redirect(url, code=302)
    

if __name__ == "__main__":
    app.run()

    # gq778