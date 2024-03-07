import os

#Database Name: travel_planning
#Username: postgres

#Host: localhost (This indicates it's on your local machine)



os.environ.setdefault("IP","0.0.0.0")
os.environ.setdefault("PORT","5000")
os.environ.setdefault("SECRET_KEY","any_secret_key")
os.environ.setdefault("DEBUG", "False")

os.environ.setdefault("DEVELOPMENT","True")
os.environ.setdefault("DATABASE_URL","postgresql://postgres:soor1993@localhost/travel_planning")
#os.environ.setdefault("DATABASE_URL","postgres://jfcqrhoydzphod:4d0314094a1ca0c690eeb167012a7d1a8d713049b1c253f00df00084aeb07e5e@ec2-34-252-169-131.eu-west-1.compute.amazonaws.com:5432/d3b8nug5gq2t3s")
#os.environ.setdefault("DATABASE_URL","postgres://$(whoami)")


os.environ.setdefault("MAIL_SERVER",'smtp.gmail.com')
os.environ.setdefault('MAIL_PORT','587')
os.environ.setdefault('MAIL_USERNAME','maisam2004@gmail.com')
os.environ.setdefault("MAIL_PASSWORD","qtxd tmyq cerj qlgb")
