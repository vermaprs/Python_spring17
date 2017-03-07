Que 1- Enron Dataset

Analysis 1 - Getting top mail receivers and senders from Enron CEO's folder : This will allow me to to reduce the dataset. I am 
             counting the nummber of mails for each person in the 'From' and 'To' category. Then, sorting the top 10 person's
             in both these categories. Same is being done for mails in the CEO Kenneth Lay's Folder and get top 10 senders and
             receivers of mails. This list gives me important persons mail ids.
             
 <img src="https://github.com/vermaprs/Python_spring17/blob/master/midterm/screenshots/Que1_Ana1.png" width="350"/>

Analysis 2 - based on the above top receivers and senders, I am reducing the mail dataset to the mails containing the mails 
             of the top senders and receivers.
             
 <img src="https://github.com/vermaprs/Python_spring17/blob/master/midterm/screenshots/Que1_Ana2.png" width="350"/>

Analysis 3 - Now I am looking for suspect keywords in the reduced mail dataset and frequency of the suspect words for top 
             senders and receivers. This gives me the mail ids of the top suspects.
             
<img src="https://github.com/vermaprs/Python_spring17/blob/master/midterm/screenshots/Que1_Ana3.png" width="350"/>


Que 2 - NYT API

Analysis 1 - I am using the archive API. I am trying to fetch the news archive from June 2016 - Nov 2016.
             I am then saving the data in json files. Then, I am finding the frequency of word "Trump" in each month's 
             news data. Finally, displaying the data for the June-Nov 2016. The conclusion is that the Donald Trump's 
             popularity was high in last two months i.e. October and November 2016.
             
<img src="https://github.com/vermaprs/Python_spring17/blob/master/midterm/screenshots/Que2_Ana1.png" width="350"/>
             
Analysis 2 - I am using the archive API. I am fetching the data for all 12 months in the year 2016. I am then saving the data
             in json files. From all this data, I am counting the frequency of words and then sorting the words based on
             frequency. This list gives me the top trending news words for the year 2016.
             

             
Analysis 3 - I am using the archive API. I am trying to fetch the news archive from June 2016 - Nov 2016.
             I am then saving the data in json files. Then, I am finding the frequency of word "Hilary" in each month's 
             news data. Finally, displaying the data for the June-Nov 2016. The conclusion is that the Hilary Clinton's 
             popularity in news was least in last two months i.e. October and November 2016.
             
             
<img src="https://github.com/vermaprs/Python_spring17/blob/master/midterm/screenshots/Que2_Ana3.png" width="350"/>          
