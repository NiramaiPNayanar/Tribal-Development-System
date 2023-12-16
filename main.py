import datetime
from pymongo import MongoClient
from datetime import date
import pprint
from bson import ObjectId

connection_string = "mongodb://localhost:27017"
client = MongoClient(connection_string)
database = client["Tribal_Management"]
tribal_memb = database["Tribal_Members"]
health_data = database["Health_Care"]
counsil_memb = database["Counsil_members"]
business_data = database["Business"]
locality_data = database["Locality"]
community_data = database["Community"]
admin_data = database["Admin"]

# tribal_memb.insert_many([
#   {
#     "member_id": 1,
#     "member_name": "Suresh Kumar",
#     "educational_status": "Graduate",
#     "age": 28,
#     "dob": "1995-09-20",
#
#     "community_id": 101,
#     "locality_id": 201
#   },
#   {
#     "member_id": 2,
#     "member_name": "Priya Sharma",
#     "educational_status": "Postgraduate",
#     "age": 32,
#     "dob": "1990-03-15",
#
#     "community_id": 102,
#     "locality_id": 202
#   },
#   {
#     "member_id": 3,
#     "member_name": "Rajiv Patel",
#     "educational_status": "Undergraduate",
#     "age": 25,
#     "dob": "1997-06-12",
#
#     "community_id": 103,
#     "locality_id": 203
#   },
#   {
#     "member_id": 4,
#     "member_name": "Anjali Singh",
#     "educational_status": "Diploma",
#     "age": 29,
#     "dob": "1993-11-05",
#
#     "community_id": 104,
#     "locality_id": 204
#   },
#   {
#     "member_id": 5,
#     "member_name": "Harish Verma",
#     "educational_status": "Postgraduate",
#     "age": 30,
#     "dob": "1992-07-18",
#
#     "community_id": 105,
#     "locality_id": 205
#   },
#   {
#     "member_id": 6,
#     "member_name": "Ayesha Khan",
#     "educational_status": "Graduate",
#     "age": 26,
#     "dob": "1996-02-25",
#
#     "community_id": 101,
#     "locality_id": 205
#   },
#   {
#     "member_id": 7,""
#     "member_name": "Prakash Tiwari",
#     "educational_status": "Diploma",
#     "age": 27,
#     "dob": "1995-04-30",
#
#     "community_id": 102,
#     "locality_id": 204
#   },
#   {
#     "member_id": 8,
#     "member_name": "Ritu Singh",
#     "educational_status": "Undergraduate",
#     "age": 24,
#     "dob": "1998-09-08",
#
#     "community_id": 103,
#     "locality_id": 201
#   },
#   {
#     "member_id": 9,
#     "member_name": "Sanjay Kumar",
#     "educational_status": "Postgraduate",
#     "age": 31,
#     "dob": "1991-12-22",
#
#     "community_id": 104,
#     "locality_id": 203
#   },
#   {
#     "member_id": 10,
#     "member_name": "Divya Sharma",
#     "educational_status": "Graduate",
#     "age": 28,
#     "dob": "1994-05-14",
#
#     "community_id": 105,
#     "locality_id": 202
#   }])
#
# tribal_memb.insert_many([
#
#     {
#         "member_id": 11,
#         "member_name": "Rahul Kumar",
#         "educational_status": "Postgraduate",
#         "age": 32,
#         "dob": "1990-08-21",
#
#         "community_id": 103,
#         "locality_id": 201
#     },
#
#     {
#         "member_id": 12,
#         "member_name": "Anjali Singh",
#         "educational_status": "Undergraduate",
#         "age": 24,
#         "dob": "1998-02-03",
#
#         "community_id": 105,
#         "locality_id": 204
#     },
#
#     {
#         "member_id": 13,
#         "member_name": "Amit Patel",
#         "educational_status": "Diploma",
#         "age": 26,
#         "dob": "1996-11-10",
#
#         "community_id": 101,
#         "locality_id": 203
#     },
#
#     {
#         "member_id": 14,
#         "member_name": "Kavita Mehta",
#         "educational_status": "Graduate",
#         "age": 29,
#         "dob": "1993-07-17",
#
#         "community_id": 102,
#         "locality_id": 205
#     },
#
#     {
#         "member_id": 15,
#         "member_name": "Sandeep Verma",
#         "educational_status": "Postgraduate",
#         "age": 31,
#         "dob": "1991-04-25",
#
#         "community_id": 104,
#         "locality_id": 202
#     },
#
#     {
#         "member_id": 16,
#         "member_name": "Pooja Sharma",
#         "educational_status": "Undergraduate",
#         "age": 23,
#         "dob": "1999-09-08",
#
#         "community_id": 101,
#         "locality_id": 205
#     },
#
#     {
#         "member_id": 17,
#         "member_name": "Rajesh Singh",
#         "educational_status": "Diploma",
#         "age": 27,
#         "dob": "1995-12-12",
#
#         "community_id": 105,
#         "locality_id": 201
#     },
#
#     {
#         "member_id": 18,
#         "member_name": "Neha Patel",
#         "educational_status": "Graduate",
#         "age": 30,
#         "dob": "1992-06-30",
#
#         "community_id": 102,
#         "locality_id": 204
#     },
#
#     {
#         "member_id": 19,
#         "member_name": "Arjun Kumar",
#         "educational_status": "Postgraduate",
#         "age": 33,
#         "dob": "1990-03-15",
#
#         "community_id": 104,
#         "locality_id": 203
#     },
#
#     {
#         "member_id": 20,
#         "member_name": "Suman Verma",
#         "educational_status": "Undergraduate",
#         "age": 25,
#         "dob": "1997-10-05",
#
#         "community_id": 103,
#         "locality_id": 202
#     },
#
#     {
#         "member_id": 21,
#         "member_name": "Vijay Mehta",
#         "educational_status": "Diploma",
#         "age": 28,
#         "dob": "1994-01-20",
#
#         "community_id": 101,
#         "locality_id": 201
#     },
#
#     {
#         "member_id": 22,
#         "member_name": "Preeti Singh",
#         "educational_status": "Graduate",
#         "age": 29,
#         "dob": "1993-08-27",
#
#         "community_id": 102,
#         "locality_id": 203
#     },
#
#     {
#         "member_id": 23,
#         "member_name": "Rakesh Patel",
#         "educational_status": "Postgraduate",
#         "age": 31,
#         "dob": "1991-05-18",
#
#         "community_id": 104,
#         "locality_id": 204
#     },
#
#     {
#         "member_id": 24,
#         "member_name": "Sonam Verma",
#         "educational_status": "Undergraduate",
#         "age": 24,
#         "dob": "1998-02-08",
#
#         "community_id": 105,
#         "locality_id": 205
#     },
#
#     {
#         "member_id": 25,
#         "member_name": "Ajay Kumar",
#         "educational_status": "Diploma",
#         "age": 26,
#         "dob": "1996-11-25",
#
#         "community_id": 103,
#         "locality_id": 202
#     }
#
# ])



