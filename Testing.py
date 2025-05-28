# Unit-III Testing: Test strategies, test planning, functional testing, stability testing and debugging techniques.

import time
import random

# 1. Test Strategies
class TestStrategies:
    def __init__(self):
        self.strategies = [
            "Black Box Testing",
            "White Box Testing",
            "Grey Box Testing",
            "Regression Testing",
            "Exploratory Testing"
        ]

    def show_strategies(self):
        print("\n🧩 Test Strategies:")
        for s in self.strategies:
            print(f"✔ {s}")

# 2. Test Planning
class TestPlan:
    def __init__(self, project_name, deadline):
        self.project_name = project_name
        self.deadline = deadline
        self.plan = {
            "Scope": "Test all user-facing features and core backend modules",
            "Resources": ["QA Lead", "2 Testers", "1 Automation Engineer"],
            "Tools": ["Selenium", "Postman", "PyTest"],
            "Schedule": "2-week sprint testing cycle"
        }

    def display_plan(self):
        print(f"\n📋 Test Plan for: {self.project_name}")
        print(f"Deadline: {self.deadline}")
        for key, val in self.plan.items():
            print(f"{key}: {val}")

# 3. Functional Testing
class FunctionalTest:
    def __init__(self, test_cases):
        self.test_cases = test_cases

    def run_tests(self):
        print("\n🔍 Running Functional Tests:")
        for case in self.test_cases:
            result = random.choice(["PASS", "FAIL"])
            print(f"Test Case '{case}': {result}")

# 4. Stability Testing
class StabilityTest:
    def __init__(self, runtime_seconds=5):
        self.runtime = runtime_seconds

    def perform(self):
        print(f"\n🔄 Running Stability Test for {self.runtime} seconds...")
        try:
            start = time.time()
            count = 0
            while time.time() - start < self.runtime:
                count += 1
                _ = sum([i ** 0.5 for i in range(1000)])  # Simulate workload
            print(f"✅ Stability Test Passed. Iterations: {count}")
        except Exception as e:
            print(f"❌ Stability Test Failed: {e}")

# 5. Debugging Techniques
class DebuggingTechniques:
    def __init__(self):
        self.techniques = [
            "Print Debugging",
            "Logging",
            "Debugger Tools (e.g., PDB)",
            "Unit Test Isolation",
            "Stack Trace Analysis",
            "Rubber Duck Debugging"
        ]

    def list_techniques(self):
        print("\n🛠️ Debugging Techniques:")
        for t in self.techniques:
            print(f"✔ {t}")

# === MAIN SIMULATION ===
if __name__ == "__main__":
    print("=== UNIT-III: Software Testing Simulation ===")

    # 1. Test Strategies
    strategies = TestStrategies()
    strategies.show_strategies()

    # 2. Test Planning
    test_plan = TestPlan(project_name="E-Learning Platform", deadline="2025-06-15")
    test_plan.display_plan()

    # 3. Functional Testing
    func_test = FunctionalTest([
        "Login with valid credentials",
        "Submit feedback form",
        "Search for course",
        "Add item to cart",
        "Process payment"
    ])
    func_test.run_tests()

    # 4. Stability Testing
    stability = StabilityTest(runtime_seconds=3)
    stability.perform()

    # 5. Debugging Techniques
    debug = DebuggingTechniques()
    debug.list_techniques()
