# 📚 CodeCraftHub - Personalized Learning Platform

> **A beginner-friendly REST API for tracking developer courses and learning progress**

Welcome to CodeCraftHub! This project is a complete learning platform backend built with Python Flask. It's designed to teach you REST API fundamentals while building something practical and useful.

---

## 🎯 What is CodeCraftHub?

CodeCraftHub is a REST API that helps developers track courses they want to learn. You can:
- ➕ **Add new courses** you want to complete
- 📖 **View all your courses** with their details
- ✏️ **Update course progress** (mark as In Progress or Completed)
- 🗑️ **Delete courses** you no longer need
- 🔍 **Filter courses** by their current status

Think of it as a "course to-do list" for developers, but accessed through a REST API instead of a web interface.

---

## ✨ Key Features

✅ **Simple REST API** - Learn REST fundamentals with clear, understandable endpoints
✅ **No Database Required** - Uses JSON file storage for simplicity
✅ **Full CRUD Operations** - Create, Read, Update, Delete courses
✅ **Input Validation** - Validates course data automatically
✅ **Comprehensive Error Handling** - Clear error messages when something goes wrong
✅ **Auto-Generated IDs** - Course IDs start from 1 and increment automatically
✅ **Timestamps** - Track when each course was created
✅ **Beginner-Friendly Code** - Well-commented for learning
✅ **Multiple Testing Options** - Manual curl, automated tests, and Postman

---

## 📁 Project Structure Explained

Here's what each file and folder does:

```
CodeCraftHub/
│
├── app.py                              # Main Flask application (the heart of the API)
│   ├── Helper functions (load/save data)
│   ├── REST API endpoint definitions
│   ├── Error handling
│   └── Server startup code
│
├── requirements.txt                    # Python packages to install
│   └── Flask, Werkzeug
│
├── data/
│   └── courses.json                   # JSON file storing course data
│
├── README.md                          # This file (project documentation)
├── API_TESTS.md                       # Manual testing guide with curl examples
├── TESTING_GUIDE.md                   # Overview of testing options
├── run_tests.sh                       # Automated test script
├── CodeCraftHub_API.postman_collection.json  # Postman collection
└── .gitignore                         # Git ignore patterns
```

### Key Files Explained

**app.py** - This is the Flask application. It contains:
- `load_courses()` - Reads courses from JSON file
- `save_courses()` - Saves courses to JSON file
- `validate_course_data()` - Checks if course data is valid
- API endpoints like `GET /api/courses`, `POST /api/courses`, etc.

**data/courses.json** - This is where course data is stored. Example:
```json
{
  "courses": [
    {
      "id": 1,
      "name": "Python Basics",
      "description": "Learn Python fundamentals",
      "target_date": "2026-04-30",
      "status": "In Progress",
      "created_at": "2026-03-17T10:00:00.000000"
    }
  ]
}
```

---

## 🔧 Installation (Step-by-Step)

### Prerequisites

