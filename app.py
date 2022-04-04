
from config.next_gen_lead_config import *
from models.dealer_model import *
from models.product_equiry_model import *


@app.route('/fetch-todays-leads', methods=['GET'])
def fetchTodaysLeads():
    """Returns the leads info for current date.."""
    log.info("fetchTodaysLeads : Started")
    dealer_result = []
    product_result = []
    dealercode = request.args.get('dealer_code')
    log.debug("dealer_code is {}".format(dealercode))

    try:
        dealer_result = session.query(Dealer).filter(Dealer.dealerCode == dealercode).all()
        log.debug("dealer_result is {}".format(dealer_result))

    except Exception as err:
        log.error("Error occured while dealer table sql transaction is {}".format(err))
        session.rollback()

    if dealer_result:
        try:
            product_result = session.query(ProductEnquiry).all()
            log.debug("product_result is {}".format(product_result))
        except Exception as err:
            session.rollback()
            log.error("Error occured while ProductEnquiry table sql transaction is {}".format(err))
        finally:
            session.close()
        product_result_dict = [item.__dict__ for item in product_result]
        log.debug("product_result_dict is {}".format(product_result_dict))
        for item in product_result_dict:
            del item['_sa_instance_state']
        log.info("fetchTodaysLeads : Ended")
        return jsonify(product_result_dict)
    else:
        log.info("fetchTodaysLeads : Ended")
        return "Unauthorized access"


@app.route('/del_single_record', methods=['DELETE'])
def del_record():
    log.info("fetchTodaysLeads : Started")
    mobile_number = request.args.get("mobile_number")
    log.debug("mobile_number is {}".format(mobile_number))
    try:
        product_results = session.query(ProductEnquiry).filter(ProductEnquiry.mobileNumber == mobile_number).all()
        log.debug("product_results is {}".format(product_results))
        if product_results:
            pass
        else:
            return "Mobile number - {} records doesn't exist".format(mobile_number)
    except Exception as err:
        log.error("Error occurred is {}".format(err))
        session.rollback()
    try:
        result = session.query(ProductEnquiry).filter(ProductEnquiry.mobileNumber == mobile_number).delete()
        log.debug("result is {}".format(result))
        session.commit()
        return "Record has been deleted successfully"
    except Exception as err:
        session.rollback()
    finally:
        session.close()


@app.route('/insert_records', methods=['POST'])
def insert_records():
    log.info("insert_records : Started")
    record = []

    request_body = request.get_json(force=True)
    log.debug("request_body is {}".format(request_body))
    try:
        for item in request_body:
            record = ProductEnquiry(customerName=item["customername"],
                                    gender=item["gender"],
                                    age=item["age"],
                                    occupation=item["occupation"],
                                    mobileNumber=item["mobileno"],
                                    emailId=item["emailid"], )

    session.add_all([record])
    session.commit()


@app.route('/getAllRecordsWithOutAnyCondition', methods=['GET'])
def getCustomRecords2112():
    log.info("getCustomRecords : Started")
    dealer_result = []
    product_result = []
    dealer_code = request.args.get('dealer_code')
    log.debug("dealer_code is {}".format(dealer_code))

    try:
        product_result = session.query(ProductEnquiry).all()
        log.debug("product_result is {}".format(product_result))
    except Exception as err:
        session.rollback()
        log.error("error occured while product enquiry table sql transaction is {}".format(err))
    finally:
        session.close()
    product_result_dict = [item.__dict__ for item in product_result]
    log.debug("product_result_dict is {}".format(product_result_dict))
    for item in product_result_dict:
        del item['_sa_instance_state']
        log.debug("product_result_dict is {}".format(product_result_dict))
        log.info("getCustomRecords : Ended")
        return jsonify(product_result_dict)


