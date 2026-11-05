# Phishing URL Detector 

##  About the Project

Phishing URL Detector is a beginner-friendly cybersecurity project developed using Python.

It analyzes URLs and identifies potentially suspicious characteristics using rule-based detection techniques.

The program assigns a suspiciousness score based on different URL indicators and provides reasons for flagging a URL.

##  Features

- Detects IP addresses used instead of domain names.
- Identifies suspicious keywords.
- Checks for excessive subdomains.
- Detects unusually long URLs.
- Identifies the use of the @ symbol.
- Calculates a suspiciousness score.
- Displays reasons behind suspicious URL detection.

##  Technologies Used

- Python 3
- Regular Expressions (re module)
- Conditional Statements
- Functions
- Lists and Dictionaries

##  How It Works

The detector uses five rule-based checks:

| Detection Rule | Score |
|---|---:|
| IP address instead of domain | +3 |
| Suspicious keywords | +1 |
| Excessive subdomains | +2 |
| URL length above 75 characters | +1 |
| Presence of @ symbol | +2 |


A URL is flagged as suspicious when its total score is 3 or higher.

##  Installation and Usage

1. Clone this repository:

```bash
git clone https://github.com/YOUR-USERNAME/Phishing-URL-Detector.git
```

2. Open the project folder:

```bash
cd Phishing-URL-Detector
```

3. Run the Python program:

```bash
python phishing_detector.py
```

4. Enter a URL when prompted.

##  Project Structure

```text
Phishing-URL-Detector/
│
├── phishing_detector.py
├── README.md
└── LICENSE
```

##  Learning Outcomes

- Understanding basic phishing detection techniques.
- Learning Python regular expressions.
- Applying conditional statements and functions.
- Understanding suspicious URL characteristics.
- Exploring basic cybersecurity concepts.

##  Disclaimer

This project is an educational demonstration of rule-based phishing URL detection.

It is not a complete phishing detection system. Legitimate URLs may be flagged, and malicious URLs may go undetected. The scoring system does not verify the actual safety of a website.

##  Author

SNEHA SARA BOBY

##  Acknowledgement

Created as a beginner cybersecurity learning project using Python.