Before you start, make sure you have:
- **Python 3.7+** installed ([Download here](https://www.python.org/downloads/))
- **Terminal/Command Prompt** (bash on macOS/Linux, PowerShell on Windows)
- **Git** installed (optional, for cloning the project)

### Step 1: Navigate to the Project Directory

```bash
cd /Users/jksn/CodeCraftHub
```

Or if you're starting from scratch:
```bash
# Clone the project (if using Git)
git clone <repository-url>
cd CodeCraftHub
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

A virtual environment keeps your project dependencies separate from your system Python.

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` at the beginning of your terminal prompt when activated.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs Flask (2.3.3) and Werkzeug (2.3.7).

**What gets installed:**
- **Flask** - Web framework for building the API
- **Werkzeug** - Utilities that Flask uses internally

### Step 4: Verify Installation

Check that everything is installed correctly:

```bash
python -c "import flask; print(f'Flask {flask.__version__} installed successfully!')"
```

You should see: `Flask 2.3.3 installed successfully!`

---

## 🚀 Running the Application

### Start the Server

```bash
python app.py
```

### Expected Output

```
============================================================
🚀 CodeCraftHub API Server Starting...
============================================================
📍 Base URL: http://localhost:5001
💾 Data File: data/courses.json
📚 API Documentation: See README.md for all endpoints
🏥 Health Check: http://localhost:5001/api/health
============================================================

 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://localhost:5001
```

### ✅ Server is Running!

Your API is now live at `http://localhost:5001`

**Keep this terminal open** - the server needs to run for the API to work.

---

## 🧪 Testing the API

Open a **new terminal** (keep the Flask server running in the first one).

### Quick Health Check

Test if the server is responding:

```bash
curl http://localhost:5001/api/health
```

**You should see:**
```json
{
  "status": "API is running",
  "service": "CodeCraftHub",
  "timestamp": "2026-03-17T14:30:45.123456"
}
```

If you see this, congratulations! Your API is working! 🎉

---

## 📚 Complete API Documentation

### What is a REST API?

REST (Representational State Transfer) is an architectural style for building web APIs. Each endpoint represents a resource:
- `GET /api/courses` - Get resource (courses)
- `POST /api/courses` - Create resource
- `PUT /api/courses/1` - Update resource
- `DELETE /api/courses/1` - Delete resource

### API Endpoints

#### 1️⃣ Health Check (Ping the Server)

**Check if the API is running and healthy**

```bash
curl http://localhost:5001/api/health
```

**Response (200 OK):**
```json
{
  "status": "API is running",
  "service": "CodeCraftHub",
  "timestamp": "2026-03-17T14:30:45.123456"
}
```

---

#### 2️⃣ Get All Courses

**Retrieve all courses in your learning list**

```bash
curl http://localhost:5001/api/courses
```

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Python Basics",
    "description": "Learn fundamental Python programming concepts",
    "target_date": "2026-04-30",
    "status": "In Progress",
    "created_at": "2026-03-17T10:00:00.000000"
  },
  {
    "id": 2,
    "name": "REST APIs with Flask",
    "description": "Master building RESTful APIs using Flask framework",
    "target_date": "2026-05-31",
    "status": "Not Started",
    "created_at": "2026-03-17T10:05:00.000000"
  }
]
```

---

#### 3️⃣ Get a Specific Course

**Retrieve details about one course**

```bash
curl http://localhost:5001/api/courses/1
```

**Replace `1` with any course ID**

**Response (200 OK):**
```json
{
  "id": 1,
  "name": "Python Basics",
  "description": "Learn fundamental Python programming concepts",
  "target_date": "2026-04-30",
  "status": "In Progress",
  "created_at": "2026-03-17T10:00:00.000000"
}
```

**If course doesn't exist (404 Not Found):**
```json
{
  "error": "Course with ID 999 not found"
}
```

---

#### 4️⃣ Create a New Course

**Add a new course to learn**

```bash
curl -X POST http://localhost:5001/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "JavaScript Fundamentals",
    "description": "Learn JavaScript basics and DOM manipulation",
    "target_date": "2026-06-30",
    "status": "Not Started"
  }'
```

**What each field means:**
- `name` (required) - Course title
- `description` (required) - What you'll learn
- `target_date` (required) - When you want to finish (YYYY-MM-DD format)
- `status` (required) - One of: `"Not Started"`, `"In Progress"`, `"Completed"`

**Response (201 Created):**
```json
{
  "id": 4,
  "name": "JavaScript Fundamentals",
  "description": "Learn JavaScript basics and DOM manipulation",
  "target_date": "2026-06-30",
  "status": "Not Started",
  "created_at": "2026-03-17T15:30:22.456789"
}
```

**Response if missing required field (400 Bad Request):**
```json
{
  "error": "Missing required fields: description"
}
```

---

#### 5️⃣ Update a Course

**Modify an existing course (status, date, description, etc.)**

Update just the status:
```bash
curl -X PUT http://localhost:5001/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "Completed"
  }'
```

Update multiple fields:
```bash
curl -X PUT http://localhost:5001/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "In Progress",
    "target_date": "2026-05-15",
    "description": "Updated course description"
  }'
```

**Response (200 OK):**
```json
{
  "id": 1,
  "name": "Python Basics",
  "description": "Updated course description",
  "target_date": "2026-05-15",
  "status": "In Progress",
  "created_at": "2026-03-17T10:00:00.000000"
}
```

---

#### 6️⃣ Delete a Course

**Remove a course from your list**

```bash
curl -X DELETE http://localhost:5001/api/courses/1
```

**Response (200 OK):**
```json
{
  "message": "Course with ID 1 deleted successfully"
}
```

**If course doesn't exist (404 Not Found):**
```json
{
  "error": "Course with ID 999 not found"
}
```

---

#### 7️⃣ Filter Courses by Status

**Get only courses with a specific status**

Get all "In Progress" courses:
```bash
curl "http://localhost:5001/api/courses/status/In%20Progress"
```

Get all "Not Started" courses:
```bash
curl "http://localhost:5001/api/courses/status/Not%20Started"
```

Get all "Completed" courses:
```bash
curl "http://localhost:5001/api/courses/status/Completed"
```

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Python Basics",
    "description": "Learn fundamental Python programming concepts",
    "target_date": "2026-04-30",
    "status": "In Progress",
    "created_at": "2026-03-17T10:00:00.000000"
  }
]
```

---

## 🧪 Testing the API

### Option 1: Manual Testing with curl (Recommended for Learning)

