from django.core.mail import send_mail


def send_confirmation_email(user, code):
    send_mail(
        'Здравствуйте, активируйте ваш аккаунт!',
        f'Что активировать ваш акккаунт нужно ввести код: '
        f'\n{code}'
        f'\nНе передовайте этот код никому!',
        'aestheticdude21@gmail.com',
        [user],
        fail_silently=False,

    )


def send_password(user, forgot_password):
    send_mail(
        subject='email',
        message='Здраствуйте, активируйте ваш новый пароль!\n'
        f'Постарайтесь не забыть:\n\n'
        f'\n{forgot_password}'
        f'\nНе передаватйте этот пароль никому!\n',
        from_email='bekurudinov@gmail.com',
        recipient_list=[user],
        fail_silently=False,
    )

