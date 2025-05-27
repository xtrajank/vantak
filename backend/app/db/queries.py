'''SQL queries'''
'''
Queries:
Authentication/User Mgmt
- create_user(username, email, password_hash)
- get_user_email(email)
- validate_user_credentials(email, password_hash)
- update_user_preferences(user_id, prefs)
- delete_user (user_id)
'''
from db.connection import get_connection # use to connect to db for each query

