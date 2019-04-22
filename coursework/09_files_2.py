content_list = ["Mike" , "Joe" , "saber"]

content = '\n'.join(content_list)

myfile = open("09_employees.txt" , "w") #w = write (new file)
                                        #a = append (existing file)
                                        #a+= append(support read/write)
                                            #take care of where is the cursor
myfile.write(content)#does not over write existing data
myfile.close()

with open("09_example.txt","w") as myfile : #with close the file for you
    myfile.write("something")

'''
from : https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/

with something_that_returns_a_context_manager() as my_resource:
    do_something(my_resource)
    print('done using my_resource')

#resources can be threads
#--------
That's it! Using with, we can call anything that returns a context manager (like the built-in open() function). 
We assign it to a variable using ... as <variable_name>. 
Crucially, the variable only exists within the indented block below the with statement. 
Think of with as creating a mini-function: we can use the variable freely in the indented portion, 
but once that block ends, the variable goes out of scope. 
When the variable goes out of scope,it automatically calls a special method 
that contains the code to clean up the resource.
 
the wording of it is wrong. 
In the case of the file-opening context manager, 
it called f.close() in the cleanup which doesn't take the file variable f itself out of scope, 
it just removes the IO handle to the file so you can't e.g. read or write to it anymore.
'''
