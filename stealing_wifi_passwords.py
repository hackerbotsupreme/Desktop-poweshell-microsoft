# first open the command prompt (cmd) in administrator mode .
# then to see all the profiles type in -->
# netsh wlan show profile 
            # C:\Windows\System32>netsh wlan show profile

            # Profiles on interface Wi-Fi:

            # Group policy profiles (read only)
            # ---------------------------------
            #     <None>

            # User profiles
            # -------------
            #     All User Profile     : mobile
            #     All User Profile     : lucky
            #     All User Profile     : TP-Link_3068
            #     All User Profile     : TP-Link_2FD6
            #     All User Profile     : OPPO F17 Pro
            #     All User Profile     : aloke


            # C:\Windows\System32>
# then to see passwords 
# type in --> 
# netsh wlan export profile  folder=c:\ key=clear
# oopen up , file explorer.
# go to c drive then you will see the extra files .
# open them with notepad .
# find --> <keymaterial> --> that is their password. 
            # C:\Windows\System32> netsh wlan export profile  folder=c:\ key=clear

            # Interface profile "mobile" is saved in file "c:\Wi-Fi-mobile.xml" successfully.

            # Interface profile "lucky" is saved in file "c:\Wi-Fi-lucky.xml" successfully.

            # Interface profile "TP-Link_3068" is saved in file "c:\Wi-Fi-TP-Link_3068.xml" successfully.

            # Interface profile "TP-Link_2FD6" is saved in file "c:\Wi-Fi-TP-Link_2FD6.xml" successfully.

            # Interface profile "OPPO F17 Pro" is saved in file "c:\Wi-Fi-OPPO F17 Pro.xml" successfully.

            # Interface profile "aloke" is saved in file "c:\Wi-Fi-aloke.xml" successfully.


            # C:\Windows\System32>
# and if you get the following msg then that will mean you done something incorrect .


        # C:\Windows\System32>  netsh wlan export profile  folder=Users key=clear
        # Specified folder "Users" is invalid.One or more parameters for the command are not correct or missing.

        # Usage: export profile [name=]<string> [folder=]<string> [[interface=]<string>] [key=<string>]

        # Parameters:

        #     Tag             Value
        #     name          - Name of the profile to export.
        #     folder        - Name of the folder in which the profile XML files
        #                     will be saved.
        #     interface     - Name of the interface which has this profile configured.
        #     key           - To display the key in plain text, set key=clear.

        # Remarks:

        #     Saves the selected profiles into XML files in the specified folder.
        #     For each exported profile, the output file will be named as
        #     "Interface Name-Profile Name.xml".

        #     Parameters folder, name and interface are all optional. If profile
        #     name is given then the specified profile will be saved. Otherwise
        #     profiles on any interface will be saved.

        #     If the folder parameter is provided it must specify an existing folder
        #     accessible from the local computer. It can either be an absolute path,
        #     or a relative path to the current working directory. In addition, "."
        #     refers to the current working directory, and ".." refers to the parent
        #     directory of the current working directory. The folder name cannot be
        #     a UNC (Universal Naming Convention) path. By default profiles will be
        #     saved in the current working directory.

        #     If interface name is given, only the specified profile on the given
        #     interface will be saved. Otherwise all profiles with the given name
        #     on the system will be saved.

        #     If a key in plain text is required and the caller is local administrator,
        #     output XML file will include the key in plain text.
        #     Otherwise, the output XML file will include encrypted key.

        # Examples:

        #     export profile name="profile 1" folder=c:\profiles
        #         interface="Wireless Network Connection"
        #     export profile name="profile 2" folder=.
        #     export profile name="profile 3" folder=. key=clear


        # C:\Windows\System32>


# at last let's also learn about syntax.
# export profile [name=]<string> [folder=]<string> [[interface=]<string>] [key=<string>]
#                 name of profile to export which have to be string type .
#                                Name of the folder in which the profile XML files will be saved also have to be string type.
#                                                  Name of the interface which has this profile configured.
#Remarks:

#     Saves the selected profiles into XML files in the specified folder.
#     For each exported profile, the output file will be named as
#     "Interface Name-Profile Name.xml".

#     Parameters folder, name and interface are all optional. If profile
#     name is given then the specified profile will be saved. Otherwise
#     profiles on any interface will be saved.

#     If the folder parameter is provided it must specify an existing folder
#     accessible from the local computer. It can either be an absolute path,
#     or a relative path to the current working directory. In addition, "."
#     refers to the current working directory, and ".." refers to the parent
#     directory of the current working directory. The folder name cannot be
#     a UNC (Universal Naming Convention) path. By default profiles will be
#     saved in the current working directory.

#     If interface name is given, only the specified profile on the given
#     interface will be saved. Otherwise all profiles with the given name
#     on the system will be saved.

#     If a key in plain text is required and the caller is local administrator,
#     output XML file will include the key in plain text.
#     Otherwise, the output XML file will include encrypted key.                                                                              key           - To display the key in plain text, set key=clear.

# #                                
# #Examples:

#     export profile name="profile 1" folder=c:\profiles
#         interface="Wireless Network Connection"
#     export profile name="profile 2" folder=.
#     export profile name="profile 3" folder=. key=clear