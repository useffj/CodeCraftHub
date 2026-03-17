# CodeCraftHub API - Comprehensive Test Cases

This document provides curl commands and test cases for testing all CodeCraftHub API endpoints. Copy and paste the commands directly into your terminal.

**Prerequisites:**
- Flask server running: `python app.py`
- Server should be running on `http://localhost:5001`

---

## 🏥 Health Check

### Test: API Health Check
**Purpose:** Verify the API is running and responding

```bash
curl -X GET http://localhost:5001/api/health
```

**Expected Response (200 OK):**
```json
{
  "status": "API is running",
  "service": "CodeCraftHub",
  "timestamp": "2026-03-17T10:30:45.123456"
}
```

---

## 📚 GET Endpoints

### Test 1: Get All Courses
**Purpose:** Retrieve all courses from the system

```bash
curl -X GET http://localhost:5001/api/courses
```

**Expected Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Python Basics",
    "description": "Learn fundamental Python programming concepts including variables, loops, and functions",
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

### Test 2: Get Specific Course (Existing)
**Purpose:** Retrieve a specific course by ID

**Command for course ID 1:**
```bash
curl -X GET http://localhost:5001/api/courses/1
```

**Expected Response (200 OK):**
```json
{
  "id": 1,
  "name": "Python Basics",
  "description": "Learn fundamental Python programming concepts including variables, loops, and functions",
  "target_date": "2026-04-30",
  "status": "In Progress",
  "created_at": "2026-03-17T10:00:00.000000"
}
```

---

### Test 3: Get Specific Course (Not Found)
**Purpose:** Test error handling when course doesn't exist

**Command for non-existent course ID 999:**
```bash
curl -X GET http://localhost:5001/api/courses/999
```

**Expected Response (404 Not Found):**
```json
{
  "error": "Course with ID 999 not found"
}
```

---

### Test 4: Filter Courses by Status
**Purpose:** Get all courses with a specific status

**Get all "In Progress" courses:**
```bash
curl -X GET "http://localhost:5001/api/courses/status/In%20Progress"
```

**Get all "Not Started" courses:**
```bash
curl -X GET "http://localhost:5001/api/courses/status/Not%20Started"
```

**Get all "Completed" courses:**
```bash
curl -X GET "http://localhost:5001/api/courses/status/Completed"
```

**Expected Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Python Basics",
    "description": "Learn fundamental Python programming concepts including variables, loops, and functions",
    "target_date": "2026-04-30",
    "status": "In Progress",
    "created_at": "2026-03-17T10:00:00.000000"
  }
]
```

---

### Test 5: Filter by Invalid Status
**Purpose:** Test error handling for invalid status values

```bash
curl -X GET "http://localhost:5001/api/courses/status/Invalid%20Status"
```

**Expected Response (400 Bad Request):**
```json
{
  "error": "Invalid status value",
  "valid_statuses": ["Not Started", "In Progress", "Completed"]
}
```

---

## 📝 POST Endpoint (Create Course)

### Test 1: Create Course (Success)
**Purpose:** Create a new course with all required fields

```bash
curl -X POST http://localhost:5001/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Web Development with HTML & CSS",
    "description": "Learn to build responsive web pages with HTML5 and modern CSS",
    "target_date": "2026-07-15",
    "status": "Not Started"
  }'
```

**Expected Response (201 Created):**
```json
{
  "id": 4,
  "name": "Web Development with HTML & CSS",
  "description": "Learn to build responsive web pages with HTML5 and modern CSS",
  "target_date": "2026-07-15",
  "status": "Not Started",
  "created_at": "2026-03-17T14:22:30.452891"
}
```

---

### Test 2: Create Course (Missing Field - name)
**Purpose:** Test validation when required field is missing

```bash
curl -X POST http://localhost:5001/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Some description",
    "target_date": "2026-08-31",
    "status": "Not Started"
  }'
```

**Expected Response (400 Bad Request):**
```json
{
  "error": "Missing required fields: name"
}
```

---

### Test 3: Create Course (Missing Multiple Fields)
**Purpose:** Test validation when multiple required fields are missing

```bash
curl -X POST http://localhost:5001/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "JavaScript Advanced"
  }'
```

**Expected Response (400 Bad Request):**
```json
{
  "error": "Missing required fields: description, target_date, status"
}
```

---

### Test 4: Create Course (Invalid Status)
**Purpose:** Test validation for invalid status value

```bash
curl -X POST http://localhost:5001/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Docker Fundamentals",
    "description": "Learn containerization with Docker",
    "target_date": "2026-09-30",
    "status": "InProgress"
  }'
```

**Expected Response (400 Bad Request):**
```json
{
  "error": "Invalid status. Must be one of: Not Started, In Progress, Completed"
}
```

---

### Test 5: Create Course (Invalid Date Format)
**Purpose:** Test validation for incorrect date format

```bash
curl -X POST http://localhost:5001/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Kubernetes Advanced",
    "description": "Master Kubernetes orchestration",
    "target_date": "31/12/2026",
    "status": "Not Started"
  }'
