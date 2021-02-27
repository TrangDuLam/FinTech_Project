from datetime import datetime, timedelta

td_load = datetime.today()
td = td_load.strftime('%m/%d/%y')
print(td)

tar = td_load - timedelta(30)
print(tar.strftime('%m/%d/%y'))
