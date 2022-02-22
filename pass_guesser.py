
#Password list maker

pwdlst = []
symbls = [".","@","_"]
fname = str(input("Enter First Name- "))
lname = str(input("Enter Last Name- "))
day = str(input("Enter Day of Birth(DD)- "))
month = str(input("Enter Month of Birth(MM)- "))
year = str(input("Enter Year of Birth(YYYY)- "))


fname_day_combo = (fname+day)
pwdlst.append(fname_day_combo)
fname_day_month_combo = (fname+day+month)
pwdlst.append(fname_day_month_combo)
fname_day_month_year_combo = (fname+day+month+year)
pwdlst.append(fname_day_month_year_combo)
fname_month_2year_combo = (fname+month+year[-2:])
pwdlst.append(fname_month_2year_combo)


for i in symbls:
    fname_day_symbls_combo = (fname+i+day)
    pwdlst.append(fname_day_symbls_combo)
    fname_symbls_lname_day_combo = (fname+i+lname+day)
    pwdlst.append(fname_symbls_lname_day_combo)
    fname_symbls_day_month_combo = (fname+i+day+month)
    pwdlst.append(fname_symbls_day_month_combo)



print(pwdlst)
