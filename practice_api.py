import requests 
import json
import pprint
url = ("http://saral.navgurukul.org/api/courses")
req=requests.get(url)
print (req)
# a=(req.content)
a=(req.text)
# print(a)
out_file = open("courses.json", "w")
# my_data=out_file.write(a)
store=json.loads(a)
# out_file.close()
# print(store)
# x=store["availableCourses"]
def my_function():
    x=store["availableCourses"]
    # print(x)
    for i in range(0,len(store["availableCourses"])):
        # print(i)
        print(i,store["availableCourses"][i]["name"])
    course_id=int(input("select the course="))
    # for j in range(len(x)):
    #     if course_id-1==j:
    #        print(x[j]["id"],x[j]["name"],x[j]["type"])
    s=(x[course_id]["id"])
        # print(i,"-----------------------")
    print(s,"=================")
    id = requests.get("http://saral.navgurukul.org/api/courses/"+(s)+"/exercises")
    courses = id.text
    # print(id.text)
    load_courses=json.loads(courses)
    my_data_couses=load_courses["data"]
    for k in range(0,len(my_data_couses)):
        print(k,my_data_couses[k]["name"])
        for j in range(len(my_data_couses[k])):
            
            var=my_data_couses[k]["childExercises"]
            for sub in range(0,(len(var))):
                print(sub," ", var[sub]["name"])
            break
    # option_type=input("enter the option=")
    # strore_option=(my_data_couses[k]["name"])
    # print(strore_option)
    
    data_choice=int(input("you want to see question:-"))
    print(data_choice)
    see=my_data_couses[data_choice]["slug"]
    print(see)
    slug=requests.get("http://saral.navgurukul.org/api/courses/"+(s)+"/exercise/getBySlug?slug="+see) 
    slug_text=slug.text
    my_file=json.loads(slug_text)
    content=my_file["content"]
    print(content,end="")

    previous_question=input("if you want see again so enter the next/previous:-")
    if previous_question=='next':
        see=my_data_couses[data_choice+1]["slug"]
        slug=requests.get("http://saral.navgurukul.org/api/courses/"+(s)+"/exercise/getBySlug?slug="+see)
        slug_text=slug.text
        my_file=json.loads(slug_text)
        content=my_file["content"]
        print(content,end="")

    elif previous_question=="previous":
        see=my_data_couses[data_choice-1]["slug"]
        slug=requests.get("http://saral.navgurukul.org/api/courses/"+(s)+"/exercise/getBySlug?slug="+see)
        slug_text=slug.text
        my_file=json.loads(slug_text)
        content=my_file["content"]
        print(content,end="")
    
        
my_function()