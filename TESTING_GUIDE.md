# CodeCraftHub - Testing Guide

This guide explains the different testing options available for the CodeCraftHub API.

## 📚 Testing Files Overview

| File | Type | Best For | How to Use |
|------|------|----------|-----------|
| [API_TESTS.md](API_TESTS.md) | Manual curl commands | Learning & understanding | Copy-paste commands into terminal |
| [run_tests.sh](run_tests.sh) | Automated bash script | Quick validation | `bash run_tests.sh` |
| [CodeCraftHub_API.postman_collection.json](CodeCraftHub_API.postman_collection.json) | Postman GUI | Visual testing | Import into Postman app |

---

## 🚀 Quick Start Guide

### Option 1: Manual Testing (Recommended for Beginners)

**Best for:** Learning how the API works, understanding REST concepts

1. Make sure Flask server is running:
   ```bash
   python app.py
   ```

2. Open [API_TESTS.md](API_TESTS.md) in your editor or browser

3. Copy any curl command and paste into your terminal:
   ```bash
   curl http://localhost:5000/api/health
   ```

4. Review the expected response shown in the file

**Advantages:**
- See every HTTP request and response
- Learn REST API concepts hands-on
- Understand curl syntax and JSON payloads
- Easy to debug and understand errors

---

### Option 2: Automated Testing

**Best for:** Quick validation, testing all endpoints at once, CI/CD pipelines

1. Make sure Flask server is running:
   ```bash
   python app.py
   ```

2. In a new terminal, run:
   ```bash
   bash run_tests.sh
   ```

3. Watch the test results appear with color-coded pass/fail indicators

**Output will show:**
- ✓ PASSED tests in green
- ✗ FAILED tests in red
- Summary of total tests passed/failed

**Advantages:**
- Tests all endpoints automatically
- Covers both success and error cases
- Shows pass/fail summary
- Great for verifying your setup works

---

### Option 3: Postman GUI Testing

**Best for:** Visual testing, saving requests for later, team collaboration

1. [Download Postman](https://www.postman.com/downloads/)

2. Launch Postman

3. Click **File** → **Import** → **Upload Files**

4. Select `CodeCraftHub_API.postman_collection.json`

5. Click on any request and click **Send**

**Advantages:**
- Visual interface, no terminal needed
- Save requests for later use
- Beautiful response formatting
- Easy to see request/response details
- Great for sharing with team members

---

## 📋 Test Coverage

### What Gets Tested

✅ **Health Check** - API is running and healthy

✅ **GET Endpoints:**
- Retrieve all courses
- Retrieve single course
- Filter by status
- Error handling (course not found, invalid status)

✅ **POST Endpoints:**
- Create course with valid data
- All error cases (missing fields, invalid data types)
- Test all valid status values

✅ **PUT Endpoints:**
- Update partial fields
- Update multiple fields
- Error handling (not found, invalid data)

✅ **DELETE Endpoints:**
- Delete existing course
- Verify deletion
- Error handling (not found)

---

## 🧪 Step-by-Step Test Workflow

### Test Everything in Order (20 minutes)

1. **Start the server**
   ```bash
   python app.py
   ```

2. **In another terminal, test health check** (1 min)
   ```bash
   curl http://localhost:5000/api/health
   ```

3. **Test GET endpoints** (3 min)
   - Get all courses
   - Get specific course
   - Test error case (non-existent course)

4. **Test POST endpoint** (5 min)
   - Create valid course
   - Test missing fields
   - Test invalid status
   - Test invalid date

5. **Test PUT endpoint** (5 min)
   - Update single field
   - Update multiple fields
   - Test error cases

6. **Test DELETE endpoint** (3 min)
   - Delete course
   - Verify deletion
   - Test deleting non-existent course

7. **Run automated tests** (3 min)
   ```bash
   bash run_tests.sh
   ```

---

## 💡 Testing Tips for Beginners

### Tip 1: Pretty-Print JSON Responses
If you have `jq` installed, make responses more readable:
```bash
curl http://localhost:5000/api/courses | jq
```

### Tip 2: Save Response to File
```bash
curl http://localhost:5000/api/courses > response.json
cat response.json
```

### Tip 3: Test Step by Step
Don't run all tests at once. Test one endpoint at a time to understand how it works.

### Tip 4: Read Error Messages
When a test fails, the error message tells you what went wrong. Read it carefully!

### Tip 5: Use Variables in Bash
```bash
# Define a variable
COURSE_ID=1

# Use it in requests
curl http://localhost:5000/api/courses/$COURSE_ID
```

### Tip 6: Check HTTP Status Codes
```bash
# Show just the status code
curl -o /dev/null -s -w "%{http_code}\n" http://localhost:5000/api/courses
```

---

## 🐛 Troubleshooting

### Problem: "Connection refused"
**Cause:** Flask server is not running
**Solution:** Start with `python app.py`

### Problem: "Request body must be JSON"
**Cause:** Missing or wrong Content-Type header
**Solution:** Add `-H "Content-Type: application/json"` to POST/PUT requests

### Problem: "Invalid JSON in curl command"
**Cause:** Wrong quotes or JSON syntax
**Solution:** Use single quotes for outer string, proper JSON inside:
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"Course","description":"Desc","target_date":"2026-12-31","status":"Not Started"}'
```

### Problem: Port 5000 already in use
**Cause:** Another app is using port 5000
**Solution:** Find and kill the process:
```bash
lsof -i :5000  # See what's using port 5000
kill -9 <PID>  # Kill the process
```

---

## 📚 HTTP Status Codes Reference

When testing, you'll see these status codes:

| Code | What It Means | Example Scenario |
|------|---------------|------------------|
| 200 | Success | Getting or updating a course |
| 201 | Created | Successfully created a new course |
| 400 | Bad Request | Missing required fields or invalid data |
| 404 | Not Found | Course doesn't exist |
| 405 | Method Not Allowed | Wrong HTTP method for endpoint |
| 500 | Server Error | Unexpected server error |

---

## 🎓 What You'll Learn

By testing the API, you'll understand:

- ✅ How REST APIs work
- ✅ HTTP methods (GET, POST, PUT, DELETE)
- ✅ HTTP status codes and error handling
- ✅ JSON request/response format
- ✅ The curl command for making HTTP requests
- ✅ API endpoint design
- ✅ Input validation concepts

---

## ❓ FAQ

**Q: Do I need all three testing options?**
A: No! Pick one that works for you. Beginners often start with manual curl testing.

**Q: Can I run the bash script on Windows?**
A: The bash script works best on macOS/Linux. On Windows, use Postman or Windows Subsystem for Linux (WSL).

**Q: How do I know if my API is working correctly?**
A: Run the automated tests with `bash run_tests.sh`. If all tests pass, your API is working!

**Q: Can I modify the test commands?**
A: Absolutely! That's a great way to learn. Try changing course IDs, statuses, or dates.

**Q: What if I want to test with different data?**
A: Great idea! Copy a test command and modify the JSON data. Test with your own course names and descriptions.

---

**Happy Testing! 🎉** Start with manual testing to understand the API, then try the automated script!
