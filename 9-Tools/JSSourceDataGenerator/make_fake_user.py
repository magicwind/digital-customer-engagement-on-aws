import csv
from faker import Faker

fake = Faker()

# Generate fake user data
users = []
for i in range(10000):
    user_id = i + 1
    username = fake.user_name()
    email = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    mobile_number = fake.phone_number()
    gender = fake.random_element(elements=('M', 'F'))
    age = fake.random_int(min=18, max=70)
    users.append((user_id, username, email, first_name, last_name, mobile_number, gender, age))

# Write data to CSV file
with open('fake_users.csv', mode='x', newline='') as csv_file:
    fieldnames = ['UserID', 'Username', 'Email', 'First Name', 'Last Name', 'Mobile Number', 'Gender', 'Age']
    writer = csv.writer(csv_file)
    writer.writerow(fieldnames)
    for user in users:
        writer.writerow(user)
