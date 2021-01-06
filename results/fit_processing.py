import activityio as aio
import pandas as pd 
import activityio as aio
import numpy as np
from django.conf import settings
from .models import RiderResult


def calculate_4d_power(fit_file_path):

    df = aio.read(fit_file_path)

    power_15s = max(np.convolve(df.pwr, np.ones((15,))/15, mode='valid'))   
    power_1min = max(np.convolve(df.pwr, np.ones((60,))/60, mode='valid'))
    power_5min = max(np.convolve(df.pwr, np.ones((300,))/300, mode='valid'))
    power_20min = max(np.convolve(df.pwr, np.ones((1200,))/1200, mode='valid'))

    return power_15s, power_1min, power_5min, power_20min

def save_powerdata_to_model(model_to_add_file_to, power_15s, power_1min, power_5min, power_20min):
    model_to_add_file_to.power_15s = power_15s
    model_to_add_file_to.power_1min = power_1min 
    model_to_add_file_to.power_5min = power_5min
    model_to_add_file_to.power_20min = power_20min
    model_to_add_file_to.save()


def process_fit_file(fit_file_name, model_to_add_file_to):

    media_folder = settings.MEDIA_ROOT
    fit_file_path = media_folder + "/fit_files/" + fit_file_name

    try:
        power_15s, power_1min, power_5min, power_20min = calculate_4d_power(fit_file_path)
        

        save_powerdata_to_model(model_to_add_file_to, power_15s, power_1min, power_5min, power_20min)

    except:
        print("Fit file not processed")






