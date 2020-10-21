import requests 
import json
import pprint
# import os.path

# def exists_data():
#     exists = os.path.exists('courses2.json')
#     if exists:
#         with open("courses2.json" ,'r') as courses_file:
#             data = courses_file.read()
#             data_in_json = json.loads(data)
#             pprint.pprint(data_in_json)
#             # print(type(data_in_json)) #data in dict
#             # print("**   WELCOME TO SARAL COURSES   **","\n")
#             # s_no = 1
#             # for courses_index in (data_in_json["availableCourses"]):
#             #     print(s_no,courses_index['name'])
#             #     s_no = s_no + 1
#             # return data_in_json 
#             # 
#             num=1  
#             for courses_index in (data_in_json["availableCourses"]):
#                 print(num,courses_index["name"])
#                 num=num+1
#                 return data_in_json
#             course=int(input("select the course="))
#             for j in (data_in_json["availableCourses"]):
#                 if course-1==j:
#                     print(data_in_json[j]["id"],data_in_json[j]["name"],data_in_json[j]["type"])

#     else:
#         res = requests.get('http://saral.navgurukul.org/api/courses')
#         with open('courses2.json', 'w') as courses_file:
#             convert = res.json()
#             json.dump(convert,courses_file)
# exists_data()






# # def func():
# #     exists = os.path.exists('courses.json')
# #     if exists:
# #         with open('courses.json', 'r') as simple_file:
# #             data = simple_file.read()
# #             data_json = json.loads(data)
# #             pprint.pprint(data_json)
# #     else:
# #         res = requests.get('http://saral.navgurukul.org/api/courses')
# #         with open('courses.json', 'w') as simple_file:
# #             convert = res.json()
# #             json.dump(convert, simple_file)
# #             # pprint.pprint(convert)
# # func()








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
    # for j in range(len(x)):
    #     if course_id-1==j:
    #        print(data_get[j]["id"],data_get[j]["name"],data_get[j]["type"])
    find_id=(data_get[course_id]["id"])ind_id=(data_get[course_id]["id"])
    #     # print(i,"-----------------------")
    print(find_id,"=================")
    id = requests.get("http://saral.navgurukul.org/api/courses/"+(find_id)+"/exercises")
    courses = id.text
    # print(id.text)
    load_courses=json.loads(courses)
    my_data_couses=load_courses["data"]
    for k in range(0,len(my_data_couses)):
        print(k,my_data_couses[k]["name"])
    #     # print(i,"-----------------------")
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

    # option_type=int(input("enter the option="))
    # store_option=(my_data_couses[ option_type]["name"])
    # store_slug=(my_data_couses[ option_type]["slug"])

    # print(store_option)
    # print(store_slug)

    # parents_slug=requests.get("http://saral.navgurukul.org/api/courses/"+str(find_id)+"/exercise/getBySlug?slug="+str(store_slug))
    # # print (parents_slug,"jiiiii")
    # # slug_response_text=(parents_slug.text["content"])
    # # print(slug_response_text,"sdfgjk")

    # parents_slug_text=parents_slug.text
    # my_parents_slug_file=json.loads(parents_slug_text)
    # parents_content=my_parents_slug_file["content"]
    # print(parents_content,"i don't have bf")

    # childExercises_slug_data=[]
    # # print((my_data_couses[ option_type],"1111111111111111"))
    # print(" ------------->>>> below is child exercise ------------->>>>")
    # for k in range(0,len(my_data_couses)):
    #     # print(k,my_data_couses[k]["name"])

    #     if my_data_couses[k]["name"] == store_option :
    #         for j in range(len(my_data_couses[k])):
            
    #             var=my_data_couses[k]["childExercises"]
    #             # print(var,"santi........")
    #         for sub in range(0,len(var)):
    #                 # print("      ", sub,var[sub]["name"])
    #                 # break 
                
    #             print("      ", sub,var[sub]["name"])
    #             childExercises_slug_data.append(var[sub]["slug"])
    #             # print(childExercises_slug_data,"====================")

    #             # break,
    # # print(childExercises_slug_data,"list..............")
    # child_data_choice=int(input("see question:-"))
    # store_slug_child=""
    # for k in range(0,len(my_data_couses)):
    #     # print(k,my_data_couses[k]["name"])

    #     if my_data_couses[k]["name"] == store_option :
    #         store_slug_child=(my_data_couses[k]["childExercises"][child_data_choice]["slug"])

    # print(store_slug_child)
    # slug_data=""
    # for i in range(0,len(childExercises_slug_data)):
    #     # print(childExercises_slug_data[i])
    #     if store_slug_child == childExercises_slug_data[i]:
    #         # print(childExercises_slug_data[i])
    #         slug_data = childExercises_slug_data[i] 
    # # print(slug_data)

        
    # # slug_data=(my_data_couses[k]["childExercises"]["slug"]
    # # print(slug_data,["slug"]["Data"])
    # slug=requests.get("http://saral.navgurukul.org/api/courses/"+str(find_id)+"/exercise/getBySlug?slug="+str(slug_data))
    
    # # print(slug,"swati")
    # slug_text=slug.text
    # # print(slug_text,"test")
    # my_file=json.loads(slug_text)
    # # print(my_file,"test")

    # content=my_file["content"]
    # print(content)
    
    # for temp in range (len(store["availableCourses"])):                         
    #     navigation_data=input("enter the up/next/previous:-")
    #     if navigation_data=='up':
    #         for i in range(0,len(store["availableCourses"])):
    #             print(i,store["availableCourses"][i]["name"])
    #         course_id=int(input("select the course id="))
    #         find_id=(data_get[course_id]["id"])
    #         print(find_id,"=================")
    #     elif navigation_data=='next':
    #         for k in range(0,len(my_data_couses)):
    #             if my_data_couses[k]["name"] == store_option :
    #                 store_slug_child=(my_data_couses[k]["childExercises"][child_data_choice]["slug"])

            
    #     elif navigation_data=='previous':
    #             for j in range(len(my_data_couses[k])):
                    
    #                 var=my_data_couses[k]["childExercises"]
    #                 for sub in range(0,len(var)):
    #                     print("      ", sub,var[sub]["name"])
    #                 break
my_function()