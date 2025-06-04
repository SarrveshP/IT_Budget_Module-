from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BudgetMaster(db.Model):
    __tablename__ = 'IT_BUDGET_MASTER'
    bm_id = db.Column(db.Integer, primary_key=True)
    bm_year = db.Column(db.String(10))
    bm_category = db.Column(db.String(50))
    bm_amount = db.Column(db.Float)
    bm_remarks = db.Column(db.String(255))
    bm_created_by = db.Column(db.String(50))
    bm_created_date = db.Column(db.DateTime)


class BudgetTransaction(db.Model):
    __tablename__ = 'IT_BUDGET_TRANSACTIONS'
    bt_id = db.Column(db.Integer, primary_key=True)
    bt_date = db.Column(db.Date)
    bt_category = db.Column(db.String(50))
    bt_division = db.Column(db.String(50))
    bt_amount = db.Column(db.Float)
    bt_purpose = db.Column(db.String(255))
    bt_entered_by = db.Column(db.String(50))
    bt_entered_date = db.Column(db.DateTime)

