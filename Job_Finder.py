"""
Resume -> Best Job Role Finder
Give your resume text, and the tool searches through a database of
job roles (with their required skills) and tells you which roles suit
you best, ranked by match percentage.
"""

# Step 1: Skill keywords we check for (same as before)
SKILL_KEYWORDS = [
    "python", "java", "c++", "sql", "html", "css", "javascript",
    "machine learning", "data analysis", "excel", "communication",
    "leadership", "git", "github", "django", "flask", "react",
    "aws", "cloud", "linux", "api", "problem solving", "teamwork",
    "data structures", "algorithms", "oop", "testing", "debugging"
]

# Step 2: A small "database" of job roles and their required skills.
# In real life this would come from a file/database of scraped job posts.
# For now, we hardcode a few common roles so the tool has something to search.
JOB_ROLES = {
    "Software Engineer Intern": [
        "python", "java", "c++", "data structures", "algorithms",
        "git", "problem solving", "oop", "debugging"
    ],
    "Data Analyst Intern": [
        "python", "sql", "excel", "data analysis", "communication",
        "problem solving"
    ],
    "Machine Learning Intern": [
        "python", "machine learning", "data analysis", "sql",
        "problem solving", "algorithms"
    ],
    "Frontend Developer Intern": [
        "html", "css", "javascript", "react", "git", "github"
    ],
    "Backend Developer Intern": [
        "python", "java", "sql", "api", "django", "flask", "git",
        "linux"
    ],
    "Cloud/DevOps Intern": [
        "aws", "cloud", "linux", "python", "git", "debugging"
    ],
    "Business/Consulting Analyst Intern": [
        "excel", "communication", "leadership", "data analysis",
        "problem solving", "teamwork"
    ],
}


def clean_text(text):
    """Lowercase text and remove punctuation so matching is reliable."""
    text = text.lower()
    for ch in ",.!?;:()[]{}\"'":
        text = text.replace(ch, " ")
    return text


def extract_skills(text, skill_list):
    """Return list of skills (from skill_list) found inside text."""
    cleaned = clean_text(text)
    found = []
    for skill in skill_list:
        if skill in cleaned:
            found.append(skill)
    return found


def match_resume_to_roles(resume_text):
    """
    Compare resume against every job role in JOB_ROLES.
    Returns a list of (role_name, match_percent, matched_skills, missing_skills)
    sorted by match_percent descending (best match first).
    """
    resume_skills = set(extract_skills(resume_text, SKILL_KEYWORDS))
    results = []

    for role_name, required_skills in JOB_ROLES.items():
        required_set = set(required_skills)
        matched = resume_skills & required_set
        missing = required_set - resume_skills

        if len(required_set) == 0:
            percent = 0
        else:
            percent = (len(matched) / len(required_set)) * 100

        results.append((role_name, round(percent, 2), matched, missing))

    # Sort roles by match_percent, highest first
    results.sort(key=lambda x: x[1], reverse=True)
    return results, resume_skills


def main():
    print("=== Resume -> Best Job Role Finder ===\n")
    resume_text = input("Enter your Skills :\n")

    results, resume_skills = match_resume_to_roles(resume_text)

    resume_skills_str = ", ".join(sorted(resume_skills)) if resume_skills else "None"
    print(f"\nSkills detected in your resume: {resume_skills_str}\n")
    print("--- Ranked Job Role Matches ---\n")

    for role_name, percent, matched, missing in results:
        matched_str = ", ".join(sorted(matched)) if matched else "None"
        missing_str = ", ".join(sorted(missing)) if missing else "None"

        print(f"{role_name}: {percent}% match")
        print(f"   Matched skills : {matched_str}")
        print(f"   Missing skills : {missing_str}")
        print()

    best_role = results[0][0]
    best_percent = results[0][1]
    print(f"Best fit for you right now: {best_role} ({best_percent}% match)")


if __name__ == "__main__":
    main()