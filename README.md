
# College Website

This website is a student website that uses HTML CSS js django.


## Installation 

### installing python3

```bash 
  sudo apt install python3-pip

```
### Installation virtual environment wrapper and using install
```
sudo pip3 install virtualenvwrapper
```

#### Specify where the virtual environment will be live
```
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh

```    

#### reloading the startup file

```
source ~/.bashrc
```



#### How to make a virtualenvs

```
mkvirtualenv <name of your virtual environment>
```
### For windows
```
python -m virtualenv .
.\scripts\activate
```


### Installing Django

```
pip3 install django~=3.1
```

#### Starting up a PROJECT

```
django-admin startproject <name of your project>
cd <name of your project>
```


#### Setting up the server
```
python manage.py runserver
```
