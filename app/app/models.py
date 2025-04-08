from django.db import models
from datetime import datetime
# Default Python Models for Auto API

class RouteExclusion(models.Model):
    """Model for URL Routes"""
    required_token = models.BooleanField(default = False)
    route = models.CharField(unique=True, max_length=255)
    is_enabled = models.BooleanField(default = False)

    def __str__(self):
        remarks = ""
        if self.is_enabled == True:
            remarks = "Enabled"
        else:
            remarks = "Disabled"

        return remarks + " : " + self.route

class AppLogs(models.Model):
    """Model for application logs, whether API Level or Function Level"""
    time_stamp = models.TextField(default=None, null=True, blank=True)
    log_type = models.TextField(default=None, null=True, blank=True)
    level = models.TextField(default=None, null=True, blank=True)
    source = models.TextField(default=None, null=True, blank=True)
    message = models.TextField(default=None, null=True, blank=True)
    user_id = models.TextField(default=None, null=True, blank=True)
    session_id = models.TextField(default=None, null=True, blank=True)
    ip_address = models.TextField(default=None, null=True, blank=True)
    request_method = models.TextField(default=None, null=True, blank=True)
    request_path = models.TextField(default=None, null=True, blank=True)
    response_status = models.TextField(default=None, null=True, blank=True)
    data = models.TextField(default=None, null=True, blank=True)
    error_type = models.TextField(default=None, null=True, blank=True)
    error_message = models.TextField(default=None, null=True, blank=True)
    execution_time = models.TextField(default=0.00, null=True, blank=True)

    def __str__(self):
        return f"{self.time_stamp}"
    
class StackTrace(models.Model):
    app_log = models.ForeignKey(AppLogs, on_delete=models.CASCADE)
    description = models.TextField()

class PredictionLog(models.Model):
    date_of_prediction = models.DateTimeField(default = datetime.now())
    anemometer = models.IntegerField(default = 1, null = False)
    rainfall = models.IntegerField(default = 1, null = False)
    humidity = models.IntegerField(default = 1, null = False)
    is_storm_present = models.BooleanField(default = False, null = False)

    def __str__(self):
        return f'{str(self.date_of_prediction) + " - " + str(self.is_storm_present)}'

class Dataset(models.Model):
    anemometer = models.IntegerField(default = 1, null = False)
    rainfall = models.IntegerField(default = 1, null = False)
    humidity = models.IntegerField(default = 1, null = False)
    is_storm_present = models.BooleanField(default = False, null = False)

class ValidationLog(models.Model):
    anemometer = models.IntegerField(default = 1, null = False)
    rainfall = models.IntegerField(default = 1, null = False)
    humidity = models.IntegerField(default = 1, null = False)
    correct_answer = models.BooleanField(default = False, null = False)
    predicted_answer = models.BooleanField(default = False, null = False)

class SensorValue(models.Model):
    anemometer = models.IntegerField(default = 1, null = False)
    rainfall = models.IntegerField(default = 1, null = False)
    humidity = models.IntegerField(default = 1, null = False)

class State(models.Model):
    dc_motor = models.BooleanField(default = False)
    dc_motor_seconds = models.IntegerField(default = 0, null = False)
    adaptive_mode = models.BooleanField(default = False, null = False)
    prediction_minutes_interval = models.IntegerField(default = 5, null = False)

class ModelInfo(models.Model):

    last_trained_state = models.DateField(default = None)
    accuracy = models.TextField(default = None)
    precision = models.TextField(default = None)
    recall = models.TextField(default = None)
    f1_score = models.TextField(default = None)
    json_info = models.TextField(default = None, null = True)

    def __str__(self):
        return f'{self.last_trained_state}'
