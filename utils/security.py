"""
Security utility functions for CyberSecEdu application.
Provides helper functions for implementing security features and validations.
"""

import re
import hashlib
import secrets
import string
from urllib.parse import urlparse, urljoin
from flask import request, url_for, abort

def is_safe_url(target):
    """
    Validates if a URL is safe to redirect to by checking if it belongs to the same host.
    
    Args:
        target (str): The URL to validate.
        
    Returns:
        bool: True if the URL is safe, False otherwise.
    """
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

def validate_password_strength(password):
    """
    Validates password strength based on common criteria.
    
    Args:
        password (str): The password to validate.
        
    Returns:
        dict: A dictionary containing validation results:
            - valid (bool): Overall validity
            - errors (list): List of error messages if any
            - strength (str): Password strength rating ('weak', 'moderate', 'strong')
    """
    result = {
        'valid': True,
        'errors': [],
        'strength': 'weak'
    }
    
    # Check minimum length
    if len(password) < 8:
        result['valid'] = False
        result['errors'].append("Password must be at least 8 characters long")
    
    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        result['valid'] = False
        result['errors'].append("Password must contain at least one uppercase letter")
    
    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        result['valid'] = False
        result['errors'].append("Password must contain at least one lowercase letter")
    
    # Check for digits
    if not re.search(r'\d', password):
        result['valid'] = False
        result['errors'].append("Password must contain at least one number")
    
    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        result['valid'] = False
        result['errors'].append("Password must contain at least one special character")
    
    # Calculate password strength
    strength = 0
    if len(password) >= 8:
        strength += 1
    if len(password) >= 12:
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'\d', password):
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    
    if strength <= 2:
        result['strength'] = 'weak'
    elif strength <= 4:
        result['strength'] = 'moderate'
    else:
        result['strength'] = 'strong'
    
    return result

def sanitize_input(input_string):
    """
    Sanitizes user input to prevent XSS and injection attacks.
    
    Args:
        input_string (str): The string to sanitize.
        
    Returns:
        str: Sanitized string.
    """
    if not input_string:
        return ""
    
    # Remove potentially harmful characters
    sanitized = re.sub(r'[<>\'";]', '', input_string)
    return sanitized.strip()

def validate_email(email):
    """
    Validates email format using a regex pattern.
    
    Args:
        email (str): The email to validate.
        
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_username(username):
    """
    Validates username format.
    
    Args:
        username (str): The username to validate.
        
    Returns:
        bool: True if the username is valid, False otherwise.
    """
    # Allow letters, numbers, underscores, 3-20 characters
    pattern = r'^[a-zA-Z0-9_]{3,20}$'
    return bool(re.match(pattern, username))

def generate_csrf_token():
    """
    Generates a secure random token for CSRF protection.
    
    Returns:
        str: A random token.
    """
    return secrets.token_hex(16)

def generate_secure_password(length=16):
    """
    Generates a cryptographically secure random password.
    
    Args:
        length (int): Length of the password to generate.
        
    Returns:
        str: A secure random password.
    """
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def compute_file_hash(file_data, algorithm='sha256'):
    """
    Computes the hash of a file's contents.
    
    Args:
        file_data (bytes): The file data to hash.
        algorithm (str): The hashing algorithm to use.
        
    Returns:
        str: The computed hash.
    """
    hash_obj = None
    
    if algorithm == 'md5':
        hash_obj = hashlib.md5()
    elif algorithm == 'sha1':
        hash_obj = hashlib.sha1()
    elif algorithm == 'sha256':
        hash_obj = hashlib.sha256()
    else:
        hash_obj = hashlib.sha256()
    
    hash_obj.update(file_data)
    return hash_obj.hexdigest()

def require_permission(permission):
    """
    Decorator to check if a user has the required permission.
    
    Args:
        permission (str): The required permission.
        
    Returns:
        function: Decorator function.
    """
    def decorator(f):
        def wrapped_function(*args, **kwargs):
            from flask_login import current_user
            
            # Check if user is authenticated
            if not current_user.is_authenticated:
                abort(401)
                
            # In a real application, you would check if the user has the specific permission
            # This is a simplified example
            if not hasattr(current_user, 'permissions') or permission not in current_user.permissions:
                abort(403)
                
            return f(*args, **kwargs)
        return wrapped_function
    return decorator
