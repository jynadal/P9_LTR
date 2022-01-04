from django.core.exceptions import ValidationError, ValidatorError


class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.is_alpha() for char in password):
            raise ValidationError('Le mot de passe doit contenir une lettre', code='password_no_letters')

    def get_help_text(self):
        return 'Le mot de passe doit contenir au moins une lettre majuscule ou minuscule.'