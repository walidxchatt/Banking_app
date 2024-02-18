from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET','POST'])
def login():

    #data = request.form
    #print(data)

    return render_template("dashboard.html")
    #return redirect('dashboard')


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():

    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        lastName = request.form.get('password')

        #Add checks later (whether info is valid or not)
        #Message flashing (COOL FLASK FEATURE)

        flash('Account created!', category='success')
        #flash('La ya misterr!', category='error')


    return render_template("sign_up.html")




    
    
    """
    if request.method == 'POST':
        data = request.get_json()

        name = data.get('name')
        password = data.get('password')
        initial_amount = data.get('initial_amount', 0)

        if name is None or password is None:
            return jsonify({'error': 'Name and password are required'}), 400

        if name in people_data:
            return jsonify({'error': 'Person with that name already exists'}), 400

        people_data[name] = {'name': name, 'password': password, 'amount': initial_amount}

        return jsonify({'message': 'Person created successfully'}), 201
    """