# health_data.insert_many([
#     {
#         "localityid":201,
#         "male_rate":58.3,
#         "female_rate":40.1,
#         "total_rate":49.2
#     },
#     {
#         "localityid":202,
#         "male_rate":61.3,
#         "female_rate":40.4,
#         "total_rate":51.1
#     },
#     {
#         "localityid":203,
#         "male_rate":80.8,
#         "female_rate":71.1,
#         "total_rate":75.8
#     },
#     {
#         "localityid":204,
#         "male_rate":71.1,
#         "female_rate":53.0,
#         "total_rate":62.1
#     },
#     {
#         "localityid":205,
#         "male_rate":74.3,
#         "female_rate":57,
#         "total_rate":65.7
#     }
# ])



# counsil_memb.insert_many([
# {
#     "member_id": 1,
#     "designation": "Chairperson"
#   },
#   {
#     "member_id": 2,
#     "designation": "Secretary"
#   },
#   {
#     "member_id": 3,
#     "designation": "Treasurer"
#   },
#   {
#     "member_id": 4,
#     "designation": "Vice Chairperson"
#   },
#   {
#     "member_id": 5,
#     "designation": "Member-at-large"
#   },
#   {
#     "member_id": 6,
#     "designation": "Advisor"
#   },
#   {
#     "member_id": 7,
#     "designation": "Spokesperson"
#   }
# ])
#
# business_data.insert_many([
#   {
#     "business_id": 1,
#     "business_name": "Green Farms",
#     "locality_id": 201,
#     "business_description": "Organic Agriculture",
#     "annual_income": 100000,
#     "member_id": 1,
#     "address": "Farm Road, Village A"
#   },
#   {
#     "business_id": 2,
#     "business_name": "Tech Solutions",
#     "locality_id": 202,
#     "business_description": "IT Services",
#     "annual_income": 150000,
#     "member_id": 1,
#     "address": "Kavalastreet, Village B"
#   },
#   {
#     "business_id": 3,
#     "business_name": "Artisan Crafts",
#     "locality_id": 203,
#     "business_description": "Handcrafted Art",
#     "annual_income": 80000,
#     "member_id": 3,
#     "address": "Kandam, Village C"
#   },
#   {
#     "business_id": 4,
#     "business_name": "Health Care Pharmacy",
#     "locality_id": 204,
#     "business_description": "Pharmaceuticals",
#     "annual_income": 120000,
#     "member_id": 4,
#     "address": "Kundamukk, Village D"
#   },
#   {
#     "business_id": 5,
#     "business_name": "GreenTech Innovations",
#     "locality_id": 205,
#     "business_description": "Environmental Technologies",
#     "annual_income": 200000,
#     "member_id": 5,
#     "address": "Poorakkad, Village E"
#   },
#   {
#     "business_id": 6,
#     "business_name": "Fashion Boutique",
#     "locality_id": 203,
#     "business_description": "Apparel and Accessories",
#     "annual_income": 90000,
#     "member_id": 5,
#     "address": "Vadakara, Village F"
#   },
#   {
#     "business_id": 7,
#     "business_name": "Tech Innovators",
#     "locality_id": 202,
#     "business_description": "Innovative Technologies",
#     "annual_income": 180000,
#     "member_id": 7,
#     "address": "Koyilandi, Village G"
#   },
#   {
#     "business_id": 8,
#     "business_name": "Food Haven",
#     "locality_id": 201,
#     "business_description": "Restaurant and Catering",
#     "annual_income": 130000,
#     "member_id": 8,
#     "address": "Kakkanad, Village H"
#   },
#   {
#     "business_id": 9,
#     "business_name": "Educare Academy",
#     "locality_id": 202,
#     "business_description": "Educational Services",
#     "annual_income": 160000,
#     "member_id": 9,
#     "address": "Kakkanad, Village I"
#   },
#   {
#     "business_id": 10,
#     "business_name": "Craftsmanship Creations",
#     "locality_id": 201,
#     "business_description": "Art and Crafts",
#     "annual_income": 110000,
#     "member_id": 10,
#     "address": "Iringal, Village J"
#   }
# ])

