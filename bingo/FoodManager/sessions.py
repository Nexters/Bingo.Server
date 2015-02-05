from FoodManager.models import FoodManager

def makeSessions(request, manager):
	request.session.clear()
	request.session.set_expiry(0)
	request.session['manager'] = manager.manager_id

def clearSessions(request):
	del request.session['manager']