from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            shifted = ord(char) + shift_amount
            if char.islower():
                result += chr((shifted - ord('a')) % 26 + ord('a'))
            elif char.isupper():
                result += chr((shifted - ord('A')) % 26 + ord('A'))
        elif char.isdigit():
            result += chr((ord(char) + shift - ord('0')) % 10 + ord('0'))
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result_text = ""
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        mode = request.form['mode']
        result_text = caesar_cipher(text, shift, mode)
    return render_template('index.html', result_text=result_text)

if __name__ == '__main__':
    app.run(debug=True)
