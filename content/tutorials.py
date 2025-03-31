"""
Cybersecurity tutorials content module.
Contains all tutorial data displayed on the website.
"""

# List of tutorial content
TUTORIALS = [
    # Fundamentals Category
    {
        "id": "intro-to-cybersecurity",
        "title": "Введение в кибербезопасность",
        "description": "Изучите основные концепции и важность кибербезопасности в современном цифровом мире.",
        "category": "fundamentals",
        "difficulty": "Начинающий",
        "duration": "15 мин",
        "objectives": "Понять, что такое кибербезопасность, почему она важна и какие существуют распространенные киберугрозы.",
        "introduction": "Кибербезопасность относится к практике защиты систем, сетей и программ от цифровых атак. Эти атаки обычно направлены на получение доступа, изменение или уничтожение конфиденциальной информации; вымогательство денег у пользователей; или нарушение нормальных бизнес-процессов. Этот учебник познакомит вас с основами кибербезопасности и объяснит, почему она имеет решающее значение в нашем все более взаимосвязанном мире.",
        "sections": [
            {
                "title": "Что такое кибербезопасность?",
                "content": [
                    "Кибербезопасность - это практика защиты компьютеров, серверов, мобильных устройств, электронных систем, сетей и данных от вредоносных атак. Она также известна как безопасность информационных технологий или безопасность электронной информации.",
                    "Эта область становится все более важной из-за нашей растущей зависимости от компьютерных систем, Интернета и стандартов беспроводных сетей, таких как Bluetooth и Wi-Fi. Рост количества 'умных' устройств, включая смартфоны, телевизоры и различные устройства IoT (Интернет вещей), также расширяет уязвимости, которые необходимо устранять."
                ]
            },
            {
                "title": "Почему кибербезопасность важна?",
                "content": [
                    "С увеличением масштаба и сложности кибератак частным лицам и организациям требуются надежные меры безопасности для защиты конфиденциальной информации. Вот почему кибербезопасность имеет значение:",
                    "1. Защита личной информации: Ваши личные данные, такие как данные банковского счета, номера социального страхования и медицинские записи, должны быть защищены от несанкционированного доступа.",
                    "2. Непрерывность бизнеса: Компаниям необходимо защищать свои данные для поддержания операций и обеспечения услуг клиентам.",
                    "3. Национальная безопасность: Правительствам необходимо защищать критически важную инфраструктуру и конфиденциальную информацию от атак на уровне государств.",
                    "4. Правовые требования: Многие отрасли имеют нормативные требования по защите данных (например, GDPR, HIPAA и др.)."
                ]
            },
            {
                "title": "Распространенные киберугрозы",
                "content": [
                    "Понимание распространенных угроз - это первый шаг к защите себя. Вот некоторые распространенные типы кибератак:",
                    "• Вредоносное ПО: Злонамеренное программное обеспечение, предназначенное для нанесения вреда или эксплуатации устройств, включая вирусы, черви, трояны и программы-вымогатели.",
                    "• Фишинг: Обманные попытки кражи конфиденциальной информации путем маскировки под доверенную организацию в электронных коммуникациях.",
                    "• Социальная инженерия: Психологические манипуляции, направленные на то, чтобы обманом заставить пользователей совершать ошибки безопасности или раскрывать конфиденциальную информацию.",
                    "• Атаки типа 'человек посередине' (MitM): Злоумышленники тайно передают и, возможно, изменяют коммуникации между двумя сторонами, которые считают, что общаются напрямую друг с другом.",
                    "• Атаки отказа в обслуживании: Атаки, направленные на то, чтобы сделать машину или сетевой ресурс недоступным путем перегрузки систем трафиком."
                ],
                "alert": {
                    "type": "warning",
                    "icon": "exclamation-triangle",
                    "title": "Важное примечание",
                    "content": "Частота и сложность кибератак постоянно увеличиваются. Быть в курсе текущих угроз крайне важно для поддержания эффективной безопасности."
                }
            },
            {
                "title": "Триада ЦРУ (CIA): Основные принципы безопасности",
                "content": [
                    "Триада ЦРУ (CIA) представляет три основных принципа информационной безопасности:",
                    "• Конфиденциальность (Confidentiality): Обеспечение доступа к информации только тем, кто имеет на это разрешение.",
                    "• Целостность (Integrity): Поддержание и обеспечение точности и полноты данных на протяжении всего их жизненного цикла.",
                    "• Доступность (Availability): Обеспечение доступа авторизованных пользователей к информации, когда это необходимо."
                ],
                "image": {
                    "url": "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/svgs/solid/shield-halved.svg",
                    "alt": "Диаграмма триады ЦРУ",
                    "caption": "Три столпа информационной безопасности: Конфиденциальность, Целостность и Доступность"
                }
            }
        ],
        "key_takeaways": [
            "Кибербезопасность - это практика защиты цифровых систем, сетей и данных от атак",
            "Важность кибербезопасности продолжает расти по мере того, как мы все больше полагаемся на цифровые технологии",
            "К распространенным киберугрозам относятся вредоносное ПО, фишинг и социальная инженерия",
            "Триада ЦРУ (Конфиденциальность, Целостность, Доступность) формирует основные принципы информационной безопасности",
            "Каждый человек играет определенную роль в поддержании кибербезопасности, а не только ИТ-специалисты"
        ],
        "exercise": {
            "title": "Самооценка безопасности",
            "description": "Оцените свои текущие практики безопасности, чтобы выявить потенциальные уязвимости.",
            "steps": [
                "Составьте список всех ваших цифровых аккаунтов (электронная почта, социальные сети, банковские услуги и т.д.)",
                "Проверьте, используете ли вы уникальные пароли для каждого аккаунта",
                "Проверьте, включена ли двухфакторная аутентификация там, где она доступна",
                "Просмотрите настройки конфиденциальности в социальных сетях",
                "Проверьте, установлены ли на ваших устройствах последние обновления безопасности"
            ],
            "hint": "Сосредоточьтесь на улучшении одного аспекта вашей безопасности за раз, начиная с наиболее важных аккаунтов, таких как электронная почта и банковские аккаунты."
        },
        "further_reading": [
            {
                "title": "Основы кибербезопасности NIST",
                "url": "https://www.nist.gov/cyberframework",
                "description": "Набор рекомендаций по снижению рисков кибербезопасности в организациях"
            },
            {
                "title": "Агентство по кибербезопасности и безопасности инфраструктуры",
                "url": "https://www.cisa.gov/",
                "description": "Ресурсы правительства США по лучшим практикам кибербезопасности"
            },
            {
                "title": "Будьте в безопасности онлайн - Национальный альянс кибербезопасности",
                "url": "https://staysafeonline.org/",
                "description": "Ресурсы по безопасности в интернете и повышению осведомленности о безопасности"
            }
        ],
        "related_tutorials": [
            {
                "id": "password-security",
                "title": "Создание надежных паролей",
                "difficulty": "Начинающий"
            },
            {
                "id": "social-engineering",
                "title": "Распознавание атак социальной инженерии",
                "difficulty": "Начинающий"
            },
            {
                "id": "data-privacy",
                "title": "Защита вашей цифровой конфиденциальности",
                "difficulty": "Начинающий"
            }
        ]
    },
    {
        "id": "cybersecurity-threats",
        "title": "Common Cybersecurity Threats",
        "description": "Explore the most prevalent types of cyber threats and attack vectors.",
        "category": "fundamentals",
        "difficulty": "Beginner",
        "duration": "20 min",
        "objectives": "Identify and understand common cyber threats, recognize attack patterns, and learn basic prevention measures.",
        "introduction": "As our lives become increasingly digital, we face a growing array of cybersecurity threats. Understanding these threats is the first step toward protecting yourself online. This tutorial explores common cyber threats, how they work, and basic strategies to avoid them.",
        "sections": [
            {
                "title": "Malware: The Digital Pandemic",
                "content": [
                    "Malware (malicious software) is any program or file designed to harm a computer, network, or server. Understanding different types of malware can help you better protect your digital assets.",
                    "Common types of malware include:",
                    "• Viruses: Programs that spread by inserting copies of themselves into other programs",
                    "• Worms: Self-replicating malware that spreads across networks without human intervention",
                    "• Trojans: Malware disguised as legitimate software that tricks users into installing it",
                    "• Ransomware: Malware that encrypts files and demands payment for decryption",
                    "• Spyware: Software that secretly monitors user activity and collects personal information",
                    "• Adware: Software that automatically displays unwanted advertisements",
                    "• Rootkits: Tools that provide unauthorized access to a computer while hiding their existence"
                ],
                "alert": {
                    "type": "danger",
                    "icon": "virus",
                    "title": "Ransomware on the Rise",
                    "content": "Ransomware attacks have increased by 150% in recent years, with average ransom payments exceeding $100,000 for businesses. Never pay ransoms as they fund criminal operations and don't guarantee data recovery."
                }
            },
            {
                "title": "Phishing: Digital Deception",
                "content": [
                    "Phishing is a type of social engineering attack often used to steal user data, including login credentials and credit card numbers. It occurs when an attacker, masquerading as a trusted entity, dupes a victim into opening an email, instant message, or text message.",
                    "Common phishing techniques include:",
                    "• Email phishing: Fraudulent emails mimicking legitimate companies",
                    "• Spear phishing: Targeted phishing attacks customized for specific individuals",
                    "• Whaling: Phishing attempts targeting high-profile executives",
                    "• Smishing: Phishing via SMS messages",
                    "• Vishing: Voice phishing using phone calls",
                    "• Clone phishing: Using previously delivered but legitimate emails with malicious replacements",
                    "Phishing attempts often create a sense of urgency, contain suspicious attachments or links, have spelling and grammar errors, or use mismatched or suspicious URLs."
                ],
                "image": {
                    "url": "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/svgs/solid/fishing-rod.svg",
                    "alt": "Phishing Attack Illustration",
                    "caption": "Phishing attacks try to trick users into revealing sensitive information by impersonating trusted entities"
                }
            },
            {
                "title": "Social Engineering: The Human Vulnerability",
                "content": [
                    "Social engineering is the psychological manipulation of people into performing actions or divulging confidential information. It relies on human error rather than technical hacking techniques to gain access to systems and data.",
                    "Common social engineering techniques include:",
                    "• Pretexting: Creating a fabricated scenario to extract information",
                    "• Baiting: Offering something enticing to an end user in exchange for private information",
                    "• Quid pro quo: Requesting private information in exchange for a service",
                    "• Tailgating: Gaining unauthorized access to a restricted area by following someone with legitimate access",
                    "• Scareware: Tricking users into thinking their system is infected with malware and offering a fake solution"
                ]
            },
            {
                "title": "Man-in-the-Middle (MitM) Attacks",
                "content": [
                    "In a MitM attack, an attacker secretly relays and possibly alters the communications between two parties who believe they are directly communicating with each other. This allows the attacker to steal data or manipulate the conversation.",
                    "Common MitM attack vectors include:",
                    "• Public Wi-Fi: Unsecured networks that allow attackers to intercept traffic",
                    "• Evil twin: Rogue Wi-Fi access points that mimic legitimate ones",
                    "• Session hijacking: Taking over an active web session to gain unauthorized access",
                    "• SSL stripping: Downgrading a secure HTTPS connection to HTTP",
                    "The best protection against MitM attacks is using encrypted connections (HTTPS), virtual private networks (VPNs), and avoiding untrusted networks."
                ],
                "code": {
                    "language": "text",
                    "snippet": "# How to check if a website is secure\n\n1. Look for 'https://' at the beginning of the website address\n2. Verify the padlock icon in your browser's address bar\n3. Click on the padlock to view the site's security certificate\n4. Check if the certificate is valid and issued by a trusted authority"
                }
            }
        ],
        "key_takeaways": [
            "Malware comes in many forms, each with different methods and goals",
            "Phishing attacks attempt to trick users into revealing sensitive information",
            "Social engineering exploits human psychology rather than technical vulnerabilities",
            "Man-in-the-Middle attacks intercept communications between two parties",
            "Most cyber attacks can be prevented with awareness and basic security practices"
        ],
        "exercise": {
            "title": "Spot the Phishing Attempt",
            "description": "Practice identifying potential phishing emails by looking for common warning signs.",
            "steps": [
                "Review your email inbox (including spam folder)",
                "Look for emails with urgent language, generic greetings, or requests for personal information",
                "Check sender addresses carefully for slight misspellings or unusual domains",
                "Hover over links (without clicking) to see if the destination URL matches the purported source",
                "Note any grammatical errors or unusual formatting that might indicate a fraudulent message"
            ],
            "hint": "Legitimate organizations rarely request sensitive information via email or create false urgency."
        },
        "further_reading": [
            {
                "title": "OWASP Top Ten",
                "url": "https://owasp.org/www-project-top-ten/",
                "description": "The top 10 most critical web application security risks"
            },
            {
                "title": "Krebs on Security",
                "url": "https://krebsonsecurity.com/",
                "description": "In-depth security news and investigation"
            },
            {
                "title": "Phishing.org",
                "url": "https://www.phishing.org/",
                "description": "Educational resources about phishing attacks"
            }
        ],
        "related_tutorials": [
            {
                "id": "intro-to-cybersecurity",
                "title": "Introduction to Cybersecurity",
                "difficulty": "Beginner"
            },
            {
                "id": "social-engineering",
                "title": "Recognizing Social Engineering Attacks",
                "difficulty": "Beginner"
            },
            {
                "id": "secure-browsing",
                "title": "Safe Web Browsing Practices",
                "difficulty": "Beginner"
            }
        ]
    },
    {
        "id": "social-engineering",
        "title": "Recognizing Social Engineering Attacks",
        "description": "Learn to identify and defend against psychological manipulation techniques used by attackers.",
        "category": "fundamentals",
        "difficulty": "Beginner",
        "duration": "20 min",
        "objectives": "Understand social engineering techniques, recognize common tactics, and develop strategies to avoid being manipulated.",
        "introduction": "Social engineering is the art of manipulating people to give up confidential information or perform actions that may compromise security. Unlike technical hacking methods, social engineering relies on human interaction and often involves tricking people into breaking normal security procedures. This tutorial will help you recognize and defend against these psychological manipulation tactics.",
        "sections": [
            {
                "title": "The Psychology Behind Social Engineering",
                "content": [
                    "Social engineering attacks exploit fundamental human tendencies and emotions. Understanding these psychological triggers can help you recognize when you're being manipulated:",
                    "• Authority: People tend to comply with requests from authority figures",
                    "• Scarcity: Limited-time offers create urgency and can lead to hasty decisions",
                    "• Social proof: People often follow the actions of others",
                    "• Familiarity: We trust people and organizations we know or recognize",
                    "• Fear: Threats or warnings can bypass rational thinking",
                    "• Curiosity: The desire to know can override caution",
                    "Attackers carefully craft scenarios that trigger these responses, making their manipulations more effective."
                ]
            },
            {
                "title": "Common Social Engineering Techniques",
                "content": [
                    "Social engineers use a variety of techniques to manipulate their targets:",
                    "• Phishing: Sending fraudulent communications that appear to come from reputable sources",
                    "• Pretexting: Creating a fabricated scenario to extract information (e.g., impersonating co-workers, police, bank officials)",
                    "• Baiting: Offering something enticing to an end user in exchange for information (e.g., free software downloads that contain malware)",
                    "• Quid pro quo: Requesting private information in exchange for a service (e.g., offering IT assistance)",
                    "• Tailgating: Following someone into a secured area or system",
                    "• Vishing: Voice phishing over the phone",
                    "• Watering hole attacks: Compromising websites frequently visited by the target"
                ],
                "alert": {
                    "type": "info",
                    "icon": "info-circle",
                    "title": "Real-World Impact",
                    "content": "According to cybersecurity reports, over 98% of cyber attacks rely on social engineering. The average cost of a social engineering attack on businesses exceeds $130,000."
                }
            },
            {
                "title": "Red Flags: How to Spot Social Engineering",
                "content": [
                    "Being able to identify the warning signs of social engineering attempts is crucial for protection. Look out for these red flags:",
                    "• Unexpected contact: Communications you weren't expecting, especially those requesting urgent action",
                    "• Too good to be true: Offers that seem unusually generous or opportune",
                    "• Unusual requests: Asking for sensitive information that the person or organization shouldn't need",
                    "• Pressure tactics: Creating a sense of urgency or threatening negative consequences",
                    "• Suspicious links or attachments: Especially in unexpected communications",
                    "• Inconsistencies: Details that don't match what you know about the person or organization",
                    "• Grammatical errors: Professional organizations typically proofread their communications",
                    "• Unusual payment methods: Requests for payment via gift cards, wire transfers, or cryptocurrency"
                ],
                "image": {
                    "url": "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/svgs/solid/user-secret.svg",
                    "alt": "Social Engineering Tactics",
                    "caption": "Social engineers exploit human psychology rather than technical vulnerabilities"
                }
            },
            {
                "title": "Defending Against Social Engineering",
                "content": [
                    "While technology can help prevent some social engineering attacks, the best defense is awareness and caution. Follow these practices to protect yourself:",
                    "• Verify identities: Independently confirm the identity of individuals requesting information",
                    "• Be skeptical: Question unexpected communications, especially those creating urgency",
                    "• Guard personal information: Share sensitive information only when absolutely necessary",
                    "• Use multi-factor authentication: This adds an extra layer of protection even if credentials are compromised",
                    "• Keep software updated: Ensure your operating system and applications have the latest security patches",
                    "• Educate yourself and others: Regular security awareness training is essential, especially in workplace environments",
                    "• Report suspected attacks: If you believe you've encountered a social engineering attempt, report it to the appropriate authorities or your IT department"
                ]
            }
        ],
        "key_takeaways": [
            "Social engineering exploits human psychology rather than technical vulnerabilities",
            "Common techniques include phishing, pretexting, baiting, and creating false urgency",
            "Red flags include unexpected communications, unusual requests, and pressure tactics",
            "The best defense is awareness, skepticism, and verification of identity",
            "Most social engineering attacks can be prevented by taking time to verify before taking action"
        ],
        "exercise": {
            "title": "Social Engineering Scenario Analysis",
            "description": "Practice identifying social engineering techniques in real-world scenarios.",
            "steps": [
                "Review each of the following scenarios and identify the social engineering technique being used",
                "An email from 'your bank' asking you to verify your account details due to suspicious activity",
                "A phone call from 'tech support' about a problem with your computer they detected",
                "A LinkedIn message offering an exclusive job opportunity that requires an upfront fee",
                "A person in a courier uniform asking to be let into a secure building because they forgot their access card",
                "A USB drive labeled 'Confidential Salary Information' left in a public area"
            ],
            "hint": "For each scenario, ask yourself: Who is making the request? What are they asking for? Why are they creating urgency? How can I verify their identity?"
        },
        "further_reading": [
            {
                "title": "Social Engineering: The Science of Human Hacking",
                "url": "https://www.amazon.com/Social-Engineering-Science-Human-Hacking/dp/111943338X",
                "description": "Book by Christopher Hadnagy on social engineering tactics and defenses"
            },
            {
                "title": "SANS Security Awareness",
                "url": "https://www.sans.org/security-awareness-training/",
                "description": "Resources for security awareness training"
            },
            {
                "title": "FTC Scam Alerts",
                "url": "https://www.consumer.ftc.gov/features/scam-alerts",
                "description": "Current information about scams and social engineering attacks"
            }
        ],
        "related_tutorials": [
            {
                "id": "cybersecurity-threats",
                "title": "Common Cybersecurity Threats",
                "difficulty": "Beginner"
            },
            {
                "id": "password-security",
                "title": "Creating Strong Passwords",
                "difficulty": "Beginner"
            },
            {
                "id": "secure-browsing",
                "title": "Safe Web Browsing Practices",
                "difficulty": "Beginner"
            }
        ]
    },
    # Password Security Category
    {
        "id": "password-security",
        "title": "Создание надежных паролей",
        "description": "Узнайте, как создавать и управлять надежными, уникальными паролями для лучшей защиты.",
        "category": "password-security",
        "difficulty": "Начинающий",
        "duration": "15 мин",
        "objectives": "Понимание уязвимостей паролей, обучение созданию надежных паролей и освоение стратегий управления паролями.",
        "introduction": "Пароли остаются основным методом аутентификации для большинства цифровых сервисов, что делает их критически важным элементом вашей онлайн-безопасности. Несмотря на их важность, многие люди продолжают использовать слабые, легко угадываемые пароли или повторно используют один и тот же пароль на нескольких сайтах. Этот учебник научит вас, как создавать надежные пароли и эффективно управлять ими для защиты вашей цифровой личности.",
        "sections": [
            {
                "title": "Почему безопасность паролей важна",
                "content": [
                    "Пароли - это ключи к вашей цифровой жизни. Когда злоумышленники получают ваши пароли, они могут:",
                    "• Получить доступ к вашей личной и финансовой информации",
                    "• Совершать покупки, используя ваши платежные методы",
                    "• Украсть вашу личность или выдавать себя за вас",
                    "• Получить доступ к системам и конфиденциальным данным вашего рабочего места",
                    "• Использовать ваши учетные записи для атак на других",
                    "Риски не просто теоретические. Согласно отчетам по кибербезопасности, 81% утечек данных вызваны слабыми или украденными паролями. Один скомпрометированный пароль может привести к взлому нескольких учетных записей из-за повторного использования пароля."
                ],
                "alert": {
                    "type": "danger",
                    "icon": "exclamation-circle",
                    "title": "Распространенные ошибки при создании паролей",
                    "content": "Самые распространенные пароли до сих пор включают '123456', 'password', 'qwerty' и 'admin'. Эти пароли можно взломать менее чем за секунду. Даже добавление одного символа, цифры или специального знака значительно увеличивает время, необходимое для взлома пароля."
                }
            },
            {
                "title": "Характеристики надежных паролей",
                "content": [
                    "Надежный пароль имеет несколько важных характеристик:",
                    "• Длина: Не менее 12 символов; более длинные пароли экспоненциально сложнее взломать",
                    "• Сложность: Сочетание прописных и строчных букв, цифр и специальных символов",
                    "• Непредсказуемость: Отсутствие распространенных слов, фраз или шаблонов",
                    "• Уникальность: Разные пароли для каждой учетной записи или сервиса",
                    "• Запоминаемость: Что-то, что вы можете запомнить, не записывая",
                    "Надежность пароля в первую очередь определяется его длиной и случайностью. Добавление всего нескольких символов к паролю может сделать его экспоненциально более сложным для взлома."
                ],
                "code": {
                    "language": "text",
                    "snippet": "# Примеры надежности паролей:\n\n'password' - Может быть взломан мгновенно\n'Password1' - Может быть взломан менее чем за день\n'P@ssw0rd!' - Может быть взломан за несколько дней\n'Tr0ub4dor&3' - Потребуется несколько месяцев для взлома\n'correct-horse-battery-staple' - Потребуются столетия для взлома при текущих технологиях"
                }
            },
            {
                "title": "Создание запоминающихся и надежных паролей",
                "content": [
                    "Задача с паролями заключается в балансировании безопасности и запоминаемости. Вот эффективные стратегии для создания паролей, которые вы можете запомнить:",
                    "• Метод парольной фразы: Объедините несколько случайных слов с пробелами или символами (например, 'correct-horse-battery-staple')",
                    "• Метод предложения: Возьмите первую букву каждого слова в запоминающемся предложении (например, 'У лукоморья дуб зелёный' становится 'Улдз')",
                    "• Метод подстановки: Замените буквы похожими на них цифрами или символами (например, 'password' становится 'p@$$w0rd')",
                    "• Личный алгоритм: Создайте систему для генерации уникальных паролей для каждого сайта (например, комбинируя название сервиса с личной фразой)",
                    "Самый безопасный подход - использовать менеджер паролей для генерации и хранения полностью случайных, уникальных паролей для каждого сервиса."
                ],
                "image": {
                    "url": "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/svgs/solid/key.svg",
                    "alt": "Иллюстрация сильного пароля",
                    "caption": "Надежные пароли - это ваша первая линия защиты от несанкционированного доступа"
                }
            },
            {
                "title": "Лучшие практики управления паролями",
                "content": [
                    "Даже с надежными паролями, правильное управление необходимо для поддержания безопасности:",
                    "• Используйте менеджер паролей: Эти инструменты генерируют, хранят и автоматически заполняют надежные, уникальные пароли для всех ваших учетных записей",
                    "• Включите двухфакторную аутентификацию (2FA): Это добавляет дополнительный уровень защиты помимо просто пароля",
                    "• Никогда не используйте пароли повторно: Каждая учетная запись должна иметь совершенно разный пароль",
                    "• Регулярно меняйте пароли: Особенно для критически важных учетных записей, таких как электронная почта и банковские услуги",
                    "• Не делитесь паролями: Даже с доверенными лицами, совместное использование снижает безопасность",
                    "• Будьте осторожны с хранением паролей: Менеджеры паролей в браузере удобны, но обычно менее безопасны, чем специализированные менеджеры паролей",
                    "• Имейте план восстановления: Знайте, как восстановить доступ, если вы забудете пароль или потеряете доступ к своему менеджеру паролей"
                ]
            }
        ],
        "key_takeaways": [
            "Надежные пароли необходимы для защиты вашей цифровой личности",
            "Надежность пароля зависит от длины, сложности и уникальности",
            "Парольные фразы (несколько случайных слов) одновременно безопасны и легко запоминаются",
            "Менеджеры паролей - самый безопасный способ создания и хранения уникальных паролей",
            "Двухфакторная аутентификация добавляет важный дополнительный уровень безопасности"
        ],
        "exercise": {
            "title": "Аудит и улучшение паролей",
            "description": "Оцените ваши текущие практики использования паролей и обновите пароли для самых важных учетных записей.",
            "steps": [
                "Составьте список ваших наиболее важных учетных записей (электронная почта, банковские сервисы, социальные сети и т.д.)",
                "Проверьте, используются ли одинаковые или похожие пароли в нескольких учетных записях",
                "Создайте новые надежные пароли для каждой учетной записи, используя изученные техники",
                "Включите двухфакторную аутентификацию на всех учетных записях, которые ее поддерживают",
                "Рассмотрите возможность использования менеджера паролей для хранения и генерации паролей"
            ],
            "hint": "Начните с вашей учетной записи электронной почты, так как она часто используется для восстановления доступа к другим учетным записям. Затем переходите к финансовым учетным записям и другим важным сервисам."
        },
        "further_reading": [
            {
                "title": "NIST Password Guidelines",
                "url": "https://pages.nist.gov/800-63-3/sp800-63b.html#sec5",
                "description": "Официальные рекомендации правительства США по безопасности паролей"
            },
            {
                "title": "Have I Been Pwned",
                "url": "https://haveibeenpwned.com/",
                "description": "Проверьте, не был ли ваш адрес электронной почты или пароль скомпрометирован в утечках данных"
            },
            {
                "title": "Password Strength Testing Tools",
                "url": "https://www.security.org/how-secure-is-my-password/",
                "description": "Инструменты для оценки того, как быстро ваш пароль может быть взломан"
            }
        ],
        "related_tutorials": [
            {
                "id": "two-factor-authentication",
                "title": "Настройка двухфакторной аутентификации",
                "difficulty": "Начинающий"
            },
            {
                "id": "password-managers",
                "title": "Использование менеджеров паролей",
                "difficulty": "Начинающий"
            },
            {
                "id": "social-engineering",
                "title": "Распознавание атак социальной инженерии",
                "difficulty": "Начинающий"
            }
        ]
    },
    {
        "id": "two-factor-authentication",
        "title": "Настройка двухфакторной аутентификации",
        "description": "Узнайте, как добавить дополнительный уровень защиты к вашим учетным записям помимо просто паролей.",
        "category": "password-security",
        "difficulty": "Начинающий",
        "duration": "15 мин",
        "objectives": "Понять, что такое двухфакторная аутентификация, почему она важна и как настроить ее на различных учетных записях.",
        "introduction": "Двухфакторная аутентификация (2FA), иногда называемая многофакторной аутентификацией, добавляет дополнительный уровень безопасности к вашим учетным записям помимо просто пароля. Она объединяет то, что вы знаете (ваш пароль) с тем, что у вас есть (например, ваш телефон) или тем, что представляет собой ваша личность (биометрические данные). Этот учебник объяснит, почему 2FA так важна, и проведет вас через процесс ее настройки на ваших самых важных учетных записях.",
        "sections": [
            {
                "title": "Понимание двухфакторной аутентификации",
                "content": [
                    "Двухфакторная аутентификация добавляет дополнительный шаг проверки при входе в ваши учетные записи. Даже если кто-то узнает ваш пароль, он все равно не сможет получить доступ к вашей учетной записи без второго фактора.",
                    "Существует несколько типов вторых факторов:",
                    "• SMS-коды: Одноразовый код, отправляемый на ваш телефон через текстовое сообщение",
                    "• Приложения аутентификации: Приложения вроде Google Authenticator или Authy, которые генерируют коды на основе времени",
                    "• Push-уведомления: Одобрение попыток входа непосредственно на вашем доверенном устройстве",
                    "• Физические ключи безопасности: USB-устройства типа YubiKey, которые вы вставляете в компьютер",
                    "• Биометрия: Отпечатки пальцев, распознавание лица или другие физические характеристики",
                    "Каждый метод предлагает различные уровни безопасности и удобства. Как правило, приложения аутентификации и физические ключи безопасности более надежны, чем SMS-коды."
                ],
                "image": {
                    "url": "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/svgs/solid/shield-alt.svg",
                    "alt": "Иллюстрация двухфакторной аутентификации",
                    "caption": "2FA добавляет второй уровень проверки, значительно повышая безопасность учетной записи"
                }
            },
            {
                "title": "Зачем вам нужна двухфакторная аутентификация",
                "content": [
                    "Двухфакторная аутентификация - одна из самых эффективных доступных мер безопасности:",
                    "• Она защищает от утечек паролей: Даже если ваш пароль украден, злоумышленники все равно не смогут получить доступ к вашей учетной записи",
                    "• Она защищает от фишинга: Большинство методов 2FA не могут быть легко перехвачены или подделаны при попытках фишинга",
                    "• Она оповещает вас о несанкционированных попытках доступа: Вы будете получать запросы аутентификации, когда кто-то пытается войти с вашим паролем",
                    "• Она рекомендуется экспертами по безопасности: Специалисты по кибербезопасности повсеместно рекомендуют использовать 2FA",
                    "Согласно данным Microsoft, учетные записи с 2FA на 99,9% менее подвержены компрометации, чем учетные записи только с паролями. Этот простой шаг может устранить большинство рисков захвата учетной записи."
                ],
                "alert": {
                    "type": "info",
                    "icon": "info-circle",
                    "title": "Защита в реальном мире",
                    "content": "Двухфакторная аутентификация могла бы предотвратить многие серьезные взломы учетных записей, включая громкие захваты учетных записей в социальных сетях и компрометацию электронной почты, которые привели к хищению данных."
                }
            },
            {
                "title": "Настройка 2FA на популярных сервисах",
                "content": [
                    "Большинство основных онлайн-сервисов теперь предлагают двухфакторную аутентификацию. Вот как включить ее на некоторых из самых важных:",
                    "Google/Gmail:",
                    "1. Перейдите в учетную запись Google (myaccount.google.com)",
                    "2. Выберите 'Безопасность' на панели навигации",
                    "3. В разделе 'Вход в Google' выберите 'Двухэтапная аутентификация'",
                    "4. Следуйте инструкциям на экране",
                    "",
                    "Facebook:",
                    "1. Нажмите на стрелку вниз в правом верхнем углу и выберите 'Настройки и конфиденциальность' → 'Настройки'",
                    "2. Нажмите 'Безопасность и вход'",
                    "3. Прокрутите до 'Двухфакторная аутентификация' и нажмите 'Редактировать'",
                    "4. Выберите желаемый метод аутентификации",
                    "",
                    "Apple ID:",
                    "1. Перейдите на appleid.apple.com и войдите в систему",
                    "2. В разделе безопасности нажмите 'Редактировать'",
                    "3. Нажмите 'Включить двухфакторную аутентификацию'",
                    "4. Следуйте инструкциям для подтверждения номера телефона"
                ],
                "code": {
                    "language": "text",
                    "snippet": "# Распространенные места для поиска настроек 2FA:\n\n• Google: Аккаунт → Безопасность → Двухэтапная аутентификация\n• Facebook: Настройки → Безопасность и вход → Двухфакторная аутентификация\n• Twitter: Настройки и конфиденциальность → Безопасность и доступ к аккаунту → Безопасность → Двухфакторная аутентификация\n• Microsoft: Аккаунт → Безопасность → Двухэтапная проверка\n• Amazon: Аккаунт и списки → Аккаунт → Безопасность и вход → Редактировать (рядом с Двухэтапной проверкой)\n• Instagram: Настройки → Безопасность → Двухфакторная аутентификация"
                }
            },
            {
                "title": "Использование приложений для аутентификации",
                "content": [
                    "Приложения для аутентификации - один из самых безопасных методов 2FA. Они генерируют одноразовые пароли на основе времени (TOTP), которые меняются каждые 30 секунд. Вот как их использовать:",
                    "1. Загрузите приложение для аутентификации, такое как:",
                    "   • Google Authenticator",
                    "   • Authy",
                    "   • Microsoft Authenticator",
                    "   • LastPass Authenticator",
                    "",
                    "2. При настройке 2FA на сервисе выберите опцию 'Приложение аутентификации'",
                    "",
                    "3. Обычно вам показывают QR-код для сканирования с помощью приложения",
                    "",
                    "4. Затем ваше приложение будет генерировать 6-значный код, который меняется каждые 30 секунд",
                    "",
                    "5. Введите текущий код для завершения настройки",
                    "",
                    "6. Храните резервные коды в безопасном месте на случай, если вы потеряете доступ к приложению аутентификации",
                    "",
                    "Важно: если вы получите новый телефон, вам потребуется перенести учетные записи из приложения аутентификации на новое устройство. Убедитесь, что вы понимаете процесс резервного копирования и восстановления для выбранного вами приложения."
                ]
            }
        ],
        "key_takeaways": [
            "Двухфакторная аутентификация значительно повышает безопасность учетной записи",
            "Приложения аутентификации и физические ключи безопасности обеспечивают лучшую защиту, чем SMS-коды",
            "Сначала включите 2FA на самых важных учетных записях (электронная почта, банковские услуги, облачное хранилище)",
            "Всегда храните резервные коды в безопасном месте",
            "2FA особенно важна для учетных записей, содержащих конфиденциальную информацию или привязанные платежные методы"
        ],
        "exercise": {
            "title": "Включение 2FA на критически важных учетных записях",
            "description": "Настройте двухфакторную аутентификацию на ваших самых важных онлайн-аккаунтах.",
            "steps": [
                "Составьте список ваших самых важных онлайн-аккаунтов (электронная почта, банковские услуги, социальные сети)",
                "Загрузите приложение аутентификации, если у вас его еще нет",
                "Для каждой учетной записи найдите раздел настроек безопасности или 2FA",
                "Следуйте инструкциям для включения 2FA (предпочтительно с использованием приложения аутентификации)",
                "Храните резервные коды в безопасном месте (менеджер паролей или печатная копия в надежном месте)"
            ],
            "hint": "Начните с вашей учетной записи электронной почты, поскольку она обычно используется для восстановления доступа к другим сервисам. Затем переходите к финансовым учетным записям, социальным сетям и облачным хранилищам."
        },
        "further_reading": [
            {
                "title": "Two Factor Auth Directory",
                "url": "https://twofactorauth.org/",
                "description": "Каталог веб-сайтов и сервисов, поддерживающих 2FA"
            },
            {
                "title": "NIST Digital Identity Guidelines",
                "url": "https://pages.nist.gov/800-63-3/",
                "description": "Официальные руководства правительства США по аутентификации"
            },
            {
                "title": "EFF's Guide to Two-Factor Authentication",
                "url": "https://ssd.eff.org/en/module/how-enable-two-factor-authentication",
                "description": "Руководство по двухфакторной аутентификации от Electronic Frontier Foundation"
            }
        ],
        "related_tutorials": [
            {
                "id": "password-security",
                "title": "Создание надежных паролей",
                "difficulty": "Начинающий"
            },
            {
                "id": "password-managers",
                "title": "Использование менеджеров паролей",
                "difficulty": "Начинающий"
            },
            {
                "id": "account-security",
                "title": "Защита ваших онлайн-аккаунтов",
                "difficulty": "Начинающий"
            }
        ]
    },
    # Network Security Category
    {
        "id": "secure-browsing",
        "title": "Безопасное использование веб-браузера",
        "description": "Узнайте, как защитить себя при просмотре интернета.",
        "category": "network-security",
        "difficulty": "Начинающий",
        "duration": "20 мин",
        "objectives": "Понять распространенные риски при веб-серфинге, распознавать безопасные веб-сайты и внедрить безопасные привычки просмотра.",
        "introduction": "Веб-браузер — ваш основной шлюз в интернет, что делает его критической точкой безопасности в вашей цифровой жизни. Понимание того, как безопасно просматривать веб-страницы, может защитить вас от многих распространенных киберугроз, включая вредоносное ПО, фишинг и кражу данных. Этот урок охватывает основные практики для более безопасного веб-серфинга на всех устройствах.",
        "sections": [
            {
                "title": "Основы безопасности браузера",
                "content": [
                    "Ваш браузер постоянно подвергается потенциальным угрозам. Вот основные меры безопасности, которые следует внедрить немедленно:",
                    "• Поддерживайте браузер в актуальном состоянии: Обновления браузера часто содержат критические патчи безопасности",
                    "• Используйте современный браузер с ориентацией на безопасность: Chrome, Firefox, Safari и Edge имеют хорошие функции безопасности",
                    "• Включите автоматические обновления: Это гарантирует, что у вас всегда будут последние средства защиты",
                    "• Просмотрите настройки безопасности браузера: Ознакомьтесь и включите ключевые функции безопасности",
                    "• Избирательно используйте расширения браузера: Устанавливайте расширения только из надежных источников и удаляйте те, которые не используете",
                    "• Регулярно очищайте данные просмотра: Это включает файлы cookie, кэш и историю просмотра",
                    "Эти основы формируют фундамент более безопасного веб-серфинга, но это только начало."
                ],
                "alert": {
                    "type": "warning",
                    "icon": "exclamation-triangle",
                    "title": "Риск расширений браузера",
                    "content": "Расширения браузера могут получить доступ ко всему, что вы делаете в браузере. Устанавливайте расширения только из надежных источников и регулярно проверяйте предоставленные им разрешения."
                }
            },
            {
                "title": "Распознавание безопасных веб-сайтов",
                "content": [
                    "Не все веб-сайты одинаково безопасны. Вот как определить более безопасные сайты:",
                    "• Проверяйте наличие HTTPS: Ищите 'https://' в начале адреса и значок замка в адресной строке",
                    "• Проверяйте адреса веб-сайтов: Обращайте внимание на опечатки или незначительные отличия, которые могут указывать на поддельный сайт",
                    "• Будьте осторожны с незнакомыми сайтами: Изучайте новые веб-сайты перед предоставлением какой-либо информации",
                    "• Ищите политики конфиденциальности и контактную информацию: Легитимные сайты обычно имеют их в легком доступе",
                    "• Проверяйте сигналы доверия: Обращайте внимание на профессиональный дизайн, обновленный контент и отзывы клиентов",
                    "• Используйте инструменты проверки безопасности сайтов: Такие как Google Safe Browsing, которые помогают выявить опасные сайты",
                    "Помните, что профессиональный внешний вид сам по себе не гарантирует легитимность сайта. Всегда проверяйте перед тем, как делиться конфиденциальной информацией."
                ],
                "image": {
                    "url": "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/svgs/solid/lock.svg",
                    "alt": "Безопасное HTTPS-соединение",
                    "caption": "Значок замка указывает на безопасное HTTPS-соединение, шифрующее данные между вашим браузером и веб-сайтом"
                }
            },
            {
                "title": "Защита вашей конфиденциальности при просмотре",
                "content": [
                    "Ваша активность в интернете может рассказать о вас многое. Вот как сохранить больше приватности:",
                    "• Используйте режим приватного просмотра: Это предотвращает сохранение браузером вашей истории, файлов cookie и данных сайтов",
                    "• Рассмотрите возможность использования VPN (виртуальной частной сети): Это шифрует ваше интернет-соединение и скрывает ваш IP-адрес",
                    "• Настройте параметры файлов cookie: Настройте браузер на удаление файлов cookie при его закрытии или блокировку сторонних файлов cookie",
                    "• Используйте поисковые системы, ориентированные на конфиденциальность: Такие как DuckDuckGo, которые не отслеживают ваши поисковые запросы",
                    "• Отключите отслеживание в браузере: Включите функцию 'Do Not Track' и другие функции защиты от отслеживания в вашем браузере",
                    "• Просматривайте разрешения браузера: Контролируйте, какие сайты могут получать доступ к вашему местоположению, камере, микрофону и уведомлениям",
                    "• Используйте блокировщики рекламы: Они могут уменьшить отслеживание и защитить от вредоносной рекламы (malvertising)",
                    "Имейте в виду, что полная анонимность в интернете труднодостижима. Эти меры повышают вашу конфиденциальность, но не гарантируют ее."
                ],
                "code": {
                    "language": "text",
                    "snippet": "# Контрольный список настроек конфиденциальности браузера\n\n1. Отключите сторонние файлы cookie\n2. Включите 'Do Not Track' (Не отслеживать)\n3. Блокируйте всплывающие окна\n4. Отключите отслеживание местоположения\n5. Просмотрите разрешения сайтов (камера, микрофон, уведомления)\n6. Установите строгую блокировку контента\n7. Включите режим HTTPS-only, если доступен\n8. Настройте автоматическое удаление истории просмотров и файлов cookie"
                }
            },
            {
                "title": "Избегание веб-угроз",
                "content": [
                    "Интернет содержит различные угрозы, направленные на компрометацию вашей безопасности. Вот как их избежать:",
                    "• Будьте осторожны с загрузками: Загружайте файлы только из надежных источников",
                    "• Сканируйте загрузки: Используйте антивирусное ПО для проверки загруженных файлов перед их открытием",
                    "• Остерегайтесь всплывающих окон: Избегайте нажатия на неожиданные всплывающие окна, особенно те, которые утверждают, что ваше устройство заражено",
                    "• Не нажимайте на подозрительные ссылки: Наведите курсор на ссылки, чтобы увидеть, куда они действительно ведут, прежде чем нажимать",
                    "• Будьте осторожны с онлайн-формами: Дважды подумайте, прежде чем отправлять личную информацию",
                    "• Остерегайтесь социальной инженерии: Скептически относитесь к срочным сообщениям или слишком хорошим, чтобы быть правдой, предложениям",
                    "• Используйте безопасные способы оплаты: При покупках в интернете используйте кредитные карты или защищенные платежные сервисы с защитой от мошенничества",
                    "Помните, что большинство веб-атак требуют от вас каких-либо действий. Взятие момента на оценку перед нажатием или загрузкой может предотвратить многие проблемы безопасности."
                ]
            }
        ],
        "key_takeaways": [
            "Поддерживайте браузер в актуальном состоянии и используйте функции безопасности, такие как режим HTTPS-only",
            "Ищите HTTPS и проверяйте адреса веб-сайтов перед тем, как делиться информацией",
            "Используйте инструменты конфиденциальности, такие как приватный просмотр, VPN и поисковые системы, ориентированные на приватность",
            "Будьте осторожны с загрузками, всплывающими окнами и запросами личной информации",
            "Рассмотрите возможность использования расширений безопасности от надежных провайдеров для усиления защиты"
        ],
        "exercise": {
            "title": "Проверка безопасности браузера",
            "description": "Оцените и улучшите настройки безопасности вашего основного веб-браузера.",
            "steps": [
                "Откройте меню настроек или предпочтений вашего браузера",
                "Проверьте, что ваш браузер обновлен до последней версии",
                "Просмотрите и настройте параметры конфиденциальности (файлы cookie, отслеживание, история просмотров)",
                "Настройте разрешения для контента (местоположение, камера, микрофон, уведомления)",
                "Просмотрите установленные расширения и удалите те, которые вы не распознаете или не используете",
                "Включите все доступные функции безопасности (защита от фишинга, сканирование на вредоносное ПО)",
                "Установите регулярное расписание для очистки данных просмотра"
            ],
            "hint": "Большинство браузеров имеют раздел безопасности или конфиденциальности в настройках, где вы можете найти большинство этих опций. Если вы не уверены в конкретной настройке, поищите название вашего браузера и настройки, чтобы найти документацию."
        },
        "further_reading": [
            {
                "title": "Mozilla's Privacy & Security Guide",
                "url": "https://support.mozilla.org/en-US/products/firefox/privacy-and-security",
                "description": "Комплексное руководство по функциям конфиденциальности и безопасности в Firefox"
            },
            {
                "title": "Electronic Frontier Foundation's Surveillance Self-Defense",
                "url": "https://ssd.eff.org/",
                "description": "Советы, инструменты и учебные материалы для более безопасного общения в Интернете"
            },
            {
                "title": "Google's Safety Center",
                "url": "https://safety.google/",
                "description": "Ресурсы для повышения безопасности при использовании продуктов Google"
            }
        ],
        "related_tutorials": [
            {
                "id": "cybersecurity-threats",
                "title": "Распространенные киберугрозы",
                "difficulty": "Начинающий"
            },
            {
                "id": "private-browsing",
                "title": "Использование VPN для приватности",
                "difficulty": "Средний"
            },
            {
                "id": "social-engineering",
                "title": "Распознавание атак социальной инженерии",
                "difficulty": "Начинающий"
            }
        ]
    },
    {
        "id": "home-network-security",
        "title": "Защита домашней сети",
        "description": "Узнайте, как защитить домашнюю сеть Wi-Fi и подключенные устройства.",
        "category": "network-security",
        "difficulty": "Начинающий",
        "duration": "25 мин",
        "objectives": "Понять риски безопасности сети, настроить параметры безопасности роутера и защитить подключенные устройства.",
        "introduction": "Ваша домашняя сеть — это шлюз, соединяющий все ваши устройства с интернетом. В случае взлома злоумышленники могут получить доступ к личным данным, отслеживать вашу онлайн-активность или использовать вашу сеть в злонамеренных целях. Этот учебник проведет вас через практические шаги по защите вашей домашней сети, обеспечивая защиту вашей цифровой жизни с самого основания.",
        "sections": [
            {
                "title": "Понимание уязвимостей домашней сети",
                "content": [
                    "Ваша домашняя сеть сталкивается с несколькими потенциальными рисками безопасности:",
                    "• Несанкционированный доступ: Другие используют вашу сеть без разрешения",
                    "• Перехват трафика: Злоумышленники перехватывают данные, отправляемые по вашей сети",
                    "• Компрометация устройств: Взлом уязвимых устройств",
                    "• Уязвимости роутера: Устаревшая прошивка с недостатками безопасности",
                    "• Настройки по умолчанию: Заводские конфигурации, которые изначально небезопасны",
                    "• Незащищенные IoT-устройства: Устройства умного дома со слабой защитой",
                    "Эти уязвимости могут привести к нарушению конфиденциальности, краже личных данных или даже использованию вашей сети в более широких атаках. Хорошая новость в том, что большинство из них можно устранить с помощью простых изменений конфигурации."
                ],
                "image": {
                    "url": "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/svgs/solid/wifi.svg",
                    "alt": "Иллюстрация домашней сети",
                    "caption": "Ваша домашняя сеть соединяет все ваши устройства с интернетом и требует правильной настройки безопасности"
                }
            },
            {
                "title": "Защита роутера",
                "content": [
                    "Ваш роутер является центральной точкой вашей сети и первой линией защиты. Вот как его защитить:",
                    "1. Измените учетные данные для входа по умолчанию:",
                    "   • Получите доступ к интерфейсу администратора роутера (обычно введя 192.168.0.1 или 192.168.1.1 в браузере)",
                    "   • Измените как имя пользователя администратора, так и пароль на надежные, уникальные значения",
                    "",
                    "2. Обновите прошивку роутера:",
                    "   • Проверьте наличие обновлений прошивки в интерфейсе администратора роутера",
                    "   • Включите автоматические обновления, если они доступны",
                    "",
                    "3. Используйте надежное шифрование:",
                    "   • Настройте Wi-Fi на использование WPA3, если доступно, или как минимум WPA2",
                    "   • Никогда не используйте устаревший протокол WEP",
                    "",
                    "4. Установите надежный пароль Wi-Fi:",
                    "   • Создайте уникальную, сложную парольную фразу длиной не менее 12 символов",
                    "   • Рассмотрите возможность периодической смены пароля",
                    "",
                    "5. Отключите удаленное управление:",
                    "   • Выключите удаленный доступ к интерфейсу администратора роутера",
                    "   • Управляйте роутером только при подключении к домашней сети",
                    "",
                    "6. Измените имя сети по умолчанию (SSID):",
                    "   • Избегайте включения личной информации или модели роутера в названии",
                    "   • Рассмотрите возможность скрытия вашего SSID (хотя это обеспечивает лишь минимальную безопасность)"
                ],
                "alert": {
                    "type": "info",
                    "icon": "info-circle",
                    "title": "Доступ к роутеру",
                    "content": "Чтобы получить доступ к интерфейсу администратора роутера, вам понадобятся учетные данные для входа по умолчанию. Они обычно напечатаны на самом роутере или указаны в руководстве. Если вы не можете их найти, проверьте веб-сайт производителя или обратитесь к вашему интернет-провайдеру, если роутер предоставлен ими."
                }
            },
            {
                "title": "Enhancing Network Configuration",
                "content": [
                    "Beyond basic router security, consider these additional network protections:",
                    "• Enable the firewall: Most routers have a built-in firewall; make sure it's active",
                    "• Use guest networks: Create a separate network for visitors and IoT devices",
                    "• Disable unused features: Turn off services you don't use, like WPS (Wi-Fi Protected Setup)",
                    "• Enable MAC address filtering: Restrict network access to specific devices (though this can be circumvented)",
                    "• Use DNS filtering: Consider services like OpenDNS or NextDNS to block malicious websites",
                    "• Implement access schedules: Set time limits for when devices can connect to the internet",
                    "• Monitor connected devices: Regularly check what devices are connected to your network",
                    "These configurations create multiple layers of protection for your network."
                ],
                "code": {
                    "language": "text",
                    "snippet": "# Common router IP addresses for admin access:\n\n192.168.0.1\n192.168.1.1\n10.0.0.1\n192.168.2.1\n\n# To find your router IP on Windows:\nOpen Command Prompt and type: ipconfig\nLook for \"Default Gateway\"\n\n# To find your router IP on Mac/Linux:\nOpen Terminal and type: netstat -nr | grep default"
                }
            },
            {
                "title": "Protecting Connected Devices",
                "content": [
                    "Even with a secure network, individual devices need protection:",
                    "• Keep all devices updated: Install security updates for computers, phones, and IoT devices",
                    "• Use security software: Install antivirus/anti-malware on compatible devices",
                    "• Enable device firewalls: Activate built-in firewalls on computers and other capable devices",
                    "• Secure IoT devices: Change default passwords and update firmware on smart home devices",
                    "• Disable unnecessary connections: Turn off Bluetooth, Wi-Fi, and other connections when not in use",
                    "• Use VPNs on public networks: Protect devices when they're away from your secure home network",
                    "• Practice safe browsing: Be cautious about what you download and which sites you visit",
                    "Remember that your network security is only as strong as your weakest device."
                ]
            }
        ],
        "key_takeaways": [
            "Your router is your first line of defense - secure it with strong credentials and updated firmware",
            "Use WPA3 or WPA2 encryption with a strong, unique Wi-Fi password",
            "Create guest networks for visitors and IoT devices to isolate them from your main network",
            "Regularly update all connected devices and change default passwords",
            "Monitor your network for unknown devices that might indicate unauthorized access"
        ],
        "exercise": {
            "title": "Home Network Security Audit",
            "description": "Evaluate and improve the security of your home network.",
            "steps": [
                "Log into your router's admin interface (using the router IP address in a web browser)",
                "Check if your router's firmware is up to date and update if necessary",
                "Verify you're using WPA2 or WPA3 encryption for your Wi-Fi",
                "Change your Wi-Fi password to a strong, unique passphrase",
                "Create a guest network for visitors and IoT devices if your router supports it",
                "Make a list of all devices connected to your network and verify they belong to you",
                "Check for and disable unnecessary features like WPS or remote administration"
            ],
            "hint": "If you're unsure how to access specific settings, search for your router's model number followed by 'manual' or 'user guide' to find documentation."
        },
        "further_reading": [
            {
                "title": "FTC's guidance on securing your wireless network",
                "url": "https://consumer.ftc.gov/articles/how-secure-your-home-wi-fi-network",
                "description": "Government recommendations for home network security"
            },
            {
                "title": "Router Security Checklist by CISA",
                "url": "https://www.cisa.gov/sites/default/files/publications/Securing_the_Internet_of_Things_Infographic_S508C.pdf",
                "description": "Cybersecurity & Infrastructure Security Agency router security guidance"
            },
            {
                "title": "IoT Security Foundation",
                "url": "https://www.iotsecurityfoundation.org/best-practice-guidelines/",
                "description": "Best practices for securing Internet of Things devices"
            }
        ],
        "related_tutorials": [
            {
                "id": "secure-browsing",
                "title": "Safe Web Browsing Practices",
                "difficulty": "Beginner"
            },
            {
                "id": "private-browsing",
                "title": "Using VPNs for Privacy",
                "difficulty": "Intermediate"
            },
            {
                "id": "iot-security",
                "title": "Smart Home Device Security",
                "difficulty": "Intermediate"
            }
        ]
    },
    # Web Security Category
    {
        "id": "website-safety",
        "title": "Evaluating Website Security",
        "description": "Learn how to identify secure websites and avoid dangerous ones.",
        "category": "web-security",
        "difficulty": "Beginner",
        "duration": "15 min",
        "objectives": "Understand how to identify secure websites, recognize warning signs of malicious sites, and safely browse the web.",
        "introduction": "Every day, we visit numerous websites for shopping, banking, social media, and information. Not all of these sites are equally secure, and some may even be dangerous. This tutorial will teach you how to evaluate website security and make informed decisions about which sites to trust with your information and activities.",
        "sections": [
            {
                "title": "The Basics of Website Security",
                "content": [
                    "Website security involves several layers of protection that help ensure your data remains private and safe from attackers. Here are the fundamental aspects to understand:",
                    "• HTTPS: Secure websites use HTTPS protocol, which encrypts data transmitted between your browser and the website",
                    "• SSL/TLS certificates: Digital certificates that verify a website's identity and enable encrypted connections",
                    "• Content security: Protections against malicious code execution and data theft",
                    "• Authentication: Secure login systems to verify user identities",
                    "• Data protection: How websites store and handle your personal information",
                    "As a user, you can't see all these protections, but there are visible indicators that can help you assess a website's security."
                ],
                "alert": {
                    "type": "warning",
                    "icon": "exclamation-triangle",
                    "title": "Critical Information",
                    "content": "Never enter sensitive information (credit card details, passwords, personal data) on websites without HTTPS. The data could be intercepted by attackers."
                }
            },
            {
                "title": "Identifying Secure Websites",
                "content": [
                    "When visiting a website, check for these security indicators:",
                    "1. HTTPS and padlock icon:",
                    "   • Look for 'https://' at the beginning of the website address",
                    "   • Check for a padlock icon in the address bar",
                    "   • Click on the padlock to view the site's security certificate information",
                    "",
                    "2. Website address verification:",
                    "   • Carefully check the domain name (the main part of the URL)",
                    "   • Watch for typos or slight variations (e.g., 'am a zon.com' instead of 'amazon.com')",
                    "   • Be wary of subdomains that might trick you (e.g., 'amazon.fake-site.com' is not Amazon)",
                    "",
                    "3. Trust indicators:",
                    "   • Look for security seals or trust badges from recognized organizations",
                    "   • Check for clear contact information, including physical address and phone number",
                    "   • Verify the site has a privacy policy and terms of service",
                    "",
                    "4. Website professionalism:",
                    "   • Professional sites typically have few grammatical errors",
                    "   • Navigation should work properly with no broken links",
                    "   • Content should be updated regularly"
                ],
                "image": {
                    "url": "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/svgs/solid/lock.svg",
                    "alt": "HTTPS Lock Icon",
                    "caption": "The padlock icon indicates a secure HTTPS connection, an essential feature for any site handling sensitive information"
                }
            },
            {
                "title": "Warning Signs of Unsafe Websites",
                "content": [
                    "Be alert for these red flags that may indicate an unsafe or fraudulent website:",
                    "• No HTTPS: The site uses only HTTP rather than HTTPS",
                    "• Browser warnings: Your browser displays security warnings about the site",
                    "• Poor design and functionality: The site looks unprofessional or poorly maintained",
                    "• Too good to be true: Offers that seem unrealistically generous",
                    "• Excessive pop-ups: Numerous pop-up windows, especially those that are difficult to close",
                    "• Pressure tactics: Countdown timers or urgent messages pushing immediate action",
                    "• Unusual payment methods: Requests for wire transfers, gift cards, or cryptocurrency only",
                    "• Missing information: No privacy policy, terms of service, or contact information",
                    "• Mismatched or suspicious URLs: The address doesn't match the purported organization",
                    "• Excessive information requests: Asking for more personal information than necessary",
                    "If you notice multiple red flags, it's best to leave the site immediately without entering any information."
                ],
                "code": {
                    "language": "text",
                    "snippet": "# How to check a website's reputation:\n\n1. Search for reviews of the website (e.g., \"is example.com safe\" or \"example.com reviews\")\n\n2. Use website safety checkers:\n   - Google Transparency Report: https://transparencyreport.google.com/safe-browsing/search\n   - Norton Safe Web: https://safeweb.norton.com\n   - McAfee WebAdvisor: https://www.mcafee.com/consumer/en-us/landing-page/webadvisor.html\n   - VirusTotal: https://www.virustotal.com/gui/home/url\n\n3. Check the WHOIS information to see when the domain was registered and by whom:\n   - https://lookup.icann.org\n   - https://whois.domaintools.com"
                }
            },
            {
                "title": "Taking Action When Unsure",
                "content": [
                    "If you're uncertain about a website's security, take these precautions:",
                    "1. Research before sharing information:",
                    "   • Search for reviews or information about the website",
                    "   • Look for the company on social media or business directories",
                    "   • Check if they have an established presence elsewhere",
                    "",
                    "2. Use protective tools:",
                    "   • Enable your browser's phishing and malware protection",
                    "   • Consider using extensions like Web of Trust (WOT) or similar trust indicators",
                    "   • Keep your antivirus and browser updated",
                    "",
                    "3. Minimize risk:",
                    "   • Use guest checkout instead of creating accounts when possible",
                    "   • Consider using virtual credit cards or payment services like PayPal",
                    "   • Never share sensitive information like your Social Security number unless absolutely necessary",
                    "",
                    "4. Trust your instincts:",
                    "   • If something feels wrong about a website, it probably is",
                    "   • There are almost always alternative websites for what you need",
                    "   • No deal or offer is worth compromising your security"
                ]
            }
        ],
        "key_takeaways": [
            "Always look for HTTPS and the padlock icon before entering sensitive information",
            "Verify website addresses carefully to avoid lookalike or imposter sites",
            "Be suspicious of websites with poor design, grammar errors, or excessive pop-ups",
            "Research unfamiliar websites before making purchases or creating accounts",
            "Use browser security features and website reputation tools when in doubt"
        ],
        "exercise": {
            "title": "Website Security Evaluation Practice",
            "description": "Assess the security of websites you regularly visit to practice identifying security features and potential issues.",
            "steps": [
                "Make a list of 5-10 websites you use regularly (shopping, banking, social media, news, etc.)",
                "For each website, check if it uses HTTPS by looking for the padlock icon",
                "Click the padlock icon to view the security certificate information",
                "Look for the privacy policy and review what data the site collects",
                "Search for reviews or information about the security of each site",
                "Note any sites that have concerning security practices and consider alternatives"
            ],
            "hint": "Pay special attention to websites where you share financial information or personal data. These should have the highest level of security."
        },
        "further_reading": [
            {
                "title": "Google's Safety Center",
                "url": "https://safety.google/security/security-tips/",
                "description": "Tips for staying safe online from Google"
            },
            {
                "title": "Mozilla's HTTPS Explainer",
                "url": "https://support.mozilla.org/en-US/kb/how-do-i-tell-if-my-connection-is-secure",
                "description": "How to tell if your connection to a website is secure"
            },
            {
                "title": "FTC's Online Shopping Tips",
                "url": "https://consumer.ftc.gov/articles/online-shopping",
                "description": "Tips for safe online shopping from the Federal Trade Commission"
            }
        ],
        "related_tutorials": [
            {
                "id": "secure-browsing",
                "title": "Safe Web Browsing Practices",
                "difficulty": "Beginner"
            },
            {
                "id": "phishing-protection",
                "title": "Protecting Against Phishing",
                "difficulty": "Beginner"
            },
            {
                "id": "online-shopping-security",
                "title": "Secure Online Shopping",
                "difficulty": "Beginner"
            }
        ]
    },
    {
        "id": "phishing-protection",
        "title": "Protecting Against Phishing",
        "description": "Learn to identify and avoid phishing attacks that try to steal your information.",
        "category": "web-security",
        "difficulty": "Beginner",
        "duration": "20 min",
        "objectives": "Understand what phishing is, learn to identify phishing attempts, and develop strategies to protect yourself.",
        "introduction": "Phishing is one of the most common and effective cyber attacks, using deception to trick people into revealing sensitive information or installing malware. These attacks can come through email, text messages, social media, or even phone calls. This tutorial will help you recognize phishing attempts and take steps to protect yourself from these increasingly sophisticated scams.",
        "sections": [
            {
                "title": "Understanding Phishing Attacks",
                "content": [
                    "Phishing is a type of social engineering attack where attackers masquerade as trusted entities to trick victims into revealing sensitive information or taking harmful actions. Here's what you need to know:",
                    "• Phishing primarily works by exploiting trust rather than technical vulnerabilities",
                    "• Attacks can target individuals (spear phishing) or cast a wide net with generic messages",
                    "• The goal is typically to steal credentials, financial information, or personal data",
                    "• Attackers may also attempt to install malware or ransomware",
                    "• Phishing comes in many forms across various communication channels",
                    "Understanding the basic types of phishing can help you identify potential attacks:"
                ],
                "image": {
                    "url": "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/svgs/solid/fish.svg",
                    "alt": "Phishing Illustration",
                    "caption": "Phishing attempts to 'hook' victims by impersonating legitimate organizations"
                }
            },
            {
                "title": "Common Types of Phishing",
                "content": [
                    "Phishing attacks come in several varieties, each with distinct characteristics:",
                    "• Email phishing: The most common type, using fraudulent emails that appear to come from legitimate organizations",
                    "• Spear phishing: Targeted attacks customized for specific individuals, often using personal information",
                    "• Whaling: Targeting high-profile individuals like executives or politicians",
                    "• Smishing: Phishing via SMS text messages",
                    "• Vishing: Voice phishing using phone calls",
                    "• Clone phishing: Replicating legitimate communications but replacing links or attachments with malicious ones",
                    "• Search engine phishing: Creating fake websites that appear in search results",
                    "• Business Email Compromise (BEC): Impersonating executives to request wire transfers or sensitive information",
                    "The techniques evolve constantly, but the core strategy remains the same: manipulation through impersonation."
                ],
                "alert": {
                    "type": "danger",
                    "icon": "exclamation-circle",
                    "title": "Increasing Sophistication",
                    "content": "Modern phishing attempts are becoming increasingly sophisticated, with fewer spelling errors, professional designs, and even interactive elements. Never assume you're too savvy to be fooled."
                }
            },
            {
                "title": "How to Identify Phishing Attempts",
                "content": [
                    "While phishing attacks are becoming more sophisticated, they often contain tell-tale signs that can help you identify them:",
                    "1. Suspicious sender addresses:",
                    "   • Slight misspellings in domain names (microsoftsupport.com instead of microsoft.com)",
                    "   • Personal email domains for business communications (amazon-support@gmail.com)",
                    "   • Mismatched sender name and email address",
                    "",
                    "2. Urgency and pressure tactics:",
                    "   • Messages creating a sense of emergency or requiring immediate action",
                    "   • Threats of negative consequences if you don't act quickly",
                    "   • Limited-time offers that are too good to be true",
                    "",
                    "3. Suspicious links and attachments:",
                    "   • Links that don't match the purported destination (hover without clicking to check)",
                    "   • Shortened URLs that hide the actual destination",
                    "   • Unexpected attachments, especially executable files (.exe, .zip, .scr)",
                    "",
                    "4. Content red flags:",
                    "   • Generic greetings (\"Dear User\" instead of your name)",
                    "   • Grammatical errors and unusual phrasing",
                    "   • Requests for sensitive information",
                    "   • Inconsistent branding or formatting",
                    "",
                    "Always verify suspicious communications through official channels before taking any requested action."
                ],
                "code": {
                    "language": "text",
                    "snippet": "# How to verify email headers and links\n\n## Checking the true destination of a link:\n1. Hover your mouse over the link (don't click)\n2. Look at the status bar or popup to see the actual URL\n3. Check if the domain matches the expected organization\n\n## Examining email headers (advanced):\n- In Gmail: Click the three dots → \"Show original\"\n- In Outlook: Open email → File → Properties → \"Internet headers\"\n\n## Red flags in URLs:\n- Misspellings (microsft.com vs microsoft.com)\n- Extra words (paypal-secure.com vs paypal.com)\n- Unexpected subdomains (login.paypal.phishing.com)\n- Unusual TLDs (.xyz, .tk instead of .com, .org)"
                }
            },
            {
                "title": "Protecting Yourself from Phishing",
                "content": [
                    "Take these steps to minimize your risk from phishing attacks:",
                    "• Verify before acting: Independently contact the organization through official channels if you're unsure",
                    "• Never click suspicious links: Type the official website address directly in your browser",
                    "• Be cautious with attachments: Scan them with security software before opening",
                    "• Use multi-factor authentication: This provides an extra layer of protection even if credentials are compromised",
                    "• Keep software updated: Ensure your devices and applications have the latest security patches",
                    "• Use email filtering: Enable spam filters and security features in your email service",
                    "• Be skeptical of urgency: Legitimate organizations rarely demand immediate action",
                    "• Report phishing attempts: Use the reporting features in your email client or forward to relevant authorities",
                    "• Educate yourself: Stay informed about current phishing techniques",
                    "Remember that even tech-savvy individuals can fall victim to sophisticated phishing. Always maintain a healthy skepticism."
                ]
            }
        ],
        "key_takeaways": [
            "Phishing attacks attempt to steal information by impersonating trusted entities",
            "Red flags include urgency, suspicious links, generic greetings, and requests for sensitive information",
            "Always verify communications through official channels before taking action",
            "Enable multi-factor authentication to protect accounts even if credentials are compromised",
            "Report phishing attempts to help protect others and improve security systems"
        ],
        "exercise": {
            "title": "Phishing Email Analysis",
            "description": "Practice identifying phishing attempts by analyzing sample emails.",
            "steps": [
                "Review your email spam folder for potential phishing attempts",
                "For each suspicious email, check the sender's address for inconsistencies",
                "Hover over links (without clicking) to see the actual destination",
                "Look for urgency, generic greetings, and requests for personal information",
                "Note grammatical errors or unusual phrasing",
                "Consider whether you were expecting this communication",
                "Determine whether the email is legitimate or a phishing attempt"
            ],
            "hint": "If you can't find examples in your own inbox, search for 'phishing email examples' online to see samples. The more examples you study, the better you'll become at spotting real attempts."
        },
        "further_reading": [
            {
                "title": "Phishing.org",
                "url": "https://www.phishing.org/what-is-phishing",
                "description": "Comprehensive resource on phishing attacks and prevention"
            },
            {
                "title": "FTC Phishing Guidance",
                "url": "https://consumer.ftc.gov/articles/how-recognize-and-avoid-phishing-scams",
                "description": "Federal Trade Commission guide to recognizing and avoiding phishing"
            },
            {
                "title": "CISA Phishing Page",
                "url": "https://www.cisa.gov/topics/cyber-threats-and-advisories/types-threats/phishing",
                "description": "Cybersecurity and Infrastructure Security Agency resources on phishing"
            }
        ],
        "related_tutorials": [
            {
                "id": "social-engineering",
                "title": "Recognizing Social Engineering Attacks",
                "difficulty": "Beginner"
            },
            {
                "id": "secure-browsing",
                "title": "Safe Web Browsing Practices",
                "difficulty": "Beginner"
            },
            {
                "id": "two-factor-authentication",
                "title": "Setting Up Two-Factor Authentication",
                "difficulty": "Beginner"
            }
        ]
    },
    # Privacy Category
    {
        "id": "data-privacy",
        "title": "Protecting Your Digital Privacy",
        "description": "Learn how to protect your personal information and maintain privacy online.",
        "category": "privacy",
        "difficulty": "Beginner",
        "duration": "25 min",
        "objectives": "Understand digital privacy threats, learn strategies to protect personal information, and take control of your online privacy.",
        "introduction": "In today's connected world, our personal information is constantly being collected, shared, and sometimes exploited. Digital privacy refers to your ability to control what personal information is collected about you and how it's used. This tutorial will help you understand privacy threats and take practical steps to protect your personal data online.",
        "sections": [
            {
                "title": "Understanding Digital Privacy",
                "content": [
                    "Digital privacy concerns the protection of your personal information in online environments. Here's what you need to understand:",
                    "• Personal data is valuable: Companies collect data to target ads, develop products, or sell to third parties",
                    "• Privacy vs. security: Privacy is about controlling your information, while security protects it from unauthorized access",
                    "• The digital footprint: Everything you do online leaves traces that can be collected and analyzed",
                    "• Data collection mechanisms: Cookies, tracking pixels, browser fingerprinting, and other technologies track your activities",
                    "• Legal frameworks: Regulations like GDPR (Europe) and CCPA (California) provide some privacy protections",
                    "Being aware of how your data is collected is the first step toward protecting it."
                ],
                "alert": {
                    "type": "info",
                    "icon": "info-circle",
                    "title": "Your Data's Value",
                    "content": "The average internet user generates significant value through their data. Estimates suggest individuals' data is worth hundreds or thousands of dollars annually to advertisers and data brokers."
                }
            },
            {
                "title": "Common Privacy Threats",
                "content": [
                    "Various entities may compromise your privacy in different ways:",
                    "• Data collection by websites and apps: Almost all online services collect information about users",
                    "• Third-party tracking: Advertising networks track your browsing across multiple sites",
                    "• Social media oversharing: Revealing too much personal information on social platforms",
                    "• Data breaches: Unauthorized access to databases containing your personal information",
                    "• Location tracking: GPS, Wi-Fi, and Bluetooth can reveal your physical movements",
                    "• Invasive permissions: Apps requesting access to more data than they need to function",
                    "• Public Wi-Fi snooping: Unencrypted networks allow others to intercept your traffic",
                    "• Metadata collection: Information about your communications (who, when, how long) even if content is private",
                    "Different privacy threats require different protective strategies."
                ],
                "image": {
                    "url": "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/svgs/solid/user-shield.svg",
                    "alt": "Digital Privacy Protection",
                    "caption": "Protecting your personal information requires a multi-layered approach to privacy"
                }
            },
            {
                "title": "Browser Privacy Techniques",
                "content": [
                    "Your web browser is a primary point for data collection. Here's how to enhance browser privacy:",
                    "1. Choose a privacy-focused browser:",
                    "   • Options include Firefox, Brave, or Tor Browser",
                    "   • Each offers different balances of privacy vs. convenience",
                    "",
                    "2. Adjust browser settings:",
                    "   • Block third-party cookies",
                    "   • Enable 'Do Not Track'",
                    "   • Use HTTPS-only mode",
                    "   • Clear browsing data regularly",
                    "",
                    "3. Use privacy extensions:",
                    "   • Ad blockers (uBlock Origin)",
                    "   • Tracker blockers (Privacy Badger)",
                    "   • HTTPS enforcers (HTTPS Everywhere)",
                    "   • Cookie managers (Cookie AutoDelete)",
                    "",
                    "4. Consider more advanced techniques:",
                    "   • Compartmentalize browsing with different browsers or profiles",
                    "   • Use private/incognito mode for sensitive browsing",
                    "   • Consider a VPN for additional privacy"
                ],
                "code": {
                    "language": "text",
                    "snippet": "# Recommended Privacy Browser Extensions\n\n## Essential Extensions:\n- uBlock Origin: Block ads and trackers\n- Privacy Badger: Learns to block invisible trackers\n- HTTPS Everywhere: Enforces secure connections\n- Decentraleyes: Protects against CDN tracking\n\n## Additional Privacy Tools:\n- Cookie AutoDelete: Automatically removes cookies\n- NoScript: Block JavaScript from untrusted sources\n- CanvasBlocker: Prevents fingerprinting\n- Disconnect: Visualizes and blocks trackers\n\n## To check your browser fingerprint:\n- Visit: https://coveryourtracks.eff.org/\n- Test how unique your browser appears to trackers"
                }
            },
            {
                "title": "Everyday Privacy Practices",
                "content": [
                    "Beyond browser settings, incorporate these privacy practices into your daily digital life:",
                    "• Audit app permissions: Review and restrict what data your apps can access",
                    "• Use privacy-focused alternatives: Consider services like ProtonMail (email), Signal (messaging), or DuckDuckGo (search)",
                    "• Read privacy policies: Pay attention to how services use your data, especially for financial or health apps",
                    "• Manage social media privacy: Regularly review and update privacy settings on all platforms",
                    "• Limit data sharing: Only provide necessary information when signing up for services",
                    "• Use strong, unique passwords: Prevent unauthorized access to your accounts",
                    "• Enable two-factor authentication: Add an extra layer of security",
                    "• Be mindful of public Wi-Fi: Use a VPN when connecting to public networks",
                    "• Regularly delete unused accounts: Reduce your digital footprint",
                    "• Check data breach notifications: Use services like Have I Been Pwned to monitor for compromised accounts",
                    "Small changes in habits can significantly improve your overall privacy posture."
                ]
            }
        ],
        "key_takeaways": [
            "Digital privacy is about controlling what personal information is collected and how it's used",
            "Privacy threats include tracking, data collection, and oversharing on social media",
            "Browser settings and privacy extensions can significantly reduce tracking",
            "Choose privacy-focused alternatives for essential services like email and messaging",
            "Regularly audit app permissions and social media privacy settings"
        ],
        "exercise": {
            "title": "Personal Privacy Audit",
            "description": "Evaluate and improve your current digital privacy practices.",
            "steps": [
                "Check your browser's privacy settings and adjust them for better protection",
                "Install at least one privacy-enhancing browser extension",
                "Review app permissions on your mobile device and revoke unnecessary access",
                "Check privacy settings on your social media accounts",
                "Search for yourself online to see what information is publicly available",
                "Set up alerts for data breaches through a service like Have I Been Pwned",
                "Create a plan to gradually adopt more privacy-focused services"
            ],
            "hint": "Focus on improving one aspect of your privacy at a time. Start with the areas that contain your most sensitive information, such as financial apps or email."
        },
        "further_reading": [
            {
                "title": "Electronic Frontier Foundation's Surveillance Self-Defense",
                "url": "https://ssd.eff.org/",
                "description": "Comprehensive guide to protecting yourself from surveillance and data collection"
            },
            {
                "title": "Privacy Tools",
                "url": "https://www.privacytools.io/",
                "description": "Curated list of privacy-focused software and services"
            },
            {
                "title": "Data Detox Kit",
                "url": "https://datadetoxkit.org/en/home",
                "description": "Simple steps to reduce your data footprint online"
            }
        ],
        "related_tutorials": [
            {
                "id": "secure-browsing",
                "title": "Safe Web Browsing Practices",
                "difficulty": "Beginner"
            },
            {
                "id": "social-media-privacy",
                "title": "Securing Your Social Media Accounts",
                "difficulty": "Beginner"
            },
            {
                "id": "private-browsing",
                "title": "Using VPNs for Privacy",
                "difficulty": "Intermediate"
            }
        ]
    },
    {
        "id": "social-media-privacy",
        "title": "Securing Your Social Media Accounts",
        "description": "Learn how to protect your privacy and security on social media platforms.",
        "category": "privacy",
        "difficulty": "Beginner",
        "duration": "20 min",
        "objectives": "Understand social media privacy risks, configure account privacy settings, and develop safe sharing habits.",
        "introduction": "Social media has become an integral part of our lives, but it can also expose personal information in ways we don't intend. From data collection by the platforms themselves to oversharing that can lead to identity theft or stalking, social media presents unique privacy and security challenges. This tutorial will help you secure your social media accounts and develop mindful sharing habits.",
        "sections": [
            {
                "title": "Social Media Privacy Risks",
                "content": [
                    "Understanding the risks is the first step to protecting yourself on social media. Key concerns include:",
                    "• Data collection by platforms: Social media companies collect extensive data about your activities, preferences, and connections",
                    "• Third-party app access: Apps connected to your social accounts can access your data and friends list",
                    "• Oversharing personal information: Revealing too much about your identity, location, or schedule",
                    "• Phishing and social engineering: Targeted attacks based on information gleaned from your profiles",
                    "• Account hacking: Unauthorized access to your accounts through weak passwords or security questions",
                    "• Location tagging: Inadvertently revealing your physical location to potential stalkers or burglars",
                    "• Image privacy: Photos containing metadata or recognizable locations that reveal more than intended",
                    "• Future implications: Posts that might affect employment opportunities or personal relationships"
                ],
                "alert": {
                    "type": "warning",
                    "icon": "exclamation-triangle",
                    "title": "Oversharing Risks",
                    "content": "Information shared on social media has been used for identity theft, stalking, home burglaries (when people post about being away), and employment screening. Once information is online, it can be difficult to completely remove."
                }
            },
            {
                "title": "Securing Your Social Media Accounts",
                "content": [
                    "Take these steps to protect your accounts from unauthorized access:",
                    "1. Use strong authentication:",
                    "   • Create a strong, unique password for each social media account",
                    "   • Enable two-factor authentication wherever available",
                    "   • Be careful with security questions (don't use easily researched answers)",
                    "",
                    "2. Review connected apps and services:",
                    "   • Regularly audit which third-party apps have access to your accounts",
                    "   • Remove access for apps you no longer use or don't recognize",
                    "   • Be selective about granting permissions to new apps",
                    "",
                    "3. Configure login alerts:",
                    "   • Set up notifications for logins from new devices or locations",
                    "   • Review active sessions and log out from unfamiliar devices",
                    "",
                    "4. Keep software updated:",
                    "   • Update your social media apps to get the latest security patches",
                    "   • Keep your device operating systems current",
                    "",
                    "Regularly performing these security checks can prevent unauthorized access to your accounts."
                ],
                "image": {
                    "url": "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/svgs/solid/user-lock.svg",
                    "alt": "Social Media Account Security",
                    "caption": "Securing access to your social media accounts is the foundation of social media privacy"
                }
            },
            {
                "title": "Configuring Privacy Settings",
                "content": [
                    "Each social media platform offers privacy controls. Here are key settings to adjust on major platforms:",
                    "Facebook:",
                    "• Profile visibility: Limit who can see your profile information",
                    "• Post audience: Control who sees each post (Public, Friends, Custom)",
                    "• Tag review: Approve tags before they appear on your timeline",
                    "• Search engine links: Prevent search engines from linking to your profile",
                    "• Face recognition: Disable facial recognition features",
                    "",
                    "Instagram:",
                    "• Account privacy: Set your account to private to approve followers",
                    "• Story controls: Choose who can see and respond to your stories",
                    "• Activity status: Hide when you're active on the platform",
                    "• Tags and mentions: Control who can tag you in posts",
                    "",
                    "Twitter:",
                    "• Tweet privacy: Protect your tweets so only followers can see them",
                    "• Photo tagging: Control who can tag you in photos",
                    "• Direct messages: Limit who can send you messages",
                    "• Discoverability: Control whether people can find you by email or phone",
                    "",
                    "LinkedIn:",
                    "• Profile viewing options: Control what others see when you view their profile",
                    "• Connection visibility: Choose who can see your connections",
                    "• Activity broadcasts: Control notifications about your activity",
                    "",
                    "Remember to review these settings regularly, as platforms often update their privacy options."
                ],
                "code": {
                    "language": "text",
                    "snippet": "# How to find privacy settings on major platforms\n\n## Facebook\nDesktop: Click your profile icon → Settings & Privacy → Settings → Privacy\nMobile app: Menu (three lines) → Settings & Privacy → Settings → Privacy Settings\n\n## Instagram\nDesktop: Click your profile → Settings → Privacy and Security\nMobile app: Profile → Menu (three lines) → Settings → Privacy\n\n## Twitter\nDesktop: More (three dots) → Settings and privacy → Privacy and safety\nMobile app: Profile icon → Settings and privacy → Privacy and safety\n\n## LinkedIn\nDesktop: Me → Settings & Privacy → Privacy\nMobile app: Profile icon → Settings → Privacy"
                }
            },
            {
                "title": "Mindful Sharing Practices",
                "content": [
                    "Beyond account settings, develop these habits for safer social media use:",
                    "• Think before posting: Consider the long-term implications of what you share",
                    "• Limit personal information: Be careful about sharing identifiers like your full birthdate, address, or phone number",
                    "• Be cautious with location data: Disable automatic location tagging and avoid real-time location sharing",
                    "• Review before tagging others: Get permission before tagging friends in posts or photos",
                    "• Use direct messages for sensitive content: Don't post private information on public timelines",
                    "• Be selective with friend/connection requests: Only connect with people you know and trust",
                    "• Periodically review your profile: Delete old posts or photos that no longer represent you",
                    "• Search yourself: Regularly check what information about you is publicly available",
                    "• Be aware of photos in the background: Check images for visible personal information (addresses, ID cards, financial information)",
                    "Remember that even with strict privacy settings, information shared on social media is never completely private."
                ]
            }
        ],
        "key_takeaways": [
            "Social media platforms collect extensive data about users and their activities",
            "Use strong, unique passwords and two-factor authentication to secure your accounts",
            "Regularly review and update privacy settings on all platforms",
            "Be mindful about what personal information you share, including in photos",
            "Consider the long-term implications of your social media presence"
        ],
        "exercise": {
            "title": "Social Media Privacy Checkup",
            "description": "Review and strengthen privacy settings across your social media accounts.",
            "steps": [
                "List all your active social media accounts",
                "For each platform, review and update privacy settings using the guide in this tutorial",
                "Check which third-party apps have access to each account and remove unnecessary connections",
                "Enable two-factor authentication on all platforms that offer it",
                "Search for yourself on each platform to see what's publicly visible",
                "Review recent posts and remove or restrict any that contain sensitive information",
                "Create a personal policy for what information you will and won't share on social media"
            ],
            "hint": "Start with the social media account you use most frequently, then work through the others. Take screenshots of your settings for future reference."
        },
        "further_reading": [
            {
                "title": "Data Detox Kit: Social Media",
                "url": "https://datadetoxkit.org/en/social-media/",
                "description": "Simple steps to minimize your data footprint on social media"
            },
            {
                "title": "Consumer Reports Security Planner",
                "url": "https://securityplanner.consumerreports.org/",
                "description": "Personalized security and privacy recommendations"
            },
            {
                "title": "Online Safety and Privacy: A Facebook Guide for Survivors",
                "url": "https://www.techsafety.org/resources-survivors/facebook-privacy-and-safety",
                "description": "Comprehensive guide to Facebook privacy for high-risk individuals"
            }
        ],
        "related_tutorials": [
            {
                "id": "data-privacy",
                "title": "Protecting Your Digital Privacy",
                "difficulty": "Beginner"
            },
            {
                "id": "password-security",
                "title": "Creating Strong Passwords",
                "difficulty": "Beginner"
            },
            {
                "id": "two-factor-authentication",
                "title": "Setting Up Two-Factor Authentication",
                "difficulty": "Beginner"
            }
        ]
    }
]
