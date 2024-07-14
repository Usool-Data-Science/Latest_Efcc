from flask import (jsonify, render_template, flash, request, 
                   redirect, url_for)
from flask_login import login_user, current_user, logout_user, login_required

from api.v1.views import app_views
from api.v1.forms import LoginForm, RegistrationForm, PetitionForm, SearchForm
import models


def wrap_petition(petitions):
    """A Nice wrapper for petition that decides what is show in
        on the dashboard or what not.
    """
    response = []
    for petition in petitions:
        petition_dict = {}

        petition_dict['id'] = petition.id
        petition_dict['Case File #'] = petition.casefile_no
        petition_dict['Credential #'] = petition.cr_no
        petition_dict['Date Assigned'] = petition.date_assigned

        complainant_names = [str(compt.name) for compt in petition.complainants]
        petition_dict['Complainants'] = ", ".join(complainant_names)

        petition_dict['Amount'] = petition.amount_involved
        petition_dict['Source'] = petition.petition_source
        petition_dict['Status'] = petition.status_signal

        response.append(petition_dict)

    return response

@app_views.route("/status", strict_slashes=False)
def status():
    return jsonify({"status": "OK!"})


@app_views.route("/", strict_slashes=False)
def home():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app_views.route("/admin", methods=['GET', 'POST'], strict_slashes=False)
def admin():
    from models import bcrypt, viewer
    from models.staff import Staff

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
                gender=form.gender.data,
                state=form.state_of_origin.data,
                admin = form.is_admin.data
            )
            models.db.session.add(staff)
            models.db.session.commit()
            flash(f"{form.first_name.data}'s staff account has been created!", 'success')
            # return redirect(url_for('app_views.login'))
        else:
            flash(f"There is an error creating your staff account", 'danger')
    # return render_template('admin/index.html', title='Admin', form=form)
    return viewer.render('admin/index.html', title='Admin', form=form)


@app_views.route("/login", methods=['GET', 'POST'], strict_slashes=False)
def login():
    from models import bcrypt
    from models.staff import Staff

    if current_user.is_authenticated:
        return redirect(url_for("app_views.dashboard"))

    form = LoginForm()
    if form.validate_on_submit():
        user = Staff.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if form.admin.data and current_user.admin:
                # Direct them to the admin page if they want to go there and has the privilege.
                return redirect(url_for("app_views.admin"))
            else:
                return redirect(next_page) if next_page else redirect(url_for("app_views.dashboard"))
        else:
            flash(f'Login not successful. Check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app_views.route("/logout", strict_slashes=False)
def logout():
    logout_user()
    return redirect(url_for('app_views.home'))

@app_views.route("/dashboard", methods=['GET', 'POST'], strict_slashes=False)
@login_required
def dashboard():
    from models.petition import Petition
    from models.complainant import Complainant
    from models.suspect import Suspect
    from models.recovery import Recovery, Cash

    gender = current_user.gender
    all_complainants = Complainant.query.all()
    all_suspects = Suspect.query.all()
    all_recoveries = Recovery.query.all()
    all_petitions = Petition.query.order_by(Petition.date_received.desc()).all()
    sum_dollar = 0
    sum_pound = 0
    sum_euro = 0
    sum_naira = 0
    sum_ui = 0
    sum_legal = 0
    sum_court = 0
    sum_convicted = 0

    """ Compute the Crime statistics For recovery"""
    all_cash = Cash.query.all()
    for cash in all_cash:
        if cash.denomination == "USD":
            sum_dollar += cash.amount
        elif cash.denomination == "EUR":
            sum_euro += cash.amount
        elif cash.denomination == "GBP":
            sum_pound += cash.amount
        else:
            sum_naira += cash.amount

    """ Compute the Crime statistics For status"""
    for petition in all_petitions:
        if petition.status_signal == "UI":
            sum_ui += 1
        elif petition.status_signal == "Legal":
            sum_legal += 1
        elif petition.status_signal == "Court":
            sum_court += 1
        else:
            sum_convicted += 1
    
    petForm = PetitionForm()
    searchForm = SearchForm()
    if request.method == 'POST':
        if petForm.submit.data and petForm.validate_on_submit():
            instance = Petition(
                casefile_no = petForm.casefile_no.data,
                cr_no = petForm.cr_no.data,
                date_received = petForm.date_received.data,
                date_assigned = petForm.date_assigned.data,
                amount_involved = petForm.amount_involved.data,
                status_signal = petForm.status_signal.data,
                petition_source = petForm.petition_source.data,
                staff_id = current_user.id)
            models.db.session.add(instance)
            models.db.session.commit()
            flash(f'A new Petition with Case File No: {petForm.casefile_no.data} has been created', 'success')
            return redirect(url_for('app_views.dashboard'))
        
        elif searchForm.validate_on_submit():
            feature = searchForm.feature.data
            value = searchForm.value.data
            this_petition = Petition.query.filter(getattr(Petition, feature) == value).all()
            response = wrap_petition(this_petition)

            return render_template("dashboard.html",
                           dashboard_result_list=response,
                           sum_petition=len(all_petitions),
                           sum_complainant=len(all_complainants),
                           sum_suspect=len(all_suspects),
                           sum_recovery=len(all_recoveries),
                           gender=gender, petForm=petForm,
                           searchForm=searchForm,sum_dollar=sum_dollar,
                           sum_pound=sum_pound, sum_euro=sum_euro,
                           sum_naira=sum_naira, sum_ui=sum_ui, 
                           sum_legal=sum_legal, sum_court=sum_court, 
                           sum_convicted=sum_convicted)
        else:
            flash('There is an error creating the Petition', 'danger')

    response = wrap_petition(all_petitions)
    return render_template("dashboard.html",
                           dashboard_result_list=response,
                           sum_petition=len(all_petitions),
                           sum_complainant=len(all_complainants),
                           sum_suspect=len(all_suspects),
                           sum_recovery=len(all_recoveries),
                           gender=gender, petForm=petForm,
                           searchForm=searchForm,sum_dollar=sum_dollar,
                           sum_pound=sum_pound, sum_euro=sum_euro,
                           sum_naira=sum_naira, sum_ui=sum_ui, 
                           sum_legal=sum_legal, sum_court=sum_court, 
                           sum_convicted=sum_convicted)


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
