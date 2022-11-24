from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
# mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'books_project'
mysql = MySQL(app)

# settings
# app.secret_key='mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT 
        bks.name, bks.quality, bk.collection, bk.location 
        FROM book as bk
        join books as bks on bk.books_id=bks.id
        ;
        """)
    books = cur.fetchall()
    cur.close()
    print("ssssssbooks")
    print(books)
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['POST'])
def Add_book():
    if request.method == 'POST':
        name = request.form['name']
        quality = request.form['quality']
        collection = request.form['collection']
        location = request.form['location']
        cur = mysql.connection.cursor()
        
        # insert data into books
        cur.execute(f'INSERT INTO books (name, quality) VALUES ("{name}","{quality}");')
        mysql.connection.commit()
        
        last_book_id_query = "select books.id from books order by id desc limit 1"
        query = f'INSERT INTO book (books_id, name, collection, location)VALUES (({last_book_id_query}),"{name}", "{collection}","{location}");'
        cur.execute(query)
        mysql.connection.commit()
        return redirect(url_for('Index'))



@app.route('/delete')
def Add_delete():
    return 'delete'

@app.route('/edit')
def Add_edit():
    return 'edit'

if __name__ == '__main__':
    app.run(port = 8000, debug = True)