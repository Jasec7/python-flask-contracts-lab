#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

#Root route to confirm Flask app is running and responding to GET requests.
@app.route("/")
def index():
    return f'<h1>Flask</h1>'

#Route to handle GET requests for a specific contract by ID
@app.route('/contract/<int:id>')
# function in charge of checking the parameter's id
def contract(id):
    #List comprehension filters contracts list for the one matching the provided ID.
    lt = [c for c in contracts if c['id'] == id]
    
    #if/else checks length to see if there's a contract if not return 404 response if no matching record is found.
    if len(lt) > 0:
        return f'This contract is for John and building a shed', 200
    else:
        return f'404: Contract not found', 404

# decorator with the 'customer_name" route expecting to be a string
@app.route('/customer/<string:customer_name>')

# function in charge of checking the customer_name
def customer(customer_name):
    #list comprehension Checks whether the given customer_name appears in the customers list
    lt = [c for c in customers if c in customer_name]

    #If/else checking the length of the list, return 404 response if no matching record is found.
    if len(lt) > 0:
        return f'{customer_name}', 204
    else:
        return f"customer no found",404



if __name__ == '__main__':
    app.run(port=5555, debug=True)
