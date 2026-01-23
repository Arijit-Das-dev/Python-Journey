score = 85
attendance = 90
submitted = True

if score >= 45:
    if attendance >= 40:
        if submitted:
            print("Pass with good result !!")
        else:
            print("Pass but assignments not submitted !!!")
    else:
        print("low attendance")
else:
    print("Fail")