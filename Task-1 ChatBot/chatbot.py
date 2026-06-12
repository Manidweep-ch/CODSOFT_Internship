"""
Career Guidance Chatbot - A rule-based NLP chatbot for career exploration

This chatbot uses regular expressions for intent detection and provides
guidance on career paths, job opportunities, required skills, and preparation roadmaps.

Author: CodSoft Task-1
"""

import random
import re

# ============================================================================
# KNOWLEDGE BASE
# ============================================================================
# Dictionary containing comprehensive career information for 8 different domains
# Each course entry includes: Description, Jobs, Skills, and Preparation steps
courses = {
    "cse": {
        "Description": "Computer Science Engineering focuses on software development, algorithms, databases, artificial intelligence, and computer systems.",
        "Jobs": ["Software Engineer", "AI Engineer", "Data Scientist"],
        "Skills": ["Python", "DSA", "DBMS"],
        "Preparation": ["Learn Programming", "Practice DSA", "Build Projects"]
    },

    "ece": {
        "Description": "Electronics and Communication Engineering focuses on electronic circuits, communication systems, embedded systems, VLSI, and IoT technologies.",
        "Jobs": ["Embedded Engineer", "VLSI Engineer", "IoT Developer"],
        "Skills": ["C Programming", "Microcontrollers", "Digital Electronics"],
        "Preparation": ["Learn C", "Study Electronics", "Build Embedded Projects"]
    },

    "mechanical": {
        "Description": "Mechanical Engineering deals with the design, manufacturing, analysis, and maintenance of machines, engines, and mechanical systems.",
        "Jobs": ["Design Engineer", "Production Engineer", "Automobile Engineer"],
        "Skills": ["CAD", "Thermodynamics", "Manufacturing"],
        "Preparation": ["Learn AutoCAD", "Study Core Subjects", "Do Industry Internships"]
    },

    "civil": {
        "Description": "Civil Engineering focuses on the planning, design, construction, and maintenance of infrastructure such as buildings, bridges, roads, and dams.",
        "Jobs": ["Site Engineer", "Structural Engineer", "Construction Manager"],
        "Skills": ["AutoCAD", "Surveying", "Structural Design"],
        "Preparation": ["Learn Design Software", "Understand Construction Processes", "Gain Field Experience"]
    },

    "ai": {
        "Description": "Artificial Intelligence focuses on building intelligent systems capable of learning from data, recognizing patterns, making decisions, and solving complex problems.",
        "Jobs": ["AI Engineer", "Machine Learning Engineer", "NLP Engineer"],
        "Skills": ["Python", "Machine Learning", "Deep Learning"],
        "Preparation": ["Learn Python", "Study ML Algorithms", "Build AI Projects"]
    },

    "cybersecurity": {
        "Description": "Cybersecurity focuses on protecting computer systems, networks, and data from cyber attacks, unauthorized access, and security threats.",
        "Jobs": ["Security Analyst", "Penetration Tester", "SOC Analyst"],
        "Skills": ["Networking", "Linux", "Ethical Hacking"],
        "Preparation": ["Learn Networking", "Study Cybersecurity Basics", "Practice on Labs"]
    },

    "data science": {
        "Description": "Data Science combines programming, statistics, and machine learning to extract insights and knowledge from large volumes of data.",
        "Jobs": ["Data Scientist", "Data Analyst", "Business Analyst"],
        "Skills": ["Python", "Statistics", "SQL"],
        "Preparation": ["Learn Python", "Study Statistics", "Build Data Projects"]
    },

    "full stack": {
        "Description": "Full Stack Development involves building complete web applications by working on both frontend user interfaces and backend server-side systems.",
        "Jobs": ["Full Stack Developer", "Backend Developer", "Frontend Developer"],
        "Skills": ["HTML", "CSS", "JavaScript", "Python"],
        "Preparation": ["Learn Frontend", "Learn Backend", "Build Web Applications"]
    }
}

