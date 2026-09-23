from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)

app.secret_key = "clave_secreta_biblioteca"

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

            return redirect(
                url_for("inicio")
            )


        else:

            mensaje = "Usuario o contraseña incorrectos."


    return render_template(
        "login.html",
        mensaje=mensaje
    )






if __name__ == "__main__":
    app.run(debug=True)