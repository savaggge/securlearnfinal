/**
 * Main JavaScript file for CyberSecEdu
 * Contains utility functions and interactive elements
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize Bootstrap popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Alert auto-dismissal 
    const alertList = document.querySelectorAll('.alert-dismissible');
    alertList.forEach(function(alert) {
        if (!alert.classList.contains('alert-persistent')) {
            setTimeout(function() {
                const closeButton = alert.querySelector('.btn-close');
                if (closeButton) {
                    closeButton.click();
                }
            }, 5000);
        }
    });

    // Code highlighting for tutorial pages
    const codeBlocks = document.querySelectorAll('pre code');
    if (codeBlocks.length > 0) {
        highlightCodeBlocks();
    }

    // Copy to clipboard functionality for code blocks
    const copyButtons = document.querySelectorAll('.copy-btn');
    copyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const targetId = this.getAttribute('data-clipboard-target');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                // Copy to clipboard
                navigator.clipboard.writeText(targetElement.textContent)
                    .then(() => {
                        // Update button text temporarily
                        const originalText = this.innerHTML;
                        this.innerHTML = '<i class="fas fa-check me-1"></i>Copied!';
                        
                        // Reset button text after 2 seconds
                        setTimeout(() => {
                            this.innerHTML = originalText;
                        }, 2000);
                    })
                    .catch(err => {
                        console.error('Failed to copy text: ', err);
                    });
            }
        });
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId !== '#' && document.querySelector(targetId)) {
                e.preventDefault();
                document.querySelector(targetId).scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Password strength visualization
    const passwordField = document.getElementById('password');
    if (passwordField) {
        passwordField.addEventListener('input', function() {
            const password = this.value;
            updatePasswordStrength(password);
        });
    }

    // Form validation enhancement
    const forms = document.querySelectorAll('.needs-validation');
    forms.forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
});

/**
 * Highlights code blocks using a simple syntax highlighting
 */
function highlightCodeBlocks() {
    const codeBlocks = document.querySelectorAll('pre code');
    
    codeBlocks.forEach(block => {
        // Get the code language if it exists
        const language = block.className.replace('language-', '');
        
        // Apply basic syntax highlighting based on language
        if (language) {
            let codeContent = block.innerHTML;
            
            // Apply basic syntax highlighting patterns
            if (language === 'html' || language === 'xml') {
                // Highlight HTML tags
                codeContent = codeContent.replace(/(&lt;[\/]?[a-zA-Z0-9]+(?:\s+[a-zA-Z0-9-]+(?:="[^"]*")?)*\s*[\/]?&gt;)/g, '<span class="text-primary">$1</span>');
                // Highlight attributes
                codeContent = codeContent.replace(/(\s+[a-zA-Z0-9-]+)=/g, '<span class="text-info">$1</span>=');
                // Highlight attribute values
                codeContent = codeContent.replace(/="([^"]*)"/g, '="<span class="text-warning">$1</span>"');
            } else if (language === 'css') {
                // Highlight selectors
                codeContent = codeContent.replace(/([a-zA-Z0-9_\-\.#]+\s*{)/g, '<span class="text-primary">$1</span>');
                // Highlight properties
                codeContent = codeContent.replace(/(\s+[a-zA-Z0-9\-]+):/g, '<span class="text-info">$1</span>:');
                // Highlight values
                codeContent = codeContent.replace(/:\s*([^;]+);/g, ': <span class="text-warning">$1</span>;');
            } else if (language === 'javascript' || language === 'js') {
                // Highlight keywords
                const keywords = ['var', 'let', 'const', 'function', 'return', 'if', 'else', 'for', 'while', 'switch', 'case', 'break', 'continue', 'new', 'class', 'this', 'import', 'export', 'default', 'try', 'catch', 'finally', 'typeof', 'instanceof'];
                keywords.forEach(keyword => {
                    const regex = new RegExp(`\\b(${keyword})\\b`, 'g');
                    codeContent = codeContent.replace(regex, '<span class="text-primary">$1</span>');
                });
                // Highlight strings
                codeContent = codeContent.replace(/(['"])(.*?)\1/g, '<span class="text-warning">$1$2$1</span>');
                // Highlight comments
                codeContent = codeContent.replace(/(\/\/.*)/g, '<span class="text-success">$1</span>');
            } else if (language === 'python') {
                // Highlight keywords
                const keywords = ['def', 'class', 'import', 'from', 'as', 'return', 'if', 'elif', 'else', 'for', 'while', 'in', 'not', 'and', 'or', 'try', 'except', 'finally', 'with', 'lambda', 'True', 'False', 'None'];
                keywords.forEach(keyword => {
                    const regex = new RegExp(`\\b(${keyword})\\b`, 'g');
                    codeContent = codeContent.replace(regex, '<span class="text-primary">$1</span>');
                });
                // Highlight strings
                codeContent = codeContent.replace(/(['"])(.*?)\1/g, '<span class="text-warning">$1$2$1</span>');
                // Highlight comments
                codeContent = codeContent.replace(/(#.*)/g, '<span class="text-success">$1</span>');
            }
            
            block.innerHTML = codeContent;
        }
    });
}

/**
 * Updates password strength visual indicator
 * @param {string} password - The password to evaluate
 */
function updatePasswordStrength(password) {
    const passwordStrengthEl = document.getElementById('password-strength');
    if (!passwordStrengthEl) return;
    
    // Clear previous content
    passwordStrengthEl.innerHTML = '';
    
    if (!password) return;
    
    // Calculate password strength
    let strength = 0;
    const patterns = [
        /.{8,}/, // At least 8 characters
        /[A-Z]/, // Uppercase letters
        /[a-z]/, // Lowercase letters
        /[0-9]/, // Numbers
        /[^A-Za-z0-9]/ // Special characters
    ];
    
    patterns.forEach(pattern => {
        if (pattern.test(password)) {
            strength++;
        }
    });
    
    // Create progress bar
    const progressBar = document.createElement('div');
    progressBar.className = 'progress';
    
    const progressBarInner = document.createElement('div');
    progressBarInner.className = 'progress-bar';
    progressBarInner.style.width = (strength / 5 * 100) + '%';
    
    if (strength < 3) {
        progressBarInner.className += ' bg-danger';
        strengthText = 'Weak';
    } else if (strength < 5) {
        progressBarInner.className += ' bg-warning';
        strengthText = 'Moderate';
    } else {
        progressBarInner.className += ' bg-success';
        strengthText = 'Strong';
    }
    
    progressBar.appendChild(progressBarInner);
    passwordStrengthEl.appendChild(progressBar);
    
    // Add strength text
    const strengthTextEl = document.createElement('small');
    strengthTextEl.className = 'mt-1 d-block';
    strengthTextEl.textContent = `Password strength: ${strengthText}`;
    passwordStrengthEl.appendChild(strengthTextEl);
}

/**
 * Simple sanitization function for displaying user content
 * @param {string} text - The text to sanitize
 * @returns {string} - Sanitized text
 */
function sanitizeText(text) {
    const tempElement = document.createElement('div');
    tempElement.textContent = text;
    return tempElement.innerHTML;
}
