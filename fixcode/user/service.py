from fixcode.authorize.models import TemporalyDataUser
from .models import User

def temp_user_to_persist_user(temporaly_user, password):
	user = User(name=temporaly_user.name,
				username=temporaly_user.username,
				email=temporaly_user.email,
				password=password)
	user.save()
	return user