# ============================================================================
# INTENT DETECTION PATTERNS
# ============================================================================
# Regex patterns for identifying user intents like job inquiries, skill questions, etc.
JOB_PATTERN = re.compile(r"\b(job|jobs|career|careers|role|roles)\b")
SKILL_PATTERN = re.compile(r"\b(skill|skills|learn|technology|technologies)\b")
PREP_PATTERN = re.compile(r"\b(prepare|preparation|study)\b")
DESC_PATTERN = re.compile(r"\b(what|explain|describe)\b")

# Dictionary of primary user intents and their regex patterns
# Used to classify user queries into greeting, help, course selection, etc.
INTENTS = {
    "greeting": re.compile(r"\b(hi|hello|hey|good morning|good afternoon|good evening)\b"),
    "help": re.compile(r"\b(help|commands)\b"),
    "course": re.compile(r"\b(cse|ece|civil|mechanical|ai|cybersecurity|data science|full stack)\b"),
    "goodbye": re.compile(r"\b(bye|exit|quit)\b"),
    "roadmap": re.compile(r"\b(roadmap|guide)\b"),
    "motivate": re.compile(r"\b(motivate|motivation|quote)\b")
}

# ============================================================================
# RECOMMENDATION SYSTEM
# ============================================================================
# Maps user interests to relevant career paths
# When user mentions an interest, the chatbot suggests related courses
recommendations = {
    "coding": ["cse", "ai", "full stack"],
    "electronics": ["ece"],
    "machines": ["mechanical"],
    "construction": ["civil"],
    "security": ["cybersecurity"],
    "data": ["data science", "ai"]
}

# Pattern to extract user name from input like "my name is John"
NAME_PATTERN = re.compile(r"my name is (\w+)")

# ============================================================================
# SESSION STATE VARIABLES
# ============================================================================
# user_name: Stores user's name for personalized responses
# last_course: Maintains context of the last discussed course for follow-up queries
user_name = None
last_course = None

# Motivational quotes displayed when user requests motivation
career_quotes = [
    "Consistency beats talent.",
    "Projects speak louder than certificates.",
    "Learning never stops."
]


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def print_course_info(course_name, info_type):
    """
    Print specific information about a course based on the requested info type.
    
    Args:
        course_name (str): The course key from the courses dictionary
        info_type (str): Type of information to display - 'description', 'jobs', 
                        'skills', 'preparation', or 'all'
    """
    course_data = courses[course_name]
    
    if info_type == "description":
        print(f"{course_data['Description']}")
    elif info_type == "jobs":
        print("Jobs:")
        for job in course_data["Jobs"]:
            print(f"  - {job}")
    elif info_type == "skills":
        print("Skills:")
        for skill in course_data["Skills"]:
            print(f"  - {skill}")
    elif info_type == "preparation":
        print("Preparation:")
        for step in course_data["Preparation"]:
            print(f"  - {step}")
    elif info_type == "all":
        # Display all information about the course
        for category, items in course_data.items():
            print(f"{category}:")
            if isinstance(items, list):
                for item in items:
                    print(f"  - {item}")
            else:
                print(f"  {items}")
            print()


def detect_intent(user_input):
    """
    Detect user intent from input string using regex patterns.
    
    Args:
        user_input (str): Processed user input (lowercase and stripped)
    
    Returns:
        str: Detected intent name or None if no intent matches
    """
    for intent, pattern in INTENTS.items():
        if pattern.search(user_input):
            return intent
    return None


def extract_course_name(user_input):
    """
    Extract course name from user input using regex matching.
    
    Args:
        user_input (str): Processed user input to search for course names
    
    Returns:
        str: Course name if found, None otherwise
    """
    for course in courses:
        if re.search(rf"\b{re.escape(course)}\b", user_input):
            return course
    return None


def handle_course_query(user_input, selected_course):
    """
    Handle course-related queries by determining what information to display.
    Uses regex patterns to identify if user is asking for jobs, skills, prep, or description.
    
    Args:
        user_input (str): User's question/input
        selected_course (str): The course to provide information about
    
    Returns:
        bool: True if information was displayed, False if no specific request was made
    """
    if DESC_PATTERN.search(user_input):
        print_course_info(selected_course, "description")
        return True
    elif JOB_PATTERN.search(user_input):
        print_course_info(selected_course, "jobs")
        return True
    elif SKILL_PATTERN.search(user_input):
        print_course_info(selected_course, "skills")
        return True
    elif PREP_PATTERN.search(user_input):
        print_course_info(selected_course, "preparation")
        return True
    else:
        # No specific request, display all information
        print_course_info(selected_course, "all")
        return True


