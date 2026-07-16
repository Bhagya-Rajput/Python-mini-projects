# 📝 Python To-Do List (CLI)

A simple Command Line Interface (CLI) To-Do List application built with **Python**. This project allows users to manage their daily tasks using a JSON file for persistent storage.

## 🚀 Features

* ➕ Add new tasks
* 📋 View all tasks
* ❌ Remove existing tasks
* ✅ Mark tasks as completed
* ⬜ Mark completed tasks as pending
* 💾 Automatically save tasks in a JSON file
* ⚠️ Handles invalid inputs using exception handling

## 🛠️ Technologies Used

* Python 3
* JSON
* File Handling
* Dictionaries
* Lists
* Match-Case Statement
* Exception Handling

## 📂 Project Structure

```
To-Do-List/
│── main.py          # Main Python program
│── Text.json        # Stores all tasks
└── README.md
```

## 📦 How It Works

Each task is stored as a dictionary inside a list.

Example:

```json
[
    {
        "task": "Learn Python",
        "status": false
    },
    {
        "task": "Build a To-Do List",
        "status": true
    }
]
```

* `"task"` stores the task description.
* `"status"` stores whether the task is completed (`true`) or pending (`false`).

## ▶️ How to Run

1. Clone the repository.

```bash
git clone https://github.com/your-username/To-Do-List.git
```

2. Navigate to the project directory.

```bash
cd To-Do-List
```

3. Run the program.

```bash
python main.py
```

## 📸 Menu

```
===== TO-DO LIST =====

1. Add Task
2. View Tasks
3. Remove Task
4. Change Task Status
5. Exit
```

## 💡 Concepts Practiced

This project helped me practice:

* Python basics
* Loops (`while`)
* Conditional statements
* Match-Case
* Functions (future enhancement)
* Lists
* Dictionaries
* JSON (`json.load()` & `json.dump()`)
* File Handling
* Exception Handling (`try` / `except`)
* User Input Validation

## 🔮 Future Improvements

* 🔍 Search tasks
* ✏️ Edit task names
* 📅 Add due dates
* ⭐ Task priorities
* 📊 Task statistics
* 🎨 Colored terminal output
* 🖥️ GUI version using Tkinter
* 🌐 Web version using Flask or Django

## 👨‍💻 Author

**Bhagya Kumar Rajput**

* GitHub: https://github.com/Bhagya-Rajput

---

⭐ If you found this project useful, consider giving it a star on GitHub!
