from flask import Flask, request, render_template

application = Flask(__name__)

@application.route('/')
def calendar():
    return render_template("index.html")

@application.route('/data')
def return_data():
    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')

    with open("data.json", "r") as input_data:
				return input_data.read()

if __name__ == "__main__":
    application.debug = True
    application.run()
