"""
CodeCraftHub - Personalized Learning Platform Backend
A simple Flask-based REST API for tracking developer courses

This application provides a complete REST API for managing courses with:
- CRUD operations (Create, Read, Update, Delete)
- JSON file-based data storage
- Input validation
- Error handling
- Auto-generated IDs and timestamps
"""

from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Path to the JSON data file
DATA_FILE = 'data/courses.json'

# Valid status values for courses
VALID_STATUSES = ['Not Started', 'In Progress', 'Completed']

# ========================
# Helper Functions
# ========================

def load_courses():
    """
    Load courses from JSON file.
    
    Returns:
        dict: Dictionary containing 'courses' list
              Returns empty list if file doesn't exist or is corrupted
    """
    if not os.path.exists(DATA_FILE):
        return {"courses": []}
    
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        # If file is corrupted, log error and return empty list
        print(f"Error reading courses file: {e}")
        return {"courses": []}


def save_courses(data):
    """
    Save courses to JSON file.
    
    Args:
        data (dict): Dictionary containing 'courses' list to save
    
    Raises:
        IOError: If file cannot be written
    """
    try:
        # Create data directory if it doesn't exist
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        
        # Write data to file with nice formatting (indent=2)
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    except IOError as e:
        print(f"Error saving courses file: {e}")
        raise


def get_next_course_id():
    """
    Generate the next course ID by finding the max ID and adding 1.
    
    Returns:
        int: Next available course ID
    """
    data = load_courses()
    if not data['courses']:
        return 1
    return max(course['id'] for course in data['courses']) + 1


def get_current_timestamp():
    """
    Get current timestamp in ISO 8601 format.
    
    Returns:
        str: Current timestamp (e.g., "2026-03-17T10:30:45.123456")
    """
    return datetime.now().isoformat()


def validate_course_data(data, is_update=False):
    """
    Validate course data has required fields and correct formats.
    
    Args:
        data (dict): Course data to validate
        is_update (bool): If True, allows partial updates (not all fields required)
    
    Returns:
        tuple: (is_valid: bool, error_message: str or None)
    """
    # For new courses, all fields are required. For updates, fields are optional
    required_fields = ['name', 'description', 'target_date', 'status']
    
    if not is_update:
        # Check for missing required fields on create
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return False, f"Missing required fields: {', '.join(missing_fields)}"
    
    # Validate status if provided
    if 'status' in data:
        if data['status'] not in VALID_STATUSES:
            return False, f"Invalid status. Must be one of: {', '.join(VALID_STATUSES)}"
    
    # Validate date format (YYYY-MM-DD) if provided
    if 'target_date' in data:
        try:
            datetime.strptime(data['target_date'], '%Y-%m-%d')
        except ValueError:
            return False, "Invalid date format. Use YYYY-MM-DD (e.g., 2026-12-31)"
    
    return True, None



# ========================
# REST API ENDPOINTS
# ========================

@app.route('/api/courses', methods=['GET'])
def get_all_courses():
    """
    GET /api/courses
    
    Retrieve all courses in the system.
    
    Returns:
        JSON array of all courses
        HTTP 200: Success
    """
    try:
        data = load_courses()
        return jsonify(data['courses']), 200
    except Exception as e:
        return jsonify({"error": "Failed to retrieve courses", "details": str(e)}), 500


