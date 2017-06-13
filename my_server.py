

@app.route('/manager/users')
def manager_users():
	manager_judge()
	users = query_db('''select * from users''', [])
	return render_template('manager_users.html', users = users)

@app.route('/manager/user/modify/<id>', methods=['GET', 'POST'])
def manger_user_modify(id):
	user_judge()
	error = None
	user = query_db('''select * from users where user_id = ?''', [id], one=True)
	if request.method == 'POST':
		if not request.form['username']:
			error = 'You have to input your name'
		elif not request.form['password']:
			db = get_db()
			db.execute('''update users set user_name=?, college=?, num=? \
				, email=? where user_id=? ''', [request.form['username'],
				request.form['college'], request.form['number'],
				request.form['email'], id])
			db.commit()
			return redirect(url_for('manager_user', id = id))
		else:
			db = get_db()
			db.execute('''update users set user_name=?, pwd=?, college=?, num=? \
				, email=? where user_id=? ''', [request.form['username'],
					generate_password_hash(request.form['password']),
				request.form['college'], request.form['number'],
				request.form['email'], id])
			db.commit()
			return redirect(url_for('manager_user', id = id))
	return render_template('manager_user_modify.html', user=user, error = error)

@app.route('/manager/user/deleter/<id>', methods=['GET', 'POST'])
def manger_user_delete(id):
	manager_judge()
	db = get_db()
	db.execute('''delete from users where user_id=? ''', [id])
	db.commit()
	return redirect(url_for('manager_users'))

@app.route('/manager/user/<id>', methods=['GET', 'POST'])
def manager_user(id):
	manager_judge()
	user = query_db('''select * from users where user_id = ?''', [id], one=True)
	books = None
	return render_template('manager_userinfo.html', user = user, books = books)


@app.route('/manager/modify/<id>', methods=['GET', 'POST'])
def manager_modify(id):
	manager_judge()
	error = None
	book = query_db('''select * from books where book_id = ?''', [id], one=True)
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
			db = get_db()
			db.execute('''update books set book_name=?, author=?, publish_com=?, publish_date=? where book_id=? ''', [request.form['name'], request.form['author'], request.form['company'], request.form['date'], id])
			db.commit()
			return redirect(url_for('manager_book', id = id))
	return render_template('manager_modify.html', book = book, error = error)

@app.route('/reader/info', methods=['GET', 'POST'])
def reader_info():
	reader_judge()
	user = query_db('''select * from users where user_name=? ''', [g.user], one = True)
	return render_template('reader_info.html', user = user)


@app.route('/reader/modify', methods=['GET', 'POST'])
def reader_modify():
	reader_judge()
	error = None
	user = query_db('''select * from users where user_name = ?''', [g.user], one=True)
	id = user[0]
	if request.method == 'POST':
		if not request.form['username']:
			error = 'You have to input your name'
		elif not request.form['password']:
			db = get_db()
			db.execute('''update users set user_name=?, college=?, num=? \
				, email=? where user_id=? ''', [request.form['username'],
				request.form['college'], request.form['number'],
				request.form['email'], id])
			db.commit()
			return redirect(url_for('reader_info'))
		else:
			db = get_db()
			db.execute('''update users set user_name=?, pwd=?, college=?, num=? \
				, email=? where user_id=? ''', [request.form['username'],
					generate_password_hash(request.form['password']),
				request.form['college'], request.form['number'],
				request.form['email'], id])
			db.commit()
			return redirect(url_for('reader_info'))
	return render_template('reader_modify.html', user=user, error = error)



@app.route('/reader/query', methods=['GET', 'POST'])
def reader_query():
	reader_judge()
	error = None
	books = None
	if request.method == 'POST':
		if request.form['item'] == 'name':
			if not request.form['query']:
				error = 'You have to input the book name'
			else:
				books = query_db('''select * from books where book_name = ?''',
						[request.form['query']])
				if not books:
					error = 'Invalid book name'
		else:
			if not request.form['query']:
				error = 'You have to input the book author'
			else:
				books = query_db('''select * from books where author = ?''',
						[request.form['query']])
				if not books:
					error = 'Invalid book author'
	return render_template('reader_query.html', books = books, error = error)

@app.route('/reader/book/<id>', methods=['GET', 'POST'])
def reader_book(id):
	reader_judge()
	error = None
	book = query_db('''select * from books where book_id = ?''', [id], one=True)
	reader = query_db('''select * from borrows where book_id = ?''', [id], one=True)
	count  = query_db('''select count(book_id) from borrows where user_name = ? ''',
			  [g.user], one = True)

	current_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	return_time = time.strftime('%Y-%m-%d',time.localtime(time.time() + 2600000))
	if request.method == 'POST':
		if reader:
			error = 'The book has already borrowed.'
		else:
			if count[0] == 3:
				error = 'You can\'t borrow more than three books.'
			else:
				db = get_db()
				db.execute('''insert into borrows (user_name, book_id, date_borrow, \
					date_return) values (?, ?, ?, ?) ''', [g.user, id,
										   current_time, return_time])
				db.execute('''insert into histroys (user_name, book_id, date_borrow, \
					status) values (?, ?, ?, ?) ''', [g.user, id,
										   current_time, 'not return'])
				db.commit()
				return redirect(url_for('reader_book', id = id))
	   	return render_template('reader_book.html', book = book, reader = reader, error = error)

@app.route('/reader/histroy', methods=['GET', 'POST'])
def reader_histroy():
	reader_judge()
	histroys = query_db('''select * from histroys, books where histroys.book_id = books.book_id and histroys.user_name=? ''', [g.user], one = False)

	return render_template('reader_histroy.html', histroys = histroys)

if __name__ == '__main__':
	
    init_db()
    app.run(host='0.0.0.0',port=81,threaded=True)
    #app.run(debug=True)



