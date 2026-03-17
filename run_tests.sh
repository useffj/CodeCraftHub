#!/bin/bash

##############################################################################
# CodeCraftHub API Test Script
# 
# This script runs automated tests for the CodeCraftHub API
# Make sure the Flask server is running before executing this script
#
# Usage: bash run_tests.sh
##############################################################################

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# API Base URL
API_URL="http://localhost:5001/api"

# Counter for tests
TESTS_PASSED=0
TESTS_FAILED=0

##############################################################################
# Helper Functions
##############################################################################

# Print section header
print_header() {
    echo ""
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}"
}

# Test a GET request
test_get() {
    local test_name=$1
    local endpoint=$2
    local expected_status=$3
    
    echo -ne "${YELLOW}Testing: $test_name${NC}... "
    
    response=$(curl -s -w "\n%{http_code}" -X GET "$API_URL$endpoint")
    http_code=$(echo "$response" | tail -n1)
    body=$(echo "$response" | head -n-1)
    
    if [ "$http_code" == "$expected_status" ]; then
        echo -e "${GREEN}✓ PASSED${NC} (HTTP $http_code)"
        echo "Response: $body"
        ((TESTS_PASSED++))
    else
        echo -e "${RED}✗ FAILED${NC} (Expected $expected_status, got $http_code)"
        echo "Response: $body"
        ((TESTS_FAILED++))
    fi
    echo ""
}

# Test a POST request
test_post() {
    local test_name=$1
    local endpoint=$2
    local json_data=$3
    local expected_status=$4
    
    echo -ne "${YELLOW}Testing: $test_name${NC}... "
    
    response=$(curl -s -w "\n%{http_code}" -X POST "$API_URL$endpoint" \
        -H "Content-Type: application/json" \
        -d "$json_data")
    
    http_code=$(echo "$response" | tail -n1)
    body=$(echo "$response" | head -n-1)
    
    if [ "$http_code" == "$expected_status" ]; then
        echo -e "${GREEN}✓ PASSED${NC} (HTTP $http_code)"
        echo "Response: $body"
        ((TESTS_PASSED++))
    else
        echo -e "${RED}✗ FAILED${NC} (Expected $expected_status, got $http_code)"
        echo "Response: $body"
        ((TESTS_FAILED++))
    fi
    echo ""
}

# Test a PUT request
test_put() {
    local test_name=$1
    local endpoint=$2
    local json_data=$3
    local expected_status=$4
    
    echo -ne "${YELLOW}Testing: $test_name${NC}... "
    
    response=$(curl -s -w "\n%{http_code}" -X PUT "$API_URL$endpoint" \
        -H "Content-Type: application/json" \
        -d "$json_data")
    
    http_code=$(echo "$response" | tail -n1)
    body=$(echo "$response" | head -n-1)
    
    if [ "$http_code" == "$expected_status" ]; then
        echo -e "${GREEN}✓ PASSED${NC} (HTTP $http_code)"
        echo "Response: $body"
        ((TESTS_PASSED++))
    else
        echo -e "${RED}✗ FAILED${NC} (Expected $expected_status, got $http_code)"
        echo "Response: $body"
        ((TESTS_FAILED++))
    fi
    echo ""
}

# Test a DELETE request
test_delete() {
    local test_name=$1
    local endpoint=$2
    local expected_status=$3
    
    echo -ne "${YELLOW}Testing: $test_name${NC}... "
    
    response=$(curl -s -w "\n%{http_code}" -X DELETE "$API_URL$endpoint")
    http_code=$(echo "$response" | tail -n1)
    body=$(echo "$response" | head -n-1)
    
    if [ "$http_code" == "$expected_status" ]; then
        echo -e "${GREEN}✓ PASSED${NC} (HTTP $http_code)"
        echo "Response: $body"
        ((TESTS_PASSED++))
    else
        echo -e "${RED}✗ FAILED${NC} (Expected $expected_status, got $http_code)"
        echo "Response: $body"
        ((TESTS_FAILED++))
    fi
    echo ""
}

##############################################################################
# Main Test Suite
##############################################################################

# Check if server is running
echo -e "${BLUE}Checking if CodeCraftHub API is running...${NC}"
if ! curl -s "$API_URL/health" > /dev/null 2>&1; then
    echo -e "${RED}✗ Error: Cannot connect to API at $API_URL${NC}"
    echo -e "${RED}Make sure Flask server is running: python app.py${NC}"
    exit 1
fi
echo -e "${GREEN}✓ API is running${NC}\n"

# ============================================================================
# HEALTH CHECK TESTS
# ============================================================================

print_header "HEALTH CHECK TESTS"
test_get "Health Check" "/health" "200"

# ============================================================================
# GET TESTS
# ============================================================================

