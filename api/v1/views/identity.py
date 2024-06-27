""" objects that handle all default RestFul API actions for identities """
from flask import (Flask, flash, jsonify, make_response, abort,
                   request, redirect, url_for, render_template)
from api.v1.views import app_views
from api.v1.forms import IdentityForm

@app_views.route('/identities', methods=['GET'], strict_slashes=False)
def get_identities():
    """
    Retrieves the list of all Identity objects
    """
    from models import db
    from models.identity import Identity

    form = IdentityForm()
    all_identities = Identity.query.all()
    identities = []
    for identity in all_identities:
        idn = identity.to_dict()
        if "__class__" in idn:
            del idn["__class__"]
        identities.append(idn)
    identities.reverse()
    return render_template("identity.html",
                           identities=identities[:5], title="Identity",
                           sum_identities=len(identities), form=form)

@app_views.route('/identities', methods=['POST'], strict_slashes=False)
def post_identities():
    """
    Creates an Identity
    """
    from models import db
    from models.identity import Identity

    form = IdentityForm()
    if form.validate_on_submit():
        print("FORM IS AVAILABLE")
        instance = Identity(id_types=form.id_types.data,
                            id_number=form.id_number.data,
                            suspect_id=form.suspect_id.data)
        db.session.add(instance)
        db.session.commit()
        flash(f'A new Identity has been created', 'success')
    else:
        flash('There is an error creating the Identity', 'danger')
    return redirect(url_for('app_views.get_identities'))

@app_views.route('/identities/<identity_id>', methods=['GET'], strict_slashes=False)
def get_identity(identity_id):
    """ Retrieves a specific Identity """
    from models import db
    from models.identity import Identity

    identity = Identity.query.get(identity_id)
    if not identity:
        abort(404)
    return jsonify(identity.to_dict())

@app_views.route('/identities/<identity_id>', methods=['DELETE'], strict_slashes=False)
def delete_identity(identity_id):
    """
    Deletes an Identity Object
    """
    from models import db
    from models.identity import Identity

    identity = Identity.query.get(identity_id)
    if not identity:
        abort(404)
    db.session.delete(identity)
    db.session.commit()
    return make_response(jsonify({}), 200)

@app_views.route('/identities/<identity_id>', methods=['PUT'], strict_slashes=False)
def put_identity(identity_id):
    """
    Updates an Identity
    """
    from models import db
    from models.identity import Identity

    identity = Identity.query.get(identity_id)
    if not identity:
        abort(404)
    
    form = IdentityForm()
    if form.validate_on_submit():
        identity.id_types = form.id_types.data
        identity.id_number = form.id_number.data
        identity.suspect_id = form.suspect_id.data
        db.session.commit()
        flash(f'Identity has been updated', 'success')
    else:
        flash('There is an error updating the Identity', 'danger')
    
    return redirect(url_for('app_views.get_identities'))
