#my answer , and I think I need to sleep !

temperatures = [10, -20, -289, 100]

def c_to_f(c):
    f = [] 
    for item in c : 
        if item >= -273.15:
            f.append(str(item * 9/5 + 32))
    return f

content_list = c_to_f(temperatures)
content = '\n'.join(content_list)

#content = '\n'.join(map(str, content_list))

with open("14_practice_result.txt","w") as myfile : #with close the file for you
    myfile.write(content)

'''
#solution from course :

temperatures = [10,-20,-289,100]
 
def writer(temperatures, filepath):
    with open(filepath, 'w') as file:
        for c in temperatures:
            if c > -273.15:
                f = c* 9/5 + 32
                file.write(str(f) + "\n")
 
writer(temperatures, "14_practice_result.txt")
'''