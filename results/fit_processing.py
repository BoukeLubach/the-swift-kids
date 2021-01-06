import activityio as aio
import pandas as pd 
import activityio as aio
import numpy as np
from django.conf import settings

def calculate_4d_power(fit_file_name):
    media_folder = settings.MEDIA_ROOT

    df = aio.read(media_folder + "/fit_files/"+ fit_file_name)

    power_15s = max(np.convolve(df.pwr, np.ones((15,))/15, mode='valid'))   
    power_1min = max(np.convolve(df.pwr, np.ones((60,))/60, mode='valid'))
    power_5min = max(np.convolve(df.pwr, np.ones((300,))/300, mode='valid'))
    power_20min = max(np.convolve(df.pwr, np.ones((1200,))/1200, mode='valid'))

    return power_15s, power_1min, power_5min, power_20min





# fit_file = 'fit_files/zwift-activity-494243861046016352.fit'






