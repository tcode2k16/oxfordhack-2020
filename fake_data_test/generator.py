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
departments = ["American Institute",
"Art",
"Classics",
"English Language and Literature",
"History",
"History of Art",
"Linguistics, Philology & Phonetics",
"Medieval and Modern Languages",
"Music",
"Oriental Studies",
"Philosophy",
"Theology and Religion",
"Chemistry",
"Computer Science",
"e-Research Centre",
"Earth Sciences",
"Engineering Science",
"Life Sciences Interface Doctoral Training Centre",
"Materials",
"Mathematics",
"Physics", 
"Plant Sciences", 
"Statistics", 
"Zoology", 
"Biochemistry", 
"Clinical Medicine",
"Clinical Neurosciences",
"Experimental Psychology", 
"Medicine",
"Oncology", 
"Orthopaedics, Rheumatology and Musculoskeletal Sciences",
"Paediatrics", 
"Pathology",
"Pharmacology", 
"Physiology, Anatomy & Genetics", 
"Population Health", 
"Primary Care Health Sciences", 
"Psychiatry", 
"Surgical Sciences", 
"Women's & Reproductive Health", 
"Anthropology and Museum Ethnography", 
"Archaeology", 
"Business",
"Economics", 
"Education", 
"Geography and the Environment", 
"Global and Area Studies", 
"Government", 
"International Development", 
"Internet Institute",
"Law",
"Oxford Martin School",
"Politics and International Relations", 
"Social Policy and Intervention", 
"Sociology", 
"Continuing Education"]
genders = ["male", "male", "male", "male", "male", "female", "female", "female", "female", "female", "non-binary", "prefer not to disclose"]
pronouns = ["he/him", "she/her", "they/them"]
hobbies = ["football", "tennis", "basketball", "swimming", "chess", "eating", "swimming", "cooking", "CS", "programming", "coding", "gamming" ]

u_number = 25
publish_number = 40
match_number = 20
accept_number = 5

u_ids = []
u_names = [names.get_full_name() for i in range(u_number)]
u_college = [random.choice(colleges) for i in range(u_number)]
u_department = [random.choice(departments) for i in range(u_number)]
u_email = [str(random.randint(100000, 1000000)) + "@ox.ac.uk" for i in range(u_number)]
u_gender = [random.choice(genders) for i in range(u_number)]
u_pronoun = [random.choice(pronouns) for i in range(u_number)]
u_year = [random.randint(2020, 2024) for i in range(u_number)]
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
        'description': 'I like ' + random.choice(hobbies),
        'password': u_password[i],
    })
    print(result.text)
    # print(":", result.json()["email"],  result.json()["password"])
    u_ids.append(result.json()["user_id"])
    user_logout()


def user_login (uid):

  print (session.post(url+'auth/login', json={
      'email': u_email[uid],
      'password': u_password[uid],
  }).text)

def user_logout():
  print (session.get(url+'auth/logout').text)

loc = ["Christ Church Meadow", "University Park", "Boatyard"]
act = ["walk", "run", "dog walking", "dove feeding"]
def publish_hangout (uid, if_requirement = False):
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
        'time': random.choice(["2020-11-08 09", "2020-11-08 11", "2020-11-16 09", "2020-11-20 17", "2020-11-17 11", "2020-11-13 11", "2020-11-14 04", "2020-11-08 10"]),
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
  result_data = results.json()
  return results.json()["feeds"]

def match (hid):
  print(session.post(url+'auth/take', json = {
        'hid': hid
        }).text)


def get_cands ():
  results = session.post(url+'auth/my_hangouts', json = {
            'hangout_type': 'matched'
            })
  result_data = results.json()
  return results.json()['hangouts']

def accept (hid):
  print(session.post(url+'auth/accept', json = {
        'hid': hid
        }).text)



generate_users (u_number)

print("begin publishing")
for i in range(publish_number):
  uid = random.randint(0, u_number - 1)
  user_login(uid)
  publish_hangout (random.randint(0, u_number - 1))
  user_logout()

print("begin matching")
for i in range(match_number):
  uid = random.randint(0, u_number - 1)
  user_login(uid)
  feeds = get_feeds()
  print("user: ", uid, "len: ", len(feeds))
  if len(feeds) == 0:
    continue 
  match(random.choice(feeds)['hangout_id'])
  # print("id::", random.choice(feeds)['hangout_id'])
  user_logout()

print("begin choosing")
for i in range(accept_number  ):
  uid = random.randint(0, u_number - 1)
  user_login(uid)
  cand = get_cands()
  if len(cand) > 0:
    accept(random.choice(cand)['hangout_id'])
  user_logout()
