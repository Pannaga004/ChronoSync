# mywebsite/mainapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import requests
import json
from .forms import QuizForm, CustomUserCreationForm, CustomAuthenticationForm
from .models import QuizSubmission

# --- Ollama API configuration ---
# The endpoint for the local Ollama server. No API key is needed.
API_ENDPOINT = "http://localhost:11434/api/generate"

def home(request):
    return render(request, 'mainapp/home.html')

def discover(request):
    return render(request, 'mainapp/discover.html')

def features(request):
    return render(request, 'mainapp/features.html')

def crs_raw(request):
    return render(request, 'mainapp/crs_raw.html')

@login_required
def dashboard_view(request):
    return render(request, 'mainapp/dashboard.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'mainapp/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'mainapp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def chronopoints_view(request):
    return render(request, 'mainapp/chronopoints.html')

def dashboard_view(request):
    return render(request, 'mainapp/dashboard.html')

def crs_ai(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            
            prompt_text = f"""
            Analyze the following circadian rhythm data and provide a personalized report.
            - Last night's sleep time: {submission.sleep_time}
            - This morning's wake time: {submission.wake_time}
            - Morning energy level: {submission.energy_level}
            - Minutes of sunlight today: {submission.sunlight_time}
            - Minutes of exercise today: {submission.exercise_time}
            - Time of last meal: {submission.last_meal_time}
            - Stress level today: {submission.stress_level}

            Based on this, give a predicted CRS score out of 100, one key insight, and one practical recommendation.
            Format the response in HTML with bold tags for headings.
            """

            # The payload for Ollama is different from Google's and is much simpler.
            payload = {
                "model": "llama3",  # This must match the model you downloaded.
                "prompt": prompt_text,
                "stream": False # Set to false to get the full response at once.
            }

            headers = {
                "Content-Type": "application/json"
            }

            try:
                # Make the POST request to the local Ollama server.
                response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(payload))
                response.raise_for_status()
                
                # Ollama's response format is a single JSON object.
                ai_response = response.json()
                
                # The generated text is in the 'response' key.
                generated_text = ai_response.get('response', "An error occurred in the AI's response.")

                submission.ai_report = generated_text
                submission.save()

                return render(request, 'mainapp/crs_ai_results.html', {'ai_response': generated_text})
            
            except requests.exceptions.RequestException as e:
                error_message = f"An error occurred while connecting to the AI service: {e}"
                return render(request, 'mainapp/error.html', {'error_message': error_message})
            except (KeyError, IndexError):
                error_message = "The AI response was not in the expected format."
                return render(request, 'mainapp/error.html', {'error_message': error_message})
    else:
        form = QuizForm()
        
    return render(request, 'mainapp/crs_ai.html', {'form': form})