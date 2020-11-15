import requests
import itertools
import os
import names
import random
import string
url = 'http://localhost:5000/'
# os.system('rm ./db.sqlite')

colleges = ["Christ Church", "Exeter", "Magdalen", "St John's", "Jesus", "Wadham", "Univ", "Trinity", "Balliol"]
departments = ["CS", "Maths", "Philosophy", "Engineering", "History", "PPE", "German", "Spanish", "Literature", "Politics"]
genders = ["male", "male", "male", "male", "male", "female", "female", "female", "female", "female", "non-binary", "prefer not to disclose"]
pronouns = ["not implemented"]
def generate_users (u_number):
  u_names = [names.get_full_name() for i in range(u_number)]
  u_college = [random.choice(colleges) for i in range(u_number)]
  u_department = [random.choice(departments) for i in range(u_number)]
  u_email = [str(random.randint(100000, 1000000)) + "@ox.ac.uk" for i in range(u_number)]
  u_gender = [random.choice(genders) for i in range(u_number)]
  u_pronoun = [random.choice(pronouns) for i in range(u_number)]
  u_year = [str(random.randint(2020, 2025)) for i in range(u_number)]
  u_phone = [str(random.randint(1000000000, 10000000000)) for i in range(u_number)]
  u_password = [''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10)) for i in range(u_number)] 
  for i in range(u_number):
    session = requests.session()
    print (session.post(url+'auth/register', json={
        'name': u_names[i],
        'college': u_college[i],
        'department': u_department[i],
        'email': u_email[i],
        'year': u_year[i],
        'phone_number': u_phone[i],
        'gender': u_gender[i],
        'pronouns': u_pronoun[i],
        'description': 'This person is lazy',
        'password': u_password[i],
    }).text)
    # login user 0
  print (requests.post(url+'auth/login', json={
      'email': u_email[0],
      'password': u_password[0],
  }).text)
  # print (session.get(url+'auth/user_info').text)

generate_users (10)







# print session.get(url+'auth/user_info').text

# for i in range(20):
#   print session.post(url+'auth/publish', json={
#       'time': 'today',
#       'location': 'uni park',
#       'activity': 'walking',
#       'cond_name': '*',
#       'cond_college': '*',
#       'cond_department': '*',
#       'cond_gender': '*',
#       'cond_year': 0,
#   }).text

# print session.post(url+'auth/publish', json={
#     'time': 'tmr',
#     'location': 'Christ Church Meadow',
#     'activity': 'running',
#     'cond_name': '12345',
#     'cond_college': '*',
#     'cond_department': '*',
#     'cond_gender': '*',
#     'cond_year': 0,
# }).text
