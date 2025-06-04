from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField, DateField, SubmitField
from wtforms.validators import DataRequired

class BudgetForm(FlaskForm):
    bm_year = SelectField('Year', choices=[('2024', '2024'), ('2025', '2025')], validators=[DataRequired()])
    bm_category = StringField('Category', validators=[DataRequired()])
    bm_amount = FloatField('Amount', validators=[DataRequired()])
    bm_remarks = StringField('Remarks')
    submit = SubmitField('Save')


class TransactionForm(FlaskForm):
    bt_date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    bt_category = SelectField('Category', choices=[], validators=[DataRequired()])
    bt_division = SelectField('Division', choices=[('HR', 'HR'), ('IT', 'IT'), ('Finance', 'Finance')], validators=[DataRequired()])
    bt_amount = FloatField('Amount', validators=[DataRequired()])
    bt_purpose = StringField('Purpose / Remarks')
    submit = SubmitField('Save')
