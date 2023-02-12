from flask import Flask, render_template
from main import  app, pages
from lista_textos import txt

@app.route('/')
def go_to_home():
    return render_template(pages['redirect_to_home'])

@app.route('/home')
def home():
    return render_template(pages['homepage'])

@app.route('/home/info/py')
def pyinfo():
    return render_template(pages['pyinfopage'], py = txt['py'])

@app.route('/home/info/js')
def jsinfo():
    return render_template(pages['jsinfopage'], js = txt['js'])

@app.route('/home/info/jv')
def jvinfo():
    return render_template(pages['jvinfopage'], jv = txt['jv'])

@app.route('/home/info/ts')
def tsinfo():
    return render_template(pages['tsinfopage'], ts = txt['ts'])

@app.route('/<wrong_url>')
def error(wrong_url):
    return '<h1>pagina não encontrada</h1> verifique se o URL está correto'

if __name__ == '__main__':
    app.run(debug=True)