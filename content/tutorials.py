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
                "title": "Улучшение конфигурации сети",
                "content": [
                    "Помимо базовой защиты роутера, рассмотрите эти дополнительные меры защиты сети:",
                    "• Включите брандмауэр: Большинство роутеров имеют встроенный брандмауэр; убедитесь, что он активен",
                    "• Используйте гостевые сети: Создайте отдельную сеть для посетителей и IoT-устройств",
                    "• Отключите неиспользуемые функции: Выключите сервисы, которые вы не используете, например WPS (Wi-Fi Protected Setup)",
                    "• Включите фильтрацию MAC-адресов: Ограничьте доступ к сети только определенными устройствами (хотя это можно обойти)",
                    "• Используйте DNS-фильтрацию: Рассмотрите сервисы типа OpenDNS или NextDNS для блокировки вредоносных веб-сайтов",
                    "• Реализуйте расписания доступа: Установите временные ограничения для подключения устройств к интернету",
                    "• Отслеживайте подключенные устройства: Регулярно проверяйте, какие устройства подключены к вашей сети",
                    "Эти конфигурации создают несколько уровней защиты для вашей сети."
                ],
                "code": {
                    "language": "text",
                    "snippet": "# Распространенные IP-адреса роутеров для доступа администратора:\n\n192.168.0.1\n192.168.1.1\n10.0.0.1\n192.168.2.1\n\n# Чтобы найти IP-адрес роутера в Windows:\nОткройте Командную строку и введите: ipconfig\nИщите \"Default Gateway\" (Шлюз по умолчанию)\n\n# Чтобы найти IP-адрес роутера в Mac/Linux:\nОткройте Терминал и введите: netstat -nr | grep default"
                }
            },
            {
                "title": "Защита подключенных устройств",
                "content": [
                    "Даже при защищенной сети отдельные устройства нуждаются в защите:",
                    "• Поддерживайте все устройства в актуальном состоянии: Устанавливайте обновления безопасности для компьютеров, телефонов и IoT-устройств",
                    "• Используйте программное обеспечение для безопасности: Установите антивирус/антивредоносное ПО на совместимые устройства",
                    "• Включите брандмауэры устройств: Активируйте встроенные брандмауэры на компьютерах и других поддерживающих это устройствах",
                    "• Защитите IoT-устройства: Измените пароли по умолчанию и обновите прошивку на устройствах умного дома",
                    "• Отключайте ненужные соединения: Выключайте Bluetooth, Wi-Fi и другие соединения, когда они не используются",
                    "• Используйте VPN в общественных сетях: Защищайте устройства, когда они находятся вне вашей защищенной домашней сети",
                    "• Практикуйте безопасный просмотр: Будьте осторожны с тем, что вы загружаете и какие сайты посещаете",
                    "Помните, что безопасность вашей сети настолько сильна, насколько сильно ваше самое слабое устройство."
                ]
            }
        ],
        "key_takeaways": [
            "Ваш роутер — это ваша первая линия защиты — защитите его надежными учетными данными и обновленной прошивкой",
            "Используйте шифрование WPA3 или WPA2 с надежным, уникальным паролем Wi-Fi",
            "Создавайте гостевые сети для посетителей и IoT-устройств, чтобы изолировать их от вашей основной сети",
            "Регулярно обновляйте все подключенные устройства и меняйте пароли по умолчанию",
            "Отслеживайте наличие неизвестных устройств в вашей сети, которые могут указывать на несанкционированный доступ"
        ],
        "exercise": {
            "title": "Аудит безопасности домашней сети",
            "description": "Оцените и улучшите безопасность вашей домашней сети.",
            "steps": [
                "Войдите в интерфейс администратора роутера (используя IP-адрес роутера в веб-браузере)",
                "Проверьте, обновлена ли прошивка роутера, и обновите при необходимости",
                "Убедитесь, что вы используете шифрование WPA2 или WPA3 для вашего Wi-Fi",
                "Измените пароль Wi-Fi на надежную, уникальную парольную фразу",
                "Создайте гостевую сеть для посетителей и IoT-устройств, если ваш роутер поддерживает эту функцию",
                "Составьте список всех устройств, подключенных к вашей сети, и убедитесь, что они принадлежат вам",
                "Проверьте и отключите ненужные функции, такие как WPS или удаленное администрирование"
            ],
            "hint": "Если вы не уверены, как получить доступ к конкретным настройкам, найдите номер модели вашего роутера, а затем поищите 'руководство' или 'инструкцию пользователя' для получения документации."
        },
        "further_reading": [
            {
                "title": "FTC's guidance on securing your wireless network",
                "url": "https://consumer.ftc.gov/articles/how-secure-your-home-wi-fi-network",
                "description": "Рекомендации правительства по безопасности домашней сети"
            },
            {
                "title": "Router Security Checklist by CISA",
                "url": "https://www.cisa.gov/sites/default/files/publications/Securing_the_Internet_of_Things_Infographic_S508C.pdf",
                "description": "Руководство по безопасности роутера от Агентства по кибербезопасности и защите инфраструктуры"
            },
            {
                "title": "IoT Security Foundation",
                "url": "https://www.iotsecurityfoundation.org/best-practice-guidelines/",
                "description": "Лучшие практики по защите устройств Интернета вещей"
            }
        ],
        "related_tutorials": [
            {
                "id": "secure-browsing",
                "title": "Безопасное использование веб-браузера",
                "difficulty": "Начинающий"
            },
            {
                "id": "private-browsing",
                "title": "Использование VPN для приватности",
                "difficulty": "Средний"
            },
            {
                "id": "iot-security",
                "title": "Безопасность устройств умного дома",
                "difficulty": "Средний"
            }
        ]
    },
    # Web Security Category
    {
        "id": "website-safety",
        "title": "Оценка безопасности веб-сайтов",
        "description": "Узнайте, как определять безопасные веб-сайты и избегать опасных.",
        "category": "web-security",
        "difficulty": "Начинающий",
        "duration": "15 мин",
        "objectives": "Понять, как определять безопасные веб-сайты, распознавать признаки вредоносных сайтов и безопасно просматривать интернет.",
        "introduction": "Каждый день мы посещаем множество веб-сайтов для совершения покупок, банковских операций, общения в социальных сетях и получения информации. Не все эти сайты одинаково безопасны, а некоторые могут быть даже опасными. Этот учебник научит вас оценивать безопасность веб-сайтов и принимать обоснованные решения о том, каким сайтам доверять свою информацию и действия.",
        "sections": [
            {
                "title": "Основы безопасности веб-сайтов",
                "content": [
                    "Безопасность веб-сайта включает в себя несколько уровней защиты, которые помогают обеспечить конфиденциальность и безопасность ваших данных от злоумышленников. Вот основные аспекты, которые необходимо понимать:",
                    "• HTTPS: Безопасные веб-сайты используют протокол HTTPS, который шифрует данные, передаваемые между вашим браузером и веб-сайтом",
                    "• Сертификаты SSL/TLS: Цифровые сертификаты, которые подтверждают личность веб-сайта и обеспечивают зашифрованное соединение",
                    "• Безопасность контента: Защита от выполнения вредоносного кода и кражи данных",
                    "• Аутентификация: Безопасные системы входа для проверки личности пользователей",
                    "• Защита данных: Как веб-сайты хранят и обрабатывают вашу личную информацию",
                    "Как пользователь, вы не можете видеть все эти защиты, но существуют видимые индикаторы, которые могут помочь вам оценить безопасность веб-сайта."
                ],
                "alert": {
                    "type": "warning",
                    "icon": "exclamation-triangle",
                    "title": "Критическая информация",
                    "content": "Никогда не вводите конфиденциальную информацию (данные кредитной карты, пароли, личные данные) на веб-сайтах без HTTPS. Данные могут быть перехвачены злоумышленниками."
                }
            },
            {
                "title": "Определение безопасных веб-сайтов",
                "content": [
                    "При посещении веб-сайта проверьте эти индикаторы безопасности:",
                    "1. HTTPS и значок замка:",
                    "   • Ищите 'https://' в начале адреса веб-сайта",
                    "   • Проверьте наличие значка замка в адресной строке",
                    "   • Нажмите на значок замка, чтобы просмотреть информацию о сертификате безопасности сайта",
                    "",
                    "2. Проверка адреса веб-сайта:",
                    "   • Внимательно проверьте доменное имя (основную часть URL)",
                    "   • Следите за опечатками или небольшими отличиями (например, 'am a zon.com' вместо 'amazon.com')",
                    "   • Остерегайтесь поддоменов, которые могут вас обмануть (например, 'amazon.fake-site.com' — это не Amazon)",
                    "",
                    "3. Индикаторы доверия:",
                    "   • Ищите печати безопасности или значки доверия от признанных организаций",
                    "   • Проверьте наличие четкой контактной информации, включая физический адрес и номер телефона",
                    "   • Убедитесь, что на сайте есть политика конфиденциальности и условия обслуживания",
                    "",
                    "4. Профессионализм веб-сайта:",
                    "   • Профессиональные сайты обычно имеют мало грамматических ошибок",
                    "   • Навигация должна работать должным образом, без неработающих ссылок",
                    "   • Содержание должно регулярно обновляться"
                ],
                "image": {
                    "url": "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/svgs/solid/lock.svg",
                    "alt": "Значок замка HTTPS",
                    "caption": "Значок замка указывает на безопасное HTTPS-соединение, важнейшую функцию для любого сайта, обрабатывающего конфиденциальную информацию"
                }
            },
            {
                "title": "Предупреждающие признаки небезопасных веб-сайтов",
                "content": [
                    "Будьте внимательны к этим красным флагам, которые могут указывать на небезопасный или мошеннический веб-сайт:",
                    "• Отсутствие HTTPS: Сайт использует только HTTP, а не HTTPS",
                    "• Предупреждения браузера: Ваш браузер отображает предупреждения о безопасности сайта",
                    "• Плохой дизайн и функциональность: Сайт выглядит непрофессионально или плохо поддерживается",
                    "• Слишком хорошо, чтобы быть правдой: Предложения, которые кажутся нереалистично щедрыми",
                    "• Чрезмерное количество всплывающих окон: Многочисленные всплывающие окна, особенно те, которые сложно закрыть",
                    "• Тактика давления: Обратные отсчеты или срочные сообщения, побуждающие к немедленным действиям",
                    "• Необычные способы оплаты: Запросы на денежные переводы, подарочные карты или только криптовалюту",
                    "• Отсутствующая информация: Нет политики конфиденциальности, условий обслуживания или контактной информации",
                    "• Несоответствующие или подозрительные URL: Адрес не соответствует заявленной организации",
                    "• Чрезмерные запросы информации: Запрашивают больше личной информации, чем необходимо",
                    "Если вы заметили несколько красных флагов, лучше всего немедленно покинуть сайт, не вводя никакой информации."
                ],
                "code": {
                    "language": "text",
                    "snippet": "# Как проверить репутацию веб-сайта:\n\n1. Поищите отзывы о веб-сайте (например, \"безопасен ли example.com\" или \"отзывы о example.com\")\n\n2. Используйте средства проверки безопасности веб-сайтов:\n   - Google Transparency Report: https://transparencyreport.google.com/safe-browsing/search\n   - Norton Safe Web: https://safeweb.norton.com\n   - McAfee WebAdvisor: https://www.mcafee.com/consumer/en-us/landing-page/webadvisor.html\n   - VirusTotal: https://www.virustotal.com/gui/home/url\n\n3. Проверьте информацию WHOIS, чтобы узнать, когда и кем был зарегистрирован домен:\n   - https://lookup.icann.org\n   - https://whois.domaintools.com"
                }
            },
            {
                "title": "Действия при неуверенности",
                "content": [
                    "Если вы не уверены в безопасности веб-сайта, примите следующие меры предосторожности:",
                    "1. Исследуйте перед предоставлением информации:",
                    "   • Поищите отзывы или информацию о веб-сайте",
                    "   • Поищите компанию в социальных сетях или бизнес-каталогах",
                    "   • Проверьте, есть ли у них устоявшееся присутствие в других местах",
                    "",
                    "2. Используйте защитные инструменты:",
                    "   • Включите защиту от фишинга и вредоносных программ в вашем браузере",
                    "   • Рассмотрите возможность использования расширений, таких как Web of Trust (WOT) или аналогичных индикаторов доверия",
                    "   • Поддерживайте антивирус и браузер в актуальном состоянии",
                    "",
                    "3. Минимизируйте риски:",
                    "   • Используйте гостевую оплату вместо создания учетных записей, когда это возможно",
                    "   • Рассмотрите возможность использования виртуальных кредитных карт или платежных сервисов, таких как PayPal",
                    "   • Никогда не делитесь конфиденциальной информацией, такой как ваш номер социального страхования, если это абсолютно не необходимо",
                    "",
                    "4. Доверяйте своей интуиции:",
                    "   • Если что-то кажется неправильным на веб-сайте, вероятно, так оно и есть",
                    "   • Почти всегда есть альтернативные веб-сайты для того, что вам нужно",
                    "   • Никакая сделка или предложение не стоит того, чтобы ставить под угрозу вашу безопасность"
                ]
            }
        ],
        "key_takeaways": [
            "Всегда ищите HTTPS и значок замка перед вводом конфиденциальной информации",
            "Тщательно проверяйте адреса веб-сайтов, чтобы избежать похожих или поддельных сайтов",
            "Относитесь с подозрением к веб-сайтам с плохим дизайном, грамматическими ошибками или чрезмерным количеством всплывающих окон",
            "Исследуйте незнакомые веб-сайты перед совершением покупок или созданием учетных записей",
            "Используйте функции безопасности браузера и инструменты проверки репутации веб-сайтов в случае сомнений"
        ],
        "exercise": {
            "title": "Практика оценки безопасности веб-сайтов",
            "description": "Оцените безопасность веб-сайтов, которые вы регулярно посещаете, чтобы практиковаться в определении функций безопасности и потенциальных проблем.",
            "steps": [
                "Составьте список из 5-10 веб-сайтов, которыми вы регулярно пользуетесь (покупки, банкинг, социальные сети, новости и т.д.)",
                "Для каждого веб-сайта проверьте, использует ли он HTTPS, посмотрев на значок замка",
                "Нажмите на значок замка, чтобы просмотреть информацию о сертификате безопасности сайта",
                "Найдите политику конфиденциальности и просмотрите, какие данные собирает сайт",
                "Поищите отзывы или информацию о безопасности каждого сайта",
                "Отметьте сайты, практики безопасности которых вызывают беспокойство, и рассмотрите альтернативы"
            ],
            "hint": "Обратите особое внимание на веб-сайты, где вы делитесь финансовой информацией или личными данными. Они должны иметь самый высокий уровень безопасности."
        },
        "further_reading": [
            {
                "title": "Google's Safety Center",
                "url": "https://safety.google/security/security-tips/",
                "description": "Советы по безопасности в интернете от Google"
            },
            {
                "title": "Mozilla's HTTPS Explainer",
                "url": "https://support.mozilla.org/en-US/kb/how-do-i-tell-if-my-connection-is-secure",
                "description": "Как определить, безопасно ли ваше соединение с веб-сайтом"
            },
            {
                "title": "FTC's Online Shopping Tips",
                "url": "https://consumer.ftc.gov/articles/online-shopping",
                "description": "Советы по безопасным покупкам в интернете от Федеральной торговой комиссии"
            }
        ],
        "related_tutorials": [
            {
                "id": "secure-browsing",
                "title": "Безопасное использование веб-браузера",
                "difficulty": "Начинающий"
            },
            {
                "id": "phishing-protection",
                "title": "Защита от фишинга",
                "difficulty": "Начинающий"
            },
            {
                "id": "online-shopping-security",
                "title": "Безопасные покупки в интернете",
                "difficulty": "Начинающий"
            }
        ]
    },
    {
        "id": "phishing-protection",
        "title": "Защита от фишинга",
        "description": "Узнайте, как распознавать и избегать фишинговых атак, которые пытаются украсть вашу информацию.",
        "category": "web-security",
        "difficulty": "Начинающий",
        "duration": "20 мин",
        "objectives": "Понять, что такое фишинг, научиться идентифицировать попытки фишинга и разработать стратегии самозащиты.",
        "introduction": "Фишинг — одна из самых распространенных и эффективных кибератак, использующая обман, чтобы заставить людей раскрыть конфиденциальную информацию или установить вредоносное ПО. Эти атаки могут поступать через электронную почту, текстовые сообщения, социальные сети или даже телефонные звонки. Этот учебник поможет вам распознавать попытки фишинга и принимать меры для защиты от этих все более изощренных мошенничеств.",
        "sections": [
            {
                "title": "Понимание фишинговых атак",
                "content": [
                    "Фишинг — это тип атаки социальной инженерии, при которой злоумышленники маскируются под доверенные организации, чтобы обманом заставить жертв раскрыть конфиденциальную информацию или совершить вредоносные действия. Вот что вам нужно знать:",
                    "• Фишинг преимущественно работает путем эксплуатации доверия, а не технических уязвимостей",
                    "• Атаки могут быть направлены на конкретных лиц (целевой фишинг) или массово распространяться с помощью общих сообщений",
                    "• Целью обычно является кража учетных данных, финансовой информации или личных данных",
                    "• Злоумышленники также могут пытаться установить вредоносное ПО или программы-вымогатели",
                    "• Фишинг встречается во многих формах через различные каналы коммуникации",
                    "Понимание основных типов фишинга может помочь вам идентифицировать потенциальные атаки:"
                ],
                "image": {
                    "url": "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/svgs/solid/fish.svg",
                    "alt": "Иллюстрация фишинга",
                    "caption": "Фишинг пытается 'подцепить' жертв, выдавая себя за легитимные организации"
                }
            },
            {
                "title": "Распространенные типы фишинга",
                "content": [
                    "Фишинговые атаки бывают нескольких видов, каждый с отличительными характеристиками:",
                    "• Фишинг по электронной почте: Наиболее распространенный тип, использующий поддельные электронные письма, которые выглядят так, как будто они поступили от легитимных организаций",
                    "• Целевой фишинг (спир-фишинг): Таргетированные атаки, настроенные для конкретных лиц, часто с использованием личной информации",
                    "• Китовый фишинг (вейлинг): Нацелен на высокопоставленных лиц, таких как руководители или политики",
                    "• Смишинг: Фишинг через SMS-сообщения",
                    "• Вишинг: Голосовой фишинг с использованием телефонных звонков",
                    "• Клонированный фишинг: Копирование легитимных коммуникаций, но с заменой ссылок или вложений на вредоносные",
                    "• Фишинг через поисковые системы: Создание поддельных сайтов, которые появляются в результатах поиска",
                    "• Компрометация деловой электронной почты (BEC): Выдача себя за руководителей для запроса денежных переводов или конфиденциальной информации",
                    "Техники постоянно развиваются, но основная стратегия остается неизменной: манипуляция через имитацию."
                ],
                "alert": {
                    "type": "danger",
                    "icon": "exclamation-circle",
                    "title": "Растущая сложность",
                    "content": "Современные попытки фишинга становятся все более сложными, с меньшим количеством орфографических ошибок, профессиональным дизайном и даже интерактивными элементами. Никогда не думайте, что вы слишком осведомлены, чтобы попасться."
                }
            },
            {
                "title": "Как идентифицировать попытки фишинга",
                "content": [
                    "Хотя фишинговые атаки становятся все более изощренными, они часто содержат характерные признаки, которые могут помочь вам их идентифицировать:",
                    "1. Подозрительные адреса отправителей:",
                    "   • Небольшие ошибки в доменных именах (microsoftsupport.com вместо microsoft.com)",
                    "   • Личные почтовые домены для деловых коммуникаций (amazon-support@gmail.com)",
                    "   • Несоответствие между именем отправителя и адресом электронной почты",
                    "",
                    "2. Тактики срочности и давления:",
                    "   • Сообщения, создающие чувство срочности или требующие немедленных действий",
                    "   • Угрозы негативных последствий, если вы не действуете быстро",
                    "   • Ограниченные по времени предложения, которые слишком хороши, чтобы быть правдой",
                    "",
                    "3. Подозрительные ссылки и вложения:",
                    "   • Ссылки, которые не соответствуют заявленному назначению (наведите без нажатия, чтобы проверить)",
                    "   • Сокращенные URL, которые скрывают реальное назначение",
                    "   • Неожиданные вложения, особенно исполняемые файлы (.exe, .zip, .scr)",
                    "",
                    "4. Признаки опасности в содержании:",
                    "   • Общие приветствия (\"Уважаемый пользователь\" вместо вашего имени)",
                    "   • Грамматические ошибки и необычные формулировки",
                    "   • Запросы конфиденциальной информации",
                    "   • Несогласованный брендинг или форматирование",
                    "",
                    "Всегда проверяйте подозрительные коммуникации через официальные каналы, прежде чем предпринимать какие-либо запрашиваемые действия."
                ],
                "code": {
                    "language": "text",
                    "snippet": "# Как проверить заголовки и ссылки электронной почты\n\n## Проверка истинного назначения ссылки:\n1. Наведите мышь на ссылку (не нажимайте)\n2. Посмотрите на строку состояния или всплывающее окно, чтобы увидеть фактический URL\n3. Проверьте, соответствует ли домен ожидаемой организации\n\n## Изучение заголовков электронной почты (продвинутый уровень):\n- В Gmail: Нажмите на три точки → \"Показать оригинал\"\n- В Outlook: Открыть письмо → Файл → Свойства → \"Заголовки Интернета\"\n\n## Предупреждающие знаки в URL:\n- Опечатки (microsft.com вместо microsoft.com)\n- Дополнительные слова (paypal-secure.com вместо paypal.com)\n- Неожиданные поддомены (login.paypal.phishing.com)\n- Необычные TLD (.xyz, .tk вместо .com, .org)"
                }
            },
            {
                "title": "Защита от фишинга",
                "content": [
                    "Предпримите следующие шаги для минимизации риска от фишинговых атак:",
                    "• Проверяйте перед действием: Самостоятельно свяжитесь с организацией через официальные каналы, если вы не уверены",
                    "• Никогда не нажимайте на подозрительные ссылки: Введите официальный адрес веб-сайта напрямую в браузере",
                    "• Будьте осторожны с вложениями: Просканируйте их с помощью программного обеспечения безопасности перед открытием",
                    "• Используйте многофакторную аутентификацию: Это обеспечивает дополнительный уровень защиты, даже если учетные данные скомпрометированы",
                    "• Поддерживайте программное обеспечение в актуальном состоянии: Убедитесь, что ваши устройства и приложения имеют последние обновления безопасности",
                    "• Используйте фильтрацию электронной почты: Включите фильтры спама и функции безопасности в вашем почтовом сервисе",
                    "• Скептически относитесь к срочности: Легитимные организации редко требуют немедленных действий",
                    "• Сообщайте о попытках фишинга: Используйте функции отчетности в вашем почтовом клиенте или пересылайте в соответствующие органы",
                    "• Образовывайте себя: Будьте в курсе современных методов фишинга",
                    "Помните, что даже технически грамотные люди могут стать жертвами изощренного фишинга. Всегда сохраняйте здоровый скептицизм."
                ]
            }
        ],
        "key_takeaways": [
            "Фишинговые атаки пытаются украсть информацию, выдавая себя за доверенные организации",
            "Предупреждающие признаки включают срочность, подозрительные ссылки, общие приветствия и запросы конфиденциальной информации",
            "Всегда проверяйте коммуникации через официальные каналы перед выполнением каких-либо действий",
            "Включите многофакторную аутентификацию для защиты учетных записей, даже если учетные данные скомпрометированы",
            "Сообщайте о попытках фишинга, чтобы защитить других и улучшить системы безопасности"
        ],
        "exercise": {
            "title": "Анализ фишинговых писем",
            "description": "Практикуйтесь в определении попыток фишинга, анализируя образцы электронных писем.",
            "steps": [
                "Просмотрите папку спама вашей электронной почты на наличие потенциальных попыток фишинга",
                "Для каждого подозрительного письма проверьте адрес отправителя на наличие несоответствий",
                "Наведите курсор на ссылки (без нажатия), чтобы увидеть фактическое назначение",
                "Обратите внимание на срочность, общие приветствия и запросы личной информации",
                "Отметьте грамматические ошибки и необычные формулировки",
                "Подумайте, ожидали ли вы это сообщение",
                "Определите, является ли письмо легитимным или попыткой фишинга"
            ],
            "hint": "Если вы не можете найти примеры в своем почтовом ящике, поищите 'примеры фишинговых писем' в интернете. Чем больше примеров вы изучите, тем лучше вы научитесь распознавать реальные попытки."
        },
        "further_reading": [
            {
                "title": "Phishing.org",
                "url": "https://www.phishing.org/what-is-phishing",
                "description": "Комплексный ресурс о фишинговых атаках и их предотвращении"
            },
            {
                "title": "FTC Phishing Guidance",
                "url": "https://consumer.ftc.gov/articles/how-recognize-and-avoid-phishing-scams",
                "description": "Руководство Федеральной торговой комиссии по распознаванию и предотвращению фишинга"
            },
            {
                "title": "CISA Phishing Page",
                "url": "https://www.cisa.gov/topics/cyber-threats-and-advisories/types-threats/phishing",
                "description": "Ресурсы Агентства кибербезопасности и безопасности инфраструктуры по фишингу"
            }
        ],
        "related_tutorials": [
            {
                "id": "social-engineering",
                "title": "Распознавание атак социальной инженерии",
                "difficulty": "Начинающий"
            },
            {
                "id": "secure-browsing",
                "title": "Безопасное использование веб-браузера",
                "difficulty": "Начинающий"
            },
            {
                "id": "two-factor-authentication",
                "title": "Настройка двухфакторной аутентификации",
                "difficulty": "Начинающий"
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
