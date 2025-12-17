from flask import Flask, render_template, request, redirect, url_for, session
import re
from datetime import datetime
app = Flask(__name__)
from utils_flightboard import get_flights_board



'''HOME PAGE'''
@app.route('/')
def homepage():
    return render_template("home_page.html")

'''FLIGHT BOARD'''
@app.route('/flights_board')
def flights_board():
    flights_data = get_flights_board()
    return render_template("flights_board.html" ,flights_data=flights_data)

'''SIGN UP PAGE'''
@app.route('/signup_page' ,methods=['GET', 'POST']) #creating signup page with forms
def signup_page():
    if request.method == "POST":
        registration_date = datetime.now()
        signup_first_name = request.form.get('signup_first_name')
        signup_last_name = request.form.get('signup_last_name')
        email_user=request.form.get('email_user')
        phones_list=request.form.getlist('phone_number_user')
        phone_1 = phones_list[0] if len(phones_list) > 0 else ""
        phone_2 = phones_list[1] if len(phones_list) > 1 else ""
        phone_3 = phones_list[2] if len(phones_list) > 2 else ""
        passport_code=request.form.get('passport_code')
        birth_date=request.form.get('birth_date')
        password_user=request.form.get('password_user')
        confirm_password_user=request.form.get('confirm_password_user')

        if not checking_validation(signup_first_name) or not checking_validation(signup_last_name): #checking if the names are really just in english letters
           return render_template("signup_page.html",
                                  error_message_name="Name must contain only English letters",
                signup_first_name = signup_first_name,
                signup_last_name = signup_last_name,
                email_user = email_user,
                passport_code = passport_code,
                birth_date = birth_date,
                phone_1 = phone_1, phone_2 = phone_2, phone_3 = phone_3)

        if birth_date:
            birth_date_obj = datetime.strptime(birth_date, '%Y-%m-%d') #Checking if the birth date is in the past
            if birth_date_obj.date() >= datetime.now().date():
                return render_template("signup_page.html",
                                       error_message_date="Birth date must be in the past",
                    signup_first_name = signup_first_name,
                    signup_last_name = signup_last_name,
                    email_user = email_user,
                    passport_code = passport_code,
                    birth_date = birth_date,
                    phone_1 = phone_1, phone_2 = phone_2, phone_3 = phone_3)

        if not checking_matching_password(password_user,confirm_password_user): #cheking the matching of confirming the password and the password
           return render_template("signup_page.html",
                                  error_message_pass="Unmatched passwords",
                                  signup_first_name=signup_first_name,
                                  signup_last_name=signup_last_name,
                                  email_user=email_user,
                                  passport_code=passport_code,
                                  birth_date=birth_date,
                                  phone_1=phone_1, phone_2=phone_2, phone_3=phone_3)

        return render_template("signup_success_page.html", name=signup_first_name)
    else:
        return render_template("signup_page.html")

"""Errors Checking functions:"""

def checking_validation(text):
    if not text:
        return False
    return bool(re.fullmatch(r'[A-Za-z ]+', text))

def checking_matching_password(pass_1,pass_2):
    return pass_1==pass_2

'''LOG IN PAGE'''
@app.route('/login_page', methods=['GET', 'POST'])
def login_page():
    current_role = request.args.get('role', 'customer') #setting entrance as a customer

    if request.method == "POST":

        form_type = request.form.get('which_form_is_this') #connecting with the HTML hidden "which form is this"

        if form_type == 'customer': #if it's a customer
            email = request.form.get('email_user')
            password = request.form.get('password_user')

            #if email == "shaked@test.com" and password == "1234": #looking if we have the user in our database
             #   return render_template("flights_board.html")  #if so, taking the user to the flight board
            #else:
             #   return render_template("login_page.html", role='customer', error_message="Wrong email or password") #error message

        elif form_type == 'manager': #if it's a manager
            manager_id = request.form.get('manager_id')
            password = request.form.get('password_manager')

            #if manager_id == "99999" and password == "admin": #looking if we have the user in our database
             #   return render_template("flights_board.html") #if so, taking the user to the flight board
            #else:
             #   return render_template("login_page.html", role='manager', error_message="Wrong Manager ID or password") #error message
    return render_template("login_page.html", role=current_role)
    ''''PAYING PAGE'''
@app.route('/paying_page')
def paying_page():
    return render_template("paying_page.html")



    return render_template("login_page.html", role=current_role)

if __name__ == '__main__':
    app.run(debug=True)
