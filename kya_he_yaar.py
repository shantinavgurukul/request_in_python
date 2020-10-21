import requests 
import json
import pprint
# url = ("http://saral.navgurukul.org/api/courses")
def my_response(url):
    response=requests.get(url)
    store=json.loads(response.text)
    return store
   
store = my_response("http://saral.navgurukul.org/api/courses")
# print(store)
with open("courses.json", "w") as file :
    json.dump(store, file)


data_get = store["availableCourses"]


def my_availableCourse():
    list_id=[]
    list_name=[]
    for i in range(len(data_get)):
        list_id.append(data_get[i]["id"])
        list_name.append(data_get[i]["name"])
    # print(list_name)
    # print(list_id)

    for i in range(len(data_get)):
        print(i,data_get[i]["name"])

    course_id=int(input("select the course id="))
    # find_id=(data_get[course_id]["id"])
    # print(find_id,"=================")
    # print(list_id[course_id])


    # def second_aip_course():
        # id = requests.get("http://saral.navgurukul.org/api/courses/"+list_id[course_id]+"/exercises")
        # load_courses=json.loads(id.text)
        # my_data_couses=load_courses["data"]
        # return my_data_couses
    #     poo = my_response("http://saral.navgurukul.org/api/courses/"+list_id[course_id]+"/exercises")
    #     return poo
    # my_data_couses = second_aip_course()
    # print(my_data_couses)

    load_courses = my_response("http://saral.navgurukul.org/api/courses/"+list_id[course_id]+"/exercises")
    my_data_couses=load_courses["data"]

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
    parents_with_child()

    option_type=int(input("enter the option="))
    store_option=my_data_couses[option_type]["name"]
    store_slug=my_data_couses[ option_type]["slug"]

    childExercises_slug_data=[]
    def parents_slug():
        parents_slug=requests.get("http://saral.navgurukul.org/api/courses/"+str(list_id[course_id])+"/exercise/getBySlug?slug="+str(store_slug))
        # parents_slug_text=parents_slug.text
        my_parents_slug_file=json.loads(parents_slug.text)
        parents_content=my_parents_slug_file["content"]
        print(parents_content)

        print(" ------------->>>> below is child exercise ------------->>>>")

        for k in range(0,len(my_data_couses)):
            if my_data_couses[k]["name"] == store_option :
                for j in range(len(my_data_couses[k])):
                    var=my_data_couses[k]["childExercises"]
                for sub in range(0,len(var)):  
                    print("      ", sub,var[sub]["name"])
                    childExercises_slug_data.append(var[sub]["slug"])
    parents_slug()
    
                
    def child_data():
        upDown=input("enter the 'up' or exercise no.:- ")
        if upDown=="up":
            my_availableCourse()
        else:
            inTerger=int(upDown)
            for k in range(len(my_data_couses)):
                if my_data_couses[k]["name"] == store_option :
                    store_slug_child=(my_data_couses[k]["childExercises"][inTerger]["slug"])
            print(store_slug_child)
            slug_data=""
            print(slug_data)
            for i in range(len(childExercises_slug_data)):          
                if store_slug_child == childExercises_slug_data[i]:
                    slug_data = childExercises_slug_data[i] 
            slug = my_response("http://saral.navgurukul.org/api/courses/"+list_id[inTerger]+"/exercise/getBySlug?slug="+str(slug_data))
            content=slug["content"]
            print(content)

            # slug_child= []
            # child_name = []
            # for k in my_data_couses[inTerger]['childExercises']:
            #     slug_child.append(k["slug"])
            #     child_name.append(k['name'])
            # print("child_name", child_name)
            # print("slug_child", slug_child)
            # parents_slug=my_response("http://saral.navgurukul.org/api/courses/"+list_id[inTerger]+"/exercise/getBySlug?slug="+slug_child[inTerger])
            # # print("http://saral.navgurukul.org/api/courses/"+list_id[inTerger]+"/exercise/getBySlug?slug="+slug_child[inTerger])
            # print("one slug_child", slug_child[inTerger])
            # print(parents_slug['content'])

            
        #     slug=my_response("http://saral.navgurukul.org/api/courses/"+list_id[inTerger]+"/exercise/getBySlug?slug="+str(slug_data))
        #     print(slug)
        
        increment = 0 
        for n in range(len(my_data_couses)):
            print(len(my_data_couses))
            # print(inTerger)
            # print(increment)
            dataNavigation=input("enter the next/previous:-")
            if dataNavigation=='next':
                increment = increment + 1

                
                # print("fg")
                for n in range(len(my_data_couses)):
                    incre=inTerger+increment
                    child_slug=my_response("http://saral.navgurukul.org/api/courses/"+list_id[incre]+"/exercise/getBySlug?slug="+slug_child[incre])
                    print(child_slug['content'])
                    break
            elif dataNavigation=="previous":
                 for n in range(len(my_data_couses)):
                    incre=incre-1
                    child_slug=my_response("http://saral.navgurukul.org/api/courses/"+list_id[incre]+"/exercise/getBySlug?slug="+slug_child[incre])
                    print(child_slug['content'])
                    break
        else:
            print("Page not found")
        
        
    child_data()

my_availableCourse()                             
