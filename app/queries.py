

def checkUserEmail():
	q = '''	SELECT count(*)
			FROM public."User"
			WHERE email =  %s'''
	return q

	
def registerUser():
	q = '''INSERT INTO public."User"
		(email, password_hash, "firstName"
		, "lastName", "activeFlag")
		VALUES (%s, %s, %s, %s, %s);'''
	return q	