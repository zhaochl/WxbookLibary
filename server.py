#!/usr/bin/env python
# coding=utf-8
#!/usr/bin/env python
# coding=utf-8
import time
from hashlib import md5
from datetime import datetime
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash, _app_ctx_stack
#
# from werkzeug import check_password_hash, generate_password_hash
import time
from book_dao import *
import sys
from pdb import *

reload(sys)
sys.setdefaultencoding('utf8')

SECRET_KEY = 'development key'
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


# 添加简单的安全性检查
def manager_judge():
    if not session['user_id']:
        error = 'Invalid admin, please login'
        return render_template('manager_login.html', error=error)


def reader_judge():
    if not session['user_id']:
        error = 'Invalid reader, please login'
        return render_template('reader_login.html', error=error)


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = session['user_id']


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user_name = request.form['username']
        password = request.form['password']

        user = query_user(user_name, password)
        if len(user) > 0:
            session['user_id'] = user_name
            if user['role'] == 1:
                return redirect(url_for('manager'))
            else:
                return redirect(url_for('reader'))
        else:
            error = '用户名或者密码错误'
            return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        if not request.form['username']:
            error = 'You have to enter a username'
        elif not request.form['password']:
            error = 'You have to enter a password'
        elif request.form['password'] != request.form['password2']:
            error = 'The two passwords do not match'
        elif check_username(request.form['username']) is not None:
            error = 'The username is already taken'
        else:
            sql = """insert into users (user_name, password, college, num, email,role) values ('{}', '{}', '{}', '{}', '{}',1)""".format(
                request.form['username'], request.form['password'], request.form['college'],
                request.form['number'], request.form['email'])
            print 'sql:', sql
            db_update(sql)
            # add_user(request)
            return redirect(url_for('login'))
    return render_template('register.html', error=error)


@app.route('/logout')
def logout():
    session.pop('user_name', None)
    return redirect(url_for('index'))


@app.route('/manager')
def manager():
    return render_template('manager.html')


@app.route('/reader')
def reader():
    return render_template('reader.html')


@app.route('/manager/books')
def manager_books():
    columns, books = convert_results('select * from books')
    #print books
    return render_template('manager_books.html', books=books)


@app.route('/manager/books/add', methods=['GET', 'POST'])
def manager_books_add():
    manager_judge()
    error = None
    if request.method == 'POST':
        if not request.form['id']:
            error = 'You have to input the book ISBN'
        elif not request.form['name']:
            error = 'You have to input the book name'

        # elif not request.form['author']:
        #    error = 'You have to input the book author'
        # elif not request.form['company']:
        #    error = 'You have to input the publish company'
        # elif not request.form['date']:
        #    error = 'You have to input the publish date'

        else:
            db_update('''
            insert into books (book_id, book_name, author, publish_com,
                publish_date,book_num) values ('{}', '{}', '{}', '{}', '{}','{}') '''
                      .format(request.form['id'], request.form['name'], request.form['author'], request.form['company'],
                              request.form['date'],request.form['book_num']))

            return redirect(url_for('manager_books'))
    return render_template('manager_books_add.html', error=error)



@app.route('/manager/modify/<id>', methods=['GET', 'POST'])
def manager_modify(id):
    manager_judge()
    #set_trace()
    error = None
    sql="select * from books where book_id = %s"%(id)
    print sql
    c,books = convert_results(sql)
    book =books[0]
    if request.method == 'POST':
        if not request.form['name']:
			error = 'You have to input the book name'
        elif not request.form['author']:
			error = 'You have to input the book author'
        elif not request.form['company']:
			error = 'You have to input the publish company'
        elif not request.form['date']:
			error = 'You have to input the publish date'
        else:
            sql="""
            update books set book_name='{}', 
            author='{}', 
            publish_com='{}', 
            publish_date='{}', 
            `status`='{}',
            `book_num`='{}'
            where book_id='{}' 
            """.format(request.form['name'], request.form['author'], request.form['company'], request.form['date'],request.form['status'],request.form['book_num'], id)


            
            print sql
            db_update(sql)
            
            return redirect(url_for('manager_book', id = id))
	        
    return render_template('manager_modify.html', book = book, error = error)