@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    GET /api/courses/<course_id>
    
    Retrieve a specific course by its ID.
    
    Args:
        course_id (int): ID of the course to retrieve
    
    Returns:
        JSON object of the course
        HTTP 200: Course found
        HTTP 404: Course not found
    """
    try:
        data = load_courses()
        course = next((c for c in data['courses'] if c['id'] == course_id), None)
        
        if not course:
            return jsonify({"error": f"Course with ID {course_id} not found"}), 404
        
        return jsonify(course), 200
    except Exception as e:
        return jsonify({"error": "Failed to retrieve course", "details": str(e)}), 500


@app.route('/api/courses', methods=['POST'])
def create_course():
    """
    POST /api/courses
    
    Create a new course.
    
    Request Body (JSON):
    {
        "name": "Course Name",
        "description": "Course Description",
        "target_date": "2026-12-31",
        "status": "Not Started"
    }
    
    Returns:
        JSON object of created course (with auto-generated id and created_at)
        HTTP 201: Course created successfully
        HTTP 400: Bad request (invalid data or missing fields)
        HTTP 500: Server error
    """
    try:
        # Check if request contains JSON
        try:
            json_data = request.get_json(force=True)
        except:
            return jsonify({"error": "Request body must be JSON"}), 400
        
        if not json_data:
            return jsonify({"error": "Request body must be JSON"}), 400
        
        # Validate the incoming data
        is_valid, error_msg = validate_course_data(json_data, is_update=False)
        if not is_valid:
            return jsonify({"error": error_msg}), 400
        
        # Load existing courses
        data = load_courses()
        
        # Create new course object with auto-generated fields
        new_course = {
            "id": get_next_course_id(),
            "name": json_data['name'].strip(),  # Remove extra whitespace
            "description": json_data['description'].strip(),
            "target_date": json_data['target_date'],
            "status": json_data['status'],
            "created_at": get_current_timestamp()  # Auto-generated timestamp
        }
        
        # Add to courses list
        data['courses'].append(new_course)
        
        # Save to file
        save_courses(data)
        
        return jsonify(new_course), 201
    
    except Exception as e:
        return jsonify({"error": "Failed to create course", "details": str(e)}), 500


@app.route('/api/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    """
    PUT /api/courses/<course_id>
    
    Update an existing course.
    
    Args:
        course_id (int): ID of the course to update
    
    Request Body (JSON):
    {
        "name": "Updated Name",  (optional)
        "description": "Updated description",  (optional)
        "target_date": "2026-12-31",  (optional)
        "status": "In Progress"  (optional)
    }
    
    Returns:
        JSON object of updated course
        HTTP 200: Course updated successfully
        HTTP 400: Bad request (invalid data)
        HTTP 404: Course not found
        HTTP 500: Server error
    """
    try:
        # Check if request contains JSON
        try:
            json_data = request.get_json(force=True)
        except:
            return jsonify({"error": "Request body must be JSON"}), 400
        
        if not json_data:
            return jsonify({"error": "Request body must be JSON"}), 400
        
        # Load existing courses
        data = load_courses()
        course = next((c for c in data['courses'] if c['id'] == course_id), None)
        
        if not course:
            return jsonify({"error": f"Course with ID {course_id} not found"}), 404
        
        # Validate the update data (is_update=True allows partial updates)
        is_valid, error_msg = validate_course_data(json_data, is_update=True)
        if not is_valid:
            return jsonify({"error": error_msg}), 400
        
        # Update fields if provided in request
        if 'name' in json_data:
            course['name'] = json_data['name'].strip()
        
        if 'description' in json_data:
            course['description'] = json_data['description'].strip()
        
        if 'target_date' in json_data:
            course['target_date'] = json_data['target_date']
        
        if 'status' in json_data:
            course['status'] = json_data['status']
        
        # Save updated courses
        save_courses(data)
        
        return jsonify(course), 200
    
    except Exception as e:
        return jsonify({"error": "Failed to update course", "details": str(e)}), 500


@app.route('/api/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    """
    DELETE /api/courses/<course_id>
    
    Delete a course by ID.
    
    Args:
        course_id (int): ID of the course to delete
    
    Returns:
        JSON success message
        HTTP 200: Course deleted successfully
        HTTP 404: Course not found
        HTTP 500: Server error
    """
    try:
        data = load_courses()
        original_length = len(data['courses'])
        
        # Filter out the course to delete
        data['courses'] = [c for c in data['courses'] if c['id'] != course_id]
        
        # Check if a course was actually deleted
        if len(data['courses']) == original_length:
            return jsonify({"error": f"Course with ID {course_id} not found"}), 404
        
        # Save updated courses
        save_courses(data)
        
        return jsonify({
            "message": f"Course with ID {course_id} deleted successfully"
        }), 200
    
    except Exception as e:
        return jsonify({"error": "Failed to delete course", "details": str(e)}), 500




# ========================
# FILTER ENDPOINTS
# ========================

@app.route('/api/courses/status/<status>', methods=['GET'])
def get_courses_by_status(status):
    """
    GET /api/courses/status/<status>
    
    Get all courses with a specific status.
    
    Args:
        status (str): One of "Not Started", "In Progress", "Completed"
    
    Returns:
        JSON array of courses with the specified status
        HTTP 200: Success
        HTTP 400: Invalid status value
        HTTP 500: Server error
    """
    try:
        if status not in VALID_STATUSES:
            return jsonify({
                "error": f"Invalid status value",
                "valid_statuses": VALID_STATUSES
            }), 400
        
        data = load_courses()
        filtered_courses = [c for c in data['courses'] if c['status'] == status]
        
        return jsonify(filtered_courses), 200
    except Exception as e:
        return jsonify({"error": "Failed to retrieve courses", "details": str(e)}), 500


# ========================
# HEALTH CHECK ENDPOINT
# ========================

@app.route('/api/health', methods=['GET'])
def health_check():
    """
    GET /api/health
    
    Health check endpoint to verify the API is running.
    
    Returns:
        JSON status message
        HTTP 200: API is running
    """
    return jsonify({
        "status": "API is running",
        "service": "CodeCraftHub",
        "timestamp": get_current_timestamp()
    }), 200


# ========================
# ERROR HANDLING
# ========================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 - Endpoint Not Found errors"""
    return jsonify({
        "error": "Endpoint not found",
        "message": "The requested URL does not exist"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 - Internal Server errors"""
    return jsonify({
        "error": "Internal server error",
        "message": "An unexpected error occurred"
    }), 500


@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 - Method Not Allowed errors"""
    return jsonify({
        "error": "Method not allowed",
        "message": "The HTTP method is not supported for this endpoint"
    }), 405


# ========================
# APPLICATION ENTRY POINT
# ========================

if __name__ == '__main__':
    """
    Main entry point for the Flask application.
    
    This section:
    1. Creates the data directory if it doesn't exist
    2. Initializes the courses.json file if needed
    3. Starts the Flask development server
    """
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Initialize courses.json with empty data if it doesn't exist
    if not os.path.exists(DATA_FILE):
        initial_data = {"courses": []}
        save_courses(initial_data)
        print(f"✅ Created {DATA_FILE} with initial data")
    else:
        print(f"📂 Using existing {DATA_FILE}")
    
    # Print startup information
    print("\n" + "="*60)
    print("🚀 CodeCraftHub API Server Starting...")
    print("="*60)
    print(f"📍 Base URL: http://localhost:5001")
    print(f"💾 Data File: {DATA_FILE}")
    print(f"📚 API Documentation: See README.md for all endpoints")
    print(f"🏥 Health Check: http://localhost:5001/api/health")
    print("="*60 + "\n")
    
    # Run the Flask app in debug mode (good for development)
    # In production, use a production WSGI server like Gunicorn
    app.run(debug=True, host='localhost', port=5001)
