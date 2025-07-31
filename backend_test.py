#!/usr/bin/env python3
"""
Comprehensive Backend API Test Suite for Pedro Gomes Portfolio
Tests all endpoints systematically and validates data integrity
"""

import requests
import json
import sys
import os
from datetime import datetime

# Get backend URL from frontend .env file
def get_backend_url():
    try:
        with open('/app/frontend/.env', 'r') as f:
            for line in f:
                if line.startswith('REACT_APP_BACKEND_URL='):
                    return line.split('=', 1)[1].strip()
    except FileNotFoundError:
        print("❌ Frontend .env file not found")
        return None
    return None

# Test configuration
BACKEND_URL = get_backend_url()
if not BACKEND_URL:
    print("❌ Could not determine backend URL")
    sys.exit(1)

API_BASE_URL = f"{BACKEND_URL}/api"
print(f"🔗 Testing API at: {API_BASE_URL}")

class PortfolioAPITester:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.test_results = []
        self.failed_tests = []
        
    def log_test(self, test_name, success, details="", response_data=None):
        """Log test results"""
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}")
        if details:
            print(f"   {details}")
        if not success:
            self.failed_tests.append(test_name)
        self.test_results.append({
            "test": test_name,
            "success": success,
            "details": details,
            "response_data": response_data
        })
    
    def test_health_check(self):
        """Test health check endpoint"""
        print("\n🏥 Testing Health Check...")
        try:
            response = self.session.get(f"{self.base_url}/health", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "healthy" and data.get("database") == "connected":
                    self.log_test("Health Check", True, "API is healthy and database connected")
                    return True
                else:
                    self.log_test("Health Check", False, f"Unhealthy response: {data}")
                    return False
            else:
                self.log_test("Health Check", False, f"HTTP {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test("Health Check", False, f"Connection error: {str(e)}")
            return False
    
    def test_personal_info(self):
        """Test personal info endpoint"""
        print("\n👤 Testing Personal Info...")
        try:
            response = self.session.get(f"{self.base_url}/personal-info", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                # Validate required fields
                required_fields = ["name", "title", "subtitle", "description", "location", "status", "contact"]
                missing_fields = [field for field in required_fields if field not in data]
                
                if missing_fields:
                    self.log_test("Personal Info Structure", False, f"Missing fields: {missing_fields}")
                    return False
                
                # Validate multilingual fields
                multilingual_fields = ["title", "subtitle", "description", "status"]
                for field in multilingual_fields:
                    if not isinstance(data[field], dict) or "pt" not in data[field] or "en" not in data[field]:
                        self.log_test("Personal Info Multilingual", False, f"Invalid multilingual field: {field}")
                        return False
                
                # Validate specific content
                if data["name"] == "Pedro Gomes":
                    self.log_test("Personal Info Name", True, "Name is correct")
                else:
                    self.log_test("Personal Info Name", False, f"Expected 'Pedro Gomes', got '{data['name']}'")
                
                # Check title content
                title_pt = data["title"].get("pt", "")
                title_en = data["title"].get("en", "")
                if "Desenvolvedor" in title_pt and "Developer" in title_en:
                    self.log_test("Personal Info Title", True, "Titles are appropriate")
                else:
                    self.log_test("Personal Info Title", False, f"Unexpected titles: PT='{title_pt}', EN='{title_en}'")
                
                # Validate contact info
                contact = data.get("contact", {})
                if "email" in contact and "linkedin" in contact and "github" in contact:
                    self.log_test("Personal Info Contact", True, "Contact info complete")
                else:
                    self.log_test("Personal Info Contact", False, "Missing contact fields")
                
                self.log_test("Personal Info Endpoint", True, "All validations passed")
                return True
                
            elif response.status_code == 404:
                self.log_test("Personal Info Endpoint", False, "Personal info not found in database")
                return False
            else:
                self.log_test("Personal Info Endpoint", False, f"HTTP {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test("Personal Info Endpoint", False, f"Error: {str(e)}")
            return False
    
    def test_skills(self):
        """Test skills endpoint"""
        print("\n🛠️ Testing Skills...")
        try:
            response = self.session.get(f"{self.base_url}/skills", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if not isinstance(data, list):
                    self.log_test("Skills Format", False, "Response is not a list")
                    return False
                
                if len(data) == 0:
                    self.log_test("Skills Data", False, "No skills found")
                    return False
                
                # Validate skill structure
                for skill in data:
                    required_fields = ["category", "technologies", "order", "is_active"]
                    missing_fields = [field for field in required_fields if field not in skill]
                    
                    if missing_fields:
                        self.log_test("Skills Structure", False, f"Missing fields in skill: {missing_fields}")
                        return False
                    
                    # Validate multilingual category
                    category = skill.get("category", {})
                    if not isinstance(category, dict) or "pt" not in category or "en" not in category:
                        self.log_test("Skills Multilingual", False, "Invalid category multilingual structure")
                        return False
                    
                    # Validate technologies is a list
                    if not isinstance(skill.get("technologies", []), list):
                        self.log_test("Skills Technologies", False, "Technologies should be a list")
                        return False
                
                # Check for expected categories
                categories = [skill["category"]["en"].lower() for skill in data]
                expected_categories = ["backend", "frontend", "tools", "soft skills"]
                found_categories = []
                
                for expected in expected_categories:
                    for category in categories:
                        if expected in category.lower():
                            found_categories.append(expected)
                            break
                
                if len(found_categories) >= 2:  # At least 2 categories should be present
                    self.log_test("Skills Categories", True, f"Found categories: {found_categories}")
                else:
                    self.log_test("Skills Categories", False, f"Expected more categories, found: {found_categories}")
                
                # Check ordering
                orders = [skill.get("order", 0) for skill in data]
                if orders == sorted(orders):
                    self.log_test("Skills Ordering", True, "Skills are properly ordered")
                else:
                    self.log_test("Skills Ordering", False, "Skills are not properly ordered")
                
                self.log_test("Skills Endpoint", True, f"Found {len(data)} skills")
                return True
                
            else:
                self.log_test("Skills Endpoint", False, f"HTTP {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test("Skills Endpoint", False, f"Error: {str(e)}")
            return False
    
    def test_education(self):
        """Test education endpoint"""
        print("\n🎓 Testing Education...")
        try:
            response = self.session.get(f"{self.base_url}/education", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if not isinstance(data, list):
                    self.log_test("Education Format", False, "Response is not a list")
                    return False
                
                if len(data) == 0:
                    self.log_test("Education Data", False, "No education records found")
                    return False
                
                # Validate education structure
                for edu in data:
                    required_fields = ["institution", "degree", "period", "status", "order", "is_active"]
                    missing_fields = [field for field in required_fields if field not in edu]
                    
                    if missing_fields:
                        self.log_test("Education Structure", False, f"Missing fields: {missing_fields}")
                        return False
                    
                    # Validate multilingual fields
                    multilingual_fields = ["degree", "status"]
                    for field in multilingual_fields:
                        field_data = edu.get(field, {})
                        if not isinstance(field_data, dict) or "pt" not in field_data or "en" not in field_data:
                            self.log_test("Education Multilingual", False, f"Invalid multilingual field: {field}")
                            return False
                
                # Check for expected institutions
                institutions = [edu["institution"] for edu in data]
                if any("Anhaguera" in inst for inst in institutions):
                    self.log_test("Education Institution", True, "Found Universidade Anhaguera")
                else:
                    self.log_test("Education Institution", False, f"Expected Anhaguera, found: {institutions}")
                
                # Check ordering
                orders = [edu.get("order", 0) for edu in data]
                if orders == sorted(orders):
                    self.log_test("Education Ordering", True, "Education records are properly ordered")
                else:
                    self.log_test("Education Ordering", False, "Education records are not properly ordered")
                
                self.log_test("Education Endpoint", True, f"Found {len(data)} education records")
                return True
                
            else:
                self.log_test("Education Endpoint", False, f"HTTP {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test("Education Endpoint", False, f"Error: {str(e)}")
            return False
    
    def test_projects(self):
        """Test projects endpoints"""
        print("\n🚀 Testing Projects...")
        
        # Test all projects
        try:
            response = self.session.get(f"{self.base_url}/projects", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if not isinstance(data, list):
                    self.log_test("Projects Format", False, "Response is not a list")
                    return False
                
                if len(data) == 0:
                    self.log_test("Projects Data", False, "No projects found")
                    return False
                
                # Validate project structure
                for project in data:
                    required_fields = ["title", "description", "technologies", "status", "featured", "order"]
                    missing_fields = [field for field in required_fields if field not in project]
                    
                    if missing_fields:
                        self.log_test("Projects Structure", False, f"Missing fields: {missing_fields}")
                        return False
                    
                    # Validate multilingual fields
                    multilingual_fields = ["title", "description"]
                    for field in multilingual_fields:
                        field_data = project.get(field, {})
                        if not isinstance(field_data, dict) or "pt" not in field_data or "en" not in field_data:
                            self.log_test("Projects Multilingual", False, f"Invalid multilingual field: {field}")
                            return False
                    
                    # Validate technologies is a list
                    if not isinstance(project.get("technologies", []), list):
                        self.log_test("Projects Technologies", False, "Technologies should be a list")
                        return False
                
                self.log_test("Projects Endpoint", True, f"Found {len(data)} projects")
                
                # Test featured projects
                featured_response = self.session.get(f"{self.base_url}/projects/featured", timeout=10)
                
                if featured_response.status_code == 200:
                    featured_data = featured_response.json()
                    
                    if isinstance(featured_data, list):
                        # All featured projects should have featured=True
                        all_featured = all(project.get("featured", False) for project in featured_data)
                        if all_featured or len(featured_data) == 0:
                            self.log_test("Featured Projects", True, f"Found {len(featured_data)} featured projects")
                        else:
                            self.log_test("Featured Projects", False, "Some featured projects don't have featured=True")
                    else:
                        self.log_test("Featured Projects Format", False, "Featured projects response is not a list")
                else:
                    self.log_test("Featured Projects", False, f"HTTP {featured_response.status_code}")
                
                return True
                
            else:
                self.log_test("Projects Endpoint", False, f"HTTP {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test("Projects Endpoint", False, f"Error: {str(e)}")
            return False
    
    def test_goals(self):
        """Test goals endpoint"""
        print("\n🎯 Testing Goals...")
        try:
            response = self.session.get(f"{self.base_url}/goals", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if not isinstance(data, list):
                    self.log_test("Goals Format", False, "Response is not a list")
                    return False
                
                if len(data) == 0:
                    self.log_test("Goals Data", False, "No goals found")
                    return False
                
                # Validate goal structure
                for goal in data:
                    required_fields = ["goal", "order", "is_active"]
                    missing_fields = [field for field in required_fields if field not in goal]
                    
                    if missing_fields:
                        self.log_test("Goals Structure", False, f"Missing fields: {missing_fields}")
                        return False
                    
                    # Validate multilingual goal field
                    goal_data = goal.get("goal", {})
                    if not isinstance(goal_data, dict) or "pt" not in goal_data or "en" not in goal_data:
                        self.log_test("Goals Multilingual", False, "Invalid goal multilingual structure")
                        return False
                
                # Check for internship-related goals
                goal_texts = []
                for goal in data:
                    goal_texts.extend([goal["goal"]["pt"].lower(), goal["goal"]["en"].lower()])
                
                has_internship_goal = any("estágio" in text or "internship" in text for text in goal_texts)
                if has_internship_goal:
                    self.log_test("Goals Content", True, "Found internship-related goal")
                else:
                    self.log_test("Goals Content", False, "No internship-related goal found")
                
                # Check ordering
                orders = [goal.get("order", 0) for goal in data]
                if orders == sorted(orders):
                    self.log_test("Goals Ordering", True, "Goals are properly ordered")
                else:
                    self.log_test("Goals Ordering", False, "Goals are not properly ordered")
                
                self.log_test("Goals Endpoint", True, f"Found {len(data)} goals")
                return True
                
            else:
                self.log_test("Goals Endpoint", False, f"HTTP {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test("Goals Endpoint", False, f"Error: {str(e)}")
            return False
    
    def test_current_learning(self):
        """Test current learning endpoint"""
        print("\n📚 Testing Current Learning...")
        try:
            response = self.session.get(f"{self.base_url}/current-learning", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if not isinstance(data, list):
                    self.log_test("Current Learning Format", False, "Response is not a list")
                    return False
                
                if len(data) == 0:
                    self.log_test("Current Learning Data", False, "No learning items found")
                    return False
                
                # Validate learning item structure
                for item in data:
                    required_fields = ["item", "order", "is_active"]
                    missing_fields = [field for field in required_fields if field not in item]
                    
                    if missing_fields:
                        self.log_test("Current Learning Structure", False, f"Missing fields: {missing_fields}")
                        return False
                    
                    # Validate multilingual item field
                    item_data = item.get("item", {})
                    if not isinstance(item_data, dict) or "pt" not in item_data or "en" not in item_data:
                        self.log_test("Current Learning Multilingual", False, "Invalid item multilingual structure")
                        return False
                
                # Check ordering
                orders = [item.get("order", 0) for item in data]
                if orders == sorted(orders):
                    self.log_test("Current Learning Ordering", True, "Learning items are properly ordered")
                else:
                    self.log_test("Current Learning Ordering", False, "Learning items are not properly ordered")
                
                self.log_test("Current Learning Endpoint", True, f"Found {len(data)} learning items")
                return True
                
            else:
                self.log_test("Current Learning Endpoint", False, f"HTTP {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test("Current Learning Endpoint", False, f"Error: {str(e)}")
            return False
    
    def test_portfolio_aggregate(self):
        """Test portfolio aggregate endpoint"""
        print("\n📋 Testing Portfolio Aggregate...")
        try:
            response = self.session.get(f"{self.base_url}/portfolio", timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                
                # Validate response structure
                if not isinstance(data, dict) or "success" not in data or "data" not in data:
                    self.log_test("Portfolio Aggregate Structure", False, "Invalid response structure")
                    return False
                
                if not data.get("success"):
                    self.log_test("Portfolio Aggregate Success", False, "Success flag is false")
                    return False
                
                portfolio_data = data.get("data", {})
                
                # Validate all sections are present
                required_sections = ["personal_info", "skills", "education", "projects", "goals", "current_learning"]
                missing_sections = [section for section in required_sections if section not in portfolio_data]
                
                if missing_sections:
                    self.log_test("Portfolio Aggregate Sections", False, f"Missing sections: {missing_sections}")
                    return False
                
                # Validate each section is the correct type
                list_sections = ["skills", "education", "projects", "goals", "current_learning"]
                for section in list_sections:
                    if not isinstance(portfolio_data[section], list):
                        self.log_test("Portfolio Aggregate Types", False, f"{section} should be a list")
                        return False
                
                if not isinstance(portfolio_data["personal_info"], dict):
                    self.log_test("Portfolio Aggregate Types", False, "personal_info should be a dict")
                    return False
                
                # Validate data integrity
                personal_info = portfolio_data["personal_info"]
                if personal_info.get("name") == "Pedro Gomes":
                    self.log_test("Portfolio Aggregate Data", True, "Personal info data is correct")
                else:
                    self.log_test("Portfolio Aggregate Data", False, "Personal info data is incorrect")
                
                # Count total items
                total_items = sum(len(portfolio_data[section]) for section in list_sections)
                self.log_test("Portfolio Aggregate Endpoint", True, f"Aggregate data complete with {total_items} total items")
                return True
                
            else:
                self.log_test("Portfolio Aggregate Endpoint", False, f"HTTP {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test("Portfolio Aggregate Endpoint", False, f"Error: {str(e)}")
            return False
    
    def test_error_handling(self):
        """Test error handling for invalid routes"""
        print("\n🚫 Testing Error Handling...")
        try:
            # Test invalid route
            response = self.session.get(f"{self.base_url}/invalid-route", timeout=10)
            
            if response.status_code == 404:
                self.log_test("Error Handling 404", True, "Invalid routes return 404")
            else:
                self.log_test("Error Handling 404", False, f"Expected 404, got {response.status_code}")
            
            return True
                
        except Exception as e:
            self.log_test("Error Handling", False, f"Error: {str(e)}")
            return False
    
    def run_all_tests(self):
        """Run all tests in sequence"""
        print("🧪 Starting Pedro Gomes Portfolio Backend API Tests")
        print("=" * 60)
        
        # Test in logical order
        tests = [
            self.test_health_check,
            self.test_personal_info,
            self.test_skills,
            self.test_education,
            self.test_projects,
            self.test_goals,
            self.test_current_learning,
            self.test_portfolio_aggregate,
            self.test_error_handling
        ]
        
        passed = 0
        total = len(tests)
        
        for test in tests:
            if test():
                passed += 1
        
        # Print summary
        print("\n" + "=" * 60)
        print("📊 TEST SUMMARY")
        print("=" * 60)
        print(f"✅ Passed: {passed}/{total}")
        print(f"❌ Failed: {total - passed}/{total}")
        
        if self.failed_tests:
            print(f"\n❌ Failed Tests:")
            for test in self.failed_tests:
                print(f"   - {test}")
        
        if passed == total:
            print("\n🎉 ALL TESTS PASSED! Backend API is working correctly.")
            return True
        else:
            print(f"\n⚠️  {total - passed} tests failed. Please check the issues above.")
            return False

def main():
    """Main test execution"""
    print("🚀 Pedro Gomes Portfolio Backend API Test Suite")
    print(f"📅 Test run: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    tester = PortfolioAPITester(API_BASE_URL)
    success = tester.run_all_tests()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()