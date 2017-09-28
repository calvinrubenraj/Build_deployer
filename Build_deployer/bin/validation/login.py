class login_validation_class():
    def login_check(self, loginform):
        # check whether it's valid:
        if loginform.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            login_dict = loginform.cleaned_data
            if (login_dict['username'] == 'administrator' and login_dict['password'] == 'cygnet@123$'):
                print("correct password")
                return True
                #return HttpResponseRedirect('/build/about/')
                
            else:
                print("wrong password")
                return False
                #return render(request, 'login_failed.jsp', {'login_form': form})
                