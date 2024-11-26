def format_date(date):
	return "".join(reversed(date.split("/")))

print(format_date("11/12/2019"))