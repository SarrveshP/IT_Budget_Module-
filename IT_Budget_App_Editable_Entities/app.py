from flask import Flask, render_template, redirect, url_for, request
from models import db, BudgetMaster, BudgetTransaction
from forms import BudgetForm, TransactionForm
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'devkey123'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return redirect(url_for('add_budget'))

@app.route('/budget', methods=['GET', 'POST'])
def add_budget():
    form = BudgetForm()
    if form.validate_on_submit():
        print("✅ Form validated successfully")
        budget = BudgetMaster(
            bm_year=form.bm_year.data,
            bm_category=form.bm_category.data,
            bm_amount=form.bm_amount.data,
            bm_remarks=form.bm_remarks.data,
            bm_created_by='admin',
            bm_created_date=datetime.now()
        )
        db.session.add(budget)
        db.session.commit()
    else:
        print("❌ Form errors:", form.errors)

    budgets = BudgetMaster.query.all()
    return render_template('budget_form.html', form=form, budgets=budgets)


@app.route('/transaction', methods=['GET', 'POST'])
def add_transaction():
    form = TransactionForm()
    form.bt_category.choices = [(b.bm_category, b.bm_category) for b in BudgetMaster.query.all()]
    if form.validate_on_submit():
        txn = BudgetTransaction(
            bt_date=form.bt_date.data,
            bt_category=form.bt_category.data,
            bt_division=form.bt_division.data,
            bt_amount=form.bt_amount.data,
            bt_purpose=form.bt_purpose.data,
            bt_entered_by='division_head',
            bt_entered_date=datetime.now()
        )
        db.session.add(txn)
        db.session.commit()
        return redirect(url_for('add_transaction'))
    else:
        if request.method == 'POST':
            print("Form errors:", form.errors)  # Add this line for debugging
    transactions = BudgetTransaction.query.all()
    return render_template('transaction_form.html', form=form, transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)
