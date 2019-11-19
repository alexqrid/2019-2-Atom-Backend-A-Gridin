from django.db import connection
from users.models import User
from django.core.exceptions import ValidationError


def user_exists(user):
    try:
        User.objects.get(username=user)
    except User.DoesNotExist:
        raise ValidationError("User %(username) does not exist", params={'username': user})
    return True


def chat_exists(sender, recipient):
    cur = connection.cursor()
    cur.execute(f"""select chat_id from 
                    (select chat_id from chats_member where user_id = {sender.id} 
                    INTERSECT 
                    select chat_id from chats_member where user_id = {recipient.id}) m 
                    inner join chats_chat c on m.chat_id = c.id where not c.is_group""")
    return cur.fetchone()
