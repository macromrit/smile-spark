from django.shortcuts import render, redirect

# imported designed csv form
from .forms import CSVFileForm

from hot_code_generator import mainy

global_list = list() # this one's used to display stuff being generated in upload_csv and make it work in displayData

def displayData(requests):
    main_dict = {"ERROR": False}

    if global_list:
        
        # the last thing in global_list must be filename
        file_name = global_list.pop()

        solution = mainy.readCsv(file_name)

        if type(solution[0]) is str:
            main_dict["ERROR"] = solution[0]
        else:
            main_dict["hot_codes"] = solution[0]
            main_dict["fields"] = solution[1]

            # filtering blank spaces and stuff
            main_dict["fields"] = main_dict["fields"].replace(" ", "")

            # # writing encoded data to a new file
            main_dict["download_link"] = mainy.writeNewStuffBack(file_name, main_dict["hot_codes"])

    else:
        main_dict["ERROR"] = True
    
    return render(requests, 'main_app/disp_data.html', main_dict)

def upload_csv(request):
    if request.method == 'POST':
        form = CSVFileForm(request.POST, request.FILES)
        if form.is_valid():

            # tryna grab files name -------------------------------->
            uploaded_file = request.FILES['file']
            file_name = uploaded_file.name
            # ------------------------------------------------------>
            form.save()
            # appending the file name to global list
            global_list.append(file_name)
            # ------------------------------------------------------>

            """
            main_dict = {"ERROR": None}

            solution = mainy.readCsv(file_name)

            if type(solution[0]) is str:
                main_dict["ERROR"] = solution[0]
            else:
                main_dict["hot_codes"] = solution[0]
                main_dict["fields"] = solution[1]

                # # writing encoded data to a new file
                # main_dict["download_link"] = mainy.writeNewStuffBack(file_name, main_dict["hot_codes"])
            """

            # return render(request, 'main_app/disp_data.html', main_dict)
            return redirect("processed_data")
        
    else:

        form = CSVFileForm()

    return render(request, 'main_app/index.html', {'form': form})
