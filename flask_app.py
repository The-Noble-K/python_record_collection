from flask import Flask, request, redirect, render_template
import sys
sys.path.insert(1, "PATH TO LOCAL PYTHON PACKAGES")
sys.path.insert(2, "PATH TO FLASK DIRECTORY")

app = Flask(__name__)

@app.route('/')
def sql_database():
    from functions.sqlquery import sql_query
    results = sql_query('''SELECT * FROM record''')
    msg = 'SELECT * FROM record'
    return render_template('sqldatabase.html', results=results, msg=msg)

@app.route('/insert',methods = ['POST', 'GET']) # User Submission

def sql_datainsert():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        artist = request.form['artist']
        title = request.form['title']
        release_year = request.form['release_year']
        sql_edit_insert(''' INSERT INTO record (artist,title,release_year)
        VALUES (?,?,?) ''', (artist,title,release_year))
    results = sql_query('''SELECT * FROM record''')
    msg = 'INSERT INTO record (artist,title,release_year) VALUES
    ('+artist+','+title+','+release_year+')'
    return render_template('sqldatabase.html', results=results, msg=msg)

@app.route('/delete',methods = ['POST', 'GET']) # User Delete

def sql_datadelete():
    from functions.sqlquery import sql_delete, sql_query
    if request.method == 'GET':
        s_artist = request.args.get('s_artist')
        s_title = request.args.get('s_title')
        sql_delete(''' DELETE FROM record WHERE artist = ? and title = ?''',
                (s_artist,s_title))
    results = sql_query(''' SELECT * FROM record''')
    msg = 'DELETE FROM record WHERE artist = ' + s_artist + ' and title = ' +
    s_title
    return render_template('sqldatabase.html', results=results, msg=msg)

@app.route('/query_edit',methods = ['POST', 'GET']) # User Edit

def sql_editlink():
    from functions.sqlquery import sql_query, sql_query2
    if request.method == 'GET':
        e_artist = request.args.get('e_artist')
        e_title = request.args.get('e_artist')
        e_results = sql_query2(''' SELECT * FROM record WHERE artist = ? and
        title = ?''', (e_artist,e_title))
    results = sql_query(''' SELECT * FROM record''')
    return render_template('sqldatabase.html', eresults=eresults,
            results=results)

@app.route('/edit',methods = ['POST', 'GET']) # User Submit Edit

def sql_dataedit():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        old_artist = request.form['old_artist']
        old_title = request.form['old_title']
        sql_edit_insert(''' UPDATE record SET artist = ?, title = ?,
        release_year = ? WHERE artist = ? and title = ? ''',
        (artist,title,old_artist,old_title))
    results = sql_query(''' SELECT * FROM record''')
    msg = 'UPDATE record SET artist = ' + artist + ', ' + title + ', ' +
    release_year + ' WHERE artist = ' + old_artist + ' and title = ' + old_title
    return render_template('sqldatabase.html', results=results, msg=msg)


if __name__ == "__main__":
    app.run(debug=True)

