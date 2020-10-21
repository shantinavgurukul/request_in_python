import requests
import json
import os
import pprint

print("***************WELCOME***********TO***********SARAL************PAGE***************")
print("@@@@@@@@@@@@@>>>>HUMARA KARTA DHARTA MAA-BAA KA  PAGE>>>@@@@@@@@@@@@@@")

def response_url(url):
    response=requests.get(url)
    store=json.loads(response.text)
    with open ("courses.json", "w") as file:
        return store

store = response_url("http://saral.navgurukul.org/api/courses")
# print(response_url(url))
courses_id=[]
def course_data():
    for i in range(len(store['availableCourses'])):
        # print(store['availableCourses'][i])
        courses=store['availableCourses'][i]
        courses_name=courses['name']
        coursesId=courses['id']
        courses_id.append(coursesId)
        print(i,courses_name,coursesId)
    return courses_id
course_data()
if os.path.exists("courses.json"):
        print ("shanti")
else:
        request(store)
        store=courses_id("courses.json")
        saral_courses(store)
        print ("headache")
course_select=int(input("select courses - "))

def selectCourse():
    load_courses = response_url("http://saral.navgurukul.org/api/courses/"+ courses_id[course_select]+"/exercises")
    my_data_couses=load_courses["data"]
    return(my_data_couses)
my_data_couses=selectCourse()
load_courses=selectCourse()

def parents_with_child():
        # slug_list=[]
        
        for k in range(len(my_data_couses)):
            # slug_list.append(my_data_couses[k]["slug"])
            print(k,my_data_couses[k]["name"])
            for j in range(len(my_data_couses[k])):
                var=my_data_couses[k]["childExercises"]
                for sub in range(0,len(var)):
                    print("      ", sub,var[sub]["name"])
                break
load_courses=parents_with_child()











