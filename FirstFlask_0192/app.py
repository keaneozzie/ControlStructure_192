from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    hasil_pesan = None
    nama_input = ""

    if request.method == "POST":
        # Mengambil parameter dari form berdasarkan atribut `name` pada <input>
        nama_input = request.form.get("nama", "").strip()

        if nama_input:
            hasil_pesan = f"Halo, {nama_input}! Data berhasil dikirim menggunakan method POST."
        else:
            hasil_pesan = "Silakan isi nama terlebih dahulu."

    return render_template("index.html", hasil_pesan=hasil_pesan, nama_input=nama_input)


if __name__ == "__main__":
    app.run(debug=True)