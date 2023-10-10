# powershell (getting started )


#content 
# 1. Dont fear the shell 
# 2. the help system 
# 3. the pipeline : getting connected 
# 4. Extended the shell 
# 5. Objects for the Admin 
# 6. The pipeline :Deeper 
# 7. the power in the shell - remoting 
# 8. Getting prepared for automation
# 9. Automation in scale 
# 10 . introducing scripting and toolmaking 


# target audience 
# IT pro 


# Suggested prerequisities / Supporting Material 
# Experience working as a Windows IT pro / Admin/ Help Desk
# Get answers in the forums  at PowerShell.Org 
# Checkout " Learn Windows Powershell 3 in a Month of Lunnches " by Don Jones and jeffery Hicks 




# join the mva community
# free online learning tailored for IT pro and developers 
# up-to-date relevevnt  training on variety of microsoft products 


# earn while you learn  
# get 50 mva points for this event 
# visit  .................
# enter thee code : powerjump 


# the purpose  to powershell 
# improved management  andautomation i.e there are peojects you have doone ... its have been a chaalnge everyone has some tools  
# manage large scale 



# i wanna talk about that whenever try to find and open poershell i find tha there are a various versins offhtem of them and i wonder wha tare the meaning of 32 , 64 that are written beside them 
# # well that means  versions 32 , 64 so that means powershell for 32 , 64 bit version .
# so if our system is 64 bit we will run 64 bit version of powershell , if our system is 32 bit then we wil runthe 
# 32 bit version of powershell .





# lets talk about how you will reconnize that the powershell that is launched that is administrator one or the normal .
# i will say here is two difference 
# when he powershell will open in the administrator mode at the title of the window it will show "administrator : poershell"
# and it can only be open by clicing on the "run as a administrator button" 
# and the title will show  only "powershell" when it on its normal version . 

# what is the advantage of administrator mode ?




# lesson 1 : always adjust the console first before sitting on the work . 
# purpose : the console has be clear enoggh that your work is visible enogh . 
# so to do that go to properties and we are gonna adjust the console .
# under fonts lets use that is nice ,bold , thick and give you a good comfie view.
# one tip: dont expand your powershell window beyond the size of your screen as sometimes based on what you are asking 
# powershell prefers  to show info on the right but sometimes on the left so for that case you wanna keep that balanced . 
# the layout whwre you adjust your screen .







# lets go into hacker mode # tell me , how the powershel is made ?
# cmd + .net + c# ==> powershell .
# getting familiar with powershell 
# cmdlets : Verb - noun
# Native commands work !
# examples -- ping, IPCconfig , calc , notepad , mspaint .
# cls- clear -host 
# cd -- set-location 
# dir, is -- Get-Childitem
# Copy, cp-- Copy-item 
#type, cat=Get-content 





