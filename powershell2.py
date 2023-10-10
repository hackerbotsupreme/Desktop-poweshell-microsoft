# 36:00

# from now on we will call each specefic command line a personalities .

# so if you type in 
# gal pwd # personality # so i will say this personality return this output 
# it gives me 
# PS C:\Users\rekha> gal pwd

        # CommandType     Name                                               Version    Source
        # -----------     ----                                               -------    ------
        # Alias           pwd -> Get-Location

        # PS C:\Users\rekha>
        
# oo, so when we type 
# gal 
            # # 
            # CommandType     Name                                               Version
            # -----------     ----                                               -------
            # Alias           ? -> Where-Object
            # Alias           % -> ForEach-Object
            # Alias           ac -> Add-Content
            # Alias           cat -> Get-Content
            # Alias           cd -> Set-Location
            # Alias           chdir -> Set-Location
            # Alias           clc -> Clear-Content
            # Alias           clear -> Clear-Host
            # Alias           clhy -> Clear-History
            # Alias           cli -> Clear-Item
            # Alias           clp -> Clear-ItemProperty
            # Alias           cls -> Clear-Host
            # .........................
# you can see there's is a ton of these .

# but the alias is very regular as well .
# gal g*
            # CommandType     Name                                               Version
            # -----------     ----                                               -------
            # Alias           gal -> Get-Alias
            # Alias           gbp -> Get-PSBreakpoint
            # Alias           gc -> Get-Content
            # Alias           gcb -> Get-Clipboard                               7.0.0.0
            # Alias           gci -> Get-ChildItem
            # Alias           gcm -> Get-Command
            # Alias           gcs -> Get-PSCallStack
            # Alias           gdr -> Get-PSDrive
            # Alias           gerr -> Get-Error
            # Alias           ghy -> Get-History
            # Alias           gi -> Get-Item
            # Alias           gin -> Get-ComputerInfo                            7.0.0.0
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
            # Alias           gtz -> Get-TimeZone                                7.0.0.0
            # Alias           gu -> Get-Unique
            # Alias           gv -> Get-Variable
# notice that all the g's start with get .
# from noticing the line  61 .
# what if we can do *sv .
# gal *sv
            # PS C:\Users\rekha> gal *sv

            # CommandType     Name                                               Version
            # -----------     ----                                               -------
            # Alias           epcsv -> Export-Csv
            # Alias           gsv -> Get-Service
            # Alias           ipcsv -> Import-Csv
            # Alias           sasv -> Start-Service
            # Alias           spsv -> Stop-Service
            # Alias           sv -> Set-Variable

            # PS C:\Users\rekha>
# so g* to find commands starting with g . only g do not particularly stands for anything bcz there are many that starts with g.
# *sv  to find commands starting with sv. sv stands for service.            
# sp*  to find the commands strting eith sp and sp starts for stop.
# ps stands for process .
# again sa* to find the commands strting eith sa and sa starts with start .
# also notice the placement of  * sign depending upon starting or ending.
# trend , connect the trends with reasons then remember abd use them strategically .


# so the main agenda for you not to memorize things  but to be able to figuring out the route to get to where you want to go. 
# so that is why you should be processing thoughtfully and schematizingly


# a lot of time you will have a cmdlet and you wnna know what is alias for this ? 
# what are parameters in powershell.
                                # what are parameter in  powershell

                                # In PowerShell, a parameter is a value that is passed to a command or function in order to modify its behavior or provide it with additional information. Parameters can be specified when invoking a command or function by including them as part of the command line or by providing their values through the pipeline.

                                # PowerShell supports two types of parameters: named parameters and positional parameters. Named parameters are identified by a prefix of "-" followed by the parameter name, and their values are specified using the syntax "-ParameterName Value". Positional parameters, on the other hand, are identified by their position in the command line, and their values are specified without any prefix.

                                # In addition to named and positional parameters, PowerShell also supports other types of parameters such as switch parameters, which are used to specify true/false values, and dynamic parameters, which are generated dynamically by the command or function based on the context in which they are being used.

                                # You can use the built-in cmdlet "Get-Help" to learn more about the available parameters for a specific PowerShell command or function. For example, you can type "Get-Help Get-ChildItem" to view the help information for the "Get-ChildItem" command and its available parameters.
# we just gonna use a parameter called defination .
# we are gonna in --> get-alias -definition get-process
# it will tell me what the alias is available for 
#notice in this case 
                        # PS C:\Users\rekha> get-alias -definition get-process

                        # CommandType     Name                                               Version
                        # -----------     ----                                               -------
                        # Alias           gps -> Get-Process
                        # Alias           ps -> Get-Process

                        # PS C:\Users\rekha>
















# the help systeem
#module oerview 
# updateble help 
# discoveribility with the help system
# understanding system 
# real-world using help


# why you need help
# Don't  memorize - disscover .
# vast resources at ypur fingertips .
# scripting sources and information .



