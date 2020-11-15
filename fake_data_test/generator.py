import requests
import itertools
import os
import names
import random
import string
url = 'http://localhost:5000/'
session = requests.session()

# os.system('rm ./db.sqlite')

colleges = ["Christ Church", "Exeter", "Magdalen", "St John's", "Jesus", "Wadham", "Univ", "Trinity", "Balliol"]
departments = ["CS", "Maths", "Philosophy", "Engineering", "History", "PPE", "German", "Spanish", "Literature", "Politics"]
genders = ["male", "male", "male", "male", "male", "female", "female", "female", "female", "female", "non-binary", "prefer not to disclose"]
pronouns = ["not implemented"]


u_number = 3
u_ids = []
u_names = [names.get_full_name() for i in range(u_number)]
u_college = [random.choice(colleges) for i in range(u_number)]
u_department = [random.choice(departments) for i in range(u_number)]
u_email = [str(random.randint(100000, 1000000)) + "@ox.ac.uk" for i in range(u_number)]
u_gender = [random.choice(genders) for i in range(u_number)]
u_pronoun = [random.choice(pronouns) for i in range(u_number)]
u_year = [random.randint(2020, 2025) for i in range(u_number)]
u_phone = [str(random.randint(1000000000, 10000000000)) for i in range(u_number)]
u_password = [''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10)) for i in range(u_number)]       

def generate_users (u_number):
  for i in range(u_number):
    
    result = session.post(url+'auth/register', json={
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
    })
    print(result.text)
    u_ids.append(result.json()["user_id"])
    user_logout()


def user_login (uid):

  print (session.post(url+'auth/login', json={
      'email': u_email[uid],
      'password': u_password[uid],
  }).text)

def user_logout():
  print (session.post(url+'auth/logout', json={

    }).text)

loc = ["Chrest Church Meadow", "Univ Park"]
act = ["walk", "run", "swim"]
def creat_hangout (uid, if_requirement = False):
  if if_requirement:
    print (session.post(url+'auth/publish', json={
          'time': "2020-11-15 11 p.m.",
          'location': random.choice(loc),
          'activity': random.choice(act),
          'cond_name': "*",
          'cond_college': "*",
          'cond_department': "*",
          'cond_gender': "*",
          'cond_year': 0,
    }).text)
  else:
    print (session.post(url+'auth/publish', json={
        'time': "2020-11-15 11 p.m.",
        'location': random.choice(loc),
        'activity': random.choice(act),
        'cond_name': "*",
        'cond_college': "*",
        'cond_department': "*",
        'cond_gender': "*",
        'cond_year': 0,
    }).text)

def get_feeds ():
  results = session.post(url+'auth/my_feed', json = {})
  # print(results)
  result_data = results.json()
  return results.json()["feeds"]

def match (hid):
  print(session.post(url+'auth/take', json = {
        'hid': hid
        }).text)

generate_users (u_number)

for i in range(10):
  uid = random.randint(0, u_number - 1)
  user_login(uid)
  creat_hangout (random.randint(0, u_number - 1))
  user_logout()

print("begin matching")
for i in range(10):
  uid = random.randint(0, u_number - 1)
  user_login(uid)
  feeds = get_feeds()
  print("user: ", uid, "len: ", len(feeds))
  if len(feeds) == 0:
    continue 
  match(random.choice(feeds)['hangout_id'])
  # print("id::", random.choice(feeds)['hangout_id'])
  user_logout()

# for i in range(1):
#   uid = random.choice(0, u_number - 1)
#   cand = get_cands(uid)
#   user_login(uid)
#   accept(random.choice(feeds))
#   user_logout()







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
