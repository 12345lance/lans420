from app import db
from app import User


db.create_all()
db.session.add(User( "ABSDCAAAS20","60","ABHYUDAYA NAGAR","ABHYUDAYA EDUCATION SOCIETY, OPP. BLDG. NO. 18, ABHYUDAYA NAGAR, KALACHOWKY, MUMBAI - 400033","MUMBAI","GREATER MUMBAI","MAHARASHTRA","ABHYUDAYA COOPERATIVE BANK LIMITED"))

db.session.commit()


print "hello"