from flask import Flask, render_template, request
import re

app = Flask(__name__)

def extract_emails(text):
    # Regex to find email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)

@app.route('/', methods=['GET', 'POST'])
def index():
    emails = []
    if request.method == 'POST':
        raw_text = request.form['raw_data']
        emails = extract_emails(raw_text)
    return render_template('index.html', emails=emails)

if __name__ == '__main__':
    app.run(debug=True)
