from django.shortcuts import render
from .. import models
from django.db import connection


def prescription_view(request,branch):
    try:
        if branch == "create" or branch == "index":
            
            cursor = connection.cursor()
            if request.method == "POST":
                new_pres_id = 0

                params = [
                    request.POST.get("id"),
                    request.POST.get("p_type"),
                    request.POST.get("med_id"),
                    request.POST.get("quantity"),
                    new_pres_id
                ]

                print(params)

                cursor.callproc('create_prescription',params)
                cursor.execute("SELECT @_create_prescription_4")
                new_pres_id = cursor.fetchone()[0]
                cursor.close()

                print(new_pres_id)
                
                if int(new_pres_id) == -1:
                    return render(request,"dbms_app/create_prescription.html",{
                        "result": "Cannot insert the record",
                        "presc_id": None
                    })
                else:
                    return render(request,"dbms_app/create_prescription.html",{
                        "result": "Prescription added. Prescription ID = " + str(new_pres_id),
                        "presc_id": new_pres_id
                    })
            
            else:
                return render(request,"dbms_app/create_prescription.html")

        if branch == "show":
            
            cursor = connection.cursor()
            presc_id = None
            flag = False

            if request.method == "POST":
                for key, value in list(request.POST.items()):
                    if key == "presc_id_show":
                        presc_id = value
                        flag = False
                        break
                    
                    if key == "presc_id_create":
                        presc_id = value
                        flag = True
                        break
                

                cursor.execute("SELECT * FROM Prescription_Report WHERE prescription_id = %s",[presc_id])
                
                result = cursor.fetchall()
                cursor.close()

                print(result)
                
                if not result:
                    return render(request,"dbms_app/show_prescription.html",{
                        "message": "No prescription with ID " + str(presc_id),
                        "flag": flag
                    })
                
                else:
                    rows = []
                    for row in result:
                        rows.append([row[1],row[2]])

                    headers = ['Prescription ID','Quantity','Medicine']
                    
                    return render(request,"dbms_app/show_prescription.html",{
                        "flag": flag,
                        "headers": headers[1:],
                        "rows" : rows,
                        "presc_id": presc_id
                    })
            
            else:
                return render(request,"dbms_app/show_prescription.html")

        return render(request,"dbms_app/create_prescription.html")
    except:
        return render(request,"dbms_app/presc_error_page.html")