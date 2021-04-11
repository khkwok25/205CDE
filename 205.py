from flask import Flask, render_template, flash, redirect, request, url_for, session, logging
from flask_mysqldb import MySQL
import sqlite3
from werkzeug.exceptions import abort
import MySQLdb.cursors
import re
import traceback

app = Flask(__name__)

app.secret_key = '123456'


#database connections
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "kellykwok"
app.config["MYSQL_PASSWORD"] = "un168168"
app.config["MYSQL_DB"] = "205CDE"

mysql = MySQL(app)

def get_product(product_id):
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT * FROM product WHERE product_id=%s',(product_id,))
	product = cursor.fetchone()
	if product is None:
		abort(404)
	else:
		return product

def get_service(service_id):
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT * FROM service WHERE service_id=%s',(service_id,))
	service = cursor.fetchone()
	if service is None:
		abort(404)
	else:
		return service

def get_venue(venue_id):
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT * FROM venue WHERE venue_id=%s',(venue_id,))
	venue = cursor.fetchone()
	if venue is None:
		abort(404)
	else:
		return venue

def get_creater(id):
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT * FROM user WHERE id=%s',(id,))
	user = cursor.fetchone()
	if user is None:
		abort(404)
	else:
		return user



@app.route('/')
def home():
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT * FROM product;')	
	product = cursor.fetchall()
	return render_template('home.html', product=product)

@app.route('/about')
def about():
	if 'loggedin' in session:
		return render_template("about1.html")
	else:
		return render_template("about.html")

#the login page
@app.route('/login', methods=['GET','POST'])
def login():
	# Output message if something goes wrong...
	msg = ''
	#check
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
	# Create variables for easy access 
		username = request.form['username']
		password = request.form['password']
		#check if account exists using MySQL
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM user WHERE username = %s AND password = %s', (username, password,))
	
		#Fetch one record and return result
		user = cursor.fetchone()
		
		if user:
			#Create session data, we can access this data in other routes
			session['loggedin'] = True
			session['id'] = user['id']
			session['username'] = user['username']
			#logged in succes
			return redirect(url_for('user'))

		else:
			# Account doesnt exist or username/pwd incorrect
			msg ="Incorrect username or password!!!"
			return render_template('login.html', msg = msg)

		#show the login form with message 
	else:
	    return render_template('login.html', msg = msg)

#logout function
@app.route('/login/logout')
def logout():
	# Remove session data, then logout
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	#redirect to login page
	return redirect(url_for('home'))

#regist page
@app.route("/signup", methods=['GET','POST'])
def SignUp():
	# Output message if something goes wrong...
	msg = ''
	##check if account exists using MySQL
	if request.method == 'POST' and 'username' in request.form and 'email' in request.form and 'password':
	    # Create variables for easy access 
		name = request.form['name']
		username = request.form['username']
		age = request.form['age']
		phone = request.form['phone']
		email = request.form['email']
		password = request.form['password']
	
		
		#check if account exists using MySQL
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM user WHERE username = %s',(username,))
		#Fetch one record and return result
		user = cursor.fetchone()
		if user:
			msg='Account already exists!'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg='Invalid email address!'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg= 'Username must contain only characters and numbers!'
		elif not re.match(r'\d{8}', phone):
			msg= 'Phone.no must contain only 8 numbers!'
		elif not username or not password or not email:
			msg='Please complete the form!'
		else:
			cursor.execute('INSERT INTO user (username, password, email, name, age, phone) VALUES (%s, %s, %s, %s, %s, %s)',
							(username, password, email, name, age, phone))
			#insert new account now
			mysql.connection.commit()
			msg = 'You have sucessfully SignUp!'
			return render_template('SignUp.html', msg = msg)
	elif request.method == 'POST':
		#Form is empty...
		msg =' Please complet the form!'
	return render_template('SignUp.html', msg = msg)

#profile of the user only can be seen after login
@app.route("/login/user/profile")
def profile():
	#check if user is logged in
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM user WHERE id = %s', (session['id'],))
		user = cursor.fetchone()
		#show info
		return render_template('profile.html', user=user)
	else:
		return redirect(url_for('login'))

#the home page after login
@app.route("/login/user")
def user():
	#check if user is loggedin
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM product')	
		product = cursor.fetchall()
		return render_template('user.html', username=session['username'],product = product)

	else:
		return render_template('home.html')

#product list after login
@app.route("/login/product_list")
def product_list1():
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT * FROM product')	
	product = cursor.fetchall()
	return render_template('product_list1.html', product = product)

