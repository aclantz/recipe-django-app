from django.shortcuts import render, redirect  
#Django authentication libraries           
from django.contrib.auth import authenticate, login, logout
#Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm 


def login_view(request):
  form = AuthenticationForm()                                     # from object 
  error_message = None                                            # initialize error_message

  if request.method == 'POST':                                    # when user hits "login" button, POST request is generated
    form = AuthenticationForm(data=request.POST)                  # read data sent by the form via POST request    
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      
      user = authenticate(username=username, password=password)   # django authenticate to validate user
      if user is not None:                                        # if user is validated, use django login func
        login(request, user)
        return redirect('recipes:list')                           # send user to desired page / may need to change ***
      else: 
        error_message = 'oops.. something went wrong (Auth)'

  context ={                                                      # prep data to send form view to template
    'form': form,
    'error_message': error_message
  }
  return render(request, 'auth/login.html', context)              # load login page using context{} info


def logout_view(request):
  logout(request)                                                 # use django logout to send request
  return redirect('success')                                      # upon success send user to success.html

def success_view(request):
  return render(request, 'auth/success.html')