from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    DecimalField,
    HiddenField,
    RadioField,
    StringField,
    SubmitField
)
from wtforms.validators import DataRequired, NumberRange


class MovimientoForm(FlaskForm):
    id = HiddenField()
    fecha = DateField('Fecha', validators=[
        DataRequired('debes indicar la fecha del movimiento')
    ])
    concepto = StringField('Concepto', validators=[
        DataRequired('no has especificado un concepto para este movimiento')
    ])
    tipo = RadioField(choices=[('I', 'Ingreso'), ('G', 'Gasto')], validators=[
        DataRequired('necesito saber si es un gasto o un ingreso')
    ])
    cantidad = DecimalField('Cantidad', places=2, validators=[
        DataRequired('no puede haber un movimiento sin una cantidad asociada'),
        NumberRange(
            min=0.1, message='no se permiten cantidades inferiores a 10 centimos')
    ])

    submit = SubmitField('Guardar')
