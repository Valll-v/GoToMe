import hashlib
from random import randint

from templated_mail.mail import BaseEmailMessage

import accounts.db_communication as db


def generate_code():
    return randint(10000, 99999)


class PasswordResetEmail(BaseEmailMessage):
    template_name = "accounts/password_reset.html"

    def get_context_data(self):
        context = super().get_context_data()
        user = context.get("user")
        code = str(generate_code())
        db.set_code(code, db.get_user(username=user))
        context["code"] = code
        return context
