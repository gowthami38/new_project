from config.next_gen_lead_config import *


# Model for data base table
class ProductEnquiry(Base):
    """ Product enquiry form model which has all details -table names & columns"""
    __tablename__ = "productenquiry"
    createdDate = Column("createddate", String)
    dealerCode = Column("dealercode", String)
    customerName = Column("customername", String)
    mobileNumber = Column("mobilenumber", Integer, primary_key=True)
    emailId = Column("emailid", String)
    vehicleModel = Column("vehiclemodel", String)
    state = Column("state", String)
    district = Column("distric", String)
    city = Column("city", String)
    existingVehicle = Column("exstingvehicle", String)
    wantTestDrive = Column("wanttestdrive", BOOLEAN)
    dealerState = Column("dealerstate", String)
    dealerTown = Column("dealertown", String)
    dealer = Column("dealer", String)
    briefAboutEnquery = Column("briefaboutenquery", String)
    expectedDateOfPurchase = Column("expecteddateofpurchase", String)
    gender = Column("gender", String)
    age = Column("age", Integer)
    occupation = Column("occupation", String)
    intendedUsage = Column("intendedusage", String)
