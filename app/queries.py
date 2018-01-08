

def checkUserEmail():
	q = '''	SELECT count(*)
			FROM public.user
			WHERE email =  %s'''
	return q

	
def registerUser():
	q = '''INSERT INTO public.user
		(email, password_hash, first_name
		, last_name, active_flag)
		VALUES (%s, %s, %s, %s, %s);'''
	return q	
	

def checkLoginEmail():
	q = """	SELECT email
			, password_hash
			, active_flag
			FROM public.user
			WHERE email =  %s
			AND active_flag = 'true'"""
	return q

	
	'''
	CREATE A NEW SCRIPT, IMPORT PSYCOPG2 AND BREAK DOWN THE QUERY FROM SCRATCH
	'''