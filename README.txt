Group:
-Dora Tan, dora.tan@ucalgary.ca
-Karmvir Singh Dhaliwal, karmvir.dhaliwal@ucalgary.ca
-Ranadip Chatterjee, ranadip.chatterjee@ucalgary.ca


HOW TO RUN WEBSITE:

1. Install Python 3.9 (Newest updated Python)
2. Install Gitbash (https://gitforwindows.org/)
3. Download folders from Github
4. Unzip downloaded package
5. Open Gitbash and locate Community-main
6. In dir with community_website & virt run the following command to activate the virtual environment:
	source virt/Scripts/activate

7. pip install django (for latest version)
8. pip install pillow
9. Move into community_website folder - should see the manage.py file
10. Run the server using the following command: 
	python manage.py runserver

11. On web browser go to localhost:8000
12. Website should be up
	To access Admin page: goto localhost:8000/admin
		Admin Username: admin
		Admin Password: admin@123456

13. Deactivate virtual environment when done using:
	deactivate


Troubleshooting:
If the above does not work, you will need to change the python path to match where you installed pyton on your own device.

1. Find the path where your python.exe is installed in your own system 
2. Copy that path
3. Go into community-main/virt/ and open pyvenv.cfg in any editor and paste the path from step 1 into the file and save


What we have available on the website:
-User login, logout and registration
-Search service providers
-Add services to the website
