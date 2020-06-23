from flask import Flask, request
import random
app = Flask(__name__)


@app.route('/tg', methods=['GET', 'POST'])
def test():
    print(request)
    return str(random.randint(0, 100))


app.run(debug=True)