```

**Expected Response (400 Bad Request):**
```json
{
  "error": "Invalid date format. Use YYYY-MM-DD (e.g., 2026-12-31)"
}
```

---

### Test 6: Create Course (No JSON Body)
**Purpose:** Test error handling when no JSON body is provided

```bash
curl -X POST http://localhost:5001/api/courses \
  -H "Content-Type: application/json"
```

**Expected Response (400 Bad Request):**
```json
{
  "error": "Request body must be JSON"
}
```

---

### Test 7: Create Course (Valid - All Fields)
**Purpose:** Create a course with valid data

```bash
curl -X POST http://localhost:5001/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "TypeScript Essentials",
    "description": "Learn TypeScript for scalable JavaScript applications",
    "target_date": "2026-06-30",
    "status": "In Progress"
  }'
```

**Expected Response (201 Created):**
```json
{
  "id": 5,
  "name": "TypeScript Essentials",
  "description": "Learn TypeScript for scalable JavaScript applications",
  "target_date": "2026-06-30",
  "status": "In Progress",
  "created_at": "2026-03-17T14:25:12.789012"
}
```

---

## ✏️ PUT Endpoint (Update Course)

### Test 1: Update Course (Success - Single Field)
**Purpose:** Update only the status of a course

```bash
curl -X PUT http://localhost:5001/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "Completed"
  }'
```

**Expected Response (200 OK):**
```json
{
  "id": 1,
  "name": "Python Basics",
  "description": "Learn fundamental Python programming concepts including variables, loops, and functions",
  "target_date": "2026-04-30",
  "status": "Completed",
  "created_at": "2026-03-17T10:00:00.000000"
}
```

---

### Test 2: Update Course (Success - Multiple Fields)
**Purpose:** Update multiple fields of a course

```bash
curl -X PUT http://localhost:5001/api/courses/2 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "In Progress",
    "target_date": "2026-06-15",
    "description": "Master building RESTful APIs with Flask framework and testing"
  }'
```

**Expected Response (200 OK):**
```json
{
  "id": 2,
  "name": "REST APIs with Flask",
  "description": "Master building RESTful APIs with Flask framework and testing",
  "target_date": "2026-06-15",
  "status": "In Progress",
  "created_at": "2026-03-17T10:05:00.000000"
}
```

---

### Test 3: Update Course (Course Not Found)
**Purpose:** Test error handling when updating non-existent course

```bash
curl -X PUT http://localhost:5001/api/courses/999 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "In Progress"
  }'
```

**Expected Response (404 Not Found):**
```json
{
  "error": "Course with ID 999 not found"
}
```

---

### Test 4: Update Course (Invalid Status)
**Purpose:** Test validation when updating with invalid status

```bash
curl -X PUT http://localhost:5001/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "OnHold"
  }'
```

**Expected Response (400 Bad Request):**
```json
{
  "error": "Invalid status. Must be one of: Not Started, In Progress, Completed"
}
```

---

### Test 5: Update Course (Invalid Date Format)
**Purpose:** Test validation when updating with invalid date

```bash
curl -X PUT http://localhost:5001/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{
    "target_date": "2026/12/31"
  }'
```

**Expected Response (400 Bad Request):**
```json
{
  "error": "Invalid date format. Use YYYY-MM-DD (e.g., 2026-12-31)"
}
```

---

### Test 6: Update Course (No JSON Body)
**Purpose:** Test error handling when no JSON body is provided

```bash
curl -X PUT http://localhost:5001/api/courses/1 \
  -H "Content-Type: application/json"
```

**Expected Response (400 Bad Request):**
```json
{
  "error": "Request body must be JSON"
}
```

---

### Test 7: Update Course (Change Name Only)
**Purpose:** Update only the course name

```bash
curl -X PUT http://localhost:5001/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Python Programming Masterclass"
  }'
```

**Expected Response (200 OK):**
```json
{
  "id": 1,
  "name": "Python Programming Masterclass",
  "description": "Learn fundamental Python programming concepts including variables, loops, and functions",
  "target_date": "2026-04-30",
  "status": "Completed",
  "created_at": "2026-03-17T10:00:00.000000"
}
```

---

## 🗑️ DELETE Endpoint

### Test 1: Delete Course (Success)
**Purpose:** Delete an existing course

```bash
curl -X DELETE http://localhost:5001/api/courses/3
```

**Expected Response (200 OK):**
```json
{
  "message": "Course with ID 3 deleted successfully"
}
```

---

### Test 2: Delete Course (Not Found)
**Purpose:** Test error handling when deleting non-existent course

```bash
curl -X DELETE http://localhost:5001/api/courses/999
```

**Expected Response (404 Not Found):**
```json
{
  "error": "Course with ID 999 not found"
}
```

---

### Test 3: Verify Course Deleted (GET)
**Purpose:** Confirm the course was actually deleted

```bash
curl -X GET http://localhost:5001/api/courses/3
```

**Expected Response (404 Not Found):**
```json
{
  "error": "Course with ID 3 not found"
}
```

---

## 🧪 Complete Test Workflow

This is a full workflow testing all operations in sequence:

### Step 1: Check Health
```bash
curl -X GET http://localhost:5001/api/health
```

### Step 2: Get All Courses
```bash
curl -X GET http://localhost:5001/api/courses
```

### Step 3: Create New Course
```bash
curl -X POST http://localhost:5001/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "React Fundamentals",
    "description": "Learn React for building interactive UI components",
    "target_date": "2026-08-15",
    "status": "Not Started"
  }'
