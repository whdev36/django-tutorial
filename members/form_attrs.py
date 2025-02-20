from django.utils.translation import gettext_lazy as _

field_attrs = {
    'first_name': {
        'placeholder': _('Enter your first name'),
        'label': _('First Name'),
        'help_text': _('Please enter your first name.'),
        'error_messages': {
            'required': _('First name is required.'),
            'max_length': _('First name cannot be longer than 100 characters.')
        }
    },
    'last_name': {
        'placeholder': _('Enter your last name'),
        'label': _('Last Name'),
        'help_text': _('Please enter your last name.'),
        'error_messages': {
            'required': _('Last name is required.'),
            'max_length': _('Last name cannot be longer than 100 characters.')
        }
    },
    'email': {
        'placeholder': _('Enter your email'),
        'label': _('Email Address'),
        'help_text': _('We will never share your email with anyone else.'),
        'error_messages': {
            'required': _('Please provide an email address.'),
            'invalid': _('Please enter a valid email address.')
        }
    },
    'username': {
        'placeholder': _('Enter your username'),
        'label': _('Username'),
        'help_text': _('Choose a unique username.'),
        'error_messages': {
            'required': _('Username is required.'),
            'max_length': _('Username cannot be longer than 150 characters.')
        }
    },
    'password1': {
        'placeholder': _('Enter your password'),
        'label': _('Password'),
        'help_text': _('Your password must be at least 8 characters long.'),
        'error_messages': {
            'required': _('Password is required.'),
            'max_length': _('Password cannot be longer than 100 characters.')
        }
    },
    'password2': {
        'placeholder': _('Confirm your password'),
        'label': _('Confirm Password'),
        'help_text': _('Confirm your password.'),
        'error_messages': {
            'required': _('Please confirm your password.'),
            'max_length': _('Password confirmation cannot be longer than 100 characters.')
        }
    },
}