# cmd means command let -- you needed to  come up with your own commands not the windows native ones .
#  why the name is command let -- there is two answers to that -- 24:25: powershell for begginners need to hear that out 




                    # what are the significance of cmd let

                    # CMD or Command Prompt is a command-line interpreter used in Windows operating systems to execute commands and scripts. It allows users to interact with the operating system through a text-based interface. CMD lets are specific commands that can be used in Command Prompt to perform specific tasks. Here are some significant CMD lets and their uses:

                    # CD (Change Directory) - This CMD let allows you to change the current working directory to a different folder. For example, "CD C:\Program Files" will change the current directory to the Program Files folder.

                    # DIR - This CMD let displays a list of files and folders in the current directory.

                    # MD (Make Directory) - This CMD let allows you to create a new directory or folder. For example, "MD NewFolder" will create a new folder named NewFolder in the current directory.

                    # RD (Remove Directory) - This CMD let allows you to delete a directory or folder. For example, "RD OldFolder" will delete a folder named OldFolder in the current directory.

                    # COPY - This CMD let allows you to copy files from one location to another. For example, "COPY C:\file.txt D:\Backup" will copy the file.txt from the C drive to the Backup folder on the D drive.

                    # XCOPY - This CMD let allows you to copy files and folders, including subdirectories, from one location to another. For example, "XCOPY C:\Source D:\Destination /E /H /C /I" will copy the Source folder and its subdirectories to the Destination folder on the D drive.

                    # TASKLIST - This CMD let displays a list of all currently running processes on the computer.

                    # TASKKILL - This CMD let allows you to terminate a running process. For example, "TASKKILL /F /IM process.exe" will forcefully terminate the process named process.exe.

                    # CMD lets are powerful tools that can be used to automate tasks and perform advanced system configurations. They are especially useful for system administrators and power users who need to perform tasks quickly and efficiently.




                    # aloke.geek@gmail.com
                    # more on above answer and dont repeat the same points 
                    # Sure, here are some more details on the significance of CMD lets:

                    # IPCONFIG - This CMD let displays the current IP configuration of your network, including your IP address, subnet mask, and default gateway. It can also be used to release and renew IP addresses and to flush the DNS resolver cache.

                    # NETSTAT - This CMD let displays active network connections, including TCP and UDP ports, the status of each connection, and the process ID of the application using the connection. It can be used to troubleshoot network connectivity issues and identify potential security risks.

                    # PING - This CMD let sends a small packet of data to a specified IP address or hostname to test network connectivity. It can be used to check whether a network device is reachable and to measure the response time.

                    # TRACERT - This CMD let traces the route that packets take from your computer to a specified destination, showing each hop along the way. It can be used to diagnose network latency and routing issues.

                    # SYSTEMINFO - This CMD let displays detailed system information, including the operating system version, installed hotfixes, hardware configuration, and system uptime. It can be used to diagnose hardware or software compatibility issues.

                    # GPRESULT - This CMD let displays the result of the group policy settings applied to the current user or computer. It can be used to diagnose group policy issues and to verify that policy settings are being applied correctly.

                    # SCHTASKS - This CMD let allows you to schedule tasks to run at specific times or intervals. It can be used to automate routine tasks or to perform maintenance tasks during off-hours.

                    # Overall, CMD lets provide a flexible and powerful way to interact with Windows operating system and perform a variety of tasks. Learning how to use CMD lets effectively can be a valuable skill for system administrators, developers, and power users.




                    # aloke.geek@gmail.com
                    # what are the pipelines in the cmd 
                    # In Command Prompt, pipelines are used to combine multiple commands to perform a more complex operation. A pipeline takes the output of one command and uses it as the input for the next command, allowing you to chain together multiple commands to achieve a desired result. The pipeline operator is represented by the vertical bar character "|".

                    # Here's an example of how pipelines can be used in Command Prompt:

                    # Suppose you want to find all files in a directory that have the .txt extension and then search for a specific word within those files. You could use the following pipeline:

                    # arduino
                    # Copy code
                    # DIR *.txt /S /B | FIND "searchterm"
                    # This pipeline first uses the DIR command to list all files in the current directory and its subdirectories that have the .txt extension, and outputs the result to the console. The /S switch tells DIR to include subdirectories, and the /B switch tells it to output only the file names. The output is then piped to the FIND command, which searches for the specified searchterm within each file and outputs any matches to the console.

                    # Pipelines can be used to combine any number of commands to perform more complex operations, making them a powerful tool for automating tasks and manipulating data in Command Prompt.




                    # aloke.geek@gmail.com
                    # what is the name of "c#" in programming 
                    # The name of the programming language "C#" is pronounced as "C sharp". The "#" symbol in the name is also referred to as the "sharp" symbol, hence the name "C sharp". C# is a modern, multi-paradigm programming language developed by Microsoft that is designed to be simple, efficient, and type-safe. It is widely used for developing a variety of applications, including desktop, web, and mobile applications, as well as games and other software.




                    # aloke.geek@gmail.com
                    # is c sharp is different from c and c++
                    # Yes, C# (pronounced "C sharp") is a different programming language from C and C++. While C# shares some similarities with C and C++, such as syntax and some programming concepts, it is a distinct language with its own unique features and capabilities.

                    # C# was developed by Microsoft in the early 2000s as a modern, object-oriented programming language designed for building applications on the Microsoft .NET Framework. It was influenced by several programming languages, including C++, Java, and Delphi, but it also introduced new features and concepts, such as garbage collection, delegates, and lambda expressions.

                    # C, on the other hand, is a procedural programming language that was developed in the early 1970s, and it is often considered one of the foundational languages of modern computing. C++ is a later extension of C that introduced object-oriented programming concepts, such as classes and inheritance.

                    # While C, C++, and C# share some similarities, they have different syntax, programming paradigms, and use cases. C is typically used for low-level programming, such as operating systems and embedded systems, while C++ is often used for system-level programming, such as device drivers and game engines. C# is often used for building Windows applications, web applications, and games, among other things.


 
 
