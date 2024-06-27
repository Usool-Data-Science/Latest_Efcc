#!/usr/bin/python3
""" objects that handle all default RestFul API actions for complainants """
from flask import (Flask, flash, jsonify, make_response, abort,
                   request, redirect, url_for, render_template)
from api.v1.views import app_views
from api.v1.forms import ComplainantForm
import models

@app_views.route('/complainants', methods=['GET'], strict_slashes=False)
def get_complainants():
    """
    Retrieves the list of all Complainant objects
    """
    from models.complainant import Complainant

    form = ComplainantForm()
    all_complainants = Complainant.query.all()
    complainants = []
    for complainant in all_complainants:
        compln = complainant.to_dict()
        if "__class__" in compln:
            del compln["__class__"]
        complainants.append(compln)
    complainants.reverse()

    return render_template("complainant.html",
                           complainants=complainants[:5], title="Complainant",
                           sum_complainants=len(complainants), form=form)

@app_views.route('/complainants', methods=['POST'], strict_slashes=False)
def post_complainants():
    """
    Creates a Complainant
    """
    from models.complainant import Complainant

    form = ComplainantForm()
    if form.validate_on_submit():
        print("FORM IS AVAILABLE")
        name = form.name.data
        instance = Complainant(name=form.name.data,
                               address=form.address.data,
                               nationality=form.nationality.data,
                               state=form.state.data,
                               gender=form.gender.data,
                               age=form.age.data,
                               occupation=form.occupation.data,
                               religion=form.religion.data,
                               education=form.education.data,
                               phone_no=form.phone.data)
        models.db.session.add(instance)
        models.db.session.commit()
        flash(f'A new Complainant {[name]} has been created', 'success')
    else:
        flash(f'There is an error creating Complainant {[name]}', 'danger')
    return redirect(url_for('app_views.get_complainants'))

@app_views.route('/complainants/<complainant_id>', methods=['GET'], strict_slashes=False)
def get_Complainant(complainant_id):
    """ Retrieves a specific Complainant """
    from models.complainant import Complainant

    complainant = Complainant.query.get(complainant_id)
    if not complainant:
        abort(404)

    return jsonify(complainant.to_dict())

@app_views.route('/complainants/<complainant_id>', methods=['DELETE'], strict_slashes=False)
def delete_Complainant(complainant_id):
    """
    Deletes a Complainant Object
    """
    from models.complainant import Complainant

    complainant = Complainant.query.get(complainant_id)
    if not complainant:
        abort(404)

    models.db.session.delete(complainant)
    models.db.session.commit()

    return make_response(jsonify({}), 200)

@app_views.route('/complainants/<complainant_id>', methods=['PUT'], strict_slashes=False)
def put_Complainant(complainant_id):
    """
    Updates a Complainant
    """
    from models.complainant import Complainant
    
    complainant = Complainant.query.get(complainant_id)
    if not complainant:
        abort(404)

    form = ComplainantForm()
    if form.validate_on_submit():
        complainant.name = form.name.data
        complainant.address = form.address.data
        complainant.nationality = form.nationality.data
        complainant.state = form.state.data
        complainant.gender = form.gender.data
        complainant.age = form.age.data
        complainant.occupation = form.occupation.data
        complainant.religion = form.religion.data
        complainant.education = form.education.data
        complainant.phone_no = form.phone.data
        models.db.session.commit()
        flash(f'Complainant {[complainant.name]} has been updated', 'success')
    else:
        flash(f'There is an error updating Complainant {[complainant.name]}', 'danger')

    return redirect(url_for('app_views.get_complainants'))

    """
    Updates a Complainant
    """
    complainant = models.storage.get(Complainant, complainant_id)

    if not complainant:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(Complainant, key, value)
    models.storage.save()
    return make_response(jsonify(complainant.to_dict()), 200)