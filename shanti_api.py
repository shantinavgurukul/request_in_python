import requests 
import json
import pprint

url = ("http://saral.navgurukul.org/api/courses")
response=requests.get(url)
# print (response)
# a=(req.content)
response_text=(response.text)
# print(response_text)
out_file = open("courses.json", "w")
# my_data=out_file.write(a)
store=json.loads(response_text)
out_file.close()
# print(store)
# data_get=store["availableCourses"]
def my_function():
    data_get=store["availableCourses"]
    # print(type(data_get))
    for i in range(0,len(store["availableCourses"])):
        # print(i)
        print(i,store["availableCourses"][i]["name"])
    course_id=int(input("select the course id="))
    # print(course_id)
    parents_slug=requests.get("http://saral.navgurukul.org/api/courses/"+str(course_id)+"/exercises")
    courses = parents_slug.text
    # print(courses)
    load_courses=json.loads(courses)
    my_data_couses=load_courses["data"]
    # print(len(find_id))
    # if len(my_data_couses) == 0:
    #     print("Not found")
    # else:
    #     data_choice=int(input("see question:-"))
    #     print(data_choice,"santi")
    #     slug_data=my_data_couses[k]["childExercises"][data_choice]["slug"]
    #     print(slug_data)
    #     slug=requests.get("http://saral.navgurukul.org/api/courses/"+str(find_id)+"/exercise/getBySlug?slug="+str(slug_data))
    #     print(slug,"swati")
        
    # print(my_data_couses)

    # for j in range(len(x)):
    #     if course_id-1==j:
    #        print(data_get[j]["id"],data_get[j]["name"],data_get[j]["type"])
    find_id=(data_get[course_id]["id"])
  # print(i,"-----------------------")
    print(find_id,"=================")
   
    id = requests.get("http://saral.navgurukul.org/api/courses/"+(find_id)+"/exercises")
    courses = id.text
    # print(id.text)
    load_courses=json.loads(courses)
    my_data_couses=load_courses["data"]
    for k in range(0,len(my_data_couses)):
        print(k,my_data_couses[k]["name"])

        # for j in range(len(my_data_couses[k])):
            
        #     var=my_data_couses[k]["childExercises"]
        #     for sub in range(0,len(var)):
        #         print("      ", sub,var[sub]["name"])
        #     break

    option_type=int(input("enter the option="))
    store_option=(my_data_couses[ option_type]["name"])
    store_slug=(my_data_couses[ option_type]["slug"])

    print(store_option)
    

    parents_slug=requests.get("http://saral.navgurukul.org/api/courses/"+str(find_id)+"/exercise/getBySlug?slug="+str(store_slug))
    # print (parents_slug,"jiiiii")
    # slug_response_text=(parents_slug.text["content"])
    # print(slug_response_text,"sdfgjk")

    parents_slug_text=parents_slug.text
    my_parents_slug_file=json.loads(parents_slug_text)
    parents_content=my_parents_slug_file["content"]
    print(parents_content,"i don't have bf")

    # print((my_data_couses[ option_type],"1111111111111111"))
    print(" ------------->>>> below is child exercise ------------->>>>")
    for k in range(0,len(my_data_couses)):
        # print(k,my_data_couses[k]["name"])

        if my_data_couses[k]["name"] == store_option :
            for j in range(len(my_data_couses[k])):
            
                var=my_data_couses[k]["childExercises"]
                # print(var,"santi........")
            for sub in range(0,len(var)):
                    # print("      ", sub,var[sub]["name"])
                    # break 
                
                print("      ", sub,var[sub]["name"])
    
    data_choice=int(input("see question:-"))
    print(data_choice,"santi")
    slug_data=my_data_couses[k]["childExercises"][data_choice]["slug"]
    print(slug_data)
    slug=requests.get("http://saral.navgurukul.org/api/courses/"+str(find_id)+"/exercise/getBySlug?slug="+str(slug_data))
    
    print(slug,"swati")
    slug_text=slug.text
    # print(slug_text,"test")
    my_file=json.loads(slug_text)
    # print(my_file,"test")

    content=my_file["content"]
    print(content,"sakhi")


    #     slug_text=slug.text
    #     my_file=json.loads(slug_text)
    #     content=my_file["content"]
    #     print(content,end="")                              
    # previous_question=input("enter the up/next/previous:-")
    # if previous_question=='next':
    #     see=my_data_couses[data_choice+1]["slug"]
    #     slug=requests.get("http://saral.navgurukul.org/api/courses/"+(s)+"/exercise/getBySlug?slug="+see)
    #     slug_text=slug.text
    #     my_file=json.loads(slug_text)
    #     content=my_file["content"]
    #     print(content,end="")

    # elif previous_question=="previous":
    #     see=my_data_couses[data_choice-1]["slug"]
    #     slug=requests.get("http://saral.navgurukul.org/api/courses/"+(s)+"/exercise/getBySlug?slug="+see)
    #     slug_text=slug.text
    #     my_file=json.loads(slug_text)
    #     content=my_file["content"]
    #     print(content,end="")
        
my_function()