@app.route('/manager/borrows')
def manager_borrows():
    sql="""
    select bo.id, bk.book_id,bk.book_name,bk.author,bk.`publish_com`,bk.`publish_date`,bo.`date_borrow`,bo.`date_return` from  borrows bo, users u,books bk
        where bo.`openid` =  u.openid
        and bo.`book_id` = bk.`book_id`
        and bo.type=1
        
        and bo.status=0
    """
    columns, books = convert_results(sql)
    return render_template('manager_borrows.html', books=books)


@app.route('/manager/borrow/<id>', methods=['GET', 'POST'])
def manager_borrow(id):
    manager_judge()
    error = None
    if request.method == 'GET':
        sql="""update borrows set status=1 where id= '{}'""".format(id)
        print sql
        db_update(sql)
        sql_book = """select book_id from borrows where id={}""".format(id)
        columns, books = convert_results(sql_book)
        book = books[0]
        book_id = book['book_id']
        update_book_info(book_id,"add")
        return redirect(url_for('manager_borrows'))

@app.route('/manager/books/delete', methods=['GET', 'POST'])
def manager_books_delete():
    manager_judge()
    error = None
    if request.method == 'GET':
        if not request.args.get('id'):
            error = 'You have to input the book name'
        else:
            db_update('''delete from books where book_id=%s''' % (request.args.get('id')))
            return redirect(url_for('manager_books'))
    return render_template('manager_books_delete.html', error=error)


@app.route('/manager/book/<id>', methods=['GET', 'POST'])
def manager_book(id):
    manager_judge()
    c,books = convert_results('''select * from books where book_id = {}'''.format(id))
    print books
    book = books[0]
    #readers,c = convert_results('''select * from borrows where book_id = {}'''.format(id))
    #reader = readers[0]
    #names,c = convert_results('''select user_id from borrows where book_id = {}'''.format(id))
    #name = names[0]
    
    #current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    #if request.method == 'POST':
    #    sql='''update histroys set status = %s, date_return = %s  where book_id=%s and user_name=%s and status=%s '''%('retruned', current_time, id, name[0], 'not return')
        
    #    sql='''delete from borrows where book_id = %s '''% (id)
    #    return redirect(url_for('manager_book', id=id))
    return render_template('manager_book.html', book=book)


@app.route('/manager/users')
def manager_users():
    manager_judge()
    c, users = convert_results('''select * from users where role=0''')
    return render_template('manager_users.html', users=users)


@app.route('/manager/user/<id>', methods=['GET', 'POST'])
def manager_user(id):
    manager_judge()
    c,user = convert_results('''select * from users where user_id = {}'''.format(id))
    books = None
    return render_template('manager_userinfo.html', user=user[0], books=books)


@app.route('/manager/user/modify/<id>', methods=['GET', 'POST'])
def manger_user_modify(id):
    manager_judge()
    error = None
    user = get_user_info_by_user_id(id)
    print 'user:',user
    if request.method == 'POST':
        if not request.form['username']:
            error = 'You have to input your name'
        elif not request.form['password']:
            sql='''update users set user_name={}, college={}, num={} , email={},role={} where user_id={} '''.format(request.form['username'],request.form['college'], request.form['number'],request.form['email'],request.form['role'],id)
            print sql
            db_update(sql) 
            return redirect(url_for('manager_user', id=id))
        else:
            sql = '''update users set user_name={}, pwd={}, college={}, num={} , email={},role={} where user_id={} '''.format(request.form['username'],request.form['password'],request.form['college'], request.form['number'],request.form['mail'],request.form['role'], id)
            print sql
            db_update(sql) 
            return redirect(url_for('manager_user', id=id))
    return render_template('manager_user_modify.html', user=user, error=error)


@app.route('/manager/user/deleter/<id>', methods=['GET', 'POST'])
def manger_user_delete(id):
    manager_judge()
    db = get_db()
    db.execute('''delete from users where user_id=? ''', [id])
    db.commit()
    return redirect(url_for('manager_users'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)
    # app.run(debug=True)