# updating help of our system 
# update-help -Force (well it does not work we need to find out which one does  )
# this used to pdate all the help content 



# you can also save them 
# by typing save help(whatever you have asked )


#get-help --> is used to get us help on stuffs / search on stffs 


# what is the differnce between get-help and help command in powershell?
#what is the differnce between get-help and help command in powershell?
                # In PowerShell, both Get-Help and Help commands are used to retrieve information about commands and topics in PowerShell.

                # The main difference between the two commands is that Get-Help is a PowerShell cmdlet, while Help is an alias for Get-Help. This means that Get-Help is the actual command that performs the help functionality, while Help is just a shorter alias for the same command.

                # Using either Get-Help or Help command followed by the command or topic name you want to learn about, will display a help file with information about the command or topic.

                # So, in summary, both Get-Help and Help are used to retrieve information about commands and topics in PowerShell, but Help is just an alias for Get-Help.
# type --> get-help get-service 
#scroll all the way to the bottom .
# i want you to notice scroll all the way to the bottom now watch the difference between 
# using help on the same thing 
# now type -->help get-service 
# look at the very bottom --> you will see a more <--
# which was not there for the previous one .
# and when there is more click space and you will move to the bottom furthur .
# man command doees the same thing -->  man get-service 
# that was our help system .
# that is actually a great tool learn to perfectly use it .





# first of all 'help' has the ability to discover stuffs 
# and i wanna see if there's any cmdlets that could help me work with 
# services by the way star is your friend it's your wild card 
# type --> get-help *service*
#


                # PS C:\Users\rekha>  get-help *service*

                # Name                              Category  Module                    Synopsis
                # ----                              --------  ------                    --------
                # Get-Service                       Cmdlet    Microsoft.PowerShell.Man… Gets the services on the computer.
                # New-Service                       Cmdlet    Microsoft.PowerShell.Man… Creates a new Windows service.
                # Remove-Service                    Cmdlet    Microsoft.PowerShell.Man… Removes a Windows service.
                # Restart-Service                   Cmdlet    Microsoft.PowerShell.Man… Stops and then starts one or more services.
                # Resume-Service                    Cmdlet    Microsoft.PowerShell.Man… Resumes one or more suspended (paused) services.
                # Set-Service                       Cmdlet    Microsoft.PowerShell.Man… Starts, stops, and suspends a service, and changes its properties.
                # Start-Service                     Cmdlet    Microsoft.PowerShell.Man… Starts one or more stopped services.
                # Stop-Service                      Cmdlet    Microsoft.PowerShell.Man… Stops one or more running services.
                # Suspend-Service                   Cmdlet    Microsoft.PowerShell.Man… Suspends (pauses) one or more running services.
                # Set-NetFirewallServiceFilter      Function  NetSecurity               …
                # Get-NetFirewallServiceFilter      Function  NetSecurity               …

                # PS C:\Users\rekha>
# it will show you all the cmdlets that have service on them .
# so we typed in get-help *service*
# let's put a g in the start 
# type in   get-help g*service*

                # PS C:\Users\rekha> get-help g*service*

                # Name                              Category  Module                    Synopsis
                # ----                              --------  ------                    --------
                # Get-Service                       Cmdlet    Microsoft.PowerShell.Man… Gets the services on the computer.
                # Get-NetFirewallServiceFilter      Function  NetSecurity               …

                # PS C:\Users\rekha>
# what happens is we filtered out that big list to the two here .
# that is what we wanna do (figuring things out / solving problems ) and that matters .
# knowing how to search things is great.




# type in --> get-help get-service --> this is the simple view with the help file .---> but this is not the full help.
#  we typed in get-help *service*
#  type in   get-help g*service*
# note how these three is working .


#  lets type --> get-help G*Adcomputer*--> bcz i want to work with active directory computers.
# now can see the options that can solve your problems but to be sure we need to see what they do.
# so to do that i will do 
# type in --> get-help get-adcomputer --> and takea look at 


# type in --> get-verb
# it will show you all the verbs so these are all the verbs 
# and we want to measure how many verbs are there ,so we type in --> get-verb |measure 
                # PS C:\Users\rekha> get-verb |measure

                # Count             : 100
                # Average           :
                # Sum               :
                # Maximum           :
                # Minimum           :
                # StandardDeviation :
                # Property          :


                # PS C:\Users\rekha>
# the deal is you gonna learn these 100 verbs .and learn those verbs then you are going to think type and get what you wanted .