#if we want t ochange the current directory location to the previous directory location 
# we will type in --> cd\
# if we want/need to see directory list 
# we will type in --> dir
# cler the screen 
# cls 



# if we want to make directories then we will type in 
# mk dir <directory name>



#if you want help 
#tyoe --> help



# if you want to open calculator 
# type --> calc

# what is ipconfig /all


# why should we use powershell over cmd ? the idea is open up powershell donot open up the command prompt 
# bcz yo are going to start then learning the command lets/ cmd is also compressed and integrated into powershell
# so in that way if you start with powershell you will be learning both at the same time and you learning curve will be much smoother .



# what are alias in powershell ?
            # what are alias in powershell ?
            # In PowerShell, an alias is a shortcut or shorthand way of referring to a command or a set of commands. An alias can be a single letter, a word, or a combination of characters that is assigned to a longer command or sequence of commands.

            # Aliases are commonly used to save time and increase productivity by providing a shorter and more convenient way of executing frequently used commands. For example, instead of typing "Get-ChildItem" every time you want to list the contents of a directory, you can create an alias for it, such as "ls" or "dir", and use the alias instead.

            # PowerShell comes with a set of default aliases that are pre-defined for commonly used commands. You can also create your own custom aliases using the New-Alias cmdlet. Aliases can be viewed, created, and removed using the Get-Alias, Set-Alias, and Remove-Alias cmdlets.

            # It's worth noting that while aliases can be useful, they can also be confusing if overused or if they obscure the underlying command. It's important to use aliases judiciously and to ensure that they are clear and unambiguous.




            # aloke.geek@gmail.com
            # more on above answer and dont repeat the same points 
            # In addition to providing a shorter way of executing commands, aliases in PowerShell can also be used to make commands more readable and easier to remember. For example, you could create an alias for a complex or lengthy command that you use frequently, and assign it a more memorable or descriptive name.

            # Aliases can also be used to override or replace existing commands, which can be useful if you want to customize or extend the functionality of a particular command. For example, you could create an alias for the "Get-ChildItem" command that includes additional parameters or options that are not available in the default command.

            # Another use for aliases in PowerShell is to provide compatibility with other command-line interfaces, such as the Command Prompt or Unix shells. PowerShell supports a number of common aliases that are used in these other interfaces, which can make it easier for users to transition to PowerShell.

            # It's worth noting that aliases in PowerShell are case-insensitive, so "ls" and "LS" would refer to the same alias. However, it's a good practice to use consistent casing when defining aliases to avoid confusion.

            # Finally, it's important to remember that while aliases can be a useful tool in PowerShell, they should be used judiciously and with caution. Overuse of aliases can make scripts and commands harder to read and understand, and can lead to errors and confusion. As with any tool, it's important to use aliases in a responsible and effective manner.




            # aloke.geek@gmail.com
            # when i should consider the use of alias 
            # You should consider using an alias in PowerShell when:

            # You find yourself typing the same command or sequence of commands repeatedly. In this case, an alias can save time and improve efficiency by providing a shorter way to execute the command.

            # You are working with a complex or lengthy command that is difficult to remember or type. In this case, an alias can make the command more readable and easier to remember.

            # You want to customize or extend the functionality of a particular command. In this case, an alias can provide a way to override or replace the existing command with a new command that includes additional parameters or options.

            # You want to provide compatibility with other command-line interfaces. In this case, using common aliases can make it easier for users to transition to PowerShell and to work with commands that they are already familiar with.

            # It's worth noting that while aliases can be a useful tool in PowerShell, they should be used judiciously and with caution. Overuse of aliases can make scripts and commands harder to read and understand, and can lead to errors and confusion. As with any tool, it's important to use aliases in a responsible and effective manner.




            # aloke.geek@gmail.com

            # more on above answer and dont repeat the same points 
            # Here are some additional points to consider when deciding whether to use aliases in PowerShell:

            # When using aliases, it's important to choose a name that is clear, unambiguous, and easy to remember. Avoid using names that are too short or too generic, as these can be confusing or easily forgotten. Similarly, try to avoid using names that are too similar to existing commands, as this can lead to mistakes and errors.

            # You should also consider whether an alias is appropriate for the particular command or sequence of commands that you are working with. Some commands may be too complex or too specific to be effectively replaced by an alias, while others may be simple and straightforward enough to benefit from an alias.

            # Another factor to consider is whether the use of an alias will improve or detract from the readability and maintainability of your scripts and commands. While aliases can save time and improve efficiency, they can also make scripts and commands harder to understand and modify, especially for other users who may not be familiar with the aliases that you have defined.

            # Finally, it's worth noting that aliases can be overridden or redefined by other users or scripts, which can lead to unexpected behavior and errors. To avoid this, it's important to use aliases in a consistent and well-documented manner, and to communicate any changes or updates to other users or team members who may be affected.


