from flask import Flask, render_template,request,session,redirect, url_for,flash

app = Flask(__name__)
app.secret_key = "unaclavesecreta"

# lista de usuarios y contreseñas correspondientes
credenciales = ({'usuario':'Alvaro','contrasena':'A123'},
            {'usuario':'Elizabeth','contrasena':'E111'})

@app.route("/")
def index():
    if 'login' not in session:
        # Inicializar login como lista
        session['login'] = []

    return render_template('index.html',login = session['login'])

@app.route("/procesa", methods=['GET','POST'])
def procesa():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        contrasena = request.form.get('contrasena')

        if 'login' not in session:
            # inicializar login como lista
            session['login'] = []

        # Verificar credenciales
        for credencial in credenciales:
            if usuario == credencial['usuario'] and contrasena == credencial['contrasena']:
                session['login'].append({'usuario':usuario,'contrasena':contrasena})
                session.modified=True
                return redirect(url_for("bienvenida"))
    flash('Nombre de usuario o contraseña incorrectos')    
    return redirect(url_for("index"))
            
@app.route("/bienvenida")
def bienvenida():
    if 'login' in session:
        return render_template('bienvenida.html', login=session['login'])
    return redirect(url_for("index"))

@app.route('/salir')
def salir():
    session.pop('login', None)
    return redirect(url_for('index'))
    
if __name__ == "__main__":
    app.run(debug = True)
