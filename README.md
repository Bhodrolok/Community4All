<h1 align="center">Community - Neighboorhood Services</h1>

<p align="center">Related Course: CPSC 571 - Design and Implementation of Database Systems</p>

<p> Mobile friendly web‑based app that acts as an online community posting board for services offered by residents living the neighborhood such
as babysitting, tutoring, catering, and plumbing services with options for service receivers to provide ratings and comments.

<br></br>

# Starting the Application
1. Install Python 3.9 (Newest updated Python). <br>
2. Install Gitbash (https://gitforwindows.org/). <br>
3. Download folders from Github. <br>
4. Unzip downloaded package. <br>
5. Open Gitbash and locate Community-main. <br>
6. In dir with community_website & virt run the following command to activate the virtual environment: `source virt/Scripts/activate` <br>
7. pip install django (for latest version). <br>
8. pip install pillow. <br>
9. Move into community_website folder - should see the manage.py file. <br>
10. Run the server using the following command: `python manage.py runserver` <br>
11. On web browser go to localhost:8000. <br>
12. Website should be up. <br>
        To access Admin page: goto localhost:8000/admin <br>
            Admin Username: admin <br>
            Admin Password: admin@123456 <br>
13. Deactivate virtual environment when done using: `deactivate`.

<br></br>

# Troubleshooting
If the above installation process does not work, you will need to change the python path to match where you installed pyton on your own device.

1. Find the path where your python.exe is installed in your own system. <br>
2. Copy that path. <br>
3. Go into `community-main/virt/` and open `pyvenv.cfg` in any editor and past the path from step 1 into the file and save.

<br></br>

# Built With
- Python
- Django

<br></br>

# Functionalities Implemented
- Acocunt registration
- Login to valid/created accounts
- User logout
- Search for services by name or service providers
- Logged in users may add additional service listings 

<br></br>

# Authors

[**Ranadip Chatterjee**](https://github.com/oBhodrolok)

[**Dora Tan**](https://github.com/DoughraT)
