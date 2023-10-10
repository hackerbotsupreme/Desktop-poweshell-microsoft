# get-help get-service -Showwindow 
# opens up a window .
# on upside of that window you can find stuffs .




# a lot of times a lot of guys would do  you will open two powershell so you do help in one 
# then you can work in another one .



# keep in mind as there are paremeters there is arguments as well . 



# sometimes you want commandlet to alter its output or alter its output 
# change what its actually doing for you . like get-service is great but its gonna give you you the list of all the service .
# maybe i want the one with bits . so the syntax of the command will explain to you the options that are available .
# type in --> get-service  -Name bits 
# now instead of giving me whole list it will give me one with bits and here - is signifies parameter and bits is valiue 
# and a lot of parameters take mltiple arguments .let's show you what that look like 
# type in --> grt-service  -Name bits , bfe -->notice the comma 
# under the syntax in the window beside the arguments if you see [] then it could take multiple arguments .
# like -- Get-service [[-Name] <System.String[]>]  -- see the [] beside the string 


# let's do wildcards 
# get-service -name b*
# im ginna get all the services that ssstart with b .

# you can also do these 
# get-service -name b*,c*
# ao now i get both the ones begins with b's and c's .


#[[-Name] <System.String[]>]
# [-Exclude <System.String[]>] --> notice the difference here  for the first one there is [] for both parrameter and the argument 
# but for second one there's only one [] for both. and that means you dont have to use those its optional .
# wait we are not finished 

# syntax-->
# 1.Get-Service [-DependentServices ] -DisplayName <System.String[]> [-Exclude <System.String[]>] [-Include <System.String[]>] [-RequiredServices ] [<CommonParameters>]

# 2.Get-Service [-DependentServices ] [-Exclude <System.String[]>] [-Include <System.String[]>] [-InputObject <System.ServiceProcess.ServiceController[]>] [-RequiredServices ] [<CommonParameters>]

# 3.Get-Service [[-Name] <System.String[]>] [-DependentServices ] [-Exclude <System.String[]>] [-Include <System.String[]>] [-RequiredServices ] [<CommonParameters>]
# notice that 2 and 3 number syntax has [] these around them that means every single one of them is optinal .
# so all is i have to do type--> get service-->  that will get me the full lisst .
#  no parameters are required but  look at the 1st syntax see how--> -DisplayName <System.String[]> --> these does not have []
# well that means if you gonna need displayname you gotta put it in and you gotta give me a value .
# example --> get-service -Displayname "value (long one )"
# look at these 
# get-service b*
# you can already say displayname is very long and not possible to remember 
#  so type in --> get-service -Displayname Bit*
# and that it ! this will give you your required one .


# [[-Name] <System.String[]>]
#  |     |
# this are positional arguments . this something called positional parameters .
# so that means if you just specify the value you dont have to specify name .
# so that means 
# type --> get -service -name bits
# and then in the second line --> get-service bits --> means you dont have to type in -name thats what positional means .
# and this both will give the same answer .
# but we can take it a step further. 
# type--> gsv bits 


# and the revision 
# a dash(-) means that you have  a parameter .
# and followed by <> means you can put argument on it .
# and if its got [] then its can take multiple arguments seperated bya comma .
# and if the total is surrounded by [] then that's mean its optional you dont hav eto do it at all .
# and if the parameter is surrounded by [] then that means its a positional argument .


# you guys using the tab key --> to go back and forth on the commands that you typed in. 
# it cycle's through the things you typed in .



# letme show you another example of finding something as kind of a summery . finding a cmdlet then taking look at its 
# syntax then we are gonna show you how to start to put commandlets together on teh pipeline .
# get-help *eventlog*
# see the names of the event log and now to find out what they do we will look at the help file .
# get-help get-eventlog -detailed (also if i have any questions about the para meters i want to be able to see the definitions of those arameters )
#  type --> get-eventlog -logname press tab's to cyclethrough and find what you want . if you dont remember it .

            # # what is a log file 
            # A log file is a file that contains a record of events that have occurred on a computer system or within an application. It's used to keep track of system or application activity, including error messages, warnings, and other events that might be relevant to troubleshooting or monitoring the system's behavior.

            # Log files can be generated automatically by an operating system, software application, or web server, or they can be manually created by developers or system administrators. They typically contain timestamped entries, along with information such as the type of event that occurred, the severity of the event, and any additional details that might be relevant for diagnosing or addressing issues.

            # Log files can be valuable tools for debugging and troubleshooting software applications, identifying security issues or anomalies, and monitoring system performance over time. They can also be used to audit and analyze user behavior or application usage patterns.
# if i want to find 3 latest errors what i will type .
# get-eventlog -logname System -newest 3 -Entrytype error 
# this will give me 3 errors .
# now if i want to find 3 latest errors from 3 different computers what i will type.
#  # get-eventlog -logname System -newest 3 -Entrytype error  -Computername dc,s1,s2
# one more thing , 
# type in --> get-help *eventlog*
# and at the bottom you will see --> about-eventlog --> that's mean it is conceptual  topics .
# it is   conceptual  topics. so question is how do we access these ?
# type in --> cls ; help about_Event logs
# and then it clears the screen and shows mw about . 
# if you do --> type in -->  help about_*--> it gonna show you lots of about topics .
# look closely and you wil see -->about-wildcards, about-powershell_4.0,  about-powershell_ISE
# SO YOU  see making use of help system is really helpful .
# you can also do like--> get-help -category dfshj
            # PS C:\Users\rekha> get-help -category dfshj
            # Get-Help: Cannot validate argument on parameter 'Category'. The argument "dfshj" does not belong to the set "Alias,Cmdlet,Provider,General,FAQ,Glossary,HelpFile,ScriptCommand,Function,Filter,ExternalScript,All,DefaultHelp,DscResource,Class,Configuration" specified by the ValidateSet attribute. Supply an argument that is in the set and then try the command again.
            # PS C:\Users\rekha>
# oh, so we can type in --> get-help -category provider 

 

# 


 
# 