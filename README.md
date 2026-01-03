# Phishing Research and Automated Detection Toolset

## Overview
This repository contains a technical study of credential-harvesting attack vectors and the implementation of a logic-based defense system. The project is divided into two modules: a high-fidelity phishing simulation and a standalone URL analysis engine.

## Technical Modules

### 1. Phishing Simulation (Offensive Analysis)
This module demonstrates the mechanisms used in social engineering to capture sensitive user data.
* **Architecture**: Developed using the Python Flask micro-framework.
* **User Interface**: A custom-styled login portal designed with modern CSS to replicate a legitimate corporate authentication environment.
* **Logic Flow**: The application captures POST requests, logs credential patterns to a local file, and redirects the user to an alert-driven awareness page.

### 2. URL Analyzer (Defensive Logic)
A standalone Python utility designed to programmatically evaluate the security risk of a given URL.
* **Security Checks**: Validates HTTPS encryption status and analyzes subdomain frequency.
* **Heuristic Analysis**: Scans for high-risk keywords used to create a false sense of urgency or legitimacy.

## Execution Instructions
1. **Install dependencies**: Use the command `pip install -r requirements.txt`.
2. **Run the simulation**: Execute `python app.py` and navigate to `http://127.0.0.1:5000/`.
3. **Execute the detector**: Execute `python phishing_detector.py` and input a URL for analysis.
## Project Structure
```
Phishing_Project/
├── static/
│   └── style.css            
├── templates/
│   ├── login.html           
│   └── warning.html        
├── .gitignore               
├── app.py                   
├── phishing_detector.py      
├── README.md                
└── requirements.txt         
```
## Ethical Disclosure

This project is for authorized security research and educational purposes only. Unauthorized use against real-world targets is strictly prohibited.

