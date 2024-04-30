# FAST API PROJECT FOR LEARNING 
The repo for learing purpose of the fats-api

## Project Structure
It invloves the coverage of the project by adding of the models and Controllers


## To run Locally
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# then run via uvicorn:
uvicorn slack:app --reload

## To deploy on heroku
heroku login  
heroku create
git push heroku main
heroku open