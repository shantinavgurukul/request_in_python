import requests 
import json
import pprint

print("@@*******************WELCOME TO SARAL PAGE*******************@@")
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
pprint.pprint(data_get)


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
            # print(k,my_data_couses[k]["name"])

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
            input_slug=""
            for k in range(0,len(my_data_couses)):
            # print(k,my_data_couses[k]["name"])

                if my_data_couses[k]["name"] == store_option :
                    # for j in range(len(my_data_couses[k])):
                    
                    var=my_data_couses[k]["childExercises"]
                    # print(var,"asdfghjk santi")
                    input_slug=var[inTerger]["slug"]
                    # print(input_slug,"qqqqqqqqwertyuiop")

                    for i in (childExercises_slug_data):
                        
                        if  i == input_slug:

                            child_slug=requests.get("http://saral.navgurukul.org/api/courses/"+str(list_id[course_id])+"/exercise/getBySlug?slug="+input_slug)
                            my_child_slug_file=json.loads(child_slug.text)
                            child_content=my_child_slug_file["content"]
                            print(child_content)

        increment = 0 
        next_child_slug=""
        pri_child_slug=""
        inTerger=int(upDown)
        for n in range(len(childExercises_slug_data)):
            # if inTerger>0
            dataNavigation=input("enter the next/previous:-")
            if dataNavigation=='next':
                
                input_slug=""
                for k in range(0,len(my_data_couses)):
                # print(k,my_data_couses[k]["name"])

                    if my_data_couses[k]["name"] == store_option :
                        # for j in range(len(my_data_couses[k])):
                        
                        var=my_data_couses[k]["childExercises"]
                        # print(var,"asdfghjk santi")
                        input_slug=var[inTerger+1]["slug"]
                        # print(input_slug,"qqqqqqqqwertyuiop")

                        for i in (childExercises_slug_data):
                            
                            if  i == input_slug:

                                child_slug=requests.get("http://saral.navgurukul.org/api/courses/"+str(list_id[course_id])+"/exercise/getBySlug?slug="+input_slug)
                                my_child_slug_file=json.loads(child_slug.text)
                                child_content=my_child_slug_file["content"]
                                print(child_content)
                        inTerger=inTerger+1
            elif dataNavigation== "previous" : 
                # inTerger=int(upDown)
                input_slug=""
                for k in range(0,len(my_data_couses)):
                # print(k,my_data_couses[k]["name"])

                    if my_data_couses[k]["name"] == store_option :
                        # for j in range(len(my_data_couses[k])):
                        
                        var=my_data_couses[k]["childExercises"]
                        # print(var,"asdfghjk santi")
                        input_slug=var[inTerger-1]["slug"]
                        # print(input_slug,"qqqqqqqqwertyuiop")

                        for i in (childExercises_slug_data):
                            
                            if  i == input_slug:

                                child_slug=requests.get("http://saral.navgurukul.org/api/courses/"+str(list_id[course_id])+"/exercise/getBySlug?slug="+input_slug)
                                my_child_slug_file=json.loads(child_slug.text)
                                child_content=my_child_slug_file["content"]
                                print(child_content)
                        inTerger=inTerger-1
                        
            else:
                print("Page not found")
                break
        
        
    child_data()
my_availableCourse()                             
