import json
import random
from datetime import datetime, timedelta

# Lists for generating varied data
first_names = [
    "John", "Jane", "Alice", "Bob", "Carol", "David", "Emma", "Frank", "Grace", "Henry",
    "Ivy", "Jack", "Katherine", "Liam", "Mia", "Noah", "Olivia", "Paul", "Quinn", "Rachel",
    "Samuel", "Tina", "Umar", "Victoria", "William", "Xena", "Yasin", "Zoe", "Aaron", "Bella",
    "Caleb", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia", "Kevin", "Laura",
    "Michael", "Nina", "Oscar", "Paula", "Quentin", "Rebecca", "Steven", "Tiffany", "Ulysses", "Vanessa",
    "Walter", "Ximena", "Yuri", "Zara", "Adam", "Brooke", "Christian", "Danielle", "Elijah", "Faith",
    "Gabriel", "Hailey", "Isaac", "Jasmine", "Kyle", "Lily", "Mason", "Natalie", "Oliver", "Penelope",
    "Quincy", "Rose", "Sebastian", "Taylor", "Ursula", "Victor", "Wendy", "Xander", "Yara", "Zachary"
]

last_names = [
    "Doe", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez",
    "Martinez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "White",
    "Harris", "Clark", "Lewis", "Robinson", "Walker", "Young", "Allen", "King", "Wright", "Scott",
    "Green", "Baker", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell",
    "Parker", "Evans", "Edwards", "Collins", "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook"
]

# Comprehensive role data with department, designation, and skills
role_data = {
    "Frontend Developer": {
        "department": "Engineering",
        "team": ["UI/UX Team", "Web Platform", "Customer Portal"],
        "designation": ["Junior Frontend Developer", "Frontend Developer", "Senior Frontend Developer"],
        "skills": ["React.js", "Vue.js", "Angular", "TypeScript", "Tailwind CSS", "Next.js"]
    },
    "Backend Developer": {
        "department": "Engineering",
        "team": ["API Team", "Core Services", "Database Team"],
        "designation": ["Junior Backend Developer", "Backend Developer", "Senior Backend Developer"],
        "skills": ["Node.js", "Python", "Java", "Go", "PostgreSQL", "MongoDB", "Redis"]
    },
    "Full Stack Developer": {
        "department": "Engineering",
        "team": ["Product Team", "Integration Team", "Features Team"],
        "designation": ["Full Stack Developer", "Senior Full Stack Developer", "Lead Full Stack Developer"],
        "skills": ["React.js", "Node.js", "TypeScript", "MongoDB", "Express.js", "GraphQL"]
    },
    "UI/UX Designer": {
        "department": "Design",
        "team": ["Product Design", "User Research", "Brand Team"],
        "designation": ["Junior Designer", "UI/UX Designer", "Senior Designer", "Design Lead"],
        "skills": ["Figma", "Adobe XD", "Sketch", "User Research", "Prototyping", "Wireframing"]
    },
    "Project Manager": {
        "department": "Project Management",
        "team": ["Agile Team", "Delivery Team", "Client Services"],
        "designation": ["Associate Project Manager", "Project Manager", "Senior Project Manager"],
        "skills": ["Agile", "Scrum", "JIRA", "Risk Management", "Stakeholder Management"]
    },
    "QA Engineer": {
        "department": "Quality Assurance",
        "team": ["Testing Team", "Automation Team", "Performance Team"],
        "designation": ["QA Analyst", "QA Engineer", "Senior QA Engineer", "QA Lead"],
        "skills": ["Selenium", "Cypress", "Jest", "Manual Testing", "Automation", "API Testing"]
    },
    "DevOps Engineer": {
        "department": "Infrastructure",
        "team": ["Cloud Team", "Platform Team", "SRE Team"],
        "designation": ["DevOps Engineer", "Senior DevOps Engineer", "Cloud Architect"],
        "skills": ["AWS", "Docker", "Kubernetes", "Jenkins", "Terraform", "CI/CD", "Linux"]
    },
    "Data Scientist": {
        "department": "Data & Analytics",
        "team": ["Analytics Team", "ML Team", "BI Team"],
        "designation": ["Data Analyst", "Data Scientist", "Senior Data Scientist"],
        "skills": ["Python", "SQL", "Machine Learning", "TensorFlow", "Pandas", "Tableau"]
    },
    "Product Manager": {
        "department": "Product",
        "team": ["Product Strategy", "Innovation Team", "Growth Team"],
        "designation": ["Associate Product Manager", "Product Manager", "Senior Product Manager"],
        "skills": ["Product Strategy", "Market Research", "Roadmap Planning", "User Stories", "Analytics"]
    },
    "Security Engineer": {
        "department": "Security",
        "team": ["Security Operations", "Compliance Team", "Risk Team"],
        "designation": ["Security Analyst", "Security Engineer", "Senior Security Engineer"],
        "skills": ["Penetration Testing", "Network Security", "Encryption", "SIEM", "Compliance"]
    }
}

