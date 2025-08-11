from faker import Faker
import json, random, datetime

# Initialize faker for random text
fake = Faker()

# Configurable lists
categories = ["Math", "Science", "Art", "Music", "History", "Coding"]
types = ["ONE_TIME", "COURSE", "CLUB"]
grade_ranges = [
    ("1st–3rd", 6, 8),
    ("4th–5th", 9, 11),
    ("6th–8th", 11, 13),
    ("9th–12th", 14, 18)
]

courses = []
for i in range(1, 51):  # Generates exactly 50 records
    grade_range, min_age, max_age = random.choice(grade_ranges)
    course = {
        "id": f"course-{i:03d}",
        "title": fake.sentence(nb_words=4).replace(".", ""),
        "description": fake.paragraph(nb_sentences=2),
        "category": random.choice(categories),
        "type": random.choice(types),
        "gradeRange": grade_range,
        "minAge": min_age,
        "maxAge": max_age,
        "price": round(random.uniform(5, 100), 2),
        "nextSessionDate": (
            datetime.datetime(2025, 6, 1) +
            datetime.timedelta(days=random.randint(0, 120))
        ).strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    courses.append(course)

# Save to JSON file
with open("sample-courses.json", "w") as f:
    json.dump(courses, f, indent=2)

print("✅ sample-courses.json with 50 records generated successfully.")
