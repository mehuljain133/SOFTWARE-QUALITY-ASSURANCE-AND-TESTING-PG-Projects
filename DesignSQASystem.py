# Unit-II Designing software quality assurance system: Statistical methods in quality assurance, fundamentals of statistical process control, process capability, Six-sigma quality

import random
import numpy as np

class StatisticalQualityAssurance:
    def __init__(self):
        self.data = [random.gauss(50, 2) for _ in range(30)]  # Simulated process data

    def summary_statistics(self):
        mean = np.mean(self.data)
        std_dev = np.std(self.data)
        print("\n📊 Statistical Summary:")
        print(f"Mean: {mean:.2f}")
        print(f"Standard Deviation: {std_dev:.2f}")
        return mean, std_dev

class StatisticalProcessControl:
    def __init__(self, data):
        self.data = data
        self.mean = np.mean(data)
        self.std_dev = np.std(data)

    def control_limits(self):
        ucl = self.mean + 3 * self.std_dev
        lcl = self.mean - 3 * self.std_dev
        print("\n📉 Statistical Process Control Limits:")
        print(f"UCL (Upper Control Limit): {ucl:.2f}")
        print(f"LCL (Lower Control Limit): {lcl:.2f}")
        return ucl, lcl

    def is_in_control(self):
        print("\n🔎 Checking if process is under control...")
        for i, point in enumerate(self.data):
            if point < self.mean - 3*self.std_dev or point > self.mean + 3*self.std_dev:
                print(f"⚠️ Out of Control Point at Index {i}: {point:.2f}")
                return False
        print("✅ Process is statistically in control.")
        return True

class ProcessCapability:
    def __init__(self, data, USL, LSL):
        self.data = data
        self.USL = USL
        self.LSL = LSL
        self.mean = np.mean(data)
        self.std_dev = np.std(data)

    def calculate_cp_cpk(self):
        cp = (self.USL - self.LSL) / (6 * self.std_dev)
        cpu = (self.USL - self.mean) / (3 * self.std_dev)
        cpl = (self.mean - self.LSL) / (3 * self.std_dev)
        cpk = min(cpu, cpl)

        print("\n⚙️ Process Capability Indices:")
        print(f"Cp: {cp:.2f}")
        print(f"Cpk: {cpk:.2f}")
        return cp, cpk

    def is_capable(self):
        cp, cpk = self.calculate_cp_cpk()
        if cp >= 1.33 and cpk >= 1.33:
            print("✅ Process is capable (Cp and Cpk ≥ 1.33)")
        else:
            print("❌ Process is NOT capable (Cp or Cpk < 1.33)")

class SixSigma:
    def __init__(self, defect_rate):
        self.defect_rate = defect_rate  # defects per million opportunities

    def sigma_level(self):
        if self.defect_rate == 0:
            sigma = 6
        else:
            sigma = round(6 - (np.log10(self.defect_rate / 1e6)), 2)
        print(f"\n🎯 Six Sigma Evaluation:")
        print(f"Defect Rate: {self.defect_rate} defects per million")
        print(f"Sigma Level: {sigma}σ")
        return sigma

# === Main Simulation ===

if __name__ == "__main__":
    print("=== UNIT-II: Designing Software Quality Assurance System ===")

    # 1. Statistical Methods in QA
    stats = StatisticalQualityAssurance()
    mean, std_dev = stats.summary_statistics()

    # 2. Statistical Process Control
    spc = StatisticalProcessControl(stats.data)
    spc.control_limits()
    spc.is_in_control()

    # 3. Process Capability
    pc = ProcessCapability(stats.data, USL=55, LSL=45)
    pc.is_capable()

    # 4. Six Sigma Quality
    ss = SixSigma(defect_rate=233)  # Example: 233 defects per million opportunities
    ss.sigma_level()
