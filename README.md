# bike
#Setup Environment

conda create --name main-ds python=3.11
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel

#Run Dashboard

python -m streamlit run main.py
