from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.db.models.functions import Greatest
from django.contrib.auth.models import User


from .models import Profile, EduHistory, JobHistory, Company
from .forms import JobHistoryForm, EduHistoryForm, AddOwnersForm

def signup(request):
    # Handle the POST request
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # STEP 1: Create a user in the databse from the UserCreationForm
            login(request, user) # STEP 2: Log in as the created user
            return redirect('profile-index')
        else:
            error_message = 'Invalid sign up - try again'
    # Handle the GET request (render the form)
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'error_message': error_message})

def company_index(request):
    companies = Company.objects.annotate(
        most_recent=Greatest('created_at', 'updated_at')
    ).order_by('-most_recent')
    return render(request,'companies/index.html',{'companies':companies})

def profile_index(request):
    # profiles = Profile.objects.all() <--- this queries all profiles, including the current user
    other_profiles = Profile.objects.exclude(user=request.user)
    me = Profile.objects.filter(user=request.user).first()
    
    context = {
        'profiles': other_profiles,
        'me': me,
    }

    return render(request,'profiles/index.html', context)

def profile_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    job_histories = JobHistory.objects.filter(profile=profile)
    edu_histories = EduHistory.objects.filter(profile=profile)

    return render(request,'profiles/detail.html', {
        'profile': profile,
        'job_histories': job_histories,
        'edu_histories': edu_histories,
    })


class Home(LoginView):
    template_name = 'home.html'


class ProfileCreate (LoginRequiredMixin, CreateView):
    model = Profile
    fields = [
        'full_name',
        'headline',
        'location',
        'about',
        'profile_image',
    ]

    def get_success_url(self):
        # Redirect to the profile detail page after creating the profile
        return reverse('profile-detail', kwargs={'profile_id': self.object.id}) 

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class ProfileUpdate (LoginRequiredMixin, UpdateView):
    model = Profile
    fields = [
        'full_name',
        'headline',
        'location',
        'about',
        'profile_image',
    ]
    def get_success_url(self):
        # Redirect to the profile detail page after editing
        return reverse('profile-detail', kwargs={'profile_id': self.object.id})

class ProfileDelete(LoginRequiredMixin, DeleteView):
    model = Profile
    success_url = '/profiles'



class JobHistoryCreate (LoginRequiredMixin, CreateView):
    model = JobHistory
    form_class = JobHistoryForm

    template_name = 'main_app/job_history_form.html'
    
    def get_success_url(self):
        # Redirect to the profile detail page after editing
        profile_id = self.object.profile.id
        return reverse('profile-detail', kwargs={'profile_id': profile_id})

    def form_valid(self, form):
        # Retrieve the profile of the logged-in user
        profile = get_object_or_404(Profile, user=self.request.user)
        # Assign the logged in user (self.request.user)
        form.instance.profile = profile # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class JobHistoryUpdate (LoginRequiredMixin, UpdateView):
    model = JobHistory
    form_class = JobHistoryForm

    template_name = 'main_app/job_history_form.html'

    def get_success_url(self):
        # Redirect to the profile detail page after editing
        profile_id = self.object.profile.id
        return reverse('profile-detail', kwargs={'profile_id': profile_id})

class JobHistoryDelete(LoginRequiredMixin, DeleteView):
    model = JobHistory
    template_name = 'main_app/job_history_confirm_delete.html'

    def get_success_url(self):
        job_history = self.get_object()
        return reverse_lazy('profile-detail', kwargs={'profile_id': job_history.profile.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job_history = self.get_object()
        context['profile'] = job_history.profile
        return context


class EduHistoryCreate (LoginRequiredMixin, CreateView):
    model = EduHistory
    form_class = EduHistoryForm
    template_name = 'main_app/edu_history_form.html'

    def get_success_url(self):
        # Redirect to the profile detail page after editing
        profile_id = self.object.profile.id
        return reverse('profile-detail', kwargs={'profile_id': profile_id})


    def form_valid(self, form):
        # Retrieve the profile of the logged-in user
        profile = get_object_or_404(Profile, user=self.request.user)
        # Assign the logged in user (self.request.user)
        form.instance.profile = profile # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class EduHistoryUpdate (LoginRequiredMixin, UpdateView):
    model = EduHistory
    form_class = EduHistoryForm

    template_name = 'main_app/edu_history_form.html'

    def get_success_url(self):
        # Redirect to the profile detail page after editing
        profile_id = self.object.profile.id
        return reverse('profile-detail', kwargs={'profile_id': profile_id})

class EduHistoryDelete(LoginRequiredMixin, DeleteView):
    model = EduHistory
    template_name = 'main_app/edu_history_confirm_delete.html'

    def get_success_url(self):
        edu_history = self.get_object()
        return reverse_lazy('profile-detail', kwargs={'profile_id': edu_history.profile.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        edu_history = self.get_object()
        context['profile'] = edu_history.profile
        return context


class CompanyCreate (LoginRequiredMixin, CreateView):
    model = Company
    fields = [
        'name',
        'about',
        'location',
        'employee_count',
        'industry',
        'company_image',
    ]
    success_url = '/companies'

    def form_valid(self, form):
        response = super().form_valid(form)
        # Add the current user as an owner of the company
        self.object.page_owners.add(self.request.user)
        return response

class CompanyUpdate (LoginRequiredMixin, UpdateView):
    model = Company
    fields = [
        'name',
        'about',
        'location',
        'employee_count',
        'industry',
        'company_image',
    ]
    success_url = '/companies'
   
class CompanyDelete(LoginRequiredMixin, DeleteView):
    model = Company
    success_url = '/companies'


def company_detail(request, company_id):
    company = Company.objects.get(id=company_id)

    # job_histories = JobHistory.objects.filter(profile=profile)
    # edu_histories = EduHistory.objects.filter(profile=profile)

    return render(request,'companies/detail.html', {
        'company': company,
        # 'job_histories': job_histories,
        # 'edu_histories': edu_histories,
    })


@login_required

def add_owner(request, company_id):
    company = get_object_or_404(Company, id=company_id)

    # Only page owners can access the add owners form
    if request.user not in company.page_owners.all():
        return redirect('company-detail', company_id=company_id)

    if request.method == 'POST':
        form = AddOwnersForm(request.POST, owners_queryset=User.objects.exclude(id__in=company.page_owners.values_list('id', flat=True)))
        if form.is_valid():
            new_owners = form.cleaned_data['new_owners']
            for new_owner in new_owners:
                company.page_owners.add(new_owner)
            return redirect('company-detail', company_id=company.id)
    else:
        form = AddOwnersForm(owners_queryset=User.objects.exclude(id__in=company.page_owners.values_list('id', flat=True)))

    return render(request, 'main_app/add_owner_form.html', {'form': form, 'company': company})