print_header "GET ENDPOINT TESTS"
test_get "Get all courses" "/courses" "200"
test_get "Get course with ID 1" "/courses/1" "200"
test_get "Get non-existent course (999)" "/courses/999" "404"
test_get "Filter by 'In Progress' status" "/courses/status/In%20Progress" "200"
test_get "Filter by invalid status" "/courses/status/InvalidStatus" "400"

# ============================================================================
# POST TESTS - SUCCESS CASES
# ============================================================================

print_header "POST ENDPOINT TESTS - SUCCESS CASES"

test_post "Create course with all valid fields" "/courses" \
    '{"name":"DevOps Fundamentals","description":"Learn Docker and Kubernetes","target_date":"2026-09-30","status":"Not Started"}' \
    "201"

test_post "Create course - In Progress status" "/courses" \
    '{"name":"Advanced Python","description":"Deep dive into Python advanced features","target_date":"2026-08-31","status":"In Progress"}' \
    "201"

test_post "Create course - Completed status" "/courses" \
    '{"name":"Git Basics","description":"Learn version control with Git","target_date":"2026-03-31","status":"Completed"}' \
    "201"

# ============================================================================
# POST TESTS - ERROR CASES
# ============================================================================

print_header "POST ENDPOINT TESTS - ERROR CASES"

test_post "Create course - missing name field" "/courses" \
    '{"description":"Missing name field","target_date":"2026-10-31","status":"Not Started"}' \
    "400"

test_post "Create course - missing description field" "/courses" \
    '{"name":"Missing Description","target_date":"2026-10-31","status":"Not Started"}' \
    "400"

test_post "Create course - missing target_date field" "/courses" \
    '{"name":"Missing Date","description":"No target date","status":"Not Started"}' \
    "400"

test_post "Create course - missing status field" "/courses" \
    '{"name":"Missing Status","description":"No status provided","target_date":"2026-10-31"}' \
    "400"

test_post "Create course - invalid status value" "/courses" \
    '{"name":"Invalid Status","description":"Wrong status value","target_date":"2026-10-31","status":"OnHold"}' \
    "400"

test_post "Create course - invalid date format" "/courses" \
    '{"name":"Invalid Date","description":"Wrong date format","target_date":"31/12/2026","status":"Not Started"}' \
    "400"

test_post "Create course - no JSON body" "/courses" \
    "" \
    "400"

# ============================================================================
# PUT TESTS - SUCCESS CASES
# ============================================================================

print_header "PUT ENDPOINT TESTS - SUCCESS CASES"

test_put "Update course - change status only" "/courses/1" \
    '{"status":"In Progress"}' \
    "200"

test_put "Update course - change name only" "/courses/2" \
    '{"name":"REST APIs with Python"}' \
    "200"

test_put "Update course - change multiple fields" "/courses/1" \
    '{"status":"Completed","target_date":"2026-05-15","description":"Updated description"}' \
    "200"

# ============================================================================
# PUT TESTS - ERROR CASES
# ============================================================================

print_header "PUT ENDPOINT TESTS - ERROR CASES"

test_put "Update course - course not found" "/courses/9999" \
    '{"status":"In Progress"}' \
    "404"

test_put "Update course - invalid status" "/courses/1" \
    '{"status":"Paused"}' \
    "400"

test_put "Update course - invalid date format" "/courses/1" \
    '{"target_date":"2026/12/31"}' \
    "400"

test_put "Update course - no JSON body" "/courses/1" \
    "" \
    "400"

# ============================================================================
# DELETE TESTS
# ============================================================================

print_header "DELETE ENDPOINT TESTS"

# First, create a course to delete
echo -e "${YELLOW}Creating test course for deletion...${NC}"
CREATE_RESPONSE=$(curl -s -X POST "$API_URL/courses" \
    -H "Content-Type: application/json" \
    -d '{"name":"Course to Delete","description":"This will be deleted","target_date":"2026-12-31","status":"Not Started"}')

COURSE_ID=$(echo "$CREATE_RESPONSE" | jq -r '.id // empty')
echo -e "${GREEN}✓ Created course with ID: $COURSE_ID${NC}\n"

# Test delete successful
test_delete "Delete existing course (ID: $COURSE_ID)" "/courses/$COURSE_ID" "200"

# Test delete non-existent
test_delete "Delete non-existent course (999)" "/courses/999" "404"

# Verify deletion
test_get "Verify course was deleted" "/courses/$COURSE_ID" "404"

# ============================================================================
# SUMMARY
# ============================================================================

print_header "TEST SUMMARY"

echo -e "${GREEN}Tests Passed: $TESTS_PASSED${NC}"
echo -e "${RED}Tests Failed: $TESTS_FAILED${NC}"

TOTAL=$((TESTS_PASSED + TESTS_FAILED))
echo -e "${BLUE}Total Tests: $TOTAL${NC}"

if [ $TESTS_FAILED -eq 0 ]; then
    echo -e "\n${GREEN}✓ All tests passed!${NC}"
    exit 0
else
    echo -e "\n${RED}✗ Some tests failed. Check the output above.${NC}"
    exit 1
fi
