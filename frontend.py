from flask import Flask, render_template, request
from clumsySQL import Database as db

app = Flask(__name__)
db = db("Jozeph.csql")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'connect' in request.form:
            db.connect() # Connect to the database

    
        elif 'disconnect' in request.form:
            db.disconnect() # Disconnect from the database

        
        elif 'create_table' in request.form:
            db.create_table(["ID", "Name", "Mum Name", "Age"], "testing") # Create a table in the database

        
        elif 'get_data' in request.form:
            db.get_data() # Retrieve data from the database
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
