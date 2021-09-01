import datetime
import pandas
import random
import smtplib

MY_EMAIL = 'Enter@YourEmail.com'
MY_PASS = 'Ent3rP@ssW0rD'
SMTP_PROV = 'smtp.gmail.com' # or Whatever the smtp address is of your email provider


today = datetime.datetime.now()
cur_mon = today.month
cur_day = today.day
today_tuple = (cur_mon,cur_day)

data = pandas.read_csv('birthdays.csv')

birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    person = birthday_dict[today_tuple]
    random_pick = random.randint(1,3)
    path = f'./letter_templates/letter_{random_pick}.txt'
    with open(path) as filereader:
        content = filereader.read()
        content = content.replace('[NAME]', person.name )
        
    with smtplib.SMTP(SMTP_PROV) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=person.email, msg=f'Subject:Happy Birthday!\n\n{content}')

