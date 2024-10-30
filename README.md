# Personal Expense Tracker

A web-based application for tracking personal expenses, built with **Python** and **Flask**. This application helps users monitor their spending by recording and categorizing expenses, with data stored on your live **MySQL** server.

---

## Features

- **Expense Tracking**: Log daily expenses with descriptions and amounts.
- **Categorization**: Organize expenses by customizable categories.
- **Live Data Storage**: Securely stores expense data on your live MySQL server.
- **Insights**: View a summary of expenses to analyze spending habits.

## Tech Stack

- **Backend**: Python, Flask
- **Database**: MySQL (live server)
- **Frontend**: HTML, CSS, JavaScript (optional for UI enhancements)

---

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker
2. **Install Dependencies:**
 - This will install the the   dependencies that were used while building the project.
  
   ```bash
   pip install -r requirements.txt
3. **Configure Database:**
   - Ensure your live MySQL server is accessible.
   - Open config.py and replace the placeholder values with your MySQL credentials.
4. **Run the Application:**
    ```bash
    flask run
5. **Access the Application:** Open your browser and go to http://127.0.0.1:5000 to use the expense tracker. You can see this on your terminal where the flask output is available.

---

## Usage

1. **Log Expenses**: Use the "Add Expense" tab to log your expense.
2. **View Summary**: Use the 
"summary" tab to view your total expense per category.
3. **Delete Entry**: Delete your entry using the "delete" tab

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Acknowledgements

- Thanks to the [flask documentation](https://flask.palletsprojects.com/en/stable/) for the helpful resources.
- Inspiration from various open-source projects.