ta = courses(baseUrl)
courses = data["name"]
ids = data["id"]
print(ids)
for j in range(len(courses)):
    print(j+1," "+courses[j])
     

def coursesDetails(baseUrl,id):
    userInput = int(input("Select your course :- "))
    print(id[userInput-1])
    url = baseUrl+"/courses/"+id[userInput-1]+"/exercises"
    req = requests.get(url)
    data = req.json()
    print(data)




coursesDetails(baseUrl,ids)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                