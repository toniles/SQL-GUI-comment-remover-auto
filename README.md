# SQL Comment Remover v3.0 📝

🧹 Clean up your SQL files in seconds by removing comments effortlessly!

SQL Comment Remover is a Python tool with a user-friendly GUI for removing comments from SQL files. Streamline your SQL code by eliminating unnecessary comments quickly and easily.

## 🎯 Key Features

- 🚀 Removes single-line (--) and multi-line (/* */) comments from SQL files
- 🖥️ Drag-and-drop support for easy file selection
- 📄 Process multiple files simultaneously
- 💻 Intuitive GUI built with Tkinter
- 🛠️ Supports various character encodings
- 📦 Automatic dependency installation

![DEMO](https://github.com/user-attachments/assets/78d70583-5cfc-4710-ac7f-00a5f065f617)

## 🚀 Quick Start Guide

1. Ensure you have Python 3.8+ installed
2. Clone the repository and run the application:
   ```
   git clone https://github.com/your-repo/sql-comment-remover.git
   cd sql-comment-remover
   python sql_comment_remover.py
   ```
   The application will automatically install required dependencies on first run.

## 💡 How It Works

1. Drag and drop SQL files into the app window or use the "Select Files" button
2. Click "Process Files" to remove comments
3. Cleaned files are saved with "_without_comments" appended to the filename

## 📊 Example

Original SQL:
```sql
-- This is a comment
SELECT * FROM users;
/* Multi-line comment
   continues here */
INSERT INTO users (id, name) VALUES (1, 'John Doe');
```

Cleaned SQL:
```sql
SELECT * FROM users;
INSERT INTO users (id, name) VALUES (1, 'John Doe');
```

## 📄 License

This software is released into the public domain under the Unlicense.

## 📢 Feedback & Support

For issues or suggestions, please open an issue or submit a pull request!
