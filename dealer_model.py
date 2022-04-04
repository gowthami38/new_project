from config.next_gen_lead_config import *


class Dealer(Base):
    """ Dealer model which has all details -table names & columns"""
    __tablename__ = "dealer"
    dealerName = Column("dealername", String, primary_key=True)
    dealerCode = Column("dealercode", String)
