from flask import Blueprint, render_template, request, redirect, session, flash, url_for, jsonify
from models import storage, User
import uuid

auth_bp = Blueprint('auth', __name__)

# take the new data (User) and save it to the DB
@auth_bp.route('/', strict_slashes=False)
@auth_bp.route("/signup", strict_slashes=False, methods=["GET","POST"])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        role = request.form.get('role')

        new_user = User(email=email, first_name=first_name, last_name=last_name, role=role)
        new_user.user_password = password 
        storage.new(new_user)
        storage.save()
        flash('User signUp successfully!', 'success')
        return redirect(url_for('auth.signin'))
    return render_template('signup.html', cache_id=uuid.uuid4())


@auth_bp.route('/signin', strict_slashes=False, methods=["GET", "POST"])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        users = storage.all(User).values()
        
        # Loop through users to find a matching email and password
        for user in users:
            if user and user.email == email and user.check_password(password):
                # Set the user ID in the session
                session['user_id'] = str(user.id)  # Ensure user.id is stored as a string
                
                # Role-based redirection
                if user.role == 'professor':
                    flash('Welcome, Professor', 'success')
                    return redirect(url_for('main.home_product'))
                elif user.role == 'lab manager':
                    flash('Welcome, Lab Manager', 'success')
                    return redirect(url_for('admin.manager_page'))
        
        # If no user is found, display an error message
        flash('Incorrect email or password', 'error')
        return redirect(url_for("auth.signin"))
    
    # If the request method is GET, render the sign-in page
    return render_template('signin.html', cache_id=uuid.uuid4())