# gal g*
            # PS C:\Users\rekha> gal g*

            # CommandType     Name                                               Version    Source
            # -----------     ----                                               -------    ------
            # Alias           gal -> Get-Alias
            # Alias           gbp -> Get-PSBreakpoint
            # Alias           gc -> Get-Content
            # Alias           gcb -> Get-Clipboard                               7.0.0.0    Microsoft.PowerShell.Management
            # Alias           gci -> Get-ChildItem
            # Alias           gcm -> Get-Command
            # Alias           gcs -> Get-PSCallStack
            # Alias           gdr -> Get-PSDrive
            # Alias           gerr -> Get-Error
            # Alias           ghy -> Get-History
            # Alias           gi -> Get-Item
            # Alias           gin -> Get-ComputerInfo                            7.0.0.0    Microsoft.PowerShell.Management
            # Alias           gjb -> Get-Job
            # Alias           gl -> Get-Location
            # Alias           gm -> Get-Member
            # Alias           gmo -> Get-Module
            # Alias           gp -> Get-ItemProperty
            # Alias           gps -> Get-Process
            # Alias           gpv -> Get-ItemPropertyValue
            # Alias           group -> Group-Object
            # Alias           gsn -> Get-PSSession
            # Alias           gsv -> Get-Service
            # Alias           gtz -> Get-TimeZone                                7.0.0.0    Microsoft.PowerShell.Management
            # Alias           gu -> Get-Unique
            # Alias           gv -> Get-Variable

            # PS C:\Users\rekha>


# what if i did --> gal *sv 


            # #PS C:\Users\rekha> gal *sv

            # CommandType     Name                                               Version    Source
            # -----------     ----                                               -------    ------
            # Alias           epcsv -> Export-Csv
            # Alias           gsv -> Get-Service
            # Alias           ipcsv -> Import-Csv
            # Alias           sasv -> Start-Service
            # Alias           spsv -> Stop-Service
            # Alias           sv -> Set-Variable

            # PS C:\Users\rekha>


# gal sa*
            # PS C:\Users\rekha>  gal sa*

            # CommandType     Name                                               Version    Source
            # -----------     ----                                               -------    ------
            # Alias           sajb -> Start-Job
            # Alias           sal -> Set-Alias
            # Alias           saps -> Start-Process
            # Alias           sasv -> Start-Service

            # PS C:\Users\rekha>
            
# now by showing you these three commands i want you to notice the trend of words with output.
# whats the point is if you being a little thoughtful then you could  use all of it pretty easily .
# not only that it will be very easy for you to search through things . 
 


37:40


















