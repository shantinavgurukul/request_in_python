import requests 
import json
import pprint
import os.path

def exists_data():
    exists = os.path.exists('courses2.json')
    if exists:
        with open("courses2.json" ,'r') as courses_file:
            data = courses_file.read()
            data_in_json = json.loads(data)
            # pprint.pprint(data_in_json)
            print(type(data_in_json)) #data in dict
            print("**   WELCOME TO SARAL COURSES   **","\n")
            s_no = 1
            for courses_index in (data_in_json["availableCourses"]):
                print(s_no,courses_index['name'])
                s_no = s_no + 1
            return data_in_json 
            # 
            num=1  
            for courses_index in (data_in_json["availableCourses"]):
                print(num,courses_index["name"])
                num=num+1
                return data_in_json
            course=int(input("select the course="))
            for j in (data_in_json["availableCourses"]):
                if course-1==j:
                    print(data_in_json[j]["id"],data_in_json[j]["name"],data_in_json[j]["type"])

    else:
        res = requests.get('http://saral.navgurukul.org/api/courses')
        with open('courses2.json', 'w') as courses_file:
            convert = res.json()
            json.dump(convert,courses_file)
exists_data()
# def parents_