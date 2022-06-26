#%%
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta


sdate = date(2021, 12, 22)  # start date
edate = date(2022, 4, 9)  # end date

#pd.date_range(sdate,edate-timedelta(days=15),freq='d')
#last_date_of_month = date(sdate.year, sdate.month, 1) + relativedelta(months=1, days=-1)

def get_slots(sdate, edate):
    """
    Parameters
    -----------------------
    sdate : Date
    Start date of the time window

    edate : Date
    End date of the time window

    Returns
    -------------------------
    slots : DataFrame
    Bi-Monthly Slots between Start and End Date

    Example:

    >> sdate = date(2021, 12, 22)  # start date
    >> edate = date(2022, 4, 9)  # end date

    >> get_slots(sdate, edate)

            Start         End
        0  2021-12-01  2021-12-15
        1  2021-12-16  2021-12-31
        2  2022-01-01  2022-01-15
        3  2022-01-16  2022-01-31
        4  2022-02-01  2022-02-15
        5  2022-02-16  2022-02-28
        6  2022-03-01  2022-03-15
        7  2022-03-16  2022-03-31

    """
    slots = []

    cdate = date(sdate.year, sdate.month, 1)
    
    while True:
        print('--', cdate, )
        if date(cdate.year, cdate.month, 15)>edate:
            print(date(cdate.year, cdate.month, 15), ' -- ', edate)
            break
        else:
            slots.append(
                [date(cdate.year, cdate.month, 1), date(cdate.year, cdate.month, 15)]
            )

        if date(cdate.year, cdate.month, 1) + relativedelta(months=1, days=-1)>edate:
            print(date(cdate.year, cdate.month, 1) + relativedelta(months=1, days=-1), ' -- ' ,edate)
            break
        else:
            slots.append(
                [
                    date(cdate.year, cdate.month, 16),
                    date(cdate.year, cdate.month, 1) + relativedelta(months=1, days=-1),
                ]
            )

        cdate = date(cdate.year, cdate.month, 1) + relativedelta(months=1)

    slots_df = pd.DataFrame(slots)
    slots_df.columns = ['Start', 'End']

    slots_df['Start'] = pd.to_datetime(slots_df['Start'])
    slots_df['End'] = pd.to_datetime(slots_df['End'])

    return slots_df
    

res = get_slots(sdate, edate)
