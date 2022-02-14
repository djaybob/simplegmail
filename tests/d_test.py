from simplegmail import Gmail
from numpy import random
import random
import datetime
from time import sleep

begin_time = datetime.datetime.now()

gmail = Gmail()

messages = gmail.get_spam_messages()

for message in messages:
    #set of Actions
    Actions = set([
        message.mark_as_read(),
        message.mark_as_important(),
        message.star(),
        message.mark_as_not_spam(),
        message.modify_labels(to_add='INBOX',to_remove='SPAM')
       ])
    for Action in Actions:
        random.choice(list(Actions))
        time.sleep(random.uniform(2, 4)) # Sleep for x seconds

print(datetime.datetime.now() - begin_time) # Max Total Execution Time: Total No. of Messages*4 | # Min Total Execution Time: Total No. of Messages*2
