import m06_greet

"""If we do this -->> m06_greet.greet("Bisu")
   then if will give output like this ---> 
                                            Enter your name here : Biswajit
                                            Good Morning Biswajit !! #reason : The file as a whole is being run whenever it is called
                                            Good Morning Bisu !!
                                            
    Solution :  if __name__=="__main__": #reason -> If the program is running directly then the [__name__] will return [__main__] and when the file is called by some other program to be used then the name fx will return the file name of that file hence making the if condition false
                    name = input("Enter your name here : ")
                    greet(name)"""

m06_greet.greet("Bisu")