# locality_data.insert_many([
#   {
#     "locality_id": 201,
#     "locality_name": "Upper Himachal",
#     "state":"Andhra Pradesh",
#     "population_density": "Low",
#     "locality_area": 50
#   },
#   {
#     "locality_id": 202,
#     "locality_name": "Lower Himachal",
#     "state":"Bihar",
#     "population_density": "Medium",
#     "locality_area": 30
#   },
#   {
#     "locality_id": 203,
#     "locality_name": "Western Ghats",
#     "state":"Kerala",
#     "population_density": "High",
#     "locality_area": 15
#   },
#   {
#     "locality_id": 204,
#     "locality_name": "Pavizhamala",
#     "state":"Karnataka",
#     "population_density": "Low",
#     "locality_area": 70
#   },
#   {
#     "locality_id": 205,
#     "locality_name": "Coastal region",
#     "state":"Maharashtra",
#     "population_density": "Medium",
#     "locality_area": 40
#   }
# ])

# community_data.insert_many([
#     {
#         "community_id": 101,
#         "community_name": "Gond Tribe",
#         "locality_id": 201
#     },
#     {
#         "community_id": 102,
#         "community_name": "Bhil Tribe",
#         "locality_id": 202
#     },
#     {
#         "community_id": 103,
#         "community_name": "Santhal Tribe",
#         "locality_id": 203
#     },
#     {
#         "community_id": 104,
#         "community_name": "Munda Tribe",
#         "locality_id": 204
#     },
#     {
#         "community_id": 105,
#         "community_name": "Khasi Tribe",
#         "locality_id": 205
#     }
#
# ])

# admin_data.insert_one({"id":"Rohit","password":"mydb"})

# tribal_memb.drop()
