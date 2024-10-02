from flask import Flask, render_template
app = Flask(__name__)
# Sample data - list of dictionaries
books = [
{"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
{"title": "1984", "author": "George Orwell", "year": 1949},
{"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
]
@app.route('/')
def index():
    return render_template('opg2lek6.html', books=books)
if __name__ == '__main__':
        app.run(debug=True)
