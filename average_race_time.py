# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
import re
import datetime
import os
import pandas as pd
import numpy as np
import io
import time


def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content


def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    data = io.StringIO(races)
    df = pd.read_fwf(data)
    df = df[['TIME', 'Athlete']].query('Athlete.str.contains("Jennifer Rhines")')

    return list(df['TIME'])


def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    df = pd.DataFrame(racetimes, columns=['time'])
    total = 0
    for time in df['time']:
        mins = int(time[:2])
        secs = int(time[3:5])
        if time[6:10]:
            msecs = time[6:10]
        else:
            msecs = 0
        msecs = int(msecs)
        total += (mins * 60 + secs) * 1000 + msecs

    avg = total / 1000 / 60 / len(df)

    return f'{str(avg)[:2]}:{str(avg)[3:5]}.{int(str(avg)[6:7])}'
