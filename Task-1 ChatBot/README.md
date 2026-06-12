# Career Guidance Chatbot

## 📌 Project Overview

A simple Python chatbot that helps students explore 8 different career paths, learn required skills, discover job opportunities, and get preparation guidance. Uses regex patterns for understanding user questions.

---

## ✨ Features

- 🎯 Career guidance for 8 domains (CSE, ECE, AI, Cybersecurity, Data Science, etc.)
- 💼 Job recommendations for each career path
- 🛠️ Skill requirements and preparation steps
- 👤 User name recognition and personalization
- 💭 Remember last discussed course for follow-up questions
- 📚 Career recommendations based on interests
- 🎓 Interactive help system and motivational quotes
- 🔧 Built with Python regex patterns for intent detection

---

## 🚀 Quick Start

### Requirements
- Python 3.6+
- No external packages needed

### Run the Chatbot
```bash
cd "C:\Users\chint\Desktop\CodSoft\Task-1 ChatBot"
python chatbot.py
```

### Example Commands
```
You: help                    → See available courses
You: tell me about cse      → Learn about Computer Science
You: what jobs?             → See jobs for last discussed course
You: my name is john        → Introduce yourself
You: i like coding          → Get course recommendations
You: roadmap                → See career development steps
You: motivate               → Get a motivational quote
You: bye                    → Exit chatbot
```


---

## 📚 Supported Career Domains

1. **CSE** - Computer Science Engineering
2. **ECE** - Electronics and Communication Engineering
3. **Mechanical** - Mechanical Engineering
4. **Civil** - Civil Engineering
5. **AI** - Artificial Intelligence
6. **Cybersecurity** - Cybersecurity Engineering
7. **Data Science** - Data Science and Analytics
8. **Full Stack** - Full Stack Development

---

## 💻 How It Works

The chatbot processes user input in these steps:

1. **Read Input** → Convert to lowercase and remove whitespace
2. **Check Name** → Look for "my name is..." pattern
3. **Detect Intent** → Recognize if user wants jobs, skills, help, etc.
4. **Find Course** → Extract course name if mentioned
5. **Retrieve Data** → Get information from knowledge base
6. **Generate Response** → Format and display answer

---

## 📁 Project Files

```
Task-1 ChatBot/
├── chatbot.py          # Main application (382 lines)
├── README.md           # This file
```

**Key Functions:**
- `print_course_info()` - Display course information
- `detect_intent()` - Understand what user wants
- `extract_course_name()` - Find course name in input
- `handle_course_query()` - Route to correct information

---

## 💬 Example Conversation

```
You: hello
Bot: Hello! I can guide you about different career paths.

You: my name is alex
Bot: Nice to meet you Alex!

You: tell me about ai
Bot: Description:
     Artificial Intelligence focuses on building intelligent systems capable 
     of learning from data, recognizing patterns, making decisions...
     
     Jobs:
       - AI Engineer
       - Machine Learning Engineer
       - NLP Engineer
     
     Skills:
       - Python
       - Machine Learning
       - Deep Learning
     
     Preparation:
       - Learn Python
       - Study ML Algorithms
       - Build AI Projects

You: what skills do i need?
Bot: Skills:
       - Python
       - Machine Learning
       - Deep Learning

You: bye
Bot: Thank you for using Career Guidance Chatbot. Good luck with your career!
```

---

## ✅ What's Included

- ✅ Fully documented code with comments
- ✅ 4 utility functions for clean code
- ✅ All bugs fixed and tested
- ✅ PEP 8 code style compliant
- ✅ Better error handling
- ✅ Improved user experience
- ✅ Professional documentation

---

## 🚀 Future Ideas

- **GUI Interface** - Add Tkinter for graphical interface
- **Database** - Store user conversations and progress
- **More Careers** - Add cloud computing, blockchain, game development
- **Web App** - Convert to Flask/Django web application
- **Voice** - Add speech recognition for voice input
- **Mobile** - Create bot for Telegram or Discord
- **ML** - Use machine learning for better intent detection

---

## ❓ FAQ

**Q: How do I add a new career domain?**  
A: Add a new entry to the `courses` dictionary in `chatbot.py` with Description, Jobs, Skills, and Preparation fields.

**Q: Can I modify the regex patterns?**  
A: Yes! Edit the `INTENTS` dictionary to add or change intent patterns.

**Q: How accurate is this?**  
A: Very accurate for clear, direct questions within the chatbot's knowledge. It uses rule-based patterns instead of machine learning.

**Q: Can I deploy this online?**  
A: Yes! You can wrap it with Flask/Django to create a web app or bot for Discord/Telegram.

**Q: What if the chatbot doesn't understand me?**  
A: Try using keywords like "jobs", "skills", "prepare", or course names directly.

---

## 📖 Learning from This Project

This chatbot teaches:
- How regex patterns work for text classification
- Building conversational systems
- Python code organization and functions
- Data structures (dictionaries, lists)
- User state management
- Rule-based vs machine learning NLP

---

## 🎯 Technologies

- **Language**: Python 3.6+
- **Pattern Matching**: Regular Expressions (regex)
- **Data**: Dictionaries and Lists
- **No External Libraries** - Uses only Python standard library
