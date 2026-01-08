# Python_Project_CLI_TDO_LIST_Manager
CLI To‑Do List Manager (Python) 1. Project Overview The CLI To‑Do List Manager is a Python-based command‑line application designed to help users efficiently manage their daily tasks. It provides a simple, interactive, and lightweight interface to add, view, update, delete, and organize tasks without relying on any graphical environment.
Key Features


Add Tasks
Users can create new tasks with optional due dates and priority levels.


View Tasks
Display all tasks in a clean tabular format, categorized by status (Pending/Completed).


Mark Tasks as Completed
Update a task’s status once it is finished.


Edit/Update Tasks
Modify details such as task name, due date, or priority.


Delete Tasks
Remove unwanted tasks permanently.


Task Filtering (optional but recommended)

Filter by priority (High, Medium, Low)
Filter by completion status
Filter by due date



Export to CSV
Allows users to save their task list to a .csv file for backup or external use.


Persistent Storage
All tasks are stored locally using file handling (JSON/CSV/TXT), ensuring data is preserved between sessions.



3. Technology Stack

Programming Language: Python 3
Libraries Used:

os (for system operations)
json or csv (for data storage)
datetime (for due dates)
tabulate (optional, for table formatting)
