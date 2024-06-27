from flask import (Flask, jsonify, render_template, flash, request, 
                   redirect, url_for)
from flask_login import login_user, current_user, logout_user, login_required

import api
from api.v1.views import app_views
from api.v1.forms import LoginForm, RegistrationForm
import models


@app_views.route("/status", strict_slashes=False)
def status():
    return jsonify({"status": "OK!"})


@app_views.route("/", strict_slashes=False)
def home():
    return render_template('identity.html')


@app_views.route("/register", methods=['GET', 'POST'], strict_slashes=False)
def register():
    from api.v1.app import bcrypt
    from models.staff import Staff

    if current_user.is_authenticated:
        return redirect(url_for("app_views.dashboard"))

    form = RegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            pasw_hs = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
            staff = Staff(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                password=pasw_hs,
                age=form.age.data,
                state=form.state_of_origin.data,
            )
            models.db.session.add(staff)
            models.db.session.commit()
            flash(f'Your staff account has been created!', 'success')
            return redirect(url_for('app_views.login'))
        else:
            flash(f"There is an error creating your staff account", 'danger')
    return render_template('register.html', title='Register', form=form)


@app_views.route("/login", methods=['GET', 'POST'], strict_slashes=False)
def login():
    from api.v1.app import bcrypt
    from models.staff import Staff

    if current_user.is_authenticated:
        return redirect(url_for("app_views.dashboard"))

    form = LoginForm()
    if form.validate_on_submit():
        user = Staff.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for("app_views.dashboard"))
        else:
            flash(f'Login not successful. Check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app_views.route("/logout", strict_slashes=False)
def logout():
    logout_user()
    return redirect(url_for('app_views.home'))


@app_views.route("/dashboard", strict_slashes=False)
@login_required
def dashboard():
    response = []
    all_petitions = Petition.query.all()
    """Get complainants names"""
    for petition in all_petitions:
        petition_dict = {}

        petition_dict['Case File #'] = petition.casefile_no
        petition_dict['Credential #'] = petition.cr_no
        petition_dict['Date Assigned'] = petition.date_assigned

        complainant_names = [str(compt.name) for compt in petition.complainants]
        petition_dict['Complainants'] = ", ".join(complainant_names)

        petition_dict['Amount'] = petition.amount_involved
        petition_dict['Source'] = petition.petition_source
        petition_dict['Status'] = petition.status_signal

        response.append(petition_dict)

    return render_template("dashboard.html",
                           dashboard_result_list=response,
                           sum_petition=len(all_petitions))


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """

    from models.complainant import Complainant
    from models.suspect import Suspect
    from models.fingerprint import FingerPrint
    from models.identity import Identity
    from models.petition import Petition
    from models.recovery import (Monetary, Bank, Crypto, Cash, Recovery,
                                Electronic, Phone, Laptop, Other,
                                Automobile, Jewelry, LandedProperty)

    classes = {"Complainant": Complainant, "Suspect": Suspect,
               "FingerPrint": FingerPrint, "Identity": Identity, "Petition": Petition,
               "Monetary": Monetary, "Bank": Bank, "Crypto": Crypto, "Cash": Cash,
               "Recovery": Recovery, "Electronic": Electronic, "Phone": Phone,
               "Laptop": Laptop, "Other": Other, "Automobile": Automobile,
               "Jewelry": Jewelry, "LandedProperty": LandedProperty}

    num_objs = {}
    for k, v in classes.items():
        num_objs[k] = models.db.session.query(v).count()

    return jsonify(num_objs)
