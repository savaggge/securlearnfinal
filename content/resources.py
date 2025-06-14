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
        "description": "Набор рекомендаций по снижению рисков кибербезопасности организаций, разработанный Национальным институтом стандартов и технологий. Предоставляет основу политик для руководства по компьютерной безопасности.",
        "category": "guides",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://www.nist.gov/cyberframework",
        "tags": ["фреймворк", "стандарты", "лучшие практики", "соответствие"]
    },
    {
        "name": "OWASP Top Ten",
        "description": "Регулярно обновляемый отчет, описывающий 10 наиболее критических рисков безопасности веб-приложений. Это важный справочник для разработчиков и специалистов по безопасности для понимания распространенных уязвимостей.",
        "category": "guides",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://owasp.org/www-project-top-ten/",
        "tags": ["веб-безопасность", "уязвимости", "безопасность приложений", "лучшие практики"]
    },
    {
        "name": "EFF's Surveillance Self-Defense",
        "description": "Руководство по защите от электронного наблюдения с использованием инструментов шифрования и лучших практик. Создано Electronic Frontier Foundation, чтобы помочь пользователям защитить свою конфиденциальность.",
        "category": "guides",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://ssd.eff.org/",
        "tags": ["конфиденциальность", "шифрование", "наблюдение", "самозащита"]
    },
    {
        "name": "Google Safety Center",
        "description": "Ресурс от Google, который предоставляет инструменты и советы, чтобы помочь вам оставаться в большей безопасности в интернете и управлять вашей конфиденциальностью, безопасностью и информацией в сети.",
        "category": "guides",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://safety.google/",
        "tags": ["цифровая безопасность", "конфиденциальность", "советы по безопасности", "защита аккаунта"]
    },
    {
        "name": "Citizen Lab Security Planner",
        "description": "Инструмент, который предоставляет персонализированные рекомендации по онлайн-безопасности на основе ваших цифровых привычек, потребностей и опасений. Он предлагает простые советы по улучшению вашей кибербезопасности.",
        "category": "guides",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://securityplanner.org/",
        "tags": ["персонализированная безопасность", "советы по конфиденциальности", "цифровая безопасность", "оценка рисков"]
    },
    
    # Websites Section
    {
        "name": "Krebs on Security",
        "description": "Подробный блог о новостях безопасности и расследованиях, который ведет Брайан Кребс, бывший репортер Washington Post. Сайт освещает последние угрозы кибербезопасности, взломы и события.",
        "category": "websites",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://krebsonsecurity.com/",
        "tags": ["новости безопасности", "взломы", "расследования", "угрозы"]
    },
    {
        "name": "Cybersecurity & Infrastructure Security Agency",
        "description": "Веб-сайт CISA предоставляет ресурсы по кибербезопасности, предупреждения и рекомендации от правительства США. Он предлагает инструменты и информацию как для частных лиц, так и для организаций.",
        "category": "websites",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://www.cisa.gov/cybersecurity",
        "tags": ["правительственные ресурсы", "предупреждения", "безопасность инфраструктуры", "руководство"]
    },
    {
        "name": "Naked Security by Sophos",
        "description": "Блог по кибербезопасности, который предлагает новости, мнения, советы и исследования. Он охватывает широкий спектр тем безопасности в доступной и понятной форме.",
        "category": "websites",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://nakedsecurity.sophos.com/",
        "tags": ["новости безопасности", "исследования", "угрозы", "советы"]
    },
    {
        "name": "The Hacker News",
        "description": "Надежная и широко читаемая новостная платформа по кибербезопасности, которая фокусируется на новостях о взломах, утечках и вредоносных программах. Она сообщает о последних уязвимостях и кибератаках.",
        "category": "websites",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://thehackernews.com/",
        "tags": ["новости кибербезопасности", "уязвимости", "взлом", "вредоносное ПО"]
    },
    {
        "name": "US-CERT",
        "description": "Группа реагирования на компьютерные инциденты США предоставляет предупреждения, бюллетени и советы по кибербезопасности для защиты систем и данных.",
        "category": "websites",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://www.us-cert.gov/",
        "tags": ["правительственные ресурсы", "предупреждения", "бюллетени", "реагирование на инциденты"]
    },
    
    # Courses Section
    {
        "name": "Cybersecurity Fundamentals",
        "description": "Курс для начинающих, охватывающий основы кибербезопасности, включая идентификацию угроз, управление рисками и защитные меры.",
        "category": "courses",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://www.coursera.org/learn/cyber-security-basics",
        "provider": "Coursera",
        "tags": ["основы", "начинающие", "идентификация угроз", "управление рисками"]
    },
    {
        "name": "Introduction to Cyber Security",
        "description": "Узнайте о безопасности в интернете и о том, как защитить свою цифровую жизнь. Этот курс охватывает необходимые знания для понимания киберугроз и способов защиты от них.",
        "category": "courses",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://www.futurelearn.com/courses/introduction-to-cyber-security",
        "provider": "FutureLearn & The Open University",
        "tags": ["начинающие", "онлайн-безопасность", "цифровая защита", "основы"]
    },
    {
        "name": "Cyber Security Awareness: Building Your Digital Shield",
        "description": "Комплексный курс, который поможет вам понять основы кибербезопасности и внедрить практические меры для защиты себя в интернете.",
        "category": "courses",
        "price_type": "paid",
        "price_type_color": "danger",
        "url": "https://www.udemy.com/course/cyber-security-awareness/",
        "provider": "Udemy",
        "tags": ["осведомленность", "практическая безопасность", "онлайн-защита", "угрозы"]
    },
    {
        "name": "Cybersecurity Essentials",
        "description": "Развивайте понимание киберпреступности, принципов безопасности, технологий и процедур, используемых для защиты сетей. Рекомендовано для студентов, планирующих учиться на сертификацию CompTIA Security+.",
        "category": "courses",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://www.netacad.com/courses/cybersecurity/cybersecurity-essentials",
        "provider": "Cisco Networking Academy",
        "tags": ["принципы безопасности", "защита сети", "подготовка к сертификации", "киберпреступность"]
    },
    {
        "name": "Complete Cyber Security Course",
        "description": "Серия углубленных курсов, охватывающих анонимность, конфиденциальность, методы взлома и основы безопасности. Разработана для обеспечения комплексного понимания кибербезопасности.",
        "category": "courses",
        "price_type": "paid",
        "price_type_color": "danger",
        "url": "https://www.udemy.com/course/the-complete-internet-security-privacy-course-volume-1/",
        "provider": "Udemy",
        "tags": ["комплексный", "конфиденциальность", "анонимность", "методы взлома"]
    },
    
    # Books Section
    {
        "name": "Cybersecurity For Dummies",
        "description": "Дружелюбное введение в концепции кибербезопасности для начинающих, объясняющее угрозы, защитные меры и лучшие практики простым языком, доступным для нетехнических читателей.",
        "category": "books",
        "price_type": "paid",
        "price_type_color": "danger",
        "url": "https://www.wiley.com/en-us/Cybersecurity+For+Dummies-p-9781119560326",
        "author": "Joseph Steinberg",
        "tags": ["начинающие", "основы", "нетехнический", "введение"]
    },
    {
        "name": "Social Engineering: The Science of Human Hacking",
        "description": "Исследует методы социальной инженерии и дает представление о том, как распознавать и защищаться от тактик манипуляции, используемых злоумышленниками.",
        "category": "books",
        "price_type": "paid",
        "price_type_color": "danger",
        "url": "https://www.wiley.com/en-us/Social+Engineering%3A+The+Science+of+Human+Hacking%2C+2nd+Edition-p-9781119433385",
        "author": "Christopher Hadnagy",
        "tags": ["социальная инженерия", "манипуляции", "психология", "человеческий фактор"]
    },
    {
        "name": "Practical Malware Analysis",
        "description": "Практическое руководство по анализу вредоносного ПО для понимания того, как оно работает, как его идентифицировать и как с ним бороться.",
        "category": "books",
        "price_type": "paid",
        "price_type_color": "danger",
        "url": "https://nostarch.com/malware",
        "author": "Michael Sikorski & Andrew Honig",
        "tags": ["вредоносное ПО", "анализ", "обратная инженерия", "обнаружение угроз"]
    },
    {
        "name": "The Web Application Hacker's Handbook",
        "description": "Комплексное руководство по поиску и использованию уязвимостей в веб-приложениях. Необходимо для разработчиков и специалистов по безопасности, которые хотят защитить веб-приложения.",
        "category": "books",
        "price_type": "paid",
        "price_type_color": "danger",
        "url": "https://www.wiley.com/en-us/The+Web+Application+Hacker%27s+Handbook%3A+Finding+and+Exploiting+Security+Flaws%2C+2nd+Edition-p-9781118026472",
        "author": "Dafydd Stuttard & Marcus Pinto",
        "tags": ["веб-безопасность", "тестирование на проникновение", "уязвимости", "безопасность приложений"]
    },
    {
        "name": "CISSP All-in-One Exam Guide",
        "description": "Комплексное руководство по темам, охватываемым в экзамене Certified Information Systems Security Professional, но также служит отличным справочником для профессионалов в области кибербезопасности.",
        "category": "books",
        "price_type": "paid",
        "price_type_color": "danger",
        "url": "https://www.amazon.com/CISSP-All-One-Guide-Eighth/dp/1260142655/",
        "author": "Shon Harris & Fernando Maymi",
        "tags": ["сертификация", "комплексный", "справочник", "профессиональный"]
    },
    
    # Blogs & News Section
    {
        "name": "Schneier on Security",
        "description": "Блог Брюса Шнайера, известного специалиста по технологиям безопасности, охватывающий темы безопасности, конфиденциальности и криптографии. Содержит анализ текущих событий и технологий безопасности.",
        "category": "blogs",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://www.schneier.com/",
        "tags": ["экспертный анализ", "криптография", "конфиденциальность", "комментарии по безопасности"]
    },
    {
        "name": "Dark Reading",
        "description": "Новостной сайт по кибербезопасности, который предоставляет новости, анализ и исследования в области безопасности информационных технологий. Освещает последние новости, уязвимости, угрозы и многое другое.",
        "category": "blogs",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://www.darkreading.com/",
        "tags": ["новости безопасности", "анализ", "исследования", "уязвимости"]
    },
    {
        "name": "Threatpost",
        "description": "Независимый новостной сайт, посвященный темам ИТ-безопасности, включая уязвимости, вредоносное ПО, утечки данных и проблемы конфиденциальности.",
        "category": "blogs",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://threatpost.com/",
        "tags": ["новости безопасности", "уязвимости", "вредоносное ПО", "утечки данных"]
    },
    {
        "name": "The Record by Recorded Future",
        "description": "Новостной сайт, ориентированный на кибербезопасность, разведку и национальную безопасность. Предлагает оригинальные репортажи о киберугрозах, инцидентах и тенденциях.",
        "category": "blogs",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://therecord.media/",
        "tags": ["разведка угроз", "новости кибербезопасности", "инциденты", "анализ"]
    },
    {
        "name": "SANS Internet Storm Center",
        "description": "Служба мониторинга уровней интернет-угроз и возникающих угроз. Предоставляет ежедневные сводки о значительных киберсобытиях и образовательные материалы.",
        "category": "blogs",
        "price_type": "free",
        "price_type_color": "success",
        "url": "https://isc.sans.edu/",
        "tags": ["мониторинг угроз", "ежедневные обновления", "возникающие угрозы", "образовательный"]
    }
]
