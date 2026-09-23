from flask import Flask, render_template, request, redirect, url_for, session, make_response

app = Flask(__name__)

app.secret_key = "biblioteca#123"

usuarios = {
    "carlos": "1111",
    "laura": "2222",
    "diego": "3333"
}
lista_libros = [
    {
        "titulo": "Python desde cero",
        "autor": "Juan Pérez",
        "disponibles": 4
    },

    {
        "titulo": "Desarrollo Web",
        "autor": "María López",
        "disponibles": 2
    },

    {
        "titulo": "Inteligencia Artificial",
        "autor": "Pedro García",
        "disponibles": 0
    }
]

@app.route("/")
def inicio():
    ultimo_usuario = request.cookies.get("ultimo_usuario")
    if ultimo_usuario:
        mensaje = f"Último usuario registrado: {ultimo_usuario}"
    else:
        mensaje = "Bienvenido al Portal de Biblioteca."

    return render_template("index.html",mensaje=mensaje)

@app.route("/login", methods=["GET", "POST"])
def login():
    mensaje = ""
    if request.method == "POST":
        usuario = request.form.get("usuario")
        contraseña = request.form.get("contraseña")
        if usuario in usuarios and usuarios[usuario] == contraseña:
            session["usuario"] = usuario
            respuesta = redirect(url_for("mostrar_libros"))
            respuesta.set_cookie("ultimo_usuario",usuario)
            return respuesta
        else:
            mensaje = "Usuario o contraseña incorrectos."

    return render_template("login.html",mensaje=mensaje)

@app.route("/perfil")
def perfil():
    if "usuario" not in session:
        return redirect(url_for("login"))
    usuario = session["usuario"]

    return render_template("perfil.html",usuario=usuario)

@app.route("/libros")
def mostrar_libros():
    if "usuario" not in session:
        return redirect(url_for("login"))

    return render_template("libros.html",libros=lista_libros)

@app.route("/eliminar_cookie")
def eliminar_cookie():
    respuesta = make_response(redirect(url_for("inicio")))
    respuesta.set_cookie("ultimo_usuario","",expires=0)

    return respuesta


if __name__ == "__main__":
    app.run(debug=True)