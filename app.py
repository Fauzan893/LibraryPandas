from flask import Flask, render_template, send_file
import pandas as pd
import io

app = Flask(__name__)

@app.route("/")
def index():
    # Contoh data (dengan tambahan 2 nama)
    data = {
        "Nama": ["Ali", "Fauzan", "Zan", "Muhammad", "Fatah"],
        "NIM": ["240907500027", "240907500028", "240907500030", "240907500031", "240907500032"],
        "Nilai": [85, 88, 90, 92, 78]
    }
    df = pd.DataFrame(data)

    # Convert DataFrame ke HTML tabel
    table_html = df.to_html(classes='data', index=False)

    return render_template("index.html", table=table_html)

if __name__ == '__main__':
    app.run(debug=True)

