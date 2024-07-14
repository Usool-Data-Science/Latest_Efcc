""" objects that handle all default RestFul API actions for identities """
from flask import (Flask, flash, jsonify, make_response, abort,
                   request, redirect, url_for, render_template)
from api.v1.views import app_views
from api.v1.forms import (RecoveryForm, MonetaryForm, BankForm, CashForm,
                          CryptoForm, AutomobileForm, ElectronicForm, PhoneForm,
                          OtherForm, JewelryForm, LandedPropertyForm, LaptopForm)

@app_views.route('/recoveries', methods=['POST'], strict_slashes=False)
def post_recoveries():
    """
    Creates a Recovery
    """
    import models
    from models.recovery import Recovery

    form = RecoveryForm()

    if form.validate_on_submit():
        instance = Recovery(
            petition_id=form.petition_id.data,
            suspect_id=form.suspect_id.data
        )
        models.db.session.add(instance)
        models.db.session.commit()
        flash(f'A new Recovery(ID: {instance.id}) has been created', 'success')
    else:
        flash('There is an error creating the Recovery', 'danger')
    return redirect(url_for('app_views.get_petition', petition_id=form.petition_id.data))

@app_views.route('/monetaries', methods=['POST'], strict_slashes=False)
def post_monetaries():
    """
    Creates a Monetary
    """
    import models
    from models.recovery import Monetary
    from models.recovery import Recovery

    form = MonetaryForm()

    if form.validate_on_submit():
        instance = Monetary(
            status=form.status.data,
            recovery_id=form.recovery_id.data
        )
        models.db.session.add(instance)
        models.db.session.commit()
        flash(f'A new monetary(ID: {instance.id}) recovery has been created', 'success')
        recov = Recovery.query.filter(Recovery.id == form.recovery_id.data).first()
        petition_id = recov.petition_id
        return redirect(url_for('app_views.get_petition', petition_id=petition_id))
    else:
        flash('There is an error creating the Monetary recovery', 'danger')
    return redirect(url_for('app_views.dashboard'))

@app_views.route('/banks', methods=['POST'], strict_slashes=False)
def post_banks():
    """
    Creates a Bank
    """
    import models
    from models.recovery import Bank, Monetary, Recovery

    form = BankForm()

    if form.validate_on_submit():
        instance = Bank(
            bank_name=form.bank_name.data,
            serial_number=form.serial_number.data,
            amount=form.amount.data,
            favour_off=form.favour_off.data,
            monetary_id=form.monetary_id.data
        )
        models.db.session.add(instance)
        models.db.session.commit()
        flash(f'A new Bank(ID: {instance.id}) recovery has been created', 'success')
        money = Monetary.query.filter(Monetary.id == form.monetary_id.data).first()
        recov = Recovery.query.filter(Recovery.id == money.recovery_id).first()
        petition_id = recov.petition_id
        return redirect(url_for('app_views.get_petition', petition_id=petition_id))
    else:
        flash('There is an error creating the Bank recovery', 'danger')
    return redirect(url_for('app_views.dashboard'))

@app_views.route('/cryptos', methods=['POST'], strict_slashes=False)
def post_cryptos():
    """
    Creates a Crypto
    """
    import models
    from models.recovery import Crypto, Monetary, Recovery

    form = CryptoForm()

    if form.validate_on_submit():
        instance = Crypto(
            asset_name=form.asset_name.data,
            asset_size=form.asset_size.data,
            asset_worth=form.asset_worth.data,
            monetary_id=form.monetary_id.data
        )
        models.db.session.add(instance)
        models.db.session.commit()
        flash(f'A new Crypto(ID: {instance.id}) recovery for asset has been created', 'success')
        money = Monetary.query.filter(Monetary.id == form.monetary_id.data).first()
        recov = Recovery.query.filter(Recovery.id == money.recovery_id).first()
        petition_id = recov.petition_id
        return redirect(url_for('app_views.get_petition', petition_id=petition_id))
    else:
        flash('There is an error creating the Crypto recovery', 'danger')
    return redirect(url_for('app_views.dashboard'))

@app_views.route('/cashes', methods=['POST'], strict_slashes=False)
def post_cashes():
    """
    Creates a Cash
    """
    import models
    from models.recovery import Cash, Monetary, Recovery

    form = CashForm()

    if form.validate_on_submit():
        instance = Cash(
            denomination=form.denomination.data,
            amount=form.amount.data,
            monetary_id=form.monetary_id.data
        )
        models.db.session.add(instance)
        models.db.session.commit()
        flash(f'A new Cash recovery(ID: {instance.id}) with amount has been created', 'success')
        money = Monetary.query.filter(Monetary.id == form.monetary_id.data).first()
        recov = Recovery.query.filter(Recovery.id == money.recovery_id).first()
        petition_id = recov.petition_id
        return redirect(url_for('app_views.get_petition', petition_id=petition_id))
    else:
        flash('There is an error creating the Cash recovery', 'danger')
    return redirect(url_for('app_views.dashboard'))

@app_views.route('/automobiles', methods=['POST'], strict_slashes=False)
def post_automobiles():
    """
    Creates an Automobile
    """
    import models
    from models.recovery import Automobile, Recovery

    form = AutomobileForm()

    if form.validate_on_submit():
        instance = Automobile(
            description=form.description.data,
            plate_number=form.plate_number.data,
            chasis_number=form.chasis_number.data,
            colar=form.colar.data,
            other_info=form.other_info.data,
            status=form.status.data,
            recovery_id=form.recovery_id.data
        )
        models.db.session.add(instance)
        models.db.session.commit()
        flash(f'A new Automobile(ID: {instance.id}) recovery with plate number has been created', 'success')
        recov = Recovery.query.filter(Recovery.id == form.recovery_id.data).first()
        petition_id = recov.petition_id
        return redirect(url_for('app_views.get_petition', petition_id=petition_id))
    else:
        flash('There is an error creating the Automobile recovery', 'danger')
    return redirect(url_for('app_views.dashboard'))

