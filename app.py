from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)

app.secret_key = "biblioteca#123"

usuarios = {
    "carlos": "1111",
    "laura": "2222",
    "diego": "3333"
}
@app.route("/")
def inicio():
    return render_template("base.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    mensaje = ""
    if request.method == "POST":
        usuario = request.form.get("usuario")
        contraseña = request.form.get("contraseña")
        if usuario in usuarios and usuarios[usuario] == contraseña:
            session["usuario"] = usuario
            return redirect(url_for("inicio"))
        else:
            mensaje = "Usuario o contraseña incorrectos."

    return render_template("login.html",mensaje=mensaje)

@app.route("/libros")
def libros():
    if "usuario" not in session:
        return redirect(url_for("login"))

    return "Bienvenido a la biblioteca"

@app.route("/perfil")
def perfil():
    if "usuario" not in session:
        return redirect(url_for("login"))
    usuario = session["usuario"]
    
    return render_template("perfil.html",usuario=usuario)


if __name__ == "__main__":
    app.run(debug=True)