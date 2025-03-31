"""
Cybersecurity glossary module.
Contains definitions and explanations of cybersecurity terms.
"""

# Glossary terms with definitions, categories, and related terms
GLOSSARY_TERMS = [
    {
        "term": "Adware",
        "definition": "Software that automatically displays or downloads advertising material such as banners or pop-ups when a user is online. While not always malicious, adware can sometimes contain spyware components.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["Malware", "Spyware", "Browser Hijacker"]
    },
    {
        "term": "Authentication",
        "definition": "The process of verifying the identity of a user, device, or system, typically to grant access to resources. Common authentication methods include passwords, biometrics, smart cards, and security tokens.",
        "example": "When you enter your username and password to log into your email account, you're going through an authentication process.",
        "category": "Authentication",
        "category_color": "primary",
        "related_terms": ["Multi-Factor Authentication", "Single Sign-On", "Password"]
    },
    {
        "term": "Backdoor",
        "definition": "A method, often secret, of bypassing normal authentication or encryption in a system. Backdoors may be created by system developers for troubleshooting or maintenance, but they can also be installed by attackers to gain unauthorized access.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["Malware", "Trojan", "Remote Access Tool"]
    },
    {
        "term": "Biometrics",
        "definition": "The measurement and statistical analysis of people's unique physical and behavioral characteristics, used for identification and access control. Common biometric methods include fingerprint scanning, facial recognition, voice recognition, and iris scanning.",
        "example": "Unlocking your smartphone with your fingerprint or facial scan is an example of biometric authentication.",
        "category": "Authentication",
        "category_color": "primary",
        "related_terms": ["Authentication", "Two-Factor Authentication", "Identity Verification"]
    },
    {
        "term": "Botnet",
        "definition": "A network of compromised computers (bots) infected with malware and controlled remotely by an attacker (botmaster). Botnets are often used for distributed denial-of-service attacks, spam distribution, or credential stuffing.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["DDoS", "Malware", "Zombie Computer"]
    },
    {
        "term": "Brute Force Attack",
        "definition": "An attack method that uses trial and error to crack passwords, login credentials, or encryption keys by systematically checking all possible combinations until the correct one is found.",
        "example": "An attacker trying every possible four-digit PIN from 0000 to 9999 to unlock a stolen phone is using a brute force attack.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["Dictionary Attack", "Password Cracking", "Rainbow Table"]
    },
    {
        "term": "CIA Triad",
        "definition": "A model designed to guide policies for information security within an organization. The three core principles are: Confidentiality (ensuring data is accessible only to authorized parties), Integrity (maintaining accuracy and trustworthiness of data), and Availability (ensuring authorized users have access to information when needed).",
        "category": "General",
        "category_color": "info",
        "related_terms": ["Confidentiality", "Integrity", "Availability"]
    },
    {
        "term": "Confidentiality",
        "definition": "The principle of ensuring that information is accessible only to those authorized to have access. It is one of the three components of the CIA triad of information security.",
        "example": "Encryption transforms readable data into an encoded format that can only be read by someone with the decryption key, maintaining confidentiality.",
        "category": "General",
        "category_color": "info",
        "related_terms": ["CIA Triad", "Encryption", "Privacy"]
    },
    {
        "term": "Cryptography",
        "definition": "The practice and study of techniques for secure communication in the presence of adversaries. Modern cryptography concerns itself with confidentiality, integrity, authentication, and non-repudiation.",
        "category": "Cryptography",
        "category_color": "success",
        "related_terms": ["Encryption", "Public Key Infrastructure", "Hash Function"]
    },
    {
        "term": "Data Breach",
        "definition": "An incident where sensitive, protected, or confidential data is copied, transmitted, viewed, stolen, or used by an unauthorized individual. Data breaches may involve personal health information (PHI), personally identifiable information (PII), trade secrets, or intellectual property.",
        "example": "When a company's database containing customer credit card information is hacked and the data is stolen, that's a data breach.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["Data Leak", "Identity Theft", "Exfiltration"]
    },
    {
        "term": "DDoS Attack",
        "definition": "Distributed Denial of Service. An attack where multiple compromised systems (often infected with malware) are used to target a single system, service, or website with a flood of traffic. The goal is to overwhelm the target, causing it to slow down or crash and deny service to legitimate users.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["DoS Attack", "Botnet", "Traffic Amplification"]
    },
    {
        "term": "Defense in Depth",
        "definition": "A cybersecurity strategy that employs multiple layers of security controls throughout a system. The idea is that if one layer fails, additional layers provide further protection, rather than relying on a single security mechanism.",
        "example": "A company using firewalls, intrusion detection systems, encryption, and employee training is implementing defense in depth.",
        "category": "General",
        "category_color": "info",
        "related_terms": ["Security Controls", "Layered Security", "Risk Management"]
    },
    {
        "term": "Encryption",
        "definition": "The process of converting information into a code to prevent unauthorized access. Encryption uses an algorithm and a key to transform plaintext into ciphertext, which appears random and can only be read by decrypting it with the appropriate key.",
        "category": "Cryptography",
        "category_color": "success",
        "related_terms": ["Cryptography", "Decryption", "End-to-End Encryption"]
    },
    {
        "term": "End-to-End Encryption",
        "definition": "A system of communication where only the communicating users can read the messages. In principle, it prevents potential eavesdroppers – including telecom providers, internet providers, and the service provider itself – from accessing the cryptographic keys needed to decrypt the conversation.",
        "example": "When you send a message via WhatsApp or Signal, it's encrypted on your device and only decrypted on the recipient's device, with no ability for the service provider to read the content.",
        "category": "Cryptography",
        "category_color": "success",
        "related_terms": ["Encryption", "Secure Messaging", "Privacy"]
    },
    {
        "term": "Exploit",
        "definition": "A piece of software, a command, or a methodology that takes advantage of a vulnerability or security flaw in a system or application. Exploits are often used as part of an attack to gain unauthorized access to a system or network.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["Vulnerability", "Zero-Day", "Payload"]
    },
    {
        "term": "Firewall",
        "definition": "A network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. Firewalls establish a barrier between a trusted network and an untrusted network, such as the internet.",
        "example": "A firewall might be configured to block all incoming traffic to ports that aren't specifically needed for approved applications.",
        "category": "Network",
        "category_color": "warning",
        "related_terms": ["Network Security", "Packet Filtering", "DMZ"]
    },
    {
        "term": "Hash Function",
        "definition": "A mathematical function that converts an input of arbitrary length into a fixed-size string of bytes. The output, known as the hash value or digest, is unique to each unique input. Hash functions are used for data integrity checks, password storage, and digital signatures.",
        "category": "Cryptography",
        "category_color": "success",
        "related_terms": ["Cryptography", "MD5", "SHA-256"]
    },
    {
        "term": "HTTPS",
        "definition": "Hypertext Transfer Protocol Secure. An extension of HTTP that uses SSL/TLS for security. HTTPS encrypts the data exchanged between a user's browser and the website, protecting against eavesdropping, tampering, and man-in-the-middle attacks.",
        "example": "When you see a padlock icon in your browser and 'https://' in the URL, it indicates the connection is encrypted using HTTPS.",
        "category": "Network",
        "category_color": "warning",
        "related_terms": ["HTTP", "SSL/TLS", "Encryption"]
    },
    {
        "term": "Identity Theft",
        "definition": "The deliberate use of someone else's identity, usually as a method to gain financial advantage or obtain credit and other benefits in the other person's name, and perhaps to the other person's disadvantage or loss.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["Phishing", "Data Breach", "Social Engineering"]
    },
    {
        "term": "Integrity",
        "definition": "In information security, integrity means maintaining and assuring the accuracy and completeness of data over its entire lifecycle. This means data cannot be modified in an unauthorized or undetected manner.",
        "example": "Digital signatures are used to verify that a message hasn't been altered in transit, maintaining its integrity.",
        "category": "General",
        "category_color": "info",
        "related_terms": ["CIA Triad", "Digital Signature", "Hash Function"]
    },
    {
        "term": "Intrusion Detection System (IDS)",
        "definition": "A device or software application that monitors a network or systems for malicious activity or policy violations. IDS systems collect and analyze information from various areas within a computer or network to identify possible security breaches.",
        "category": "Network",
        "category_color": "warning",
        "related_terms": ["Intrusion Prevention System", "Security Information and Event Management", "Network Monitoring"]
    },
    {
        "term": "Keylogger",
        "definition": "A type of surveillance software or hardware that has the capability to record every keystroke made on a computer. Keyloggers can be used legitimately by IT departments to troubleshoot issues or by parents to monitor children's activities, but they are often used maliciously to steal passwords and other sensitive information.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["Spyware", "Malware", "Surveillance"]
    },
    {
        "term": "Malware",
        "definition": "Short for 'malicious software,' this is any software intentionally designed to cause damage to a computer, server, client, or computer network. Malware includes viruses, worms, trojans, ransomware, spyware, adware, and other malicious programs.",
        "example": "Ransomware is a type of malware that encrypts a victim's files and demands payment for the decryption key.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["Virus", "Ransomware", "Spyware"]
    },
    {
        "term": "Man-in-the-Middle Attack",
        "definition": "An attack where the attacker secretly relays and possibly alters the communications between two parties who believe they are directly communicating with each other. This allows the attacker to intercept, read, and modify data passing between the two parties.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["Eavesdropping", "Session Hijacking", "SSL Stripping"]
    },
    {
        "term": "Multi-Factor Authentication (MFA)",
        "definition": "An authentication method that requires the user to provide two or more verification factors to gain access to a resource. These factors typically include something you know (password), something you have (security token), and something you are (biometric verification).",
        "example": "When logging into your bank account requires both a password and a verification code sent to your phone, that's multi-factor authentication.",
        "category": "Authentication",
        "category_color": "primary",
        "related_terms": ["Two-Factor Authentication", "Authentication", "Security Token"]
    },
    {
        "term": "Network Security",
        "definition": "The policies, processes, and practices adopted to prevent, detect, and monitor unauthorized access, misuse, modification, or denial of a computer network and network-accessible resources.",
        "category": "Network",
        "category_color": "warning",
        "related_terms": ["Firewall", "Intrusion Detection System", "VPN"]
    },
    {
        "term": "Patch",
        "definition": "A software update designed to address security vulnerabilities or other bugs in a program or operating system. Regularly applying patches is a critical security practice.",
        "example": "Microsoft regularly releases patches on 'Patch Tuesday' to fix security vulnerabilities in Windows and other Microsoft products.",
        "category": "General",
        "category_color": "info",
        "related_terms": ["Vulnerability", "Security Update", "Patch Management"]
    },
    {
        "term": "Payload",
        "definition": "In the context of malware or exploits, the payload is the part of the code that performs the malicious action, such as stealing data, encrypting files, or creating a backdoor. It's the 'weapon' that's delivered after a vulnerability has been exploited.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["Exploit", "Malware", "Virus"]
    },
    {
        "term": "Penetration Testing",
        "definition": "An authorized simulated cyberattack on a computer system, performed to evaluate the security of the system. The test is performed to identify vulnerabilities, strengths, and weaknesses in a system's security.",
        "example": "A company might hire ethical hackers to attempt to breach their systems to identify security weaknesses before real attackers can exploit them.",
        "category": "General",
        "category_color": "info",
        "related_terms": ["Ethical Hacking", "Vulnerability Assessment", "Red Team"]
    },
    {
        "term": "Phishing",
        "definition": "A type of social engineering attack often used to steal user data, including login credentials and credit card numbers. It occurs when an attacker, masquerading as a trusted entity, dupes a victim into opening an email, instant message, or text message and clicking on a malicious link or attachment.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["Social Engineering", "Spear Phishing", "Whaling"]
    },
    {
        "term": "Public Key Infrastructure (PKI)",
        "definition": "A set of roles, policies, hardware, software, and procedures needed to create, manage, distribute, use, store, and revoke digital certificates and manage public-key encryption. PKI facilitates the secure electronic transfer of information for activities such as e-commerce, internet banking, and confidential email.",
        "category": "Cryptography",
        "category_color": "success",
        "related_terms": ["Digital Certificate", "Public Key Cryptography", "Certificate Authority"]
    },
    {
        "term": "Ransomware",
        "definition": "A type of malicious software designed to block access to a computer system or data until a sum of money (ransom) is paid. Ransomware typically encrypts files on the victim's system and demands payment to provide the decryption key.",
        "example": "The WannaCry ransomware attack in 2017 affected hundreds of thousands of computers worldwide by encrypting files and demanding Bitcoin payments.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["Malware", "Encryption", "Crypto-locker"]
    },
    {
        "term": "Risk Management",
        "definition": "The identification, assessment, and prioritization of risks followed by coordinated application of resources to minimize, monitor, and control the probability or impact of adverse events. In cybersecurity, risk management involves identifying vulnerabilities and threats, assessing their potential impact, and implementing controls to mitigate them.",
        "category": "General",
        "category_color": "info",
        "related_terms": ["Vulnerability Assessment", "Threat Modeling", "Security Controls"]
    },
    {
        "term": "Social Engineering",
        "definition": "The psychological manipulation of people into performing actions or divulging confidential information. It's a type of confidence trick for the purpose of information gathering, fraud, or system access.",
        "example": "An attacker calling an employee and pretending to be IT support to trick them into revealing their password is using social engineering.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["Phishing", "Pretexting", "Baiting"]
    },
    {
        "term": "Spear Phishing",
        "definition": "A targeted phishing attack directed at specific individuals or companies. Unlike regular phishing attacks, which cast a wide net, spear phishing is highly customized and often uses personal information about the target to increase credibility.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["Phishing", "Social Engineering", "Whaling"]
    },
    {
        "term": "Spyware",
        "definition": "Software that secretly gathers user information through the user's internet connection without their knowledge, usually for advertising purposes. Spyware can also harvest sensitive information like passwords or financial data.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["Malware", "Adware", "Tracking Cookie"]
    },
    {
        "term": "SSL/TLS",
        "definition": "Secure Sockets Layer (SSL) and its successor, Transport Layer Security (TLS), are cryptographic protocols designed to provide communications security over a computer network. They're commonly used to secure communications on the web, email, and other data transfers.",
        "example": "When you see 'https://' in your browser's address bar, it indicates the site is using SSL/TLS encryption to secure the connection.",
        "category": "Cryptography",
        "category_color": "success",
        "related_terms": ["HTTPS", "Encryption", "Certificate"]
    },
    {
        "term": "Two-Factor Authentication (2FA)",
        "definition": "A security process in which a user provides two different authentication factors to verify their identity. This is a more secure method than single-factor authentication, as it adds an additional layer of security.",
        "example": "When logging into an account requires both a password and a verification code sent to your phone, that's two-factor authentication.",
        "category": "Authentication",
        "category_color": "primary",
        "related_terms": ["Multi-Factor Authentication", "Authentication", "One-Time Password"]
    },
    {
        "term": "Virtual Private Network (VPN)",
        "definition": "A service that creates a private, encrypted connection over a less secure network, such as the public internet. VPNs protect your online activity from snooping, interference, and censorship by extending a private network across a public network.",
        "category": "Network",
        "category_color": "warning",
        "related_terms": ["Encryption", "Tunnel", "Remote Access"]
    },
    {
        "term": "Virus",
        "definition": "A type of malicious software that, when executed, replicates itself by modifying other computer programs and inserting its own code. When this replication succeeds, the affected areas are then said to be 'infected' with a virus.",
        "example": "The ILOVEYOU virus in 2000 spread via email and overwrote files, causing billions of dollars in damage worldwide.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["Malware", "Worm", "Trojan"]
    },
    {
        "term": "Vulnerability",
        "definition": "A weakness in a system, application, or network that could be exploited by a threat actor to perform unauthorized actions. Vulnerabilities can exist in software code, design, implementation, or operation.",
        "category": "General",
        "category_color": "info",
        "related_terms": ["Exploit", "Patch", "Zero-Day"]
    },
    {
        "term": "Whaling",
        "definition": "A specific type of phishing attack that targets high-profile individuals like C-level executives, politicians, or celebrities. These attacks are highly personalized and often involve substantial research about the target.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["Phishing", "Spear Phishing", "Social Engineering"]
    },
    {
        "term": "Zero-Day Vulnerability",
        "definition": "A software vulnerability that is unknown to those who should be interested in mitigating it, including the vendor. Zero-day vulnerabilities are particularly dangerous because there are no available patches or defenses, and attackers can exploit them before developers have a chance to address them.",
        "example": "In 2017, the EternalBlue exploit targeted a zero-day vulnerability in Microsoft's SMB protocol, later used in the WannaCry ransomware attack.",
        "category": "Threats",
        "category_color": "danger",
        "related_terms": ["Vulnerability", "Exploit", "Patch"]
    },
    {
        "term": "Zero Trust",
        "definition": "A security concept centered on the belief that organizations should not automatically trust anything inside or outside their perimeters and must verify everything trying to connect to their systems before granting access. The principle is 'never trust, always verify.'",
        "category": "General",
        "category_color": "info",
        "related_terms": ["Least Privilege", "Micro-segmentation", "Identity Verification"]
    }
]
