import requests
import json
import os
import pprint
saral_url="http://saral.navgurukul.org/api/courses"

def response_url(url):
    response=requests.get(url)
    store=json.loads(response.text)
    with open ("courses.json", "w") as file:
        return store

store = response_url("http://saral.navgurukul.org/api/courses")
coursesIdList=[]
def saral_courses(data_load):

        for index in range(len(data_load['availableCourses'])):
                courses=data_load['availableCourses'][index]
                courses_name=courses['name']
                coursesId=courses['id']
                coursesIdList.append(coursesId)
                print(index+1,"-",courses_name,coursesId)
        return coursesIdList
# saral_courses()

if os.path.exists("coursesData.json"):
        data_load=read_file("coursesData.json")
        saral_courses(data_load)
        print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
else:
        request("coursesData.json")
        data_load=read_file("coursesData.json")
        saral_courses(data_load)
        print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

userInput=input("select courses - ")
def selectCourse():
        selecteCourseId=coursesIdList[userInput-1]
        return selecteCourseId
print (selectCourse())
print ("*****************************************************************")
# request(saral_url)

saral_url1= saral_url+"/"+ str(selectCourse()) +"/exercises"
print(saral_url1)
# saral_url2= saral_url+"/"+ str(selectCourse()) +"/exercises"


def requestExercises(url1):
        response= requests.get(url1)
        with open("exercises_"+str(selectCourse())+".json","w") as exercisesFile:
                exercisesFile.write(response.content)
        return response.json()
# requestExercises(saral_url1)
# pprint.pprint(requestExercises(saral_url1))


def read_file(f_read):
        with open("exercises_"+str(selectCourse())+".json","r") as exercisesFile:
                data_read=exercisesFile.read()
                data_load1=json.loads(data_read)
        return(data_load1)

# all_exercises=None
childExercise = []
exercisesSlugList=[]
def saral_exercises(data_lode1):


        available_exercises=data_lode1['data']
        for index in range(len(available_exercises)):
                exercises=available_exercises[index]

                all_exercises=exercises['parentExerciseId']
                # print all_exercises
                childExerciseList = exercises["childExercises"]
                childExercise.append(childExerciseList)
                if all_exercises !=[]:
                    exercises_name=exercises['name']
                    exercisesSlug=exercises['slug']
                    exercisesSlugList.append(exercisesSlug)
                print (index+1,"-",exercises_name)
        return childExercise
# saral_exercises()

# print ("********************************************************")



if os.path.exists("exercises_"+str(selectCourse())+".json"):
        data_lode1=read_file("exercises_"+str(selectCourse())+".json")
        saral_exercises(data_lode1)
        print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
else:

        requestExercises(saral_url1)
        data_lode1=read_file("exercises_"+str(selectCourse())+".json")
        saral_exercises(data_lode1)
        print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print ("*************************************************************")
