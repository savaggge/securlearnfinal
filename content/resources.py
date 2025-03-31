"""
Cybersecurity resources module.
Contains educational resources, tools, and references for the website.
"""

# List of cybersecurity educational resources
RESOURCES = [
    # Tools Section
    {
        "name": "Have I Been Pwned",
        "description": "Бесплатный сервис, который позволяет проверить, не утекли ли ваши email или телефон при взломе баз данных. Он помогает узнать, были ли скомпрометированы ваши аккаунты, и предпринять необходимые действия.",
        "category": "tools",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://haveibeenpwned.com/",
        "tags": ["уведомления о взломах", "безопасность аккаунта", "утечки данных", "мониторинг"]
    },
    {
        "name": "Qualys SSL Labs",
        "description": "Бесплатный онлайн-сервис, который выполняет глубокий анализ конфигурации SSL/TLS веб-сервера. Помогает выявить потенциальные проблемы безопасности в конфигурации вашего веб-сайта.",
        "category": "tools",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://www.ssllabs.com/ssltest/",
        "tags": ["ssl", "tls", "безопасность веб-сайта", "тестирование конфигурации"]
    },
    {
        "name": "OWASP ZAP",
        "description": "OWASP Zed Attack Proxy - это бесплатный инструмент безопасности, который помогает находить уязвимости в веб-приложениях на этапе разработки и тестирования.",
        "category": "tools",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://www.zaproxy.org/",
        "tags": ["безопасность веб-приложений", "сканер уязвимостей", "тестирование на проникновение"]
    },
    {
        "name": "Wireshark",
        "description": "Бесплатный анализатор сетевых пакетов с открытым исходным кодом, используемый для устранения неполадок в сети, анализа и обеспечения безопасности. Позволяет видеть, что происходит в вашей сети на микроскопическом уровне.",
        "category": "tools",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://www.wireshark.org/",
        "tags": ["анализ сети", "захват пакетов", "анализатор протоколов", "сетевая безопасность"]
    },
    {
        "name": "Bitwarden",
        "description": "Менеджер паролей с открытым исходным кодом, который безопасно хранит и управляет паролями. Бесплатная версия предлагает основные функции для индивидуальных пользователей, а платные планы добавляют расширенные возможности.",
        "category": "tools",
        "price_type": "freemium",
        "price_type_color": "warning",
        "url": "https://bitwarden.com/",
        "tags": ["менеджер паролей", "учетные данные", "аутентификация", "безопасное хранение"]
    },
    {
        "name": "Privacy Badger",
        "description": "Бесплатное расширение для браузера, которое автоматически учится блокировать невидимые трекеры. Вместо хранения списков того, что нужно блокировать, Privacy Badger обучается, наблюдая, какие домены, похоже, отслеживают ваши действия.",
        "category": "tools",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://privacybadger.org/",
        "tags": ["конфиденциальность", "защита от отслеживания", "расширение для браузера", "сбор данных"]
    },
    # Guides Section
    {
        "name": "NIST Cybersecurity Framework",
        "description": "A set of guidelines for mitigating organizational cybersecurity risks, developed by the National Institute of Standards and Technology. It provides a policy framework of computer security guidance.",
        "category": "guides",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://www.nist.gov/cyberframework",
        "tags": ["framework", "standards", "best practices", "compliance"]
    },
    {
        "name": "OWASP Top Ten",
        "description": "A regularly updated report outlining the top 10 most critical web application security risks. It's an essential reference for developers and security professionals to understand common vulnerabilities.",
        "category": "guides",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://owasp.org/www-project-top-ten/",
        "tags": ["web security", "vulnerabilities", "application security", "best practices"]
    },
    {
        "name": "EFF's Surveillance Self-Defense",
        "description": "A guide to protecting yourself from electronic surveillance by using encryption tools and best practices. Created by the Electronic Frontier Foundation to help users protect their privacy.",
        "category": "guides",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://ssd.eff.org/",
        "tags": ["privacy", "encryption", "surveillance", "self-defense"]
    },
    {
        "name": "Google Safety Center",
        "description": "A resource by Google that provides tools and tips to help you stay safer online and manage your privacy, security, and online information.",
        "category": "guides",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://safety.google/",
        "tags": ["digital safety", "privacy", "security tips", "account protection"]
    },
    {
        "name": "Citizen Lab Security Planner",
        "description": "A tool that provides personalized online safety recommendations based on your digital habits, needs, and concerns. It offers straightforward advice for improving your cybersecurity.",
        "category": "guides",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://securityplanner.org/",
        "tags": ["personalized security", "privacy tips", "digital safety", "risk assessment"]
    },
    
    # Websites Section
    {
        "name": "Krebs on Security",
        "description": "An in-depth security news and investigation blog by Brian Krebs, a former Washington Post reporter. The site covers the latest cybersecurity threats, breaches, and developments.",
        "category": "websites",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://krebsonsecurity.com/",
        "tags": ["security news", "breaches", "investigations", "threats"]
    },
    {
        "name": "Cybersecurity & Infrastructure Security Agency",
        "description": "CISA's website provides cybersecurity resources, alerts, and guidance from the U.S. government. It offers tools and information for both individuals and organizations.",
        "category": "websites",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://www.cisa.gov/cybersecurity",
        "tags": ["government resources", "alerts", "infrastructure security", "guidance"]
    },
    {
        "name": "Naked Security by Sophos",
        "description": "A cybersecurity blog that offers news, opinion, advice, and research. It covers a wide range of security topics in an accessible, easy-to-understand manner.",
        "category": "websites",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://nakedsecurity.sophos.com/",
        "tags": ["security news", "research", "threats", "advice"]
    },
    {
        "name": "The Hacker News",
        "description": "A trusted and widely-read cybersecurity news platform that focuses on hacking news, breaches, and malware. It reports on the latest vulnerabilities and cyber attacks.",
        "category": "websites",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://thehackernews.com/",
        "tags": ["cybersecurity news", "vulnerabilities", "hacking", "malware"]
    },
    {
        "name": "US-CERT",
        "description": "The United States Computer Emergency Readiness Team provides cybersecurity alerts, bulletins, and tips to help protect systems and data.",
        "category": "websites",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://www.us-cert.gov/",
        "tags": ["government resources", "alerts", "bulletins", "incident response"]
    },
    
    # Courses Section
    {
        "name": "Cybersecurity Fundamentals",
        "description": "A beginner-friendly course covering the basics of cybersecurity, including threat identification, risk management, and protective measures.",
        "category": "courses",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://www.coursera.org/learn/cyber-security-basics",
        "provider": "Coursera",
        "tags": ["fundamentals", "beginners", "threat identification", "risk management"]
    },
    {
        "name": "Introduction to Cyber Security",
        "description": "Learn about online security and how to protect your digital life. This course covers the essential knowledge needed to understand cyber threats and how to protect against them.",
        "category": "courses",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://www.futurelearn.com/courses/introduction-to-cyber-security",
        "provider": "FutureLearn & The Open University",
        "tags": ["beginners", "online security", "digital protection", "fundamentals"]
    },
    {
        "name": "Cyber Security Awareness: Building Your Digital Shield",
        "description": "A comprehensive course to help you understand the basics of cybersecurity and implement practical measures to protect yourself online.",
        "category": "courses",
        "price_type": "paid",
        "price_type_color": "danger",
        "url": "https://www.udemy.com/course/cyber-security-awareness/",
        "provider": "Udemy",
        "tags": ["awareness", "practical security", "online protection", "threats"]
    },
    {
        "name": "Cybersecurity Essentials",
        "description": "Develop an understanding of cybercrime, security principles, technologies, and procedures used to defend networks. Recommended for students planning to study for the CompTIA Security+ certification.",
        "category": "courses",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://www.netacad.com/courses/cybersecurity/cybersecurity-essentials",
        "provider": "Cisco Networking Academy",
        "tags": ["security principles", "network defense", "certification prep", "cybercrime"]
    },
    {
        "name": "Complete Cyber Security Course",
        "description": "An in-depth series of courses covering anonymity, privacy, hacking techniques, and security fundamentals. Designed to provide comprehensive cybersecurity knowledge.",
        "category": "courses",
        "price_type": "paid",
        "price_type_color": "danger",
        "url": "https://www.udemy.com/course/the-complete-internet-security-privacy-course-volume-1/",
        "provider": "Udemy",
        "tags": ["comprehensive", "privacy", "anonymity", "hacking techniques"]
    },
    
    # Books Section
    {
        "name": "Cybersecurity For Dummies",
        "description": "A beginner-friendly introduction to cybersecurity concepts, explaining threats, protective measures, and best practices in plain language accessible to non-technical readers.",
        "category": "books",
        "price_type": "paid",
        "price_type_color": "danger",
        "url": "https://www.wiley.com/en-us/Cybersecurity+For+Dummies-p-9781119560326",
        "author": "Joseph Steinberg",
        "tags": ["beginners", "fundamentals", "non-technical", "introduction"]
    },
    {
        "name": "Social Engineering: The Science of Human Hacking",
        "description": "Examines social engineering techniques and provides insights into how to recognize and protect against manipulation tactics used by attackers.",
        "category": "books",
        "price_type": "paid",
        "price_type_color": "danger",
        "url": "https://www.wiley.com/en-us/Social+Engineering%3A+The+Science+of+Human+Hacking%2C+2nd+Edition-p-9781119433385",
        "author": "Christopher Hadnagy",
        "tags": ["social engineering", "manipulation", "psychology", "human factors"]
    },
    {
        "name": "Practical Malware Analysis",
        "description": "A hands-on guide to dissecting malicious software to understand how it works, how to identify it, and how to defeat it.",
        "category": "books",
        "price_type": "paid",
        "price_type_color": "danger",
        "url": "https://nostarch.com/malware",
        "author": "Michael Sikorski & Andrew Honig",
        "tags": ["malware", "analysis", "reverse engineering", "threat detection"]
    },
    {
        "name": "The Web Application Hacker's Handbook",
        "description": "A comprehensive guide to finding and exploiting security flaws in web applications. Essential for developers and security professionals who want to secure web applications.",
        "category": "books",
        "price_type": "paid",
        "price_type_color": "danger",
        "url": "https://www.wiley.com/en-us/The+Web+Application+Hacker%27s+Handbook%3A+Finding+and+Exploiting+Security+Flaws%2C+2nd+Edition-p-9781118026472",
        "author": "Dafydd Stuttard & Marcus Pinto",
        "tags": ["web security", "penetration testing", "vulnerabilities", "application security"]
    },
    {
        "name": "CISSP All-in-One Exam Guide",
        "description": "A comprehensive guide to the topics covered in the Certified Information Systems Security Professional exam, but also serves as an excellent reference for cybersecurity professionals.",
        "category": "books",
        "price_type": "paid",
        "price_type_color": "danger",
        "url": "https://www.amazon.com/CISSP-All-One-Guide-Eighth/dp/1260142655/",
        "author": "Shon Harris & Fernando Maymi",
        "tags": ["certification", "comprehensive", "reference", "professional"]
    },
    
    # Blogs & News Section
    {
        "name": "Schneier on Security",
        "description": "A blog by Bruce Schneier, a renowned security technologist, covering topics in security, privacy, and cryptography. Features analyses of current events and security technologies.",
        "category": "blogs",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://www.schneier.com/",
        "tags": ["expert analysis", "cryptography", "privacy", "security commentary"]
    },
    {
        "name": "Dark Reading",
        "description": "A cybersecurity news site that delivers news, analysis, and research on information technology security. Covers breaking news, vulnerabilities, threats, and more.",
        "category": "blogs",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://www.darkreading.com/",
        "tags": ["security news", "analysis", "research", "vulnerabilities"]
    },
    {
        "name": "Threatpost",
        "description": "An independent news site dedicated to covering IT security topics, including vulnerabilities, malware, data breaches, and privacy issues.",
        "category": "blogs",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://threatpost.com/",
        "tags": ["security news", "vulnerabilities", "malware", "data breaches"]
    },
    {
        "name": "The Record by Recorded Future",
        "description": "A news site focused on cybersecurity, intelligence, and national security. Features original reporting on cyber threats, incidents, and trends.",
        "category": "blogs",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://therecord.media/",
        "tags": ["threat intelligence", "cybersecurity news", "incidents", "analysis"]
    },
    {
        "name": "SANS Internet Storm Center",
        "description": "A monitoring service for internet threat levels and emerging threats. Provides daily summaries of significant cyber activities and educational materials.",
        "category": "blogs",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://isc.sans.edu/",
        "tags": ["threat monitoring", "daily updates", "emerging threats", "educational"]
    }
]
