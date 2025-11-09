def suppress_alert():
    error_code = 4040
    retry_count = 4
    is_maintenance = False 

    check_alert = (error_code == 200      \
                   or error_code == 404)  \
                   or is_maintenance 
    
    print(check_alert)

suppress_alert()
