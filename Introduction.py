# Unit-I Introduction: Concept of Software quality, product and process quality, software quality metrics, quality control and total quality management, quality tools and techniques, quality standards, defect management for quality and improvement.

# Software Quality Assurance and Testing - Unit I Simulation

class SoftwareQuality:
    def __init__(self):
        self.attributes = ["Functionality", "Reliability", "Usability", "Efficiency", "Maintainability", "Portability"]
    
    def evaluate(self):
        print("Evaluating Software Quality Attributes:")
        for attr in self.attributes:
            print(f"✔ {attr}")

class QualityType:
    def __init__(self):
        self.product_quality = "Focuses on correctness, usability, performance of the final product."
        self.process_quality = "Focuses on the efficiency and control of the software development process."

    def compare(self):
        print("\nProduct vs Process Quality:")
        print(f"Product Quality: {self.product_quality}")
        print(f"Process Quality: {self.process_quality}")

class QualityMetrics:
    def __init__(self):
        self.metrics = {
            "LOC": 1000,
            "Function Points": 120,
            "Cyclomatic Complexity": 15,
            "Defect Density": "0.5 defects/KLOC",
            "MTTF": "72 hours",
            "Test Coverage": "85%"
        }

    def report(self):
        print("\nQuality Metrics Report:")
        for metric, value in self.metrics.items():
            print(f"{metric}: {value}")

class QualityManagement:
    def __init__(self):
        self.qc = "Identify and fix product defects (reactive)."
        self.tqm = "Focus on continuous process improvement (proactive)."

    def show(self):
        print("\nQuality Management Techniques:")
        print(f"Quality Control: {self.qc}")
        print(f"Total Quality Management: {self.tqm}")

class QualityTools:
    def __init__(self):
        self.tools = ["Fishbone Diagram", "Check Sheet", "Pareto Chart", "Histogram", "Flowchart", "Scatter Diagram"]
        self.techniques = ["Inspection", "Walkthrough", "Peer Review", "Statistical Process Control"]

    def display(self):
        print("\nQuality Tools and Techniques:")
        print("Tools: ", ", ".join(self.tools))
        print("Techniques: ", ", ".join(self.techniques))

class QualityStandards:
    def __init__(self):
        self.standards = ["ISO 9001", "ISO/IEC 25010", "CMMI", "Six Sigma"]

    def list_standards(self):
        print("\nQuality Standards:")
        for std in self.standards:
            print(f"✔ {std}")

class DefectManagement:
    def __init__(self):
        self.defects = []

    def report_defect(self, desc, severity):
        self.defects.append({"description": desc, "severity": severity})
        print(f"🔧 Defect Logged: {desc} (Severity: {severity})")

    def summary(self):
        print("\nDefect Management Summary:")
        for i, d in enumerate(self.defects, 1):
            print(f"{i}. {d['description']} - Severity: {d['severity']}")
        print(f"Total defects: {len(self.defects)}")

# --- Simulation Starts Here ---

if __name__ == "__main__":
    print("=== SOFTWARE QUALITY ASSURANCE & TESTING SIMULATION ===\n")

    # 1. Quality Attributes
    qa = SoftwareQuality()
    qa.evaluate()

    # 2. Product vs Process Quality
    qt = QualityType()
    qt.compare()

    # 3. Metrics Reporting
    qm = QualityMetrics()
    qm.report()

    # 4. QC and TQM
    management = QualityManagement()
    management.show()

    # 5. Tools and Techniques
    tools = QualityTools()
    tools.display()

    # 6. Standards
    standards = QualityStandards()
    standards.list_standards()

    # 7. Defect Management System
    dm = DefectManagement()
    dm.report_defect("Login button not responding", "High")
    dm.report_defect("Misspelled label on dashboard", "Low")
    dm.report_defect("Crash when uploading file", "Critical")
    dm.summary()
