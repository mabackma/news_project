from flask import Flask, jsonify, request
from newstools import search, top_headlines

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def get_query():
    # Get the request JSON data
    data = request.get_json()

    # Extract the query from the object. data contains a list of only one json object
    for item in data:
        query = item.get('query')
        search_in = item.get('search_in')
        sort_items = item.get('sort_items')
        language = item.get('language')
        page_size = item.get('page_size')
        page = item.get('page')
        start = item.get('start')
        end = item.get('end')

    # Perform the search operation and get the results
    results = search(query, search_in, sort_items, language, page_size, page, start, end)

    # Return the results as JSON response
    print(results)
    return jsonify(results)

@app.route('/headlines', methods=['POST'])
def get_headlines():
    # Get the request JSON data
    data = request.get_json()

    # Extract the query from the object. data contains a list of only one json object
    for item in data:
        country = item.get('country')
        category = item.get('category')

    # Perform the search operation and get the results
    results = top_headlines(country, category)

    # Return the results as JSON response
    print(results)
    return jsonify(results)

if __name__ == '__main__':
    app.run()
