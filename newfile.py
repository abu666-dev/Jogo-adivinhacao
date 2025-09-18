from flask import Flask, render_template, request
import random

app = Flask(__name__)
numero = random.randint(1, 10)
tentativas = 0  # contador global de tentativas

@app.route("/", methods=["GET", "POST"])
def home():
    global numero, tentativas
    mensagem = ""
    if request.method == "POST":
        try:
            palpite = int(request.form["palpite"])
        except ValueError:
            mensagem = "Digite apenas números!"
            return render_template("index.html", mensagem=mensagem, tentativas=tentativas)

        # Validação do intervalo
        if palpite < 1 or palpite > 10:
            mensagem = "Só pode números de 1 a 10!"
        else:
            tentativas += 1
            if palpite < numero:
                mensagem = "Mais alto!"
            elif palpite > numero:
                mensagem = "Mais baixo!"
            else:
                mensagem = f"Parabéns! Acertou em {tentativas} tentativas!"
                numero = random.randint(1, 10)  # Reinicia o jogo
                tentativas = 0  # zera o contador
    return render_template("index.html", mensagem=mensagem, tentativas=tentativas)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)