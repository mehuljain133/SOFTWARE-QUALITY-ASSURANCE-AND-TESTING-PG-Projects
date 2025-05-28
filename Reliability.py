# Unit-IV Reliability: Basic concepts, reliability measurements, predictions and management

import math
import random
import numpy as np

# 1. Basic Concepts of Reliability
class ReliabilityConcepts:
    def show(self):
        print("\n📘 Basic Concepts of Reliability:")
        concepts = {
            "Definition": "Reliability is the probability that software performs its intended functions under specified conditions for a specified time.",
            "Failure": "Deviation of software from expected behavior.",
            "Fault": "A defect in the software code or logic.",
            "Error": "Human action that results in software fault.",
            "MTTF": "Mean Time To Failure - average time to failure of a system.",
            "MTTR": "Mean Time To Repair - average time taken to repair a failure."
        }
        for key, value in concepts.items():
            print(f"{key}: {value}")

# 2. Reliability Measurements
class ReliabilityMetrics:
    def __init__(self, failure_times):
        self.failure_times = failure_times

    def calculate_metrics(self):
        mttf = np.mean(self.failure_times)
        mttr = random.uniform(1.0, 3.0)  # simulate repair time in hours
        availability = mttf / (mttf + mttr)
        failure_rate = 1 / mttf

        print("\n📏 Reliability Measurements:")
        print(f"MTTF (Mean Time To Failure): {mttf:.2f} hrs")
        print(f"MTTR (Mean Time To Repair): {mttr:.2f} hrs")
        print(f"Availability: {availability:.2%}")
        print(f"Failure Rate (λ): {failure_rate:.5f} failures/hr")

# 3. Reliability Prediction
class ReliabilityPrediction:
    def __init__(self, usage_hours, failure_rate):
        self.usage_hours = usage_hours
        self.failure_rate = failure_rate

    def predict_reliability(self):
        reliability = math.exp(-self.failure_rate * self.usage_hours)
        print(f"\n📈 Reliability Prediction:")
        print(f"Predicted Reliability after {self.usage_hours} hrs: {reliability:.4f}")

# 4. Reliability Management
class ReliabilityManagement:
    def show_plan(self):
        print("\n🗂️ Reliability Management Plan:")
        plan = {
            "Goal": "Achieve 99.9% uptime with reduced failure rate.",
            "Approach": [
                "Design for fault tolerance",
                "Code reviews and static analysis",
                "Automated testing and stress tests",
                "Monitor failure logs continuously",
                "Preventive maintenance and patching"
            ],
            "Tools": ["Sentry", "LogRocket", "New Relic", "SonarQube"]
        }
        for key, val in plan.items():
            if isinstance(val, list):
                print(f"{key}:")
                for item in val:
                    print(f" - {item}")
            else:
                print(f"{key}: {val}")

# === MAIN SIMULATION ===
if __name__ == "__main__":
    print("=== UNIT-IV: Reliability Simulation ===")

    # 1. Basic Concepts
    concepts = ReliabilityConcepts()
    concepts.show()

    # 2. Reliability Metrics
    failure_times = [40, 50, 45, 55, 42]  # simulated failures in hours
    metrics = ReliabilityMetrics(failure_times)
    metrics.calculate_metrics()

    # 3. Reliability Prediction
    failure_rate = 1 / np.mean(failure_times)
    prediction = ReliabilityPrediction(usage_hours=100, failure_rate=failure_rate)
    prediction.predict_reliability()

    # 4. Reliability Management
    management = ReliabilityManagement()
    management.show_plan()
