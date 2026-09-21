from tokenize import String

from flask_wtf import FlaskForm
from h11 import Data
from wtforms import FloatField, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length

# mao multe tipuri de fields:
# https://wtforms.readthedocs.io/en/stable/fields/#basic-fields
class ProductForm(FlaskForm):
    # acceptam input doar pt campurile modificabile 
    # si care nu se generaza automat
    product_name = StringField('Product Name', validators = 
                               [DataRequired(message="Need product name!"), Length(max=100)])

    product_code = StringField(label='Product Code', validators=
                               [DataRequired(message="Need product code!"), Length(max=64)])
    
    product_price = FloatField('Product Price', validators = 
                                 [DataRequired(message="Need product price!")])

    product_brand = StringField('Product Brand', validators = 
                                [DataRequired("Need product brand!"), Length(max=64)])

    product_quantity = IntegerField('Product Quantity', validators=
                                    [InputRequired()])

    submit = SubmitField('Submit')

    
    

