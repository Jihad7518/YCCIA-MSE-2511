from django.shortcuts import render
from .llm_module import generate_month_plan

def plan_page(request):
    context = {
        'age': '',
        'gender': 'female',
        'weight': '',
        'height': '',
        'result': None,
        'error': None,
    }

    if request.method == 'POST':
        age = request.POST.get('age', '').strip()
        gender = request.POST.get('gender', 'female').strip().lower()
        weight = request.POST.get('weight', '').strip()
        height = request.POST.get('height', '').strip()

        context.update({'age': age, 'gender': gender, 'weight': weight, 'height': height})

        try:
            age_val = int(age)
            weight_val = float(weight)
            height_val = float(height)

            if age_val <= 0 or weight_val <= 0 or height_val <= 0:
                context['error'] = 'Age, weight, and height must be greater than zero.'
            elif gender not in ['male', 'female']:
                context['error'] = 'Gender must be either male or female.'
            else:
                context['result'] = generate_month_plan(age_val, gender, weight_val, height_val)
        except ValueError:
            context['error'] = 'Please enter valid numeric values.'

    return render(request, 'plan.html', context)