#product list before login
@app.route("/product_list")
def product_list():
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT * FROM product')	
	product = cursor.fetchall()
	return render_template('product_list.html', product = product)

#service list before login
@app.route("/service_list")
def service_list():
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT * FROM service')	
	service = cursor.fetchall()
	return render_template('service_list.html', service = service)

#service list after login
@app.route("/login/service_list")
def service_list1():
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT * FROM service')	
	service = cursor.fetchall()
	return render_template('service_list1.html', service = service)

#venue list before login
@app.route("/venue_list")
def venue_list():
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT * FROM venue')	
	venue = cursor.fetchall()
	return render_template('venue_list.html', venue = venue)

#venue list after login
@app.route("/login/venue_list")
def venue_list1():
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT * FROM venue')	
	venue = cursor.fetchall()
	return render_template('venue_list1.html', venue = venue)

#venue page after login
@app.route("/login/venue/<int:venue_id>/")
def venue1(venue_id):
	venue = get_venue(venue_id)
	return render_template('venue1.html', venue= venue)

#venue page before login
@app.route("/venue/<int:venue_id>/")
def venue(venue_id):
	venue = get_venue(venue_id)
	return render_template('venue.html', venue= venue)

#service page after login
@app.route("/login/service/<int:service_id>/")
def service1(service_id):
	service = get_service(service_id)
	return render_template('service1.html', service= service)

#service page before login
@app.route("/service/<int:service_id>/")
def service(service_id):
	service = get_service(service_id)
	return render_template('service.html', service= service)

#user list only can be see after login
@app.route("/login/user_list")
def user_list():
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT * FROM user')	
	user = cursor.fetchall()
	return render_template('user_list.html', user = user)
	
#product page before login
@app.route("/product/<int:product_id>/")
def product1(product_id):
	product = get_product(product_id)
	return render_template('product.html', product= product)

#product page after login
@app.route("/login/product/<int:product_id>/")
def product(product_id):
	product = get_product(product_id)
	return render_template('product1.html', product= product)

#create page of product
@app.route('/login/create', methods=('GET', 'POST'))
def create():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM user WHERE id = %s', (session['id'],))
		user = cursor.fetchone()
		
		if request.method == 'POST' and 'name' in request.form:
			name = request.form['name']
			discription = request.form['discription']
			creater_id = session['id']

			cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
			cursor.execute('SELECT * FROM product WHERE name = %s',(name,))
			product = cursor.fetchone()

			if not name:
				flash('Product Name is required!')
			else:
				cursor.execute('INSERT INTO product (name, discription, creater_id) VALUES (%s, %s, %s)',
								(name, discription, creater_id))
				mysql.connection.commit()
				return redirect(url_for('created'))
		else:
			return render_template('create.html')
	else:
		return redirect(url_for('login'))

#create page of service
@app.route('/login/createS', methods=('GET', 'POST'))
def createS():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM user WHERE id = %s', (session['id'],))
		user = cursor.fetchone()
		
		if request.method == 'POST' and 'name' in request.form:
			name = request.form['name']
			discription = request.form['discription']
			creater_id = session['id']

			cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
			cursor.execute('SELECT * FROM service WHERE name = %s',(name,))
			product = cursor.fetchone()

			if not name:
				flash('Service Title is required!')
			else:
				cursor.execute('INSERT INTO service (name, discription, creater_id) VALUES (%s, %s, %s)',
								(name, discription, creater_id))
				mysql.connection.commit()
				
				return redirect(url_for('created'))
		else:
			return render_template('createS.html')
	else:
		return redirect(url_for('login'))

#create page of service
@app.route('/login/createV', methods=('GET', 'POST'))
def createV():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM user WHERE id = %s', (session['id'],))
		user = cursor.fetchone()
		
		if request.method == 'POST' and 'name' in request.form:
			name = request.form['name']
			address = request.form['address']
			discription = request.form['discription']
			creater_id = session['id']

			cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
			cursor.execute('SELECT * FROM venue WHERE name = %s',(name,))
			venue = cursor.fetchone()

			if not name:
				flash('Venue Name is required!')
			else:
				cursor.execute('INSERT INTO venue (name, address, discription, creater_id) VALUES (%s, %s, %s, %s)',
								(name, address, discription, creater_id))
				mysql.connection.commit()
				return redirect(url_for('created'))
		else:
			return render_template('createV.html')
	else:
		return redirect(url_for('login'))