See [API_TESTS.md](API_TESTS.md) for comprehensive curl examples:
- Copy-paste commands for every endpoint
- Example JSON payloads
- Expected responses
- Error test cases

### Option 2: Automated Testing

Run all tests automatically:
```bash
bash run_tests.sh
```

This tests:
- ✅ All endpoints (GET, POST, PUT, DELETE)
- ✅ Success scenarios
- ✅ Error scenarios (missing fields, invalid data)
- ✅ Shows pass/fail summary

### Option 3: Postman GUI Testing

For visual, point-and-click testing:
1. [Download Postman](https://www.postman.com/downloads/)
2. Open Postman
3. Click **Import** → Select `CodeCraftHub_API.postman_collection.json`
4. All endpoints ready to test!

### Option 4: Complete Testing Guide

See [TESTING_GUIDE.md](TESTING_GUIDE.md) for overview and comparison of all testing methods.

---

## 🚨 Troubleshooting Common Issues

### ❌ Problem: "python: command not found"

**Cause:** Python is not installed or not in your PATH

**Solution:**
1. [Download Python](https://www.python.org/downloads/)
2. During installation, check "Add Python to PATH"
3. Restart your terminal
4. Try `python --version`

---

### ❌ Problem: "No module named 'flask'"

**Cause:** Flask is not installed

**Solution:**
```bash
pip install -r requirements.txt
```

Or install Flask directly:
```bash
pip install Flask==2.3.3
```

---

### ❌ Problem: "Connection refused" when testing

**Cause:** Flask server is not running

**Solution:**
1. Open a terminal
2. Make sure you're in the project directory
3. Run: `python app.py`
4. Keep this terminal open
5. Open a **new terminal** to run tests

---

### ❌ Problem: "Address already in use" error

**Cause:** Port 5000 is already being used by another application

**Solution (Option 1):** Kill the existing process
```bash
lsof -i :5001  # See what's using port 5000
kill -9 <PID>  # Replace <PID> with the number shown
```

**Solution (Option 2):** Use a different port
Edit `app.py` and change the last line:
```python
app.run(debug=True, host='localhost', port=5001)  # Use 5001 instead
```

---

### ❌ Problem: "Request body must be JSON" error

**Cause:** Missing Content-Type header in POST/PUT requests

**Solution:** Always include the header:
```bash
curl -X POST http://localhost:5001/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"Course","description":"Desc","target_date":"2026-12-31","status":"Not Started"}'
```

---

### ❌ Problem: "Invalid date format" error

**Cause:** Date is not in YYYY-MM-DD format

**Solution:** Use correct format:
```bash
# ❌ Wrong
"target_date": "12/31/2026"

# ✅ Correct
"target_date": "2026-12-31"
```

---

### ❌ Problem: "Invalid status" error

**Cause:** Status is not one of the three valid options

**Solution:** Use only these values:
```
"status": "Not Started"
"status": "In Progress"
"status": "Completed"
```

---

### ❌ Problem: JSON file permission error

**Cause:** Cannot write to `data/courses.json`

**Solution:**
```bash
# Fix file permissions
chmod 644 data/courses.json

# Or recreate the file
rm data/courses.json
python app.py  # This will create a new one
```

---

## 📊 Course Data Model

Every course has these fields:

| Field | Type | Example | Description |
|-------|------|---------|-------------|
| id | integer | 1 | Unique identifier (auto-generated) |
| name | string | "Python Basics" | Course title |
| description | string | "Learn Python fundamentals" | Course details |
| target_date | string | "2026-12-31" | Goal completion date (YYYY-MM-DD) |
| status | string | "In Progress" | One of: Not Started, In Progress, Completed |
| created_at | string | "2026-03-17T10:00:00" | When course was added (auto-generated) |

---

## 🔄 Complete Example Workflow

Here's a complete workflow showing how to use the API:

```bash
# 1. Check if API is running
curl http://localhost:5001/api/health

# 2. Get all courses
curl http://localhost:5001/api/courses

# 3. Create a new course
curl -X POST http://localhost:5001/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "React Advanced",
    "description": "Learn advanced React patterns",
    "target_date": "2026-08-30",
    "status": "Not Started"
  }'
# Response includes: id: 4

# 4. Get the new course
curl http://localhost:5001/api/courses/4

# 5. Update status to "In Progress"
curl -X PUT http://localhost:5001/api/courses/4 \
  -H "Content-Type: application/json" \
  -d '{"status": "In Progress"}'

# 6. Filter to see all "In Progress" courses
curl "http://localhost:5001/api/courses/status/In%20Progress"

# 7. Complete the course
curl -X PUT http://localhost:5001/api/courses/4 \
  -H "Content-Type: application/json" \
  -d '{"status": "Completed"}'

# 8. Delete the course (if you want)
curl -X DELETE http://localhost:5001/api/courses/4

# 9. Verify it's deleted
curl http://localhost:5001/api/courses/4
# Returns 404 Not Found
```

---

## 📖 Learning Concepts

By building and testing this API, you'll learn:

### REST Fundamentals
- ✅ HTTP methods (GET, POST, PUT, DELETE)
- ✅ HTTP status codes (200, 201, 400, 404, etc.)
- ✅ Request and response structure
- ✅ JSON data format

### Python Flask
- ✅ Creating routes with `@app.route()`
- ✅ Handling different HTTP methods
- ✅ Processing JSON in requests
- ✅ Returning JSON responses
- ✅ Error handling

### Programming Concepts
- ✅ Data validation
- ✅ File input/output
- ✅ Date/time handling
- ✅ Error handling and messages
- ✅ Auto-incrementing IDs

### Testing
- ✅ Testing APIs with curl
- ✅ Automated testing scripts
- ✅ Test-driven thinking

---

## 🎯 Real-World Use Cases

After learning this foundation, you can:

1. **Build a Web UI** - Create a website that calls these API endpoints
2. **Add Authentication** - Let users create accounts and see only their courses
3. **Upgrade to Real Database** - Move from JSON to SQLite or PostgreSQL
4. **Add More Features:**
   - Course ratings and reviews
   - Course progress tracking (% completed)
   - Learning resources (links, videos)
   - Course difficulty levels
   - Study schedules and reminders

5. **Deploy to Production** - Deploy to Heroku, AWS, Google Cloud, etc.

---

## 📚 Flask Concepts Reference

### Flask Route Decorator
```python
@app.route('/api/courses', methods=['GET'])
def get_all_courses():
    # This function runs when someone visits /api/courses with GET
    return jsonify(courses_list), 200
```

### HTTP Methods in Flask
```python
@app.route('/api/courses', methods=['POST'])      # Create new
@app.route('/api/courses', methods=['GET'])       # Retrieve
@app.route('/api/courses/<id>', methods=['PUT'])  # Update
@app.route('/api/courses/<id>', methods=['DELETE'])  # Delete
```

### Returning JSON
```python
# Flask converts Python dicts to JSON automatically
return jsonify({"id": 1, "name": "Python"}), 200
```

### HTTP Status Codes
```python
200  # OK - Request succeeded
201  # Created - Resource created successfully
400  # Bad Request - Invalid data
404  # Not Found - Resource doesn't exist
500  # Server Error - Something went wrong on the server
```

---

## 🆘 Need Help?

### Check These Resources

1. **API Testing Examples** - See [API_TESTS.md](API_TESTS.md)
2. **Testing Guide** - See [TESTING_GUIDE.md](TESTING_GUIDE.md)
3. **Flask Documentation** - https://flask.palletsprojects.com/
4. **REST API Best Practices** - https://restfulapi.net/
5. **HTTP Status Codes** - https://httpwg.org/specs/rfc7231.html#status.codes

### Common Questions

**Q: Do I need to install a database?**
A: No! This project uses a JSON file for simplicity. Upgrading to a real database (SQLite, PostgreSQL) is a future enhancement.

**Q: Can I run this on Windows?**
A: Yes! Just use `pip` instead of `pip3` and activate the virtual environment with `venv\Scripts\activate`

**Q: How do I change the port from 5000?**
A: Edit the last line of `app.py` and change `port=5000` to `port=5001` (or any other free port)

**Q: Can I remove the debug mode?**
A: Yes, change `debug=True` to `debug=False` in the last line of `app.py`. This disables auto-reloading and detailed error messages.

**Q: How do I backup my course data?**
A: Just copy the `data/courses.json` file to another location.

**Q: What if I want to delete all courses and start fresh?**
A: Delete the `data/courses.json` file. A new one will be created with empty data when you restart the server.

---

## 🎓 Next Learning Steps

1. **Understand the Code** - Read through `app.py` line by line
2. **Test All Endpoints** - Try every curl command in [API_TESTS.md](API_TESTS.md)
3. **Modify and Experiment** - Change code and see what happens
4. **Add Features** - Try adding new endpoints or fields
5. **Learn Databases** - Upgrade from JSON to SQLite
6. **Build a Frontend** - Create a web interface using HTML/CSS/JavaScript

---

## 📄 License

This is a school project created for learning purposes.

---

## 👨‍💻 What You've Built

Congratulations! You now have a working REST API that demonstrates:
- ✅ How to build REST APIs with Flask
- ✅ How to structure API endpoints
- ✅ How to handle JSON data
- ✅ How to validate user input
- ✅ How to return appropriate HTTP responses
- ✅ How to handle errors gracefully

This is the foundation for building professional web applications! 🚀

**Happy Learning!**
