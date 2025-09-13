# mywebsite/mainapp/models.py
from django.db import models

class QuizSubmission(models.Model):
    # Core questions
    sleep_time = models.TimeField()
    wake_time = models.TimeField()
    energy_level = models.CharField(max_length=10)
    sunlight_time = models.IntegerField()
    exercise_time = models.IntegerField(null=True, blank=True)
    last_meal_time = models.TimeField(null=True, blank=True)
    stress_level = models.CharField(max_length=10, null=True, blank=True)
    
    # New 'intrusive' questions
    work_schedule = models.CharField(max_length=20, null=True, blank=True)
    dietary_habits = models.TextField(null=True, blank=True)
    medication = models.TextField(null=True, blank=True)
    
    # AI response field
    ai_report = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quiz Submission from {self.created_at.strftime('%Y-%m-%d')}"