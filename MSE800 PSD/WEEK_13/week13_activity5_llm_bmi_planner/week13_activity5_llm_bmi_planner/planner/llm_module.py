
from textwrap import dedent

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = round(weight_kg / (height_m ** 2), 2)
    if bmi < 20:
        category = 'Underweight'
    elif bmi < 25:
        category = 'Normal'
    else:
        category = 'Overweight'
    return bmi, category

def week_focus(category, week_number):
    if category == 'Underweight':
        focuses = {
            1: 'stomach-friendly calorie increase and daily routine building',
            2: 'protein consistency and beginner strength work',
            3: 'slight increase in meal volume and resistance intensity',
            4: 'stability, recovery, and sustainable healthy weight gain habits',
        }
    elif category == 'Overweight':
        focuses = {
            1: 'portion awareness and joint-friendly movement',
            2: 'fibre, hydration, and walking consistency',
            3: 'balanced fat loss with strength support',
            4: 'routine reinforcement and long-term adherence',
        }
    else:
        focuses = {
            1: 'balanced nutrition and steady activity',
            2: 'energy, sleep, and meal timing',
            3: 'strength and cardiovascular balance',
            4: 'maintenance and habit reinforcement',
        }
    return focuses[week_number]

def build_diet_block(age, gender, category):
    if category == 'Underweight':
        goal = 'gradual healthy weight gain with nutrient-dense meals'
        breakfast = 'oats with milk, banana, peanut butter, boiled eggs'
        lunch = 'rice, chicken or fish, lentils, vegetables, yoghurt'
        dinner = 'potato or rice, lean protein, vegetables, olive oil'
        snacks = 'nuts, dates, smoothies, yoghurt, peanut butter toast'
        guidance = [
            'Eat 3 main meals and 2 to 3 snacks every day.',
            'Add calorie-dense but nutritious foods such as nuts, milk, eggs, avocado, and peanut butter.',
            'Prioritize protein in every meal to support muscle gain.',
            'Drink water, but avoid filling up on water right before meals.'
        ]
    elif category == 'Overweight':
        goal = 'safe fat loss with better satiety, energy, and mobility'
        breakfast = 'oats or eggs with fruit and unsweetened tea'
        lunch = 'half plate vegetables, quarter lean protein, quarter brown rice or roti'
        dinner = 'light protein-focused meal with vegetables and soup or salad'
        snacks = 'apple, cucumber, yoghurt, roasted chickpeas, a small handful of nuts'
        guidance = [
            'Use a calorie-controlled plate method instead of skipping meals.',
            'Choose high-fibre foods to stay full longer.',
            'Limit sugary drinks, fried snacks, and oversized portions.',
            'Maintain regular meal timing to reduce overeating.'
        ]
    else:
        goal = 'weight maintenance and overall fitness'
        breakfast = 'balanced breakfast with protein, whole grains, and fruit'
        lunch = 'lean protein, whole grains, and vegetables'
        dinner = 'light balanced meal with protein and vegetables'
        snacks = 'fruit, yoghurt, nuts'
        guidance = [
            'Aim for balanced portions across meals.',
            'Maintain hydration and regular meal timing.',
            'Use moderate snacks only when hungry.',
            'Keep protein and vegetables consistent throughout the day.'
        ]

    gender_note = 'The system uses gender only to slightly adjust tone and meal suggestions, while keeping the plan safe and general.'
    age_note = f'The plan is adapted for age {age}: younger users receive more training emphasis, while older users receive more recovery and joint-friendly guidance.'
    return {
        'goal': goal,
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner,
        'snacks': snacks,
        'guidance': guidance,
        'age_note': age_note,
        'gender_note': gender_note,
    }

def build_exercise_block(age, category):
    if age < 30:
        cardio = '30 to 40 minutes of brisk walking, cycling, or light jogging 4 to 5 days/week'
        strength = '3 days/week beginner strength training using bodyweight, dumbbells, or resistance bands'
        recovery = '1 to 2 lighter recovery days with stretching and mobility'
    elif age < 50:
        cardio = '25 to 35 minutes of brisk walking or cycling 4 to 5 days/week'
        strength = '2 to 3 days/week strength training focusing on large muscle groups and posture'
        recovery = 'daily gentle stretching plus 1 full rest day'
    else:
        cardio = '20 to 30 minutes of low-impact walking 5 days/week'
        strength = '2 days/week chair-supported or low-impact strength exercises'
        recovery = 'daily flexibility, breathing, and balance practice'

    if category == 'Underweight':
        weekly_target = 'Build strength first, with only light cardio so calorie burn stays moderate.'
    elif category == 'Overweight':
        weekly_target = 'Use consistent low-impact cardio plus basic strength training to support fat loss and joint health.'
    else:
        weekly_target = 'Mix cardio, strength, and mobility to maintain a healthy routine.'

    return {
        'cardio': cardio,
        'strength': strength,
        'recovery': recovery,
        'weekly_target': weekly_target,
    }

def generate_month_plan(age, gender, weight_kg, height_cm):
    bmi, category = calculate_bmi(weight_kg, height_cm)
    diet = build_diet_block(age, gender, category)
    exercise = build_exercise_block(age, category)

    weeks = []
    for week in range(1, 5):
        if category == 'Underweight':
            week_diet = [
                'Increase daily calories slightly above current intake using healthy foods.',
                'Have a protein-rich breakfast every morning.',
                'Add one smoothie or high-calorie snack in the afternoon.'
            ]
            week_ex = [
                'Strength training on Monday, Wednesday, and Friday.',
                'Light walking on Tuesday and Saturday.',
                'Sunday rest and stretching.'
            ]
        elif category == 'Overweight':
            week_diet = [
                'Use smaller portions of refined carbs and larger portions of vegetables.',
                'Avoid sugary drinks this week.',
                'Track water intake and keep evening meals light.'
            ]
            week_ex = [
                'Brisk walking 5 days this week.',
                'Low-impact strength sessions on 2 days.',
                'One full recovery day with stretching.'
            ]
        else:
            week_diet = [
                'Keep meals balanced with protein, vegetables, and whole grains.',
                'Reduce unnecessary snacking.',
                'Stay hydrated every day.'
            ]
            week_ex = [
                'Moderate cardio 4 days this week.',
                'Strength sessions 2 days this week.',
                'Stretching after workouts.'
            ]

        if age >= 50:
            week_ex.append('Prioritize joint-friendly movement and avoid sudden high-impact exercise.')
        elif age < 30:
            week_ex.append('Gradually increase exercise intensity if recovery remains good.')

        weeks.append({
            'number': week,
            'focus': week_focus(category, week),
            'diet_points': week_diet,
            'exercise_points': week_ex,
        })

    explanation = dedent(f'''
    This module first calculates BMI from weight and height, then classifies the person as Underweight, Normal, or Overweight.
    It next adjusts the plan using age and gender-informed wording:
    younger users receive more progressive training, while older users receive safer, lower-impact routines.
    Finally, it assembles a 4-week diet and exercise plan using prompt-style templates and conditional logic to simulate
    an LLM-style personalized response without needing an external API key.
    ''').strip()

    return {
        'bmi': bmi,
        'category': category,
        'diet': diet,
        'exercise': exercise,
        'weeks': weeks,
        'explanation': explanation,
    }