# let's start getting into what these vebs can do for you .
# first, get-help g*service *
# second , get-help get-service 
# these are the simplified help view. 
# bbbut there is more to help just this once you updated help , this help will be extended or expanded upon .
# now watch , get-help get-service -Detailed (parameter:parameter changes how the cmdlet acts )
                # what is defination and whaat is parameter in powershell cmdlets 

                # In PowerShell, a cmdlet is a lightweight command that is used to perform a specific task. Cmdlets are designed to be easy to use and to work together in a pipeline.

                # A cmdlet consists of a verb and a noun separated by a hyphen, for example, Get-Process or New-Item. The verb describes the action that the cmdlet performs, while the noun describes the object that the cmdlet acts upon.

                # A parameter is a value that is passed to a cmdlet to modify its behavior. Parameters are enclosed in parentheses and can be specified by their name or by their position in the parameter list. For example, the Get-Process cmdlet accepts a parameter called -Name that allows you to specify the name of the process you want to retrieve:

                # arduino
                # Copy code
                # Get-Process -Name explorer
                # In this example, explorer is the value of the -Name parameter.

                # Cmdlets can have many different parameters, each of which modifies the behavior of the cmdlet in a specific way. For example, some cmdlets accept parameters that allow you to filter their output, while others accept parameters that allow you to specify the location of a file or folder. The exact parameters accepted by a cmdlet are documented in the cmdlet's help documentation.
# and remember that when you use the '-detailed' as a parameter then at the bottom we will see relevent examples .



# also if you want to directly look at the examples then there is also a parameter for that .
# type i n--> get-help get-service -Examples 
# also if you gonna do(this is a big deal)
# type in --> get-help get-service -full
# this is a little different than -definition bcz there's some imp and sensitive info  as this helps us understand how a command works  .


# here's also a crazy one 
# type in --> get-help get-service -online 
# opens up browser and takes me to the updated one where you can see full help for whatever it is you are looking for .


# get-help get-service -examples 
                        # PS C:\Users\rekha> get-help get-service -examples

                        # NAME
                        #     Get-Service

                        # SYNOPSIS
                        #     Gets the services on the computer.


                        #     --------- Example 1: Get all services on the computer ---------

                        #     Get-Service


                        #     --- Example 2: Get services that begin with a search string ---

                        #     Get-Service "wmi*"


                        #     --- Example 3: Display services that include a search string ---

                        #     Get-Service -Displayname "*network*"


                        #     Example 4: Get services that begin with a search string and an exclusion

                        #     Get-Service -Name "win*" -Exclude "WinRM"


                        #     ---- Example 5: Display services that are currently active ----

                        #     Get-Service | Where-Object {$_.Status -eq "Running"}

                        #     `Get-Service` gets all the services on the computer and sends the objects down the pipeline. The `Where-Object` cmdlet, selects only the services with
                        #     a Status property that equals `Running`.

                        #     Status is only one property of service objects. To see all of the properties, type `Get-Service | Get-Member`.
                        #     Example 6: List the services on the computer that have dependent services

                        #     Get-Service |
                        #       Where-Object {$_.DependentServices} |
                        #         Format-List -Property Name, DependentServices, @{
                        #           Label="NoOfDependentServices"; Expression={$_.dependentservices.count}
                        #         }

                        #     Name                  : AudioEndpointBuilder
                        #     DependentServices     : {AudioSrv}
                        #     NoOfDependentServices : 1

                        #     Name                  : Dhcp
                        #     DependentServices     : {WinHttpAutoProxySvc}
                        #     NoOfDependentServices : 1
                        #     ...

                        #     The `Get-Service` cmdlet gets all the services on the computer and sends the objects down the pipeline. The `Where-Object` cmdlet selects the services
                        #     whose DependentServices property isn't null.

                        #     The results are sent down the pipeline to the `Format-List` cmdlet. The Property parameter displays the name of the service, the name of the dependent
                        #     services, and a calculated property that displays the number of dependent services for each service.
                        #     ---------- Example 7: Sort services by property value ----------

                        #     Get-Service "s*" | Sort-Object status

                        #     Status   Name               DisplayName
                        #     ------   ----               -----------
                        #     Stopped  stisvc             Windows Image Acquisition (WIA)
                        #     Stopped  SwPrv              MS Software Shadow Copy Provider
                        #     Stopped  SysmonLog          Performance Logs and Alerts
                        #     Running  Spooler            Print Spooler
                        #     Running  srservice          System Restore Service
                        #     Running  SSDPSRV            SSDP Discovery Service
                        #     Running  ShellHWDetection   Shell Hardware Detection
                        #     Running  Schedule           Task Scheduler
                        #     Running  SCardSvr           Smart Card
                        #     Running  SamSs              Security Accounts Manager
                        #     Running  SharedAccess       Windows Firewall/Internet Connectio...
                        #     Running  SENS               System Event Notification
                        #     Running  seclogon           Secondary Logon


                        #     ------ Example 8: Get the dependent services of a service ------

                        #     Get-Service "WinRM" -RequiredServices


                        #     ---- Example 9: Get a service through the pipeline operator ----

                        #     "WinRM" | Get-Service



# line 362 , lets type this 
# run this 
# also ,type get-help get-service -Showwindow 
# this will open up a window now this has all of the great stuffs one of these is settings you can say hey i wanna just see this this and this .and ok .
# now go onthe timing 1;02;50 then you cantake the line like line 362 ,paste then the next one 
# so it will a great workflow .
# 






 




