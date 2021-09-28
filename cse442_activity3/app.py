from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    host = '0.0.0.0'
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    print(port)
    app.run(port=port, host=host)
