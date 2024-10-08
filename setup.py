from setuptools import setup, find_packages
import subprocess
import re

# Function to dynamically fetch the version from VCS (git in this case)
def get_version():
    try:
        # Get the output from git describe
        version = subprocess.check_output(["git", "describe", "--tags", "--long"]).strip().decode("utf-8")
        
        # Remove the leading 'v' (if present) and convert the version to a valid PEP 440 format
        # Example: v1.0.1-1-g68c95a7 -> 1.0.1+1.g68c95a7
        match = re.match(r"v?(\d+\.\d+\.\d+)(?:-(\d+)-g([0-9a-f]+))?", version)
        if match:
            base_version = match.group(1)  # 1.0.1
            if match.group(2):  # Handle non-tagged commits (e.g., 1 commit after tag)
                version = f"{base_version}+{match.group(2)}.g{match.group(3)}"  # 1.0.1+1.g68c95a7
            else:
                version = base_version  # If it's exactly a tagged version
        return version
    except Exception:
        return "0.0.1"  # Default/fallback version if VCS version not available

setup(
    name="particleloader",
    version=get_version(),  # Dynamic versioning based on VCS
    description="Code for downloading Particle Physics datasets",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Rikab Gambhir",
    author_email="rikab@mit.edu",
    url="https://github.com/rikab/ParticleLoader",
    project_urls={
        "Documentation": "https://github.com/rikab/ParticleLoader",
        "Homepage": "https://github.com/rikab/ParticleLoader",
        "Issue Tracker": "https://github.com/rikab/ParticleLoader/issues",
        "Releases": "https://github.com/rikab/ParticleLoader/releases",
        "Source Code": "https://github.com/rikab/ParticleLoader",
    },
    packages=find_packages(where="src"),  # Assuming the code is in the "src" directory
    package_dir={"": "src"},  # Maps the root package to src/
    python_requires=">=3.7",
    install_requires=[
        "pandas",
        "tqdm",
        "matplotlib>=3.5.0",
        "numpy",  # Compatible versions controlled through scipy
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    keywords=["top tagging", "jet physics", "machine learning"],
    license="MIT",
    include_package_data=True,
    data_files=[
        ("", ["LICENSE", "README.md", "pyproject.toml"])
    ],
    zip_safe=False,
)
