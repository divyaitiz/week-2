"""
Developer onboarding check script with advanced features.
"""

import sys
import subprocess
import importlib
import argparse
import shutil
import time


def check_python_version():
    start = time.time()
    version = sys.version_info
    ok = version >= (3, 10)
    result = f"{version.major}.{version.minor}.{version.micro}"
    return ok, result, time.time() - start


def check_virtual_env():
    start = time.time()
    ok = hasattr(sys, "base_prefix") and sys.prefix != sys.base_prefix
    result = sys.prefix if ok else "Not in virtual environment"
    return ok, result, time.time() - start


def check_package(pkg_name, fix=False):
    start = time.time()
    try:
        module = importlib.import_module(pkg_name)
        version = getattr(module, "__version__", "unknown")
        return True, version, time.time() - start
    except ImportError:
        if fix:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", pkg_name],
                check=False,
            )
            return check_package(pkg_name, fix=False)
        return False, "not installed", time.time() - start


def check_internet():
    start = time.time()
    try:
        import requests  # pylint: disable=import-outside-toplevel

        response = requests.get("https://www.google.com", timeout=5)
        ok = response.status_code == 200
        return ok, "OK" if ok else "Failed", time.time() - start
    except Exception:
        return False, "Failed", time.time() - start


def check_disk_space():
    start = time.time()
    total, used, free = shutil.disk_usage("/")
    free_gb = free / (1024 ** 3)
    ok = free_gb >= 1
    return ok, f"{free_gb:.2f} GB free", time.time() - start


def parse_args():
    parser = argparse.ArgumentParser(description="Onboarding script")
    parser.add_argument("--verbose", action="store_true", help="Detailed output")
    parser.add_argument("--fix", action="store_true", help="Auto-fix missing packages")
    return parser.parse_args()


def main():
    args = parse_args()

    print("=== Developer Onboarding Check ===")
    total_start = time.time()

    results = []

    results.append(("Python version", *check_python_version(), ">= 3.10 required"))
    results.append(("Virtual environment", *check_virtual_env(), ""))

    results.append(("pylint installed", *check_package("pylint", args.fix), ""))
    results.append(("black installed", *check_package("black", args.fix), ""))
    results.append(("numpy installed", *check_package("numpy", args.fix), ""))

    results.append(("Internet connectivity", *check_internet(), ""))
    results.append(("Disk space", *check_disk_space(), ">= 1GB required"))

    pass_count = 0
    report_lines = ["=== Developer Onboarding Check ==="]

    for name, status, value, duration, extra in results:
        status_str = "PASS" if status else "FAIL"
        if status:
            pass_count += 1

        line = f"[{status_str}] {name}: {value}"
        if extra:
            line += f" ({extra})"

        if args.verbose:
            line += f" | Time: {duration:.4f}s"

        print(line)
        report_lines.append(line)

    total = len(results)
    total_time = time.time() - total_start

    summary = f"\nResult: {pass_count}/{total} checks passed"
    timing = f"Total execution time: {total_time:.4f}s"

    print(summary)
    print(timing)

    report_lines.append(summary)
    report_lines.append(timing)

    with open("setup_report.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(report_lines))

    print("Report saved to: setup_report.txt")


if __name__ == "__main__":
    main()