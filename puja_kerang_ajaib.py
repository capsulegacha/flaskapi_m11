from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__, template_folder='templates')

# List of default messages for Puja Kerang Ajaib
default_messages = [
    "Jangan dimakan",
    "Lebih baik kamu berdansa saja",
    "Jangan terlalu serius, ini hanya kerang ajaib",
    "Pikirkan lagi, dan bertanyalah",
    "Aku melihat ke dalam masa depanmu",
    "Jawabannya di depanmu, tapi kau tidak melihatnya",
    "Ayo aja gue mah",
    "Mungkin nanti",
    "Coba lagi",
    "Pemujaan berlebihan itu tidak sehat",
    "Tidak",
    "Jangan",
    "Boleh saja",
    "Sebaiknya lakukan tahun depan",
    "Mulailah dari sekarang"
]


# Random message
@app.route('/', methods=['GET'])
def message():
    message = random.choice(default_messages)
    
    return jsonify({'message': message})

# Endpoint for getting a random message
@app.route('/pesan/<name>', methods=['GET'])
def get_kerang(name='name'):
    query_name = request.args.get('name')
    if query_name:
        name = query_name

    message = f"{name}, {random.choice(default_messages)}"
    
    return jsonify({'message': message})

# Endpoint for handling POST requests
@app.route('/welcome/', methods=['POST'])
def post_kerang(name=None):
    name = request.form.get('name')
    if name:
        return f"Selamat datang, {name}, anda berhasil masuk ke Puja Kerang Ajaib"
    else:
        return f"Selamat datang, anda berhasil masuk ke Puja Kerang Ajaib"

# HTML
@app.route("/masuk")
def post_html_kerang():
    return render_template("postkerang.html")

# if __name__ == '__main__':
#     app.run(debug=True)
