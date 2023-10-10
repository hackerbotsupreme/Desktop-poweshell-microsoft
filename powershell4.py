# topic 3 # getting connected  with pipeline 
# module
# what's the pipeline ? what does it do?
# Exporting/importing  CSV
# Exporting importing  XML
# other files and printers 
# Displaying information in a gui
# making a webpage of information 
# |--> this is called pipe 
# type--> Get-service -name bits 
# take a guess of what what i could do if i wanted to stop this service 
# there's a command called stop-service 
# you can type in --> stop-service -name bits 
# here's an interesting thing i  can pipe it to stop service 
# type in --> Get-service -name bits |  stop-service 
# what's gonna happen is we're going to take bit service  then send it across those pipeline 
# stop-service gonna grab  a hold of that and do exaatly what it says it gonna do 
# it gonna stopo service 


# undrstanding pipeline is very important . and its crucially important to  troubleshooting stuffs .

# and again to start service --> 
# get-service -name bits || start-service -passthru


# now it's a simple pipeline but the concept of taking something sending across the pipeline and something else act on it 
# is very important and we can continue  to pipe to thing to next to next. 

# for example lets start out with some cool y=things 
# powershell is very very useful thing in tecnology. like, a very sharp knief now you can do so many things with it to make your life easy , but at the same point dont give it to kids , people as they can stab you with it and take everything away. 
# and that also keep in mind, if you not know to use the knief dont play with it bcz you may cut yourseelf unknowingly  , aand besides it doesnot ask you are you sure also it only waits till you hit the enter so it assumes you know what you are doing . 
# 
# type--> get-service 
# type--> get-service| stop-service 
# note what happens .




# to export csv  we can do .
# get-service | export-CSV -path c:\service.CSV
# notepad c:\service.CSV
# as we have just exported it so in order to use that data again we have place  right back so we wil import it . to do that -->
# import -CSV c:\service.CSV
            # that means take the information and export it to csv 
            # # what is csv file 
            # what are csv files 
            # CSV stands for Comma Separated Values, which is a file format used to store and exchange data in a simple tabular form. In a CSV file, data is organized into rows and columns, with each row representing a record and each column representing a field or attribute of that record.

            # Each value in a CSV file is separated by a delimiter, which is typically a comma (hence the name "Comma Separated Values"), but it can also be a semicolon or a tab. CSV files are plain text files that can be opened and edited using any text editor or spreadsheet software.

            # CSV files are commonly used for storing and exchanging data between different software applications, such as databases, spreadsheets, and programming languages. They are widely used in data analysis, data science, and machine learning tasks because they provide a simple and lightweight way to store and manipulate data.

# now all that data comes back and its formatted correctly . 
# great example you guys used to do onlije banking years ago .
            #you go the buy something and swipe the cresit card three days later it show up in your account .
            # today yu swipe it when's it show up in your account , as just you finish the swiping  
            # its xml baby  
# let's export xml files 
# get-process  | Export -clixml -Path  c:\good.xml
# 1:40 

