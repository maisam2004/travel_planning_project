import os

uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)


os.environ.setdefault("IP","0.0.0.0")
os.environ.setdefault("PORT","5000")
os.environ.setdefault("SECRET_KEY","any_secret_key")
os.environ.setdefault("DEBUG","True")
os.environ.setdefault("DEVELOPMENT","True")
#os.environ.setdefault("DB_URL","postgresql://postgres:soor1993@localhost/travel_planning")
os.environ.setdefault("DATABASE_URL","postgres://jqlmmofnytqpko:1cb0882f86a7ac9d7c9b0750a16d5fb07fe6db9370327b75c0ebb434eda651d7@ec2-52-215-68-14.eu-west-1.compute.amazonaws.com:5432/d6lmh6qmtbmafa")
#os.environ.setdefault("DATABASE_URL","postgres://$(whoami)")


os.environ.setdefault("MAIL_SERVER",'smtp.gmail.com')
os.environ.setdefault('MAIL_PORT','587')
os.environ.setdefault('MAIL_USERNAME','maisam2004@gmail.com')
os.environ.setdefault("MAIL_PASSWORD","Soorarash2004")