@app.route('/fecth_records', methods=['GET'])
def fetchRecords():
    log.info("fetchRecords : Started")
    myDict = request.args
    log.debug("mydict is {}".format(myDict))
    filter_condition = []
    product_result = []
    if "mobile_num" in myDict:
        filter_condition.append(ProductEnquiry.mobileNumber == request.args.get("mobile_num"))
    if "email_id" in myDict:
        filter_condition.append(ProductEnquiry.emailId == request.args.get("email_id"))
    if "state" in myDict:
        filter_condition.append(ProductEnquiry.state == request.args.get("state"))
        try:
            product_result = session.query(ProductEnquiry).filter(*filter_condition).all()
            return str(product_result)
        except Exception as err:
            session.rollback()
            log.error("error occured while product enquiry table sql transaction is {}".format(err))
        finally:
            session.close()
        product_result_dict = [item.__dict__ for item in product_result]
        log.debug("product_result_dict is {}".format(product_result_dict))
        for item in product_result_dict:
            del item['_sa_instance_state']
            log.debug("product_result_dict is {}".format(product_result_dict))
            log.info("fetchRecords : Ended")
            return jsonify(product_result_dict)
        else:
            log.info("fetchTodaysLeads : Ended")
            return "Unauthorized access"


@app.route('/generic-fetch', methods=['GET'])
def genericFetch():
    """Returns the leads info for current date.."""
    log.info("genericFetch : Started")

    filter_condition = []
    product_result = []

    myDict = request.args
    log.debug("mydict is {}".format(myDict))

    if "mobile_num" in myDict:
        filter_condition.append(ProductEnquiry.mobileNumber == request.args.get("mobile_num"))
    if "email_id" in myDict:
        filter_condition.append(ProductEnquiry.emailId == request.args.get("email_id"))
    if "state" in myDict:
        filter_condition.append(ProductEnquiry.state == request.args.get("state"))
    if "city" in myDict:
        filter_condition.append(ProductEnquiry.city == request.args.get("city"))
    if "district" in myDict:
        filter_condition.append(ProductEnquiry.district == request.args.get("district"))
    if "vehicleModel" in myDict:
        filter_condition.append(ProductEnquiry.vehicleModel == request.args.get("vehicle_model"))
    if "gender" in myDict:
        filter_condition.append(ProductEnquiry.gender == request.args.get("gender"))
    if "age" in myDict:
        filter_condition.append(ProductEnquiry.age == request.args.get("age"))
        log.debug("Filter condition is {}".format(filter_condition))
    try:
        product_result = session.query(ProductEnquiry).filter(*filter_condition).all()
        log.debug("product_result is {}".format(product_result))
    except Exception as err:
        session.rollback()
        log.error("Error occured while ProductEnquiry table sql transaction is {}".format(err))
    finally:
        session.close()
    product_result_dict = [item.__dict__ for item in product_result]
    log.debug("product_result_dict is {}".format(product_result_dict))
    for item in product_result_dict:
        del item['_sa_instance_state']
    log.info("fetchTodaysLeads : Ended")
    return jsonify(product_result_dict)


@app.route('/starts_record', methods=['GET'])
def startsRecord():
    """Returns the leads info for current date.."""
    log.info("startsRecord : Started")
    product_result = []
    mobile = request.args.get('mobile')
    log.debug("mobile is {}".format(mobile))

    try:
        product_result = session.query(ProductEnquiry).filter(
            ProductEnquiry.mobileNumber.like(mobile + '%')).all()
        log.debug("product_result is {}".format(product_result))

    except Exception as err:
        session.rollback()
        log.error("Error occured while ProductEnquiry table sql transaction is {}".format(err))
    finally:
        session.close()
        product_result_dict = [item.__dict__ for item in product_result]
        log.debug("product_result_dict is {}".format(product_result_dict))
        for item in product_result_dict:
            del item['_sa_instance_state']
        log.info("starts_record : Ended")
        return jsonify(product_result_dict)


@app.route('/ends_record', methods=['GET'])
def endsRecord():
    """Returns the leads info for current date.."""
    log.info("endsRecord : endsRecord")
    product_result = []
    mobile = request.args.get('mobile')
    name = request.args.get('name')
    log.debug("mobile is {}".format(mobile))
    log.debug("name is {}".format(name))

    try:
        product_result = session.query(ProductEnquiry).filter(
            ProductEnquiry.mobileNumber.like('%' + mobile), ProductEnquiry.customerName.like('%' + name)).all()
        log.debug("product_result is {}".format(product_result))

    except Exception as err:
        session.rollback()
        log.error("Error occurred while ProductEnquiry table sql transaction is {}".format(err))
    finally:
        session.close()
        product_result_dict = [item.__dict__ for item in product_result]
        log.debug("product_result_dict is {}".format(product_result_dict))
        for item in product_result_dict:
            del item['_sa_instance_state']
        log.info("starts_record : Ended")
        return jsonify(product_result_dict)


