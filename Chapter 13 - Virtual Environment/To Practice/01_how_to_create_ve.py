"""
   Steps:-
1. Open terminal and write ->> virtualenv myproject1 
2. Your virtual environment will tak some time and after few time it will start showing also
3. Similarly create a another virtual environment with name --->> myproject2
4. Now lets activate the myproject1 environment to do this u have to write --> myproject1/Scripts/activate
5. Now we have to install some pip modules for test purpose so for this write ---> 
                    pip install black
                    pip install playsound
                    pip install emoji
                    
6. Now we have some pip modules in our brand new environment. 

Q. But....what if we want to install all this modules in our other environment too ?
Ans So for this we have a very good modules which is called freeze.

   Steps to clone modules :-
1. Be on the desired environment from which you want to clone modules
2. Write -->      pip freeze > anyname.txt
   in the terminal
3. Doing the above thing will generate a txt file which will have all the modules name in that 
4. Now move to the environment where you want to install all the modules
5. Wrtite --> pip install -r anyname.txt
6. Enjoy !! It will install all the modules for you from that file
"""