# Flat roles list for selection
roles = list(role_data.keys())

# Cities with their details
cities = [
    {"name": "New York", "state": "NY", "zip": "10001", "country": "USA"},
    {"name": "Los Angeles", "state": "CA", "zip": "90001", "country": "USA"},
    {"name": "Chicago", "state": "IL", "zip": "60601", "country": "USA"},
    {"name": "Houston", "state": "TX", "zip": "77001", "country": "USA"},
    {"name": "London", "state": "England", "zip": "EC1A", "country": "UK"},
    {"name": "Toronto", "state": "ON", "zip": "M5V", "country": "Canada"},
    {"name": "Sydney", "state": "NSW", "zip": "2000", "country": "Australia"},
    {"name": "Berlin", "state": "BE", "zip": "10115", "country": "Germany"},
    {"name": "Singapore", "state": "SG", "zip": "018906", "country": "Singapore"},
    {"name": "Bangalore", "state": "KA", "zip": "560001", "country": "India"}
]

# Genders
genders = ["Male", "Female", "Other"]

# Marital statuses
marital_statuses = ["Single", "Married", "Divorced", "Widowed"]

# Project names
project_names = [
    "ERP Management System", "Customer Portal", "Mobile Banking App", "E-commerce Platform",
    "Inventory Management", "HRMS System", "CRM Integration", "Data Analytics Dashboard",
    "Cloud Migration", "Security Audit System", "AI Chatbot", "Payment Gateway",
    "Learning Management System", "Healthcare Portal", "Real Estate Platform"
]

def generate_phone(user_id):
    area_codes = ["202", "212", "310", "415", "312", "617", "206", "303", "404", "305"]
    area = area_codes[user_id % len(area_codes)]
    return f"+1-{area}-555-{str(user_id)[-4:]}"

def generate_joining_date(user_id):
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2026, 5, 15)
    random_days = random.randint(0, (end_date - start_date).days)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

