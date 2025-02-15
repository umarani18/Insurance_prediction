import os
import joblib
import nbformat
from nbconvert import PythonExporter
from django.shortcuts import render
from django.http import JsonResponse
from .forms import InsuranceForm

MODEL_FILE = "insurance_model.pkl"
NOTEBOOK_FILE = "insurance_prediction.ipynb"

def load_model():
    if os.path.exists(MODEL_FILE):
        return joblib.load(MODEL_FILE)

    # Convert notebook to script
    with open(NOTEBOOK_FILE) as f:
        notebook_content = nbformat.read(f, as_version=4)

    exporter = PythonExporter()
    script, _ = exporter.from_notebook_node(notebook_content)

    script_file = "insurance_prediction.py"
    with open(script_file, "w") as f:
        f.write(script)

    exec(open(script_file).read(), globals())

    return joblib.load(MODEL_FILE)

model = load_model()

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def predict_insurance(request):
    if request.method == "POST":
        form = InsuranceForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            sex = 1 if form.cleaned_data['sex'] == 'male' else 0
            bmi = form.cleaned_data['bmi']
            children = form.cleaned_data['children']
            smoker = 1 if form.cleaned_data['smoker'] == 'yes' else 0
            region = form.cleaned_data['region']

            region_mapping = {'northwest': 0, 'northeast': 1, 'southwest': 2, 'southeast': 3}
            region_encoded = region_mapping[region]

            prediction = model.predict([[age, sex, bmi, children, smoker, region_encoded]])[0]

            return JsonResponse({'prediction': prediction})
    else:
        form = InsuranceForm()
    return render(request, 'insurance_form.html', {'form': form})

