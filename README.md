# Author: Niall Horgan

#

# Week 01 Task
# hello_world.py

A program that outputs the statement "Hello World".



## Week 02 Task
## bank.py

A program that read 2 integers in cents and outputs the sum of those integers in Euro format.

Here I just wanted to show separately the 3 different ways of creating output. 


### Week 03 Task 
### accounts.py

https://learnpython.com/blog/substring-of-string-python/#:~:text=Much%20like%20arrays%20and%20lists,substring%20of%20the%20original%20string.

A program that firstly reads in a 10 digit number and outputs first 6 numbers 
replaced with X's and final 4 numbers as they are.

Testing would be needed to ensure initial number is numeric and of length 10.
While above works, the input entered incorrectly, so can be entered as alphanumeric by mistake so result can still be incorrect.
This is because we are taking input as string and not int.




#### Task Week 04
#### collatz.py

A program that read an integer input and if even divides by 2, if odd it multiplys by 3 and adds 1.
It outputs each calculation successively, separated by a space until it reaches the number "1"

https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/

Input a positive integer
While not equal to 1 (when == 1 end calc)
If int is even -> divide by 2
If int is odd  -> multiply by 3 and add 1
Output successive calcs on 1 line separated by a space until program end



##### Week 05 Task
##### Author Niall Horgan
##### weekday.py

# Import datetime
Datetime was imported and used to tell us the day of the week it is
today = current_date.strftime("%A")
https://www.w3schools.com/python/python_datetime.asp

# Lists: 
2 lists are set up, 1 containing weekdays and 1 containing weekend days

# if today in weekdays:
An if statement to check through the "weekdays" list and if found print resulting statement
https://flexiple.com/python/python-list-contains/

# elif today in weekend:
If not fount in first list we then search through "weekend" list and print resulting statement



###### Week 06 Task
###### root.py

Source: chatgpt

Chatgpt used a slightly diffenent calculation to other Newtons method formula.
while abs(num - guess ** 2) > .0001:
Here it uses the calculation of the difference betweeen the number and the squre  of the initial guess and so on.

The code it came up with was in the form of a function so I just tweaked it around a bit to just have it as normal code

I searched almost 20 websites to see if i could find this calculation anywhere but wasnt able to find it.


# ####### Week 07 Task
# es.py

https://machinelearningmastery.com/command-line-arguments-for-your-python-script/
https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/

file_to_read = sys.argv[1]
We have to tell our program to take in an argument when our program is called
Here it will be moby_dick.txt

data.count() is used to count both lowercase 'e' and upper case 'E'.
Both of these figures are then added to print out our result



#
# ####### Week 08 Task
# ####### plottask.py

https://www.w3schools.com/python/python_ml_normal_data_distribution.asp
https://vitalflux.com/normal-distribution-explained-python-examples/?utm_content=cmp-true
https://www.youtube.com/watch?v=yj31agJRBoI

Plot a Normal Histogram with Mean of 10 and Standard Deviation of 2
The variables Mean: 'm' Standard Deviation: 'sd' can be amended at start of program for a different value of choosing.
m = 10
sd = 2

The size of this random sample is 1000 ad  can be altered inside the random call
norm_data = np.random.normal(m, sd, size=1000 )
