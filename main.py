import mail_notifier

#test
if __name__ == '__main__':
    notifier = mail_notifier.MailNotifier()
    # Получатель, если нет письма смотреть в Спаме
    recipient = 'test@gmail.com'
    subject = 'Тестовое уведомление'
    body = 'Это тестовое сообщение от Python скрипта'

    notifier.send_email(recipient, subject, body)
