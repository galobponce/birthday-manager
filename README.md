# :birthday: Birthday Manager

## :raised_hands: Description:

A web application where each user can manage their own birthday's dates.

## :unlock: Features:

  - Log in, Register & Log out functions.
  - All users & its birthdays are saved in a database.
  - Mobile Responsive.
  - You can store, eliminate and search through your birthdays

## :wrench: Built with:

  - HTML
  - CSS
  - Bootstrap
  - JQuery
  - Flask
  - SQLite


## :camera: Demonstration:

### Desktop view

![register](https://github.com/galobponce/birthday-manager/blob/main/static/images/register.desktop.png)

![menu](https://github.com/galobponce/birthday-manager/blob/main/static/images/menu-dekstop.png)

### Mobile View

![homepage](https://github.com/galobponce/birthday-manager/blob/main/static/images/homepage-mobile.png)

![search](https://github.com/galobponce/birthday-manager/blob/main/static/images/search-mobile.png)

## :computer: Deployment on localhost:

  ### First Step:

  Download .zip file or clone the repo.

  ## Second Step:

  You should have installed _python_ and _pip_ / _pip3_ in your computer in order to deploy the proyect.
  
   ### Windows:
  
   - You can install pip dowloading [This pip installer](https://bootstrap.pypa.io/get-pip.py) and executing `python get-pip.py` on your windows terminal (with administrator permissions).
  
   ### Linux (Debian based distro):
  
   - You can install pip by executing `sudo apt install python-pip` or `sudo apt install python3-pip` on your terminal.
     
  ## Third Step:
  
  Execute `pip install -r requirements.txt`, so all libraries used on project's are installed on your computer.
  
  If that does not work, you can do `pip install <library>` to install each of all libraries from _requirements.txt_'s file
  
  ## Fourth Step:
  
  Execute `FLASK_ENV=development` to see possible errors, and then `flask run` on project's directory with your terminal to run app on localhost.
