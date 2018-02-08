from models.wl import Wl
from routes import *

main = Blueprint('todo', __name__)
Model = Wl


@main.route('/')
def index():
    ms = Model.query.all()
    return render_template('wl_list.html', ms=ms)


@main.route('/edit/<id>')
def edit(id):
    t = Model.query.filter_by(id=id).first()
    return render_template('wl_edit.html', todo=t)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    t = Model(form)
    t.save()
    return redirect(url_for('.index'))


@main.route('/update/<id>', methods=['POST'])
def update(id):
    form = request.form
    t = Model.query.filter_by(id=id).first()
    t.update(form)
    return redirect(url_for('.index'))


@main.route('/delete/<id>')
def delete(id):
    t = Model.query.filter_by(id=id).first()
    t.delete()
    return redirect(url_for('.index'))