@app_views.route('/electronics', methods=['POST'], strict_slashes=False)
def post_electronics():
    """
    Creates an Electronic
    """
    import models
    from models.recovery import Electronic, Recovery

    form = ElectronicForm()

    if form.validate_on_submit():
        instance = Electronic(
            status=form.status.data,
            recovery_id=form.recovery_id.data
        )
        models.db.session.add(instance)
        models.db.session.commit()
        flash(f'A new Electronic(ID: {instance.id}) recovery has been created', 'success')
        recov = Recovery.query.filter(Recovery.id == form.recovery_id.data).first()
        petition_id = recov.petition_id
        return redirect(url_for('app_views.get_petition', petition_id=petition_id))
    else:
        flash('There is an error creating the Electronic recovery', 'danger')
    return redirect(url_for('app_views.dashboard'))

@app_views.route('/phones', methods=['POST'], strict_slashes=False)
def post_phones():
    """
    Creates a Phone
    """
    import models
    from models.recovery import Phone, Electronic, Recovery

    form = PhoneForm()

    if form.validate_on_submit():
        instance = Phone(
            phone_name=form.phone_name.data,
            color=form.color.data,
            imei=form.imei.data,
            electronic_id=form.electronic_id.data
        )
        models.db.session.add(instance)
        models.db.session.commit()
        flash(f'A new Phone(ID: {instance.id}) recovery has been created', 'success')
        elect = Electronic.query.filter(Electronic.id == form.electronic_id.data).first()
        recov = Recovery.query.filter(Recovery.id == elect.recovery_id).first()
        petition_id = recov.petition_id
        return redirect(url_for('app_views.get_petition', petition_id=petition_id))
    else:
        flash('There is an error creating the Phone recovery', 'danger')
    return redirect(url_for('app_views.dashboard'))

@app_views.route('/laptops', methods=['POST'], strict_slashes=False)
def post_laptops():
    """
    Creates a Laptop
    """
    import models
    from models.recovery import Laptop, Electronic, Recovery

    form = LaptopForm()

    if form.validate_on_submit():
        instance = Laptop(
            serial_no=form.serial_no.data,
            color=form.color.data,
            name=form.name.data,
            electronic_id=form.electronic_id.data
        )
        models.db.session.add(instance)
        models.db.session.commit()
        flash(f'A new Laptop(ID: {instance.id}) recovery with serial number has been created', 'success')
        elect = Electronic.query.filter(Electronic.id == form.electronic_id.data).first()
        recov = Recovery.query.filter(Recovery.id == elect.recovery_id).first()
        petition_id = recov.petition_id
        return redirect(url_for('app_views.get_petition', petition_id=petition_id))
    else:
        flash('There is an error creating the Laptop recovery', 'danger')
    return redirect(url_for('app_views.dashboard'))

@app_views.route('/others', methods=['POST'], strict_slashes=False)
def post_others():
    """
    Creates an Other
    """
    import models
    from models.recovery import Other, Electronic, Recovery

    form = OtherForm()

    if form.validate_on_submit():
        instance = Other(
            description=form.description.data,
            electronic_id=form.electronic_id.data
        )
        models.db.session.add(instance)
        models.db.session.commit()
        flash(f'A new recovery of other(ID: {instance.id}) type has been created', 'success')
        elect = Electronic.query.filter(Electronic.id == form.electronic_id.data).first()
        recov = Recovery.query.filter(Recovery.id == elect.recovery_id).first()
        petition_id = recov.petition_id
        return redirect(url_for('app_views.get_petition', petition_id=petition_id))
    else:
        flash('There is an error creating the Phone recovery', 'danger')
    return redirect(url_for('app_views.dashboard'))

@app_views.route('/jewelries', methods=['POST'], strict_slashes=False)
def post_jewelries():
    """
    Creates a Jewelry
    """
    import models
    from models.recovery import Jewelry, Recovery

    form = JewelryForm()

    if form.validate_on_submit():
        instance = Jewelry(
            name=form.name.data,
            description=form.description.data,
            status=form.status.data,
            recovery_id=form.recovery_id.data
        )
        models.db.session.add(instance)
        models.db.session.commit()
        flash(f'A new Jewelry(ID: {instance.id}) recovery has been created', 'success')
        recov = Recovery.query.filter(Recovery.id == form.recovery_id.data).first()
        petition_id = recov.petition_id
        return redirect(url_for('app_views.get_petition', petition_id=petition_id))
    else:
        flash('There is an error creating the Jewelry recovery', 'danger')
    return redirect(url_for('app_views.dashboard'))

@app_views.route('/landedproperties', methods=['POST'], strict_slashes=False)
def post_landedproperties():
    """
    Creates a LandedProperty
    """
    import models
    from models.recovery import LandedProperty, Recovery

    form = LandedPropertyForm()

    if form.validate_on_submit():
        instance = LandedProperty(
            location=form.location.data,
            size=form.size.data,
            status=form.status.data,
            recovery_id=form.recovery_id.data
        )
        models.db.session.add(instance)
        models.db.session.commit()
        flash(f'A new Landed Property(ID: {instance.id}) has been created', 'success')
        recov = Recovery.query.filter(Recovery.id == form.recovery_id.data).first()
        petition_id = recov.petition_id
        return redirect(url_for('app_views.get_petition', petition_id=petition_id))
    else:
        flash('There is an error creating the Landed Property recovery', 'danger')
    return redirect(url_for('app_views.dashboard'))

