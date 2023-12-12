from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'secreto'


@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/porcesar/result', methods=['POST'])         
def procesar_datos():
    session["datos"] = request.form
    return redirect("/resultado")

@app.route("/resultado")         
def resultados():
    return render_template("resultados.html")


if __name__=="__main__":   
    app.run(debug=True)