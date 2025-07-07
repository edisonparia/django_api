from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for demo purposes
items = []

@app.route('/items', methods=['GET', 'POST'])
def handle_items():
    if request.method == 'POST':
        data = request.get_json(silent=True) or {}
        name = data.get('name')
        if not name:
            return jsonify({'error': 'name is required'}), 400
        item = {'id': len(items) + 1, 'name': name}
        items.append(item)
        return jsonify(item), 201
    # GET
    return jsonify(items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
