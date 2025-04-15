# Project
This is a fun project where I wanted to add different image processing functions into one place. This includes enhancing images/videos, removing background, in-painting, etc. As the project progresses there'll be more functions added. The project will initially use streamlit for the frontend, but I plan to change this sometime in the future.

## Setup
0. Make sure you have a GPU with the correct drivers installed:exclamation:
1. Create a virtual environment with Python 3.10.0 :point_left:
2. Run the following command in terminal :point_down:
    ```terminal 
    python timelens/setup.py install
    ```

## Running the Project
1. Launch the FastAPI server (locally)
   ```terminal
   cd timelens/backend
   uvicorn app.main:app --reload
   ```
2. Launch the Streamlit app
   ```terminal
   cd timelens/frontend
   streamlit run app.py
   ```
3. Enjoy!
