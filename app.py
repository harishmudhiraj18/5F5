from flask import Flask, request, render_template
app = Flask( name )
@app.route('/register', methods=['GET', 'POST'])

def register():
if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
# Store the user data in a database or file
return render_template('success.html')
# lOMoAR cPSD|31427016
return render_template('register.html')
if name == ' main ':
    app.run(host='0.0.0.0')
    print("Success")