# ============================================================================
# MAIN CHATBOT LOOP
# ============================================================================

print("=" * 50)
print("CAREER GUIDANCE CHATBOT")
print("=" * 50)
print("Type 'help' to see available courses.\n")

while True:
    # Get user input and preprocess it
    user_input = input("You: ").lower().strip()
    
    # Skip empty inputs
    if not user_input:
        continue
    
    # ========================================================================
    # STEP 1: NAME RECOGNITION
    # ========================================================================
    # Check if user is introducing themselves (e.g., "my name is John")
    name_match = NAME_PATTERN.search(user_input)
    if name_match:
        user_name = name_match.group(1)
        print(f"Nice to meet you {user_name.title()}!\n")
        continue
    
    # ========================================================================
    # STEP 2: RECOMMENDATION SYSTEM
    # ========================================================================
    # Check if user mentioned an interest keyword and suggest related courses
    recommendation_found = False
    for interest, course_list in recommendations.items():
        if interest in user_input:
            print("\nRecommended Courses:")
            for course in course_list:
                print(f"  - {course}")
            print()
            recommendation_found = True
            break
    
    if recommendation_found:
        continue
    
    # ========================================================================
    # STEP 3: INTENT DETECTION
    # ========================================================================
    # Classify user query into one of the predefined intents
    detected_intent = detect_intent(user_input)
    
    # ========================================================================
    # STEP 4: INTENT-BASED RESPONSE GENERATION
    # ========================================================================
    
    if detected_intent == "greeting":
        # Personalized greeting if user name is known
        if user_name:
            print(f"Hello {user_name.title()}! I can guide you about different career paths.\n")
        else:
            print("Hello! I can guide you about different career paths.\n")
    
    elif detected_intent == "help":
        # Display available commands and courses
        print("\nYou can ask me about the below courses:")
        for course in courses:
            print(f"  - {course}")
        print("\nYou can also ask for:")
        print("  - help (to see this message)")
        print("  - roadmap (for career guidance roadmap)")
        print("  - motivate (for a motivational quote)")
        print("  - bye (to exit)\n")
    
    elif detected_intent == "course":
        # Handle course-related queries
        selected_course = extract_course_name(user_input)
        
        # If no course mentioned, use last discussed course from context
        if selected_course is None:
            selected_course = last_course
        
        if selected_course is None:
            print("Please specify a course first. Type 'help' to see available courses.\n")
            continue
        
        # Update session memory with current course
        last_course = selected_course
        
        # Display relevant course information based on user's query
        handle_course_query(user_input, selected_course)
        print()
    
    elif detected_intent is None and (
        JOB_PATTERN.search(user_input)
        or SKILL_PATTERN.search(user_input)
        or PREP_PATTERN.search(user_input)
    ):
        # User asked about jobs/skills/prep without specifying a course
        # Try to use last discussed course from context
        if last_course is not None:
            handle_course_query(user_input, last_course)
            print()
        else:
            print("Please specify a course first. Type 'help' to see available courses.\n")
    
    elif detected_intent == "roadmap":
        # Display a step-by-step career development roadmap
        print("\nCareer Development Roadmap:")
        roadmap_steps = [
            "1. Choose a Career Path",
            "2. Learn Required Skills",
            "3. Build Projects",
            "4. Create GitHub Profile",
            "5. Apply for Internships",
            "6. Prepare for Interviews"
        ]
        for step in roadmap_steps:
            print(f"  {step}")
        print()
    
    elif detected_intent == "motivate":
        # Display a random motivational quote
        print(f"\n{random.choice(career_quotes)}\n")
    
    elif detected_intent == "goodbye":
        # Exit the chatbot gracefully
        print("Thank you for using Career Guidance Chatbot. Good luck with your career!\n")
        break
    
    else:
        # Handle unrecognized queries
        print("Sorry, I don't have information on what you asked. Type 'help' for available options.\n")
                


