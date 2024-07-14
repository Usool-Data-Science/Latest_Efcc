#!/usr/bin/python3
""" Objects that handle all default RestFul API actions for petitions """
from flask import (flash, jsonify, make_response, abort,
                   request, redirect, url_for, render_template)
from api.v1.views import app_views
from api.v1.forms import PetitionForm
import models

@app_views.route('/petitions', methods=['GET'], strict_slashes=False)
def get_petitions():
    """
    Retrieves the list of all Petition objects
    """
    from models.petition import Petition
    from api.v1.forms import SearchForm

    form = PetitionForm()
    searchForm = SearchForm()
    petitions = Petition.query.order_by(Petition.date_received.desc())
    petition_dicts = [petition.to_dict() for petition in petitions]
    return render_template("petition.html",
                           petitions=petition_dicts, title="Petition",
                           sum_petitions=petitions.count(), form=form)

@app_views.route('/petitions', methods=['POST'], strict_slashes=False)
def post_petitions():
    """
    Creates a Petition
    """
    from models.petition import Petition
    from models.complainant import Complainant

    form = PetitionForm()
    
    if form.validate_on_submit():
        title = form.title.data
        instance = Petition(
            title=form.title.data,
            description=form.description.data,
            complainant_id=form.complainant_id.data,
            status=form.status.data
        )
        models.db.session.add(instance)
        models.db.session.commit()
        flash(f'A new Petition titled "{title}" has been created', 'success')
    else:
        flash('There is an error creating the Petition', 'danger')
    return redirect(url_for('app_views.get_petitions'))

@app_views.route('/petitions/<petition_id>', methods=['GET', 'POST'], strict_slashes=False)
def get_petition(petition_id):
    """ Retrieves a specific Petition details"""
    from models.utilities import calculate_completion_percentage
    from models.petition import Petition
    # from models.complainant import Complainant
    # from models.suspect import Suspect
    # from models.recovery import Recovery

    from api.v1.forms import (ComplainantForm, SuspectForm,
                              IdentityForm, FingerPrintForm,RecoveryForm,
                              MonetaryForm, BankForm, CashForm, CryptoForm,
                              AutomobileForm, ElectronicForm, PhoneForm,
                              OtherForm, JewelryForm, LandedPropertyForm,
                              LaptopForm)

    compForm = ComplainantForm()
    suspForm = SuspectForm()
    idForm = IdentityForm()
    fingerForm = FingerPrintForm()
    recoveryForm = RecoveryForm()
    monetaryForm = MonetaryForm()
    bankForm = BankForm()
    cashForm = CashForm()
    cryptoForm = CryptoForm()
    automobileForm = AutomobileForm()
    otherForm = OtherForm()
    jewelryForm = JewelryForm()
    landedpropertyForm = LandedPropertyForm()
    laptopForm = LaptopForm()
    electronicForm = ElectronicForm()
    phoneForm = PhoneForm()


    petition = Petition.query.get(petition_id)

    complainants_dict = [comp.to_dict() for comp in petition.complainants]
    comp_progress = calculate_completion_percentage(complainants_dict)

    suspects_dict = [susp.to_dict() for susp in petition.suspects]
    susp_progress = calculate_completion_percentage(suspects_dict)
    
    recoveries_dict = [recov.to_dict() for recov in petition.recoveries]
    recovery_progress = calculate_completion_percentage(recoveries_dict)

    if not petition:
        abort(404)

    return render_template('personal.html',
                           # Object Dictionaries
                           petition=petition.to_dict(),
                           complainants_dict=complainants_dict,
                           recoveries_dict=recoveries_dict,
                           suspects_dict=suspects_dict,
                           #Progresses
                           susp_progress=int(susp_progress), 
                           comp_progress=int(comp_progress),
                           recovery_progress=int(recovery_progress),
                           # Forms
                           compForm=compForm, suspectForm=suspForm,
                           idForm=idForm, fingerForm=fingerForm,
                           recoveryForm=recoveryForm, 
                           monetaryForm=monetaryForm, bankForm=bankForm,
                           cashForm=cashForm, cryptoForm=cryptoForm,
                           automobileForm=automobileForm, otherForm=otherForm,
                           jewelryForm=jewelryForm, laptopForm=laptopForm,
                           landedPropertyForm=landedpropertyForm,
                           electronicForm=electronicForm, phoneForm=phoneForm)

@app_views.route('/petitions/<petition_id>', methods=['DELETE'], strict_slashes=False)
def delete_petition(petition_id):
    """
    Deletes a Petition Object
    """
    from models.petition import Petition
    
    petition = Petition.query.get(petition_id)
    if not petition:
        abort(404)

    models.db.session.delete(petition)
    models.db.session.commit()
    return make_response(jsonify({}), 200)


@app_views.route('/petitions/<petition_id>', methods=['PUT'], strict_slashes=False)
def put_petition(petition_id):
    """
    Updates a Petition
    """
    from models.petition import Petition
    from models.complainant import Complainant

    petition = Petition.query.get(petition_id)
    if not petition:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(petition, key, value)
    models.db.session.commit()
    return make_response(jsonify(petition.to_dict()), 200)
