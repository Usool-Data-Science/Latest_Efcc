""" objects that handle all default RestFul API actions for petitions """

from flask import (Flask, flash, jsonify, make_response, abort,
                   request, redirect, url_for, render_template)
from api.v1.views import app_views
from api.v1.forms import FingerPrintForm

@app_views.route('/fingerprints', methods=['GET'], strict_slashes=False)
def get_fingerprints():
    """
    Retrieves the list of all FingerPrint objects
    """
    from models import db
    from models.fingerprint import FingerPrint

    form = FingerPrintForm()
    all_fingerprints = FingerPrint.query.all()
    fingerprints = []
    for fingerprint in all_fingerprints:
        fp = fingerprint.to_dict()
        if "__class__" in fp:
            del fp["__class__"]
        fingerprints.append(fp)
    fingerprints.reverse()
    return render_template("fingerprint.html",
                           fingerprints=fingerprints[:5], title="Fingerprint",
                           sum_fingerprints=len(fingerprints), form=form)

@app_views.route('/fingerprints', methods=['POST'], strict_slashes=False)
def post_fingerprints():
    """
    Creates a FingerPrint
    """
    from models import db
    from models.fingerprint import FingerPrint

    form = FingerPrintForm()
    if form.validate_on_submit():
        print("FORM IS AVAILABLE")
        finger_print = form.finger_print.data
        instance = FingerPrint(finger_print=form.finger_print.data,
                               mugshot=form.mugshot.data,
                               suspect_id=form.suspect_id.data)
        db.session.add(instance)
        db.session.commit()
        flash(f'A new FingerPrint has been created', 'success')
    else:
        flash('There is an error creating the FingerPrint', 'danger')
    return redirect(url_for('app_views.get_fingerprints'))

@app_views.route('/fingerprints/<fingerprint_id>', methods=['GET'], strict_slashes=False)
def get_fingerprint(fingerprint_id):
    """ Retrieves a specific FingerPrint """
    from models import db
    from models.fingerprint import FingerPrint

    fingerprint = FingerPrint.query.get(fingerprint_id)
    if not fingerprint:
        abort(404)
    return jsonify(fingerprint.to_dict())

@app_views.route('/fingerprints/<fingerprint_id>', methods=['DELETE'], strict_slashes=False)
def delete_fingerprint(fingerprint_id):
    """
    Deletes a FingerPrint Object
    """
    from models import db
    from models.fingerprint import FingerPrint

    fingerprint = FingerPrint.query.get(fingerprint_id)
    if not fingerprint:
        abort(404)
    db.session.delete(fingerprint)
    db.session.commit()
    return make_response(jsonify({}), 200)

@app_views.route('/fingerprints/<fingerprint_id>', methods=['PUT'], strict_slashes=False)
def put_fingerprint(fingerprint_id):
    """
    Updates a FingerPrint
    """
    from models import db
    from models.fingerprint import FingerPrint

    fingerprint = FingerPrint.query.get(fingerprint_id)
    if not fingerprint:
        abort(404)
    
    form = FingerPrintForm()
    if form.validate_on_submit():
        fingerprint.finger_print = form.finger_print.data
        fingerprint.mugshot = form.mugshot.data
        fingerprint.suspect_id = form.suspect_id.data
        db.session.commit()
        flash(f'FingerPrint has been updated', 'success')
    else:
        flash('There is an error updating the FingerPrint', 'danger')
    
    return redirect(url_for('app_views.get_fingerprints'))
