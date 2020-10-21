import requests 
import json
import pprint
# url = ("http://saral.navgurukul.org/api/courses")
def my_response(url):
    response=requests.get(url)
    # print(response)
    # response_text=(response.text)
    # out_file = open("courses.json", "w")
    store=json.loads(response.text)
    return store
    # out_file.close()
# url = ("http://saral.navgurukul.org/api/courses")
store = my_response("http://saral.navgurukul.org/api/courses")
with open("courses.json", "w") as file :
    json.dump(store, file)


data_get = store["availableCourses"]

def my_availableCourse():
    # data_respose = my_response(url)
    # data_get=data_respose["availableCourses"]
    for i in range(len(data_get)):
        print(i,data_get[i]["name"])

 
    course_id=int(input("select the course id="))
    # for j in range(len(x)):
    #     if course_id-1==j:
    #        print(data_get[j]["id"],data_get[j]x["name"],data_get[j]["type"])
    find_id=(data_get[course_id]["id"])
    print(find_id,"=================")

    def second_aip_course():

        courses_data_aip=my_availableCourse
        id = requests.get("http://saral.navgurukul.org/api/courses/"+(find_id)+"/exercises")
        courses = id.text
        global load_courses
        load_courses=json.loads(courses)
        my_data_couses=load_courses["data"]
        return my_data_couses

    my_data_couses=second_aip_course()

    def parents_with_child():
        for k in range(0,len(my_data_couses)):
            print(k,my_data_couses[k]["name"])
            for j in range(len(my_data_couses[k])):
                var=my_data_couses[k]["childExercises"]
                for sub in range(0,len(var)):
                    print("      ", sub,var[sub]["name"])
                break
    parents_with_child()
   

    
# my_availableCourse()
    my_data_couses=load_courses["data"]
    option_type=int(input("enter the option="))
    store_option=my_data_couses[ option_type]["name"]
    store_slug=my_data_couses[ option_type]["slug"]
    print(store_option)
    childExercises_slug_data=[]
    def parents_slug():
        parents_slug=requests.get("http://saral.navgurukul.org/api/courses/"+str(find_id)+"/exercise/getBySlug?slug="+str(store_slug))
        parents_slug_text=parents_slug.text
        my_parents_slug_file=json.loads(parents_slug_text)
        parents_content=my_parents_slug_file["content"]
        print(parents_content,"i don't have bf")

        print(" ------------->>>> below is child exercise ------------->>>>")
        for k in range(0,len(my_data_couses)):
            # print(k,my_data_couses[k]["name"])

            if my_data_couses[k]["name"] == store_option :
                for j in range(len(my_data_couses[k])):
                
                    var=my_data_couses[k]["childExercises"]
                
                for sub in range(0,len(var)):
                    
                    
                    print("      ", sub,var[sub]["name"])
                    childExercises_slug_data.append(var[sub]["slug"])
    parents_slug()

                
    def child_data():
        # child_data_choice=int(input("see question:-"))
        upDown=input("enter the 'up' or exercise no.:- ")
        if upDown=="up":
            print("punnu")
            my_availableCourse()
        else:
            inTerger=int(upDown)
            # def content():
            # store_slug_child=""
            for k in range(len(my_data_couses)):
                # print(k,my_data_couses[k]["name"])

                if my_data_couses[k]["name"] == store_option :
                    store_slug_child=(my_data_couses[k]["childExercises"][inTerger]["slug"])

            print(store_slug_child)
            slug_data=""
            print(slug_data)
            for i in range(len(childExercises_slug_data)):
            
                if store_slug_child == childExercises_slug_data[i]:
                    slug_data = childExercises_slug_data[i] 

            slug=requests.get("http://saral.navgurukul.org/api/courses/"+str(find_id)+"/exercise/getBySlug?slug="+str(slug_data))
            
            
            slug_text=slug.text
            my_file=json.loads(slug_text)

            content=my_file["content"]
            print(content)
#             # content()
    child_data()
# # my_availableCourse()

#             for temp in range (len(my_data_couses)):
#                 dataNavigation=input("enter the next/previous:-")
#                 if dataNavigation=='next':
#                     slug_data=""
#                     print(slug_data)
#                     print
#                     for i in range(len(childExercises_slug_data)):
                    
#                         if store_slug_child == childExercises_slug_data[i]:
#                             slug_data = childExercises_slug_data[i]

#                     slug=requests.get("http://saral.navgurukul.org/api/courses/"+str(find_id)+"/exercise/getBySlug?slug="+str(slug_data))
                    
                    
#                     slug_text=slug.text
#                     my_file=json.loads(slug_text)

#                     content=my_file["content"]
#                     print(content)
                                

                    
                   

    # child_data()

        # elif navigation_data=='next':
        #     for k in range(0,len(my_data_couses)):
        # # print(k,my_data_couses[k]["name"])

        #         if my_data_couses[k]["name"] == store_option :
        #             store_slug_child=(my_data_couses[k]["childExercises"][child_data_choice]["slug"])

            
        # elif navigation_data=='previous':
        #         for j in range(len(my_data_couses[k])):
                    
        #             var=my_data_couses[k]["childExercises"]
        #             for sub in range(0,len(var)):
        #                 print("      ", sub,var[sub]["name"])
        #             break 
    # for n in range(len(child_name)):
    #         print(len(child_name))
    #         # print(inTerger)
    #         # print(increment)
    #         dataNavigation=input("enter the next/previous:-")
    #         if dataNavigation=='next':
    #             increment = increment + 1

                
    #             # print("fg")
    #             for n in range(len(child_name)):
    #                 incre=inTerger+increment
    #                 child_slug=my_response("http://saral.navgurukul.org/api/courses/"+list_id[incre]+"/exercise/getBySlug?slug="+slug_child[incre])
    #                 print(child_slug['content'])
    #                 break
    #         elif dataNavigation=="previous":
    #              for n in range(len(child_name)):
    #                 incre=incre-1
    #                 child_slug=my_response("http://saral.navgurukul.org/api/courses/"+list_id[incre]+"/exercise/getBySlug?slug="+slug_child[incre])
    #                 print(child_slug['content'])
    #                 break
    #         else:
    #             print("Page not found")
    # child_data()    
        
my_availableCourse()                             
