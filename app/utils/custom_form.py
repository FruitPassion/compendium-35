from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import EqualTo, InputRequired, Length

VALIDATE = "validateForm()"
PLACEHOLDER = "*********"


class LoginForm(FlaskForm):
    """
    Formulaire de connexion pour le personnel
    """

    login = StringField(
        validators=[InputRequired(), Length(min=5)], render_kw={"placeholder": "Dante"}
    )

    password = PasswordField(
        validators=[
            InputRequired(),
            Length(min=5, message="Le mot de passe doit faire au moins 5 caractères"),
        ],
        render_kw={"placeholder": PLACEHOLDER},
    )

    submit = SubmitField("Se connecter")


class RegisterForm(FlaskForm):
    """
    Formulaire d'inscription pour le personnel
    """

    login = StringField(
        validators=[
            InputRequired(),
            Length(min=5, message="Le pseudo foit faire au moins 5 caractères"),
        ],
        render_kw={"placeholder": "Fantin"},
    )

    password = PasswordField(
        validators=[
            InputRequired(),
            Length(min=5, message="Le mot de passe doit faire au moins 5 caractères"),
            EqualTo(
                "confirm_password", message="Les mots de passe doivent être les memes"
            ),
        ],
        render_kw={"placeholder": PLACEHOLDER},
    )

    confirm_password = PasswordField(
        validators=[InputRequired(), Length(min=5)],
        render_kw={"placeholder": PLACEHOLDER},
    )

    submit = SubmitField("S'inscrire")
