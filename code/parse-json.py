import json
 
with open("13.json") as infile:
    i = 0
    for line in infile:
        i +=1
        temp = json.loads(line)
        print(i)
        if temp.get('labels').get('namespace') == "thesis-edge-ho-ns":
            print(line)
            f = open("13only_namespace.json", "a")
            f.write(line)
            f.close()

# Opening JSON file
#f = open('test.json')
 
# returns JSON object as
# a dictionary
#data = json.load(f)
 
# Iterating through the json
# list
#for i in data['foo']:
    #print(i.get('labels').get('namespace'))
 #   if i.get('labels').get('namespace') == "tjosan":
  #      print(i)
 
# Closing file
#f.close()