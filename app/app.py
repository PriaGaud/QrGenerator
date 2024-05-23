from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample menu data
menu = [
    {'id': 1, 'name': 'Burger', 'price': 10},
    {'id': 2, 'name': 'Pizza', 'price': 12},
    {'id': 3, 'name': 'Salad', 'price': 8}
]

@app.route('/')
def index():
    return render_template('index.html', menu=menu)

@app.route('/order', methods=['POST'])
def order():
    if request.method == 'POST':
        item_id = int(request.form['item_id'])
        # Process order, e.g., save to database
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
