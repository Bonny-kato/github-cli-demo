def login(request):
	""" allow user to login into the syetm"""
	if request.method == "POST":
		pass
	else:
		return redirect("login-form" )
