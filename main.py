import sqlite3


career_data = {
    "Data Scientist": {
        "description": "Analyzes data and builds intelligent systems.",
        "skills": "Python, Statistics, Machine Learning",
        "scope": "High demand in AI industries."
    },

    "AI Engineer": {
        "description": "Develops AI and machine learning systems.",
        "skills": "Python, Deep Learning",
        "scope": "Rapidly growing AI field."
    },

    "Software Engineer": {
        "description": "Builds software applications and systems.",
        "skills": "Programming, Problem Solving",
        "scope": "High demand worldwide."
    },

    "Web Developer": {
        "description": "Creates websites and web applications.",
        "skills": "HTML, CSS, JavaScript",
        "scope": "Freelancing and job opportunities."
    },

    "Cybersecurity Analyst": {
        "description": "Protects systems from cyber attacks.",
        "skills": "Networking, Security",
        "scope": "Growing cybersecurity industry."
    },

    "Graphic Designer": {
        "description": "Designs graphics and visual content.",
        "skills": "Creativity, Designing",
        "scope": "Media and marketing industries."
    },

    "Doctor": {
        "description": "Treats patients and improves healthcare.",
        "skills": "Biology, Healthcare",
        "scope": "Stable and respected profession."
    },

    "Digital Marketer": {
        "description": "Promotes businesses online.",
        "skills": "Communication, Marketing",
        "scope": "Growing online business market."
    },

    "Teacher": {
        "description": "Educates students and provides guidance.",
        "skills": "Teaching, Communication",
        "scope": "Always needed in education."
    },

    "Accountant": {
        "description": "Handles financial records and accounts.",
        "skills": "Mathematics, Business",
        "scope": "Demand in companies and banks."
    }
}


conn = sqlite3.connect("career.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age TEXT,
qualification TEXT,
favorite_subject TEXT,
strongest_subject TEXT,
skills TEXT,
interest TEXT,
work_style TEXT,
recommended_careers TEXT
)
""")

conn.commit()


def show_title():

    print("==========================================")
    print(" AI-Based Career Recommendation System ")
    print("==========================================")


def collect_user_data():

    name = input("Enter Your Name: ")
    age = input("Enter Your Age: ")
    qualification = input("Enter Qualification: ")

    favorite_subject = input("Favorite Subject: ").lower()

    strongest_subject = input("Strongest Subject: ").lower()

    print("\nAvailable Skills")
    print("Programming")
    print("Problem Solving")
    print("Creativity")
    print("Designing")
    print("Communication")
    print("Mathematics")
    print("Networking")
    print("Security")
    print("Biology")
    print("Teaching")

    skills = input("\nEnter Skills Separated By Comma: ").lower()

    print("\nCareer Interests")
    print("Technology")
    print("Healthcare")
    print("Business")
    print("Arts")
    print("Teaching")

    interest = input("Enter Interest: ").lower()

    print("\nPreferred Work Style")
    print("Office Work")
    print("Remote Work")
    print("Team-Based Work")
    print("Creative Work")
    print("Field Work")

    work_style = input("Enter Work Style: ").lower()

    user_data = {
        "name": name,
        "age": age,
        "qualification": qualification,
        "favorite_subject": favorite_subject,
        "strongest_subject": strongest_subject,
        "skills": skills,
        "interest": interest,
        "work_style": work_style
    }

    return user_data


def recommend_careers(user_data):

    recommendations = []

    skills = user_data["skills"]

    subject = user_data["favorite_subject"]

    strong_subject = user_data["strongest_subject"]

    interest = user_data["interest"]

    if "programming" in skills and "mathematics" in skills:
        recommendations.append("Data Scientist")

    if "programming" in skills and "problem solving" in skills:
        recommendations.append("Software Engineer")

    if "programming" in skills and interest == "technology":
        recommendations.append("AI Engineer")

    if "designing" in skills or "creativity" in skills:
        recommendations.append("Graphic Designer")

    if "biology" in skills or subject == "biology":
        recommendations.append("Doctor")

    if "communication" in skills and interest == "business":
        recommendations.append("Digital Marketer")

    if "networking" in skills or "security" in skills:
        recommendations.append("Cybersecurity Analyst")

    if subject == "computer" or strong_subject == "computer":
        recommendations.append("Web Developer")

    if "teaching" in skills or interest == "teaching":
        recommendations.append("Teacher")

    if "mathematics" in skills and interest == "business":
        recommendations.append("Accountant")

    return recommendations


def display_recommendations(recommendations):

    print("\n========== Recommended Careers ==========")

    count = 1

    for career in recommendations:

        print(f"\n{count}. {career}")

        print("Description:")
        print(career_data[career]["description"])

        print("\nRequired Skills:")
        print(career_data[career]["skills"])

        print("\nFuture Scope:")
        print(career_data[career]["scope"])

        print("--------------------------------------")

        count += 1


def save_to_database(user_data, recommendations):

    careers = ", ".join(recommendations)

    cursor.execute("""
    INSERT INTO students
    (
    name,
    age,
    qualification,
    favorite_subject,
    strongest_subject,
    skills,
    interest,
    work_style,
    recommended_careers
    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,

    (
    user_data["name"],
    user_data["age"],
    user_data["qualification"],
    user_data["favorite_subject"],
    user_data["strongest_subject"],
    user_data["skills"],
    user_data["interest"],
    user_data["work_style"],
    careers
    ))

    conn.commit()

    print("\nRecord Saved Successfully In Database")


def view_records():

    print("\n========== Saved Records ==========\n")

    cursor.execute("SELECT * FROM students")

    records = cursor.fetchall()

    for row in records:

        print("ID:", row[0])
        print("Name:", row[1])
        print("Age:", row[2])
        print("Qualification:", row[3])
        print("Favorite Subject:", row[4])
        print("Strongest Subject:", row[5])
        print("Skills:", row[6])
        print("Interest:", row[7])
        print("Work Style:", row[8])
        print("Recommended Careers:", row[9])

        print("----------------------------------")


while True:

    show_title()

    print("\n1. Start Career Analysis")
    print("2. View Saved Records")
    print("3. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        user_data = collect_user_data()

        recommendations = recommend_careers(user_data)

        if len(recommendations) == 0:

            print("\nNo Career Recommendation Found")

        else:

            display_recommendations(recommendations)

            save_to_database(user_data, recommendations)

    elif choice == "2":

        view_records()

    elif choice == "3":

        print("\nThank You For Using The System")

        break

    else:

        print("\nInvalid Choice")


conn.close()
