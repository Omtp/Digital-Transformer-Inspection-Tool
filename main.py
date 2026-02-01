# DIGITAL TRANSFORMER INSPECTION AND MAINTENANCE TOOL
print("---------------------------")
print("| DIGITAL INSPECTION TOOL |")
print("---------------------------")
should_continue = True
while should_continue:
    items = ['OIL', 'TEMPERATURE', 'BREATHER', 'CLEANLINESS']
    feedback_list = []
    print("INSPECTION CHECKLIST")
    user_feedback_oil = input("Oil level within acceptable range? (Yes / No): ").upper()
    user_feedback_temperature = float(input("Record oil temperature (°C): "))
    user_feedback_breather = input("Breather condition satisfactory? (Yes / Saturated / No): ").upper()
    user_feedback_cleanliness = input("Transformer clean and free of oil leaks? (Yes / No): ").upper()

    if user_feedback_oil == "YES":
        issue_name = "PASS"
        feedback_list.append(issue_name.upper())
    else:
        issue_name = "FAIL"
        feedback_list.append(issue_name.upper())

    if user_feedback_temperature < 85:
        issue_name = 'PASS'.upper()
        feedback_list.append(issue_name)
    else:
        feedback_list.append("FAIL")

    if user_feedback_breather == "YES":
        issue_name = 'PASS'.upper()
        feedback_list.append(issue_name)
    elif user_feedback_breather == "saturated".upper():
        feedback_list.append('WARNING')
    else:
        feedback_list.append("FAIL".upper())

    if user_feedback_cleanliness == "YES":
        issue_name = 'PASS'.upper()
        feedback_list.append(issue_name)
    else:
        feedback_list.append("WARNING")

    # LOGIC
    pass_items = []
    warning_items = []
    fail_items = []
    warning_statuses = ['']
    fail_statuses = ['']
    count = 0
    for as_per_feedback in feedback_list:
        if as_per_feedback == "FAIL":
            fail_statuses[0] = as_per_feedback
            fail_items.append(items[count])
        elif as_per_feedback == "WARNING":
            warning_statuses[0] = as_per_feedback
            warning_items.append(items[count])
        else:
            pass_items.append(items[count])
        count += 1
    
    # MAINTENANCE DECISION
    if fail_statuses[0] == 'FAIL':
        print("--------------------------------------------------")
        print("| INSPECTION RESUTL: FAIL - MAINTENANCE REQUIRED |")
        print("--------------------------------------------------")
        print("FAIL LIST")
        for fail_item in fail_items:
            print(f" - {fail_item}")
        if warning_statuses[0] == "WARNING":
            print("WARNING LIST")
            for warning_item in warning_items:
                print(f" - {warning_item}")
    elif fail_statuses[0] != 'FAIL' and warning_statuses[0] == "WARNING":
        print("---------------------------------------------------------------")
        print("| INSPECTION RESULT: PASS WITH WARNING - SCHEDULE MAINTENANCE |")
        print("---------------------------------------------------------------")
        print("WARNING LIST:")
        for warning_item in warning_items:
            print(f" - {warning_item}")
    else:
        print("-----------------------------------------------------")
        print("| INSPECTION RESULT: PASS - NO MAINTENANCE REQUIRED |")
        print("-----------------------------------------------------")

    # EXIT THE WHILE LOOP
    should_continue = input("Continue or Exit: ").upper()
    if should_continue == "EXIT":
        should_continue = False