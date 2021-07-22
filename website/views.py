from flask import Blueprint, render_template,request
from flask_login import login_required, current_user
from . import db
from .models import Notes
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/notes',methods=['GET', 'POST'])
@login_required
def notes():
    if request.method == 'POST':
        note = request.form.get('note')
        new_note = Notes(data=note,user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
    return render_template('notes.html', user=current_user)