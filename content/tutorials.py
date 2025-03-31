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
        "title": "Creating Strong Passwords",
        "description": "Learn how to create and manage strong, unique passwords for better security.",
        "category": "password-security",
        "difficulty": "Beginner",
        "duration": "15 min",
        "objectives": "Understand password vulnerabilities, learn to create strong passwords, and discover password management strategies.",
        "introduction": "Passwords remain the primary authentication method for most digital services, making them a critical element of your online security. Despite their importance, many people continue to use weak, easily guessable passwords or reuse the same password across multiple sites. This tutorial will teach you how to create strong passwords and manage them effectively to protect your digital identity.",
        "sections": [
            {
                "title": "Why Password Security Matters",
                "content": [
                    "Passwords are the keys to your digital life. When attackers obtain your passwords, they can:",
                    "• Access your personal and financial information",
                    "• Make purchases using your payment methods",
                    "• Steal your identity or impersonate you",
                    "• Access your workplace systems and sensitive data",
                    "• Use your accounts to attack others",
                    "The risks aren't just theoretical. According to cybersecurity reports, 81% of data breaches are caused by weak or stolen passwords. A single compromised password can lead to multiple account breaches due to password reuse."
                ],
                "alert": {
                    "type": "danger",
                    "icon": "exclamation-circle",
                    "title": "Common Password Mistakes",
                    "content": "The most common passwords still include '123456', 'password', 'qwerty', and 'admin'. These can be cracked in less than a second. Even adding a single character, number, or symbol significantly increases the time required to crack a password."
                }
            },
            {
                "title": "Characteristics of Strong Passwords",
                "content": [
                    "A strong password has several important characteristics:",
                    "• Length: At least 12 characters; longer passwords are exponentially harder to crack",
                    "• Complexity: A mix of uppercase and lowercase letters, numbers, and special characters",
                    "• Unpredictability: Avoids common words, phrases, or patterns",
                    "• Uniqueness: Different for each account or service",
                    "• Memorability: Something you can remember without writing down",
                    "The strength of a password is primarily determined by its length and randomness. Adding just a few characters to a password can make it exponentially more difficult to crack."
                ],
                "code": {
                    "language": "text",
                    "snippet": "# Examples of password strength:\n\n'password' - Would be cracked instantly\n'Password1' - Would be cracked in less than a day\n'P@ssw0rd!' - Would be cracked in a few days\n'Tr0ub4dor&3' - Would take several months to crack\n'correct-horse-battery-staple' - Would take centuries to crack with current technology"
                }
            },
            {
                "title": "Creating Memorable Yet Strong Passwords",
                "content": [
                    "The challenge with passwords is balancing security with memorability. Here are effective strategies for creating passwords you can remember:",
                    "• Passphrase Method: Combine multiple random words with spaces or symbols (e.g., 'correct-horse-battery-staple')",
                    "• Sentence Method: Take the first letter of each word in a memorable sentence (e.g., 'Mary had a little lamb' becomes 'Mhall')",
                    "• Substitution Method: Replace letters with similar-looking numbers or symbols (e.g., 'password' becomes 'p@$$w0rd')",
                    "• Personal Algorithm: Create a system for generating unique passwords for each site (e.g., combining the service name with a personal phrase)",
                    "The most secure approach is to use a password manager to generate and store completely random, unique passwords for each service."
                ],
                "image": {
                    "url": "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/svgs/solid/key.svg",
                    "alt": "Strong Password Illustration",
                    "caption": "Strong passwords are your first line of defense against unauthorized access"
                }
            },
            {
                "title": "Password Management Best Practices",
                "content": [
                    "Even with strong passwords, proper management is essential for maintaining security:",
                    "• Use a password manager: These tools generate, store, and auto-fill strong, unique passwords for all your accounts",
                    "• Enable two-factor authentication (2FA): This adds an extra layer of security beyond just a password",
                    "• Never reuse passwords: Each account should have a completely different password",
                    "• Change passwords regularly: Especially for critical accounts like email and banking",
                    "• Don't share passwords: Even with trusted individuals, sharing reduces security",
                    "• Be cautious of password storage: Browser password managers are convenient but typically less secure than dedicated password managers",
                    "• Have a recovery plan: Know how to recover access if you forget a password or lose access to your password manager"
                ]
            }
        ],
        "key_takeaways": [
            "Strong passwords are essential for protecting your digital identity",
            "The strength of a password depends on length, complexity, and uniqueness",
            "Passphrases (multiple random words) are both secure and memorable",
            "Password managers are the most secure way to create and store unique passwords",
            "Two-factor authentication adds an essential extra layer of security"
        ],
        "exercise": {
            "title": "Password Audit and Upgrade",
            "description": "Assess your current password practices and upgrade your most important accounts.",
            "steps": [
                "Make a list of your most critical accounts (email, banking, social media, etc.)",
                "Check if any of these accounts share the same or similar passwords",
                "Create new, strong passwords for each account using the techniques learned",
                "Enable two-factor authentication on all accounts that support it",
                "Consider using a password manager to store and generate your passwords"
            ],
            "hint": "Start with your email account, as it often serves as a recovery method for other accounts. Then move on to financial accounts and other sensitive services."
        },
        "further_reading": [
            {
                "title": "NIST Password Guidelines",
                "url": "https://pages.nist.gov/800-63-3/sp800-63b.html#sec5",
                "description": "Official US government guidelines on password security"
            },
            {
                "title": "Have I Been Pwned",
                "url": "https://haveibeenpwned.com/",
                "description": "Check if your email or password has been compromised in data breaches"
            },
            {
                "title": "Password Strength Testing Tools",
                "url": "https://www.security.org/how-secure-is-my-password/",
                "description": "Tools to estimate how quickly your password could be cracked"
            }
        ],
        "related_tutorials": [
            {
                "id": "two-factor-authentication",
                "title": "Setting Up Two-Factor Authentication",
                "difficulty": "Beginner"
            },
            {
                "id": "password-managers",
                "title": "Using Password Managers",
                "difficulty": "Beginner"
            },
            {
                "id": "social-engineering",
                "title": "Recognizing Social Engineering Attacks",
                "difficulty": "Beginner"
            }
        ]
    },
    {
        "id": "two-factor-authentication",
        "title": "Setting Up Two-Factor Authentication",
        "description": "Learn how to add an extra layer of security to your accounts beyond just passwords.",
        "category": "password-security",
        "difficulty": "Beginner",
        "duration": "15 min",
        "objectives": "Understand what two-factor authentication is, why it's important, and how to set it up on various accounts.",
        "introduction": "Two-factor authentication (2FA), sometimes called multi-factor authentication, adds an additional layer of security to your accounts beyond just a password. It combines something you know (your password) with something you have (like your phone) or something you are (biometrics). This tutorial will explain why 2FA is crucial and guide you through setting it up on your most important accounts.",
        "sections": [
            {
                "title": "Understanding Two-Factor Authentication",
                "content": [
                    "Two-factor authentication adds an extra verification step when logging into your accounts. Even if someone discovers your password, they still can't access your account without the second factor.",
                    "There are several types of second factors:",
                    "• SMS codes: A one-time code sent to your phone via text message",
                    "• Authentication apps: Apps like Google Authenticator or Authy that generate time-based codes",
                    "• Push notifications: Approve login attempts directly on your trusted device",
                    "• Physical security keys: USB devices like YubiKey that you insert into your computer",
                    "• Biometrics: Fingerprints, facial recognition, or other physical characteristics",
                    "Each method offers different levels of security and convenience. Generally, authentication apps and physical security keys are more secure than SMS codes."
                ],
                "image": {
                    "url": "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/svgs/solid/shield-alt.svg",
                    "alt": "Two-Factor Authentication Illustration",
                    "caption": "2FA adds a second verification layer, dramatically increasing account security"
                }
            },
            {
                "title": "Why You Need Two-Factor Authentication",
                "content": [
                    "Two-factor authentication is one of the most effective security measures available:",
                    "• It protects against password breaches: Even if your password is stolen, attackers still can't access your account",
                    "• It defends against phishing: Most 2FA methods can't be easily intercepted or faked by phishing attempts",
                    "• It alerts you to unauthorized access attempts: You'll receive authentication prompts when someone tries to log in with your password",
                    "• It's recommended by security experts: Cybersecurity professionals universally recommend using 2FA",
                    "According to Microsoft, accounts with 2FA are 99.9% less likely to be compromised than accounts with passwords alone. This simple step can eliminate most account takeover risks."
                ],
                "alert": {
                    "type": "info",
                    "icon": "info-circle",
                    "title": "Real-World Protection",
                    "content": "Two-factor authentication would have prevented many major account breaches, including high-profile social media account takeovers and email compromises that led to data theft."
                }
            },
            {
                "title": "Setting Up 2FA on Common Services",
                "content": [
                    "Most major online services now offer two-factor authentication. Here's how to enable it on some of the most important ones:",
                    "Google/Gmail:",
                    "1. Go to your Google Account (myaccount.google.com)",
                    "2. Select 'Security' from the navigation panel",
                    "3. Under 'Signing in to Google,' select '2-Step Verification'",
                    "4. Follow the on-screen steps",
                    "",
                    "Facebook:",
                    "1. Click the down arrow in the top right and select 'Settings & Privacy' → 'Settings'",
                    "2. Click 'Security and Login'",
                    "3. Scroll to 'Two-Factor Authentication' and click 'Edit'",
                    "4. Choose the authentication method you want to use",
                    "",
                    "Apple ID:",
                    "1. Go to appleid.apple.com and sign in",
                    "2. In the Security section, click 'Edit'",
                    "3. Click 'Turn On Two-Factor Authentication'",
                    "4. Follow the instructions to verify your phone number"
                ],
                "code": {
                    "language": "text",
                    "snippet": "# Common locations to find 2FA settings:\n\n• Google: Account → Security → 2-Step Verification\n• Facebook: Settings → Security and Login → Two-Factor Authentication\n• Twitter: Settings and privacy → Security and account access → Security → Two-factor authentication\n• Microsoft: Account → Security → Two-step verification\n• Amazon: Account & Lists → Account → Login & security → Edit (next to Two-Step Verification)\n• Instagram: Settings → Security → Two-Factor Authentication"
                }
            },
            {
                "title": "Using Authentication Apps",
                "content": [
                    "Authentication apps are one of the most secure 2FA methods. They generate time-based one-time passwords (TOTP) that change every 30 seconds. Here's how to use them:",
                    "1. Download an authentication app such as:",
                    "   • Google Authenticator",
                    "   • Authy",
                    "   • Microsoft Authenticator",
                    "   • LastPass Authenticator",
                    "",
                    "2. When setting up 2FA on a service, choose the 'Authentication app' option",
                    "",
                    "3. You'll typically be shown a QR code to scan with your app",
                    "",
                    "4. Your app will then generate a 6-digit code that changes every 30 seconds",
                    "",
                    "5. Enter the current code to complete setup",
                    "",
                    "6. Store backup codes safely in case you lose access to your authentication app",
                    "",
                    "Important: If you get a new phone, you'll need to transfer your authentication app accounts to the new device. Make sure you understand the backup and recovery process for your chosen app."
                ]
            }
        ],
        "key_takeaways": [
            "Two-factor authentication dramatically improves account security",
            "Authentication apps and security keys provide better protection than SMS codes",
            "Enable 2FA on your most important accounts first (email, banking, cloud storage)",
            "Always save backup codes in a secure location",
            "2FA is especially important for accounts containing sensitive information or with payment methods attached"
        ],
        "exercise": {
            "title": "Enable 2FA on Critical Accounts",
            "description": "Set up two-factor authentication on your most important online accounts.",
            "steps": [
                "Make a list of your most critical online accounts (email, banking, social media)",
                "Download an authentication app if you don't already have one",
                "For each account, find the security or 2FA settings section",
                "Follow the instructions to enable 2FA (preferably using an authentication app)",
                "Store any backup codes in a secure location (password manager or printed copy in a safe place)"
            ],
            "hint": "Start with your email account since it's typically used to reset passwords for other services. Then move on to financial accounts, social media, and cloud storage."
        },
        "further_reading": [
            {
                "title": "Two Factor Auth Directory",
                "url": "https://twofactorauth.org/",
                "description": "A directory of websites and services that support 2FA"
            },
            {
                "title": "NIST Digital Identity Guidelines",
                "url": "https://pages.nist.gov/800-63-3/",
                "description": "Official US government guidelines on authentication"
            },
            {
                "title": "EFF's Guide to Two-Factor Authentication",
                "url": "https://ssd.eff.org/en/module/how-enable-two-factor-authentication",
                "description": "The Electronic Frontier Foundation's guide to 2FA"
            }
        ],
        "related_tutorials": [
            {
                "id": "password-security",
                "title": "Creating Strong Passwords",
                "difficulty": "Beginner"
            },
            {
                "id": "password-managers",
                "title": "Using Password Managers",
                "difficulty": "Beginner"
            },
            {
                "id": "account-security",
                "title": "Securing Your Online Accounts",
                "difficulty": "Beginner"
            }
        ]
    },
    # Network Security Category
    {
        "id": "secure-browsing",
        "title": "Safe Web Browsing Practices",
        "description": "Learn how to protect yourself while browsing the internet.",
        "category": "network-security",
        "difficulty": "Beginner",
        "duration": "20 min",
        "objectives": "Understand common web browsing risks, recognize secure websites, and implement safe browsing habits.",
        "introduction": "The web browser is your primary gateway to the internet, making it a critical point of security in your digital life. Understanding how to browse safely can protect you from many common cyber threats, including malware, phishing, and data theft. This tutorial covers essential practices for safer web browsing across all devices.",
        "sections": [
            {
                "title": "Browser Security Basics",
                "content": [
                    "Your browser is constantly exposed to potential threats. Here are essential security practices to implement immediately:",
                    "• Keep your browser updated: Browser updates often contain critical security patches",
                    "• Use a modern, security-focused browser: Chrome, Firefox, Safari, and Edge all have good security features",
                    "• Enable automatic updates: This ensures you always have the latest security protections",
                    "• Review browser security settings: Familiarize yourself with and enable key security features",
                    "• Use browser extensions selectively: Only install extensions from trusted sources and remove those you don't use",
                    "• Clear browsing data regularly: This includes cookies, cache, and browsing history",
                    "These fundamentals form the foundation of safer browsing, but they're just the beginning."
                ],
                "alert": {
                    "type": "warning",
                    "icon": "exclamation-triangle",
                    "title": "Browser Extensions Risk",
                    "content": "Browser extensions can access everything you do in your browser. Only install extensions from trusted sources, and regularly review the permissions you've granted."
                }
            },
            {
                "title": "Recognizing Secure Websites",
                "content": [
                    "Not all websites are equally secure. Here's how to identify safer sites:",
                    "• Check for HTTPS: Look for 'https://' at the beginning of the address and a padlock icon in the address bar",
                    "• Verify website addresses: Check for typos or slight variations that might indicate a fake site",
                    "• Be wary of unfamiliar sites: Research new websites before providing any information",
                    "• Look for privacy policies and contact information: Legitimate sites typically have these easily accessible",
                    "• Check for trust signals: Look for professional design, updated content, and customer reviews",
                    "• Use website safety checkers: Tools like Google Safe Browsing can help identify dangerous sites",
                    "Remember that a professional appearance alone doesn't guarantee a site is legitimate. Always verify before sharing sensitive information."
                ],
                "image": {
                    "url": "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/svgs/solid/lock.svg",
                    "alt": "HTTPS Secure Connection",
                    "caption": "The padlock icon indicates a secure HTTPS connection, encrypting data between your browser and the website"
                }
            },
            {
                "title": "Protecting Your Privacy While Browsing",
                "content": [
                    "Your browsing activity can reveal a lot about you. Here's how to maintain more privacy:",
                    "• Use private browsing mode: This prevents your browser from saving your history, cookies, and site data",
                    "• Consider a VPN (Virtual Private Network): This encrypts your internet connection and hides your IP address",
                    "• Adjust cookie settings: Set your browser to delete cookies when you close it or block third-party cookies",
                    "• Use privacy-focused search engines: Options like DuckDuckGo don't track your searches",
                    "• Disable browser tracking: Enable 'Do Not Track' and other anti-tracking features in your browser",
                    "• Review browser permissions: Control which sites can access your location, camera, microphone, and notifications",
                    "• Use ad blockers: These can reduce tracking and protect against malvertising (malicious ads)",
                    "Be aware that complete anonymity online is difficult to achieve. These measures increase your privacy but don't guarantee it."
                ],
                "code": {
                    "language": "text",
                    "snippet": "# Browser Privacy Settings Checklist\n\n1. Disable third-party cookies\n2. Enable 'Do Not Track'\n3. Block pop-ups\n4. Disable location tracking\n5. Review site permissions (camera, microphone, notifications)\n6. Set content blocking to strict\n7. Enable HTTPS-only mode if available\n8. Configure automatic deletion of browsing history and cookies"
                }
            },
            {
                "title": "Avoiding Web-Based Threats",
                "content": [
                    "The web contains various threats designed to compromise your security. Here's how to avoid them:",
                    "• Be cautious about downloads: Only download files from trusted sources",
                    "• Scan downloads: Use antivirus software to check downloaded files before opening them",
                    "• Be wary of pop-ups: Avoid clicking on unexpected pop-up windows, especially those claiming your device is infected",
                    "• Don't click suspicious links: Hover over links to see where they actually lead before clicking",
                    "• Be careful with online forms: Think twice before submitting personal information",
                    "• Watch out for social engineering: Be skeptical of urgent messages or too-good-to-be-true offers",
                    "• Use secure payment methods: When shopping online, use credit cards or secure payment services with fraud protection",
                    "Remember that most web-based attacks require some action from you. Taking a moment to evaluate before clicking or downloading can prevent many security issues."
                ]
            }
        ],
        "key_takeaways": [
            "Keep your browser updated and use security features like HTTPS-only mode",
            "Look for HTTPS and verify website addresses before sharing information",
            "Use privacy tools like private browsing, VPNs, and privacy-focused search engines",
            "Be cautious about downloads, pop-ups, and requests for personal information",
            "Consider using security extensions from reputable providers to enhance protection"
        ],
        "exercise": {
            "title": "Browser Security Checkup",
            "description": "Assess and improve the security settings of your primary web browser.",
            "steps": [
                "Open your browser's settings or preferences menu",
                "Check that your browser is updated to the latest version",
                "Review and adjust privacy settings (cookies, tracking, browsing history)",
                "Configure content permissions (location, camera, microphone, notifications)",
                "Review installed extensions and remove any you don't recognize or need",
                "Enable any available security features (phishing protection, malware scanning)",
                "Set up a regular schedule to clear browsing data"
            ],
            "hint": "Most browsers have a security or privacy section in settings where you can find most of these options. If you're unsure about a specific setting, search for your browser name plus the setting to find documentation."
        },
        "further_reading": [
            {
                "title": "Mozilla's Privacy & Security Guide",
                "url": "https://support.mozilla.org/en-US/products/firefox/privacy-and-security",
                "description": "Comprehensive guide to privacy and security features in Firefox"
            },
            {
                "title": "Electronic Frontier Foundation's Surveillance Self-Defense",
                "url": "https://ssd.eff.org/",
                "description": "Tips, tools, and tutorials for safer online communications"
            },
            {
                "title": "Google's Safety Center",
                "url": "https://safety.google/",
                "description": "Resources for staying safer online with Google products"
            }
        ],
        "related_tutorials": [
            {
                "id": "cybersecurity-threats",
                "title": "Common Cybersecurity Threats",
                "difficulty": "Beginner"
            },
            {
                "id": "private-browsing",
                "title": "Using VPNs for Privacy",
                "difficulty": "Intermediate"
            },
            {
                "id": "social-engineering",
                "title": "Recognizing Social Engineering Attacks",
                "difficulty": "Beginner"
            }
        ]
    },
    {
        "id": "home-network-security",
        "title": "Securing Your Home Network",
        "description": "Learn how to protect your home Wi-Fi network and connected devices.",
        "category": "network-security",
        "difficulty": "Beginner",
        "duration": "25 min",
        "objectives": "Understand network security risks, configure router security settings, and protect connected devices.",
        "introduction": "Your home network is the gateway connecting all your devices to the internet. If compromised, attackers could access personal data, monitor your online activities, or use your network for malicious purposes. This tutorial will guide you through practical steps to secure your home network, protecting your digital life from the foundation up.",
        "sections": [
            {
                "title": "Understanding Home Network Vulnerabilities",
                "content": [
                    "Your home network faces several potential security risks:",
                    "• Unauthorized access: Others using your network without permission",
                    "• Traffic interception: Attackers capturing data sent over your network",
                    "• Device compromise: Vulnerable devices being hacked",
                    "• Router vulnerabilities: Outdated firmware with security flaws",
                    "• Default settings: Factory configurations that are inherently insecure",
                    "• Unprotected IoT devices: Smart home devices with weak security",
                    "These vulnerabilities can lead to privacy breaches, identity theft, or even your network being used in wider attacks. The good news is that most can be addressed with simple configuration changes."
                ],
                "image": {
                    "url": "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/svgs/solid/wifi.svg",
                    "alt": "Home Network Illustration",
                    "caption": "Your home network connects all your devices to the internet and requires proper security configuration"
                }
            },
            {
                "title": "Securing Your Router",
                "content": [
                    "Your router is the central point of your network and the first line of defense. Here's how to secure it:",
                    "1. Change the default login credentials:",
                    "   • Access your router's admin interface (typically by entering 192.168.0.1 or 192.168.1.1 in your browser)",
                    "   • Change both the admin username and password to strong, unique values",
                    "",
                    "2. Update router firmware:",
                    "   • Check for firmware updates in your router's admin interface",
                    "   • Enable automatic updates if available",
                    "",
                    "3. Use strong encryption:",
                    "   • Configure your Wi-Fi to use WPA3 if available, or at minimum WPA2",
                    "   • Never use the outdated WEP protocol",
                    "",
                    "4. Set a strong Wi-Fi password:",
                    "   • Create a unique, complex passphrase at least 12 characters long",
                    "   • Consider changing it periodically",
                    "",
                    "5. Disable remote management:",
                    "   • Turn off remote access to your router's admin interface",
                    "   • Only manage your router when connected to your home network",
                    "",
                    "6. Change the default network name (SSID):",
                    "   • Avoid including personal information or router model in the name",
                    "   • Consider hiding your SSID (though this provides only minimal security)"
                ],
                "alert": {
                    "type": "info",
                    "icon": "info-circle",
                    "title": "Router Access",
                    "content": "To access your router's admin interface, you'll need the default login credentials. These are typically printed on the router itself or included in the manual. If you can't find them, check the manufacturer's website or contact your internet service provider if they provided the router."
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
