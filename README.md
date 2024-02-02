### Report CD assignment Miranda Little

I have set up a Virtual Private Server with Digital Ocean and made a folder on the server called "farm" and uploaded the files from my github repository to this folder using a ```git pull``` command. This includes a *main.py* file containing my Flask app and a *test_main.py* file with tests for the Flask app. 

In my github repository there is a *run-tests.yml* file in .github/workflows/. This file contains steps to install python and pytest in the Github Actions workspace. In the next section ```needs: run-tests``` makes sure that only when the test is successful the VPS is run.  

To securely log in to my VPS I've made secrets for the host, username, port and sshkey of the VPS in github which are accessed in the last part of the yml file:
````             
          host: ${{ secrets.HOST }}  
          USERNAME: ${{ secrets.USERNAME }}
          PORT: ${{ secrets.PORT }}
          KEY: ${{ secrets.SSHKEY }}
          script: sh bashcommands.sh
````

In the last line above I reference the *bashcommands.sh* file that is included in my repository, which includes several bash commands that are to be run on the VPS such as reading the *main.py* file and the command ```git pull``` to pull in any changes made to the code. The VPS server is then restarted. 

I have encountered problems with initializing git on my local computer and VPS and have found that to reverse initialization, the hidden *.git* folder should be removed. 

I have also encountered a problem logging into the VPS with the private SSH key I generated. The text on the top and bottom of the key ```-----BEGIN OPENSSH PRIVATE KEY-----``` and ```-----END OPENSSH PRIVATE KEY-----``` should be included in the secret on Github. 

In the bash commands file I at first didn't include the ```cd /home/farm/``` command to navigate to the directory where the *main.py* is situated and got an error that the file was not found. 