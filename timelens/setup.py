import os
import subprocess
import sys

base_path = os.path.dirname(__file__)

# automaticall install required packages during setup
def install_requirements() -> None:
    backend_path = os.path.join(base_path, 'backend')
    frontend_path = os.path.join(base_path, 'frontend')

    # install torch stack first
    subprocess.run([
        sys.executable, "-m", "pip", "install",
        "torch==1.13.1+cu117",
        "torchvision==0.14.1",
        "torchaudio==0.13.1+cu117",
        "--extra-index-url", "https://download.pytorch.org/whl/cu117"
    ], check=True)

    # install remaining backend 
    subprocess.run([
        sys.executable, "-m", "pip", "install",
        "-r",os.path.join(backend_path, "requirements.txt"),
        "--constraint", os.path.join(backend_path, "constraints.txt")
    ], check=True)

    # install frontend
    subprocess.run([
        sys.executable, "-m", "pip", "install",
        "-r", os.path.join(frontend_path, "requirements.txt")
    ], check=True)

install_requirements()

# automatically install models during setup
def install_models() -> None:
    install_models_path = os.path.join(base_path, 'install_models.py')
    subprocess.run(["python", install_models_path], check=True)

install_models()