def generate_dob(user_id):
    start_date = datetime(1980, 1, 1)
    end_date = datetime(2005, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

def generate_last_login(user_id):
    now = datetime.now()
    random_hours = random.randint(0, 168)  # Last week
    return (now - timedelta(hours=random_hours)).strftime("%Y-%m-%dT%H:%M:%SZ")

def generate_attendance():
    present = random.randint(18, 23)
    absent = 23 - present
    late = random.randint(0, 5)
    return {
        "presentDays": present,
        "absentDays": absent,
        "lateCount": late
    }

def generate_projects(user_id, role):
    num_projects = random.randint(1, 4)
    projects = []
    used_indices = set()
    for i in range(num_projects):
        idx = random.randint(0, len(project_names) - 1)
        while idx in used_indices:
            idx = random.randint(0, len(project_names) - 1)
        used_indices.add(idx)
        project = {
            "projectId": f"PRJ-{1000 + user_id + i}",
            "projectName": project_names[idx],
            "status": random.choice(["Running", "Completed", "Planning", "On Hold"])
        }
        projects.append(project)
    return projects

# Generate 1500 users from ID 1347 to 2846
users = []
random.seed(42)  # For reproducible results

for i in range(15000):
    user_id = 1111 + i
    
    # Basic name
    first_name = first_names[i % len(first_names)]
    last_name = last_names[i % len(last_names)]
    full_name = f"{first_name} {last_name}"
    username = f"{first_name.lower()}{last_name.lower()}{user_id % 100}"
    
    # Role selection
    role_name = roles[i % len(roles)]
    role_info = role_data[role_name]
    
    # Team and designation
    team = random.choice(role_info["team"])
    designation_level = i % len(role_info["designation"])
    designation = role_info["designation"][designation_level]
    
    # Experience based on designation level
    exp_years = {
        0: random.randint(0, 2),
        1: random.randint(3, 6),
        2: random.randint(7, 12)
    }.get(designation_level, random.randint(3, 8))
    
    # Salary based on experience and role
    base_salary = {
        "Frontend Developer": 4500,
        "Backend Developer": 4800,
        "Full Stack Developer": 5000,
        "UI/UX Designer": 4200,
        "Project Manager": 6000,
        "QA Engineer": 4000,
        "DevOps Engineer": 5500,
        "Data Scientist": 5800,
        "Product Manager": 6500,
        "Security Engineer": 5900
    }.get(role_name, 4500)
    
    salary = base_salary + (exp_years * 300) + random.randint(-500, 500)
    
    # Skills (select 4-6 random skills from role's skills)
    num_skills = random.randint(4, min(6, len(role_info["skills"])))
    skills = random.sample(role_info["skills"], num_skills)
    
    # Address
    city_info = cities[user_id % len(cities)]
    address = {
        "street": f"{random.randint(100, 999)} {random.choice(['Main', 'Oak', 'Pine', 'Maple', 'Cedar'])} {random.choice(['St', 'Ave', 'Blvd', 'Rd', 'Ln'])}",
        "city": city_info["name"],
        "state": city_info["state"],
        "country": city_info["country"],
        "zipCode": city_info["zip"]
    }
    
    # Gender
    gender = genders[user_id % len(genders)]
    
    # Profile image
    if gender == "Male":
        profile_image = f"https://randomuser.me/api/portraits/men/{user_id % 100}.jpg"
    else:
        profile_image = f"https://randomuser.me/api/portraits/women/{user_id % 100}.jpg"
    
    # Emergency contact relation
    relation = random.choice(["Brother", "Sister", "Spouse", "Parent", "Friend", "Cousin"])
    emergency_name = f"{random.choice(first_names)} {random.choice(last_names)}"
    
    user = {
        "id": user_id,
        "employeeCode": f"EMP-2026-{user_id}",
        "name": full_name,
        "username": username,
        "email": f"{first_name.lower()}.{last_name.lower()}@gmail.com",
        "phone": generate_phone(user_id),
        "role": role_name,
        "department": role_info["department"],
        "team": team,
        "designation": designation,
        "experience": f"{exp_years} Years",
        "skills": skills,
        "salary": salary,
        "currency": "USD",
        "joiningDate": generate_joining_date(user_id),
        "dateOfBirth": generate_dob(user_id),
        "gender": gender,
        "maritalStatus": random.choice(marital_statuses),
        "address": address,
        "socialLinks": {
            "linkedin": f"https://linkedin.com/in/{username}",
            "github": f"https://github.com/{username}",
            "portfolio": f"https://{username}.dev"
        },
        "profileImage": profile_image,
        "isActive": random.choice([True, True, True, False]),  # 75% active
        "lastLogin": generate_last_login(user_id),
        "attendance": generate_attendance(),
        "projects": generate_projects(user_id, role_name),
        "emergencyContact": {
            "name": emergency_name,
            "relation": relation,
            "phone": generate_phone(user_id + 1000)
        }
    }
    users.append(user)
    
    # Progress indicator
    if (i + 1) % 100 == 0:
        print(f"Generated {i + 1}/1500 users...")

# Save to JSON file
with open("../data/users_2.json", "w") as f:
    json.dump(users, f, indent=2)

print(f"\n✅ Successfully generated {len(users)} users!")
print(f"📊 ID Range: 1111 to {1111 + len(users) - 1}")
print(f"💾 File saved as: users_2.json")
print(f"\n📈 Statistics:")
print(f"   - Total Users: {len(users)}")
print(f"   - Departments: {len(set(u['department'] for u in users))}")
print(f"   - Roles: {len(set(u['role'] for u in users))}")
print(f"   - Active Users: {sum(1 for u in users if u['isActive'])}")
print(f"   - Average Salary: ${sum(u['salary'] for u in users) // len(users)}")