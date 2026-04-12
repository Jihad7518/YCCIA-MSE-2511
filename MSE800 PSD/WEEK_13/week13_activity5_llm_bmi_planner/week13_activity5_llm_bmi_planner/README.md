# Week 13 - Activity 5: LLM based BMI Diet & Exercise Planner

This project continues Week 13 Activity 3 by extending the BMI Django app into a simple **LLM-style health planning system**.  
The user enters **age**, **gender**, **weight (kg)**, and **height (cm)**. The system then:

1. calculates BMI,
2. classifies the person as **Underweight**, **Normal**, or **Overweight**,
3. generates a **one-month diet and exercise plan**,
4. explains how the plan was produced.

## Formula used

```python
bmi = round(weight / (height ** 2), 2)
```

> Note: height is converted from **cm to meters** before calculation.

## BMI categories

- **Underweight**: BMI < 20
- **Normal**: 20 ≤ BMI < 25
- **Overweight**: BMI ≥ 25

## How the LLM-style module works

The file `planner/llm_module.py` acts as the planning engine.

It generates the plan in 4 steps:

1. **BMI calculation**  
   Uses weight and height to calculate BMI.

2. **BMI classification**  
   Labels the user as Underweight, Normal, or Overweight.

3. **Rule-guided personalization**  
   Uses age and gender to change the tone and safety level of the diet and exercise advice.
   - Younger users get slightly more progressive exercise suggestions.
   - Older users get lower-impact and recovery-focused guidance.

4. **Prompt-style response assembly**  
   The module combines diet templates, exercise templates, weekly goals, and explanatory text into a result that looks like an LLM-generated plan.
   This keeps the project fully runnable without needing an external API key.

---

## Scenario 1: Young, underweight person

**Input**
- Age: 22
- Gender: Male
- Weight: 48 kg
- Height: 170 cm

**Result**
- BMI: 16.61
- Category: Underweight

**How the system generated the plan**
- The BMI was below 20, so the module selected the **Underweight** branch.
- Because the user is young, it added **beginner strength training** and a **gradual increase in exercise intensity**.
- The diet plan focused on **healthy calorie surplus**, **protein-rich meals**, and **2–3 snacks per day**.
- The 4-week plan emphasized **strength building**, **routine formation**, and **sustainable weight gain habits**.

See screenshot: `screenshots/scenario1_underweight.png`

---

## Scenario 2: Older, overweight person

**Input**
- Age: 58
- Gender: Female
- Weight: 92 kg
- Height: 158 cm

**Result**
- BMI: 36.85
- Category: Overweight

**How the system generated the plan**
- The BMI was 25 or above, so the module selected the **Overweight** branch.
- Because the user is older, it added **joint-friendly**, **low-impact**, and **recovery-focused** activity guidance.
- The diet plan focused on **portion control**, **higher fibre**, **lighter evening meals**, and **reduced sugary foods**.
- The 4-week plan emphasized **consistent walking**, **basic strength work**, and **long-term adherence** rather than aggressive exercise.

See screenshot: `screenshots/scenario2_overweight.png`

---

## How to run the project

```bash
cd week13_activity5_llm_bmi_planner
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open in browser:

```text
http://127.0.0.1:8000/
```

---

## Project structure

```text
week13_activity5_llm_bmi_planner/
│
├── manage.py
├── requirements.txt
├── README.md
├── screenshots/
│   ├── scenario1_underweight.png
│   └── scenario2_overweight.png
│
├── imageuploadsite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── planner/
    ├── __init__.py
    ├── views.py
    ├── llm_module.py
    ├── templates/
    │   └── plan.html
    └── static/
        └── css/
            └── style.css
```

## Submission note

Upload this project to GitHub and submit your repository link.  
The screenshots required by the activity are already included in the project folder under `screenshots/`.
