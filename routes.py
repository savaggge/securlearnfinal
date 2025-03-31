from flask import render_template, redirect, url_for, flash, request, abort, session
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from models import User, UserProgress
from datetime import datetime
import html
from urllib.parse import urlparse, urljoin
from content.tutorials import TUTORIALS
from content.glossary import GLOSSARY_TERMS
from content.resources import RESOURCES

# Security helper function to validate redirects
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tutorials')
def tutorials():
    return render_template('tutorials.html', tutorials=TUTORIALS)

@app.route('/tutorial/<tutorial_id>')
def tutorial(tutorial_id):
    # Find the specific tutorial by ID
    tutorial_data = next((t for t in TUTORIALS if t['id'] == tutorial_id), None)
    
    if not tutorial_data:
        flash('Урок не найден!', 'danger')
        return redirect(url_for('tutorials'))

    # If user is logged in, track progress
    user_completed = False
    if current_user.is_authenticated:
        progress = UserProgress.query.filter_by(
            user_id=current_user.id, 
            tutorial_id=tutorial_id
        ).first()
        
        if progress:
            user_completed = progress.completed

    return render_template('tutorial.html', tutorial=tutorial_data, completed=user_completed)

@app.route('/mark-complete/<tutorial_id>', methods=['POST'])
@login_required
def mark_complete(tutorial_id):
    # Validate the tutorial exists
    tutorial_data = next((t for t in TUTORIALS if t['id'] == tutorial_id), None)
    if not tutorial_data:
        flash('Урок не найден!', 'danger')
        return redirect(url_for('tutorials'))
    
    # Check if progress record exists
    progress = UserProgress.query.filter_by(
        user_id=current_user.id, 
        tutorial_id=tutorial_id
    ).first()
    
    if not progress:
        # Create new progress record
        progress = UserProgress(
            user_id=current_user.id,
            tutorial_id=tutorial_id,
            completed=True,
            completed_date=datetime.utcnow()
        )
        db.session.add(progress)
    else:
        # Update existing record
        progress.completed = True
        progress.completed_date = datetime.utcnow()
    
    db.session.commit()
    flash('Прогресс сохранен!', 'success')
    return redirect(url_for('tutorial', tutorial_id=tutorial_id))

@app.route('/glossary')
def glossary():
    return render_template('glossary.html', terms=GLOSSARY_TERMS)

@app.route('/resources')
def resources():
    return render_template('resources.html', resources=RESOURCES)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember_me = 'remember_me' in request.form
        
        # Basic validation
        if not email or not password:
            flash('Пожалуйста, заполните все поля', 'danger')
            return render_template('login.html')
        
        # Find user
        user = User.query.filter_by(email=email).first()
        
        # Check credentials
        if user is None or not user.check_password(password):
            flash('Неверный email или пароль', 'danger')
            return render_template('login.html')
        
        # Log in user
        login_user(user, remember=remember_me)
        user.last_login = datetime.utcnow()
        db.session.commit()
        
        # Redirect to requested page or home
        next_page = request.args.get('next')
        if not next_page or not is_safe_url(next_page):
            next_page = url_for('index')
        
        return redirect(next_page)
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Basic validation
        if not username or not email or not password or not confirm_password:
            flash('Пожалуйста, заполните все поля', 'danger')
            return render_template('register.html')
        
        if password != confirm_password:
            flash('Пароли не совпадают', 'danger')
            return render_template('register.html')
        
        # Check if username or email already exists
        if User.query.filter_by(username=username).first():
            flash('Имя пользователя уже занято', 'danger')
            return render_template('register.html')
        
        if User.query.filter_by(email=email).first():
            flash('Email уже зарегистрирован', 'danger')
            return render_template('register.html')
        
        # Create new user
        user = User(username=username, email=email)
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Регистрация успешна! Пожалуйста, войдите в систему.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error_code=404, error_message="Страница не найдена"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error_code=500, error_message="Внутренняя ошибка сервера"), 500

@app.errorhandler(403)
def forbidden(e):
    return render_template('error.html', error_code=403, error_message="Доступ запрещен"), 403
