from flask import Flask
from flask import jsonify
import pandas as pd
import wikipedia
app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is a Hello World World Page</title>
    <p><b>Hello people</b></p>
    <p><b>This is "Continuous Delivery of Flask Application on GCP"</b></p>
    <p><b>You can find the code for this on my Github:https://github.com/Vishnu-Madamanchi/flask</b><p>
    <p><b>Next Project on "Docker Container" Coming up soon! Stay tune to my Github page</b><p>
    """

@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())


@app.route('/wikipedia/<company>')
def wikipedia_route(company):

    # Imports the Google Cloud client library
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types
    result = wikipedia.summary(company, sentences=10)

    client = language.LanguageServiceClient()
    document = types.Document(
        content=result,
        type=enums.Document.Type.PLAIN_TEXT)
    entities = client.analyze_entities(document).entities
    return str(entities)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
