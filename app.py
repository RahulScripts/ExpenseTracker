from flask import Flask, render_template, request, redirect, url_for, flash
from db_utils import add_expense_to_db, get_summary_by_category, delete_entry_from_db
import datetime as dt

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        category = request.form['category']
        amount = float(request.form['amount'])
        date_str = request.form['date']

        try:
            date = dt.datetime.strptime(date_str, "%Y-%m-%d").date()
            error = add_expense_to_db(category, amount, date)
            if error:
                flash(f"Error: {error}", 'danger')
            else:
                flash("Expense added successfully!", 'success')
            return redirect(url_for('add_expense'))
        except ValueError as ve:
            flash(f"Invalid input: {ve}", 'danger')
    
    return render_template('add_expense.html')

@app.route('/summary')
def view_summary():
    summary_data = get_summary_by_category()
    print(summary_data)
    if isinstance(summary_data, str):
        flash(f"Error: {summary_data}", 'danger')
    return render_template('view_summary.html',summary=summary_data)

@app.route('/delete', methods=['GET', 'POST'])
def delete_entry():
    if request.method == 'POST':
        category = request.form['category']
        amount = float(request.form['amount'])
        error = delete_entry_from_db(category, amount)
        if error:
            flash(f"Error: {error}", 'danger')
        else:
            flash("Entry deleted successfully!", 'success')
        return redirect(url_for('delete_entry'))
    return render_template('delete_entry.html')

if __name__ == '__main__':
    app.run(debug=True)
