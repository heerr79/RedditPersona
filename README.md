# PEP: Custom – Reddit User Persona Generator (PEP 8 Style)
**Title**: Reddit User Persona Generator  
**Author**: Heer Rajesh Panchal <heer.panchal@somaiya.edu>  
**Status**: Final  
**Type**: Project  
**Created**: 14-Jul-2025  

---

## 📘 Introduction

This document describes the design and coding standards followed in the development of the **Reddit User Persona Generator** script, which was built as part of a 48-hour problem-solving and coding assignment. The project aims to demonstrate clean code practices and adhere to [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/) as recommended by the Python community.

The author, **Heer Rajesh Panchal**, implemented this project using Python and publicly available Reddit APIs via the `praw` package.

---

## 🎯 Objective

To build a Python-based script that:
1. Accepts a Reddit profile URL.
2. Scrapes recent posts and comments of the user.
3. Analyzes the data to generate a textual **User Persona**.
4. Includes **citations** for every insight (i.e., links to original posts/comments).
5. Outputs the persona in a `.txt` file.

---

## 🧱 Code Design Overview

- **Language**: Python 3
- **Libraries Used**:
  - `praw`: For accessing Reddit content.
  - `textblob`: For sentiment analysis.
  - `dotenv`: For secure storage of API keys.
- **File Structure**:
```

reddit\_persona/
├── reddit\_persona.py
├── requirements.txt
├── .env.example
├── Hungry-Move-6603\_persona.txt
├── kojied\_persona.txt
├── README.md

````

---

## 💡 Coding Style Highlights (PEP 8 Compliant)

### Indentation & Whitespace

- 4 spaces used per indentation level.
- Aligned multi-line function calls with hanging indent:
```python
user = reddit.redditor(
    extract_username(profile_url)
)
````

* No extraneous whitespace:

  ```python
  spam(ham[1], {eggs: 2})  # ✅
  ```

### Function & Variable Naming

* Snake\_case used throughout:

  ```python
  def analyze_user(username):
      top_subreddits = {}
  ```

### Maximum Line Length

* Line length limited to **79 characters** where possible.
* Docstrings and comments limited to **72 characters**.

### Blank Lines

* Two blank lines before top-level function definitions.
* Single blank line between methods inside a class (if used).

### Imports

* Grouped as:

  ```python
  import os
  import praw
  from textblob import TextBlob
  from dotenv import load_dotenv
  ```

---

## 📄 Output Format

Each generated `.txt` file follows a standard persona template:

```
=========================
🧑 Reddit User Persona
=========================
👤 Username: u/kojied

📚 Top Subreddits (Interests):
AskReddit (12 posts), funny (8 posts), technology (6 posts)

📊 Activity Type:
Posts: 20, Comments: 45

🕓 Most Active Hour: 21:00

🎭 Overall Tone: Positive

🗣️ Self-Descriptions Found:
- "I'm a software engineer based in Toronto..."
  → Source: https://reddit.com/...
```

---

## 🧪 Sample Output Files

Two sample Reddit profiles were analyzed:

* `Hungry-Move-6603_persona.txt`
* `kojied_persona.txt`

These are included in the repository for review and evaluation.

---

## 📎 Citation and Traceability

All extracted information (tone, interest, activity, self-description) includes a **source citation** (URL) for transparency.

---

## 🧠 Learnings

* Efficient use of Python’s data structures to summarize user activity.
* Applied natural language processing using TextBlob.
* Reinforced best practices from PEP 8 for clean and maintainable code.

---

## 📘 Conclusion

The Reddit User Persona Generator was developed in adherence to Python’s coding standards and demonstrates effective application of PEP 8 principles in a real-world script.

The final result is a lightweight, readable, and reusable script that can extract meaningful user personas with minimal setup.

