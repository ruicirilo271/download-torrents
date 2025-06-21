from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://torrent-api-py-nx0x.onrender.com/api/v1/all/search"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Falta o parâmetro de pesquisa'}), 400
    try:
        response = requests.get(API_URL, params={'query': query}, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        data = response.json()
        return jsonify(data.get('data', []))
    except Exception as e:
        print("Erro:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

