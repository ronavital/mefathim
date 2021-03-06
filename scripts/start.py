#!/home/mefath5/.local/bin/python3
# print("Content-Type: text/plain\n\n")

import os
import sys
import datetime
import functions

try:

    sid = functions.get_cookie_value("LoggedIn")
    if not sid:
        print("location: login.html")
        print("")
        sys.exit()

    db = functions.connect()

    sql = "SELECT `update_time`, `logged_out` FROM sessions WHERE sid = '" + sid + "'"

    time_before = (datetime.datetime.now() - datetime.timedelta(minutes=10))

    session_cursor = db.cursor()
    session_cursor.execute(sql)

    session = session_cursor.fetchall()

    time, logged = session[0]

    if time > time_before and logged == 0:
        print("location: home_page.html")
        print("")
    else:
        print("location: login.html")
        print("")

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
