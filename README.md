## Table of Contents
- [About](#-about)
- [How to Build](#-how-to-build)
- [Documentation](#-documentation)
- [Feedback and Contributions](#-feedback-and-contributions)
  


## 🚀 About
**Amazon Price Tracker** This project is an Amazon price tracker script written in Python. It monitors the price of a specified product on Amazon and sends an email alert when the price falls below a target price. This can help users purchase products at their desired prices.

## 📝 How to Build
**Prerequisites**
- Python 3.x
- Required Python packages:
  - requests
  - lxml
  - beautifulsoup4
  - smtplib
 
**To build the project follow these steps:**
  - **installation:**

```shell
# Open a terminal (Command Prompt or PowerShell for Windows, Terminal for macOS or Linux)

# Ensure Git is installed
# Visit https://git-scm.com to download and install console Git if not already installed

# Clone the repository
git clone https://github.com/Akwaowo91/amazon-price-tracker.git
cd amazon-price-tracker

# Install the required package
pip install requests lxml beautifulsoup4
```

  - **configuration:**
    
      - Email Configuration:
          - Open the script file and update the email configuration section with your email credentials:
            ```shell
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            sender_email = "your-email@gmail.com"
            receiver_email = "your-email@gmail.com"
            password = "your-email-app-password"
            target_price = 100  # Set your target price here
            ```
      - Amazon Product URL:
          - Update the API variable with the URL of the Amazon product you want to track:
             ```shell
             API = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
             ```
      - Running the Script:
          - Run the script:
            ```shell
            python price_tracker.py
            ```
              - The script will check the price of the specified product and send an email alert if the price is below the target price.
           
- **Documentation:**

  - Requests: https://docs.python-requests.org/en/latest/index.html
  - Lxml: https://lxml.de/index.html
  - BeautifulSoup4: https://beautiful-soup-4.readthedocs.io/en/latest/
  - Smtplib: https://docs.python.org/3/library/smtplib.html


## 🤝 Feedback and Contributions
I have made every effort to implement all the main aspects of the Amazon Price Tracker in the best possible way. However, the development journey doesn't end here, and your input is crucial for our continuous improvement.

> [!IMPORTANT]
> Whether you have feedback on features, have encountered any bugs, or have suggestions for enhancements, we're eager to hear from you. Your insights help us make the Abblix OIDC Server library more robust and user-friendly.

Please feel free to contribute by [submitting an issue](https://github.com/Akwaowo91/Amazon-price-tracker.Server/issues)
We appreciate your support and look forward to making our product even better with your help!

Feel free to replace placeholder texts like "your-username", "your-email@gmail.com", and the repository URL with the actual details. This README structure provides a clear and comprehensive overview of your project, guiding users on how to use and contribute to it.

            
       