```

### Step 4: Get the New Course (use ID from response above, e.g., 4)
```bash
curl -X GET http://localhost:5001/api/courses/4
```

### Step 5: Update the Course Status
```bash
curl -X PUT http://localhost:5001/api/courses/4 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "In Progress"
  }'
```

### Step 6: Filter Courses by Status
```bash
curl -X GET "http://localhost:5001/api/courses/status/In%20Progress"
```

### Step 7: Delete the Course
```bash
curl -X DELETE http://localhost:5001/api/courses/4
```

### Step 8: Verify Deletion (should return 404)
```bash
curl -X GET http://localhost:5001/api/courses/4
```

---

## 🔧 Testing Tips for Beginners

### 1. **Pretty Print JSON Responses**
If you have `jq` installed, pipe the response to format it nicely:
```bash
curl -X GET http://localhost:5001/api/courses | jq
```

### 2. **Save Response to File**
```bash
curl -X GET http://localhost:5001/api/courses -o response.json
cat response.json
```

### 3. **View Response Headers**
```bash
curl -i -X GET http://localhost:5001/api/courses
```

### 4. **Verbose Output (shows request and response)**
```bash
curl -v -X GET http://localhost:5001/api/courses
```

### 5. **Check HTTP Status Code Only**
```bash
curl -o /dev/null -s -w "%{http_code}\n" http://localhost:5001/api/courses
```

### 6. **Using Variables in Bash Script**
```bash
# Store course ID in a variable
COURSE_ID=1

# Use it in requests
curl -X GET http://localhost:5001/api/courses/$COURSE_ID
curl -X PUT http://localhost:5001/api/courses/$COURSE_ID \
  -H "Content-Type: application/json" \
  -d '{"status": "Completed"}'
```

---

## 📋 Manual Testing Checklist

Use this checklist to verify all functionality:

### GET Requests
- [ ] GET /api/health returns 200
- [ ] GET /api/courses returns 200 with course list
- [ ] GET /api/courses/1 returns 200 with single course
- [ ] GET /api/courses/999 returns 404
- [ ] GET /api/courses/status/In%20Progress returns 200 with filtered list
- [ ] GET /api/courses/status/Invalid returns 400

### POST Requests
- [ ] POST /api/courses with valid data returns 201
- [ ] POST /api/courses missing name returns 400
- [ ] POST /api/courses with invalid status returns 400
- [ ] POST /api/courses with invalid date returns 400
- [ ] New course appears in GET /api/courses

### PUT Requests
- [ ] PUT /api/courses/1 with valid data returns 200
- [ ] PUT /api/courses/999 returns 404
- [ ] PUT /api/courses/1 with invalid status returns 400
- [ ] PUT /api/courses/1 with invalid date returns 400
- [ ] Changes appear in GET /api/courses/1

### DELETE Requests
- [ ] DELETE /api/courses/1 returns 200
- [ ] DELETE /api/courses/999 returns 404
- [ ] Deleted course doesn't appear in GET /api/courses
- [ ] GET /api/courses/{deleted_id} returns 404

---

## 🐛 Troubleshooting

### Server Won't Start
```bash
# Make sure you're in the correct directory
cd /Users/jksn/CodeCraftHub

# Install Flask if not already installed
pip install -r requirements.txt

# Start the server
python app.py
```

### "Connection refused" Error
- **Problem:** Server is not running
- **Solution:** Start the Flask server with `python app.py`

### "Request body must be JSON"
- **Problem:** Missing or incorrect Content-Type header
- **Solution:** Always include `-H "Content-Type: application/json"` for POST/PUT requests

### Port Already in Use
- **Problem:** Another application is using port 5000
- **Solution:** Kill the process or change the port in app.py

### Invalid JSON in curl Command
- **Problem:** Incorrectly formatted JSON in the -d parameter
- **Solution:** Make sure to use single quotes for the outer string and proper JSON syntax inside

---

## 📚 HTTP Status Codes Reference

| Code | Meaning | Used For |
|------|---------|----------|
| 200 | OK | Successful GET, PUT, DELETE |
| 201 | Created | Successful POST (resource created) |
| 400 | Bad Request | Missing/invalid fields, bad data |
| 404 | Not Found | Course doesn't exist |
| 405 | Method Not Allowed | Wrong HTTP method for endpoint |
| 500 | Internal Server Error | Server error |

---

**Happy Testing! 🎉**
