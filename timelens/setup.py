import os
import subprocess

base_path = os.path.dirname(__file__)

# automaticall install required packages during setup
def install_requirements() -> None:
    backend_path = os.path.join(base_path, 'backend/requirements.txt')
    frontend_path = os.path.join(base_path, 'frontend/requirements.txt')
    subprocess.run(["pip", "install", "-r", backend_path], check=True)
    subprocess.run(["pip", "install", "-r", frontend_path], check=True)

install_requirements()

# automatically install models during setup
def install_models() -> None:
    install_models_path = os.path.join(base_path, 'install_models.py')
    subprocess.run(["python", install_models_path], check=True)

install_models()