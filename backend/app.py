from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# MySQL Database Connection (Uses Environment Variables)
db = mysql.connector.connect(
    host=os.getenv("DB_HOST", "mysql"),  # Use "mysql" as the hostname inside Docker
    user=os.getenv("DB_USER", "your_mysql_user"),
    password=os.getenv("DB_PASSWORD", "your_mysql_password"),
    database=os.getenv("DB_NAME", "contact_db")
)

cursor = db.cursor()

@app.route('/contact', methods=['POST'])
def contact():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')

        # Simple validation
        if not name or not email or not phone or not message:
            return jsonify({"error": "All fields are required!"}), 400

        if "@" not in email:
            return jsonify({"error": "Invalid email address!"}), 400

        if len(phone) < 10:
            return jsonify({"error": "Invalid phone number!"}), 400

        # Insert data into MySQL
        sql = "INSERT INTO contacts (name, email, phone, message) VALUES (%s, %s, %s, %s)"
        values = (name, email, phone, message)
        cursor.execute(sql, values)
        db.commit()

        return jsonify({"success": "Contact details submitted successfully!"})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

