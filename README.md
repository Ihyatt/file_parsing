# About Challenge.py

Text Files:
mobydick-chapter1.txt
mobydick-chapter2.txt
mobydick-chapter3.txt
mobydick-chapter4.txt
mobydick-chapter5.txt

Challenge.py:
Within Challenge.py is where the TF is computed for each word. I used a class structure to 
ensure that the code is resusable and easy to work with. 

To run challeng.py, simply cd to the Ai2_challenge directory within your terminal and type 'python challenge.py'
printed to the terminal, you will see: 

{'queequeg': {'mobydick-chapter4.txt': 0.006630500301386378}, 'whale': {'mobydick-chapter1.txt': 0.0013537906137184115}, 'sea': {'mobydick-chapter1.txt': 0.004512635379061372}}

Which is a nested dictionary that contains each word tested on as a key, with a dictionary as a value. Within that dictionary you will find the file  with the highest TF score as a key, and the TF score as the value. 