#create new product and service fuction and the record user created
@app.route('/login/created', methods=('GET', 'POST'))
def created():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

		cursor.execute('SELECT * FROM product WHERE creater_id = %s', (session['id'],))	
		product = cursor.fetchall()

		cursor.execute('SELECT * FROM service WHERE creater_id = %s', (session['id'],))	
		service = cursor.fetchall()

		cursor.execute('SELECT * FROM venue WHERE creater_id = %s', (session['id'],))	
		venue = cursor.fetchall()

		return render_template('created.html', username=session['username'], product = product, service=service, venue=venue)

	else:
		return render_template('user.html')

#the record creater created
@app.route('/login/creatercreated/<int:id>')
def creatercreated(id):

	user=get_creater(id)
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

	cursor.execute('SELECT * FROM product WHERE creater_id = %s', (user['id'],))	
	product = cursor.fetchall()

	cursor.execute('SELECT * FROM service WHERE creater_id = %s', (user['id'],))	
	service = cursor.fetchall()

	cursor.execute('SELECT * FROM venue WHERE creater_id = %s', (user['id'],))	
	venue = cursor.fetchall()

	return render_template('Numcreated.html', user=user, product = product, service=service, venue=venue)

#specific creater profile
@app.route("/login/creater/<int:id>/")
def creater(id):
	user = get_creater(id)
	return render_template('creater.html', user= user)

#edit function for product
@app.route("/login/<int:product_id>/edit", methods=('GET', 'POST'))
def edit(product_id):
	product = get_product(product_id)

	if request.method == 'POST':
		name = request.form['name']
		discription = request.form['discription']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM product WHERE name = %s',(name,))
		product = cursor.fetchone()

		if not name:
			flash('Name is required!')
		else:
			cursor.execute('UPDATE product SET name = %s, discription =%s' 'WHERE product_id=%s', (name, discription, product_id))
			mysql.connection.commit()
			return redirect(url_for('created'))

	else:
		return render_template('edit.html', product=product)

#delete function for product
@app.route('/login/<int:product_id>/delete', methods=('POST',))
def delete(product_id):
    product = get_product(product_id)
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('DELETE FROM product WHERE product_id = %s', (product_id,))
    mysql.connection.commit()
    cursor.close()
    flash('"{}" was successfully deleted!'.format(product['name']))
    return redirect(url_for('created'))

#edit function for service
@app.route("/login/<int:service_id>/edits", methods=('GET', 'POST'))
def edits(service_id):
	service = get_service(service_id)

	if request.method == 'POST':
		name = request.form['name']
		discription = request.form['discription']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM service WHERE name = %s',(name,))
		service = cursor.fetchone()

		if not name:
			flash('Name is required!')
		else:
			cursor.execute('UPDATE service SET name = %s, discription =%s' 'WHERE service_id=%s', (name, discription, service_id))
			mysql.connection.commit()
			return redirect(url_for('created.html'))

	else:
		return render_template('editS.html', service=service)

#delete function for service
@app.route('/login/<int:service_id>/deletes', methods=('POST',))
def deletes(service_id):
    service= get_service(service_id)
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('DELETE FROM service WHERE service_id = %s', (service_id,))
    mysql.connection.commit()
    cursor.close()
    flash('"{}" was successfully deleted!'.format(service['name']))
    return redirect(url_for('created'))

#edit function for venue
@app.route("/login/<int:venue_id>/editv", methods=('GET', 'POST'))
def editv(venue_id):
	venue = get_venue(venue_id)

	if request.method == 'POST':
		name = request.form['name']
		address = request.form['address]']
		discription = request.form['discription']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM venue WHERE name = %s',(name,))
		venue = cursor.fetchone()

		if not name:
			flash('Name is required!')
		else:
			cursor.execute('UPDATE venue SET name = %s, address=%s, discription =%s' 'WHERE venue_id=%s', (name, address, discription, venue_id))
			mysql.connection.commit()
			return redirect(url_for('created'))

	else:
		return render_template('editV.html', venue=venue)

#delete function for venue
@app.route('/login/<int:venue_id>/deletev', methods=('POST',))
def deletev(venue_id):
    venue= get_venue(venue_id)
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('DELETE FROM venue WHERE venue_id = %s', (venue_id,))
    mysql.connection.commit()
    cursor.close()
    flash('"{}" was successfully deleted!'.format(venue['name']))
    return redirect(url_for('created'))

if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0", port=8000)