@app.route('/contains_record', methods=['GET'])
def containsRecord():
    """Returns the leads info for current date.."""
    log.info("containsRecord : endsRecord")
    product_result = []
    name = request.args.get('name')
    log.debug("name is {}".format(name))

    try:
        product_result = session.query(ProductEnquiry).filter(
            ProductEnquiry.customerName.like('%' + name + '%')).all()
        log.debug("product_result is {}".format(product_result))

    except Exception as err:
        session.rollback()
        log.error("Error occured while ProductEnquiry table sql transaction is {}".format(err))
    finally:
        session.close()
        product_result_dict = [item.__dict__ for item in product_result]
        log.debug("product_result_dict is {}".format(product_result_dict))
        for item in product_result_dict:
            del item['_sa_instance_state']
        log.info("containsRecord : Ended")
        return jsonify(product_result_dict)


@app.route('/patch_record', methods=['PATCH'])
def patchRecord():
    """Returns the leads info for current date.."""
    log.info("patchRecord : endsRecord")
    product_result = []
    name = request.args.get('name')
    log.debug("name is {}".format(name))

    try:
        product_result = session.query(ProductEnquiry).filter(
            ProductEnquiry.customerName == name).update[{"dealerCode": 'BANG00'}].all()
        log.debug("product_result is {}".format(product_result))

    except Exception as err:
        session.rollback()
        log.error("Error occured while ProductEnquiry table sql transaction is {}".format(err))
    finally:
        session.close()

        log.info("patchRecord : Ended")
        return "SUCCESS"


@app.route('/single_record', methods=['GET'])
def singleRecords():
    """Returns the leads info for current date.."""
    log.info("fetchTodaysLeads : Started")
    dealer_result = []
    product_result = []
    dealercode = request.args.get('dealer_code')
    log.debug("dealer_code is {}".format(dealercode))

    try:
        dealer_result = session.query(Dealer).filter(Dealer.dealerCode == dealercode).all()
        log.debug("dealer_result is {}".format(dealer_result))

    except Exception as err:
        log.error("Error occured while dealer table sql transaction is {}".format(err))
        session.rollback()

    if dealer_result:
        try:
            product_result = session.query(ProductEnquiry).all()
            log.debug("product_result is {}".format(product_result))
        except Exception as err:
            session.rollback()
            log.error("Error occured while ProductEnquiry table sql transaction is {}".format(err))
        finally:
            session.close()
        product_result_dict = [item.__dict__ for item in product_result]
        log.debug("product_result_dict is {}".format(product_result_dict))
        for item in product_result_dict:
            del item['_sa_instance_state']
        log.info("fetchTodaysLeads : Ended")
        return jsonify(product_result_dict)
    else:
        log.info("fetchTodaysLeads : Ended")
        return "Unauthorized access"


@app.route('/single_record', methods=['GET'])
def singleRecords():
    """Returns the leads info for current date.."""
    log.info("fetchTodaysLeads : Started")
    dealer_result = []
    product_result = []
    dealercode = request.args.get('dealer_code')
    log.debug("dealer_code is {}".format(dealercode))

    try:
        dealer_result = session.query(Dealer).filter(Dealer.dealerCode == dealercode).all()
        log.debug("dealer_result is {}".format(dealer_result))

    except Exception as err:
        log.error("Error occured while dealer table sql transaction is {}".format(err))
        session.rollback()

    if dealer_result:
        try:
            product_result = session.query(ProductEnquiry).all()
            log.debug("product_result is {}".format(product_result))
        except Exception as err:
            session.rollback()
            log.error("Error occured while ProductEnquiry table sql transaction is {}".format(err))
        finally:
            session.close()
        product_result_dict = [item.__dict__ for item in product_result]
        log.debug("product_result_dict is {}".format(product_result_dict))
        for item in product_result_dict:
            del item['_sa_instance_state']
        log.info("fetchTodaysLeads : Ended")
        return jsonify(product_result_dict)
    else:
        log.info("fetchTodaysLeads : Ended")
        return "Unauthorized access"


# Run the APP
app.run(debug=False)
