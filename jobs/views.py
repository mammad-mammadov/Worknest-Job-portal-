from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Job, Application
from .forms import RegisterForm, ApplicationForm, JobForm
from .models import SavedJob

def job_list(request):
    jobs = Job.objects.filter(status='approved')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


def job_detail(request, job_id):
    job = Job.objects.get(id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('job_list')
    else:
        form = RegisterForm()

    return render(request, 'jobs/register.html', {'form': form})


@login_required
def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)

    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.user = request.user
            application.save()
            return redirect('job_detail', job_id=job.id)
    else:
        form = ApplicationForm()

    return render(request, 'jobs/apply.html', {'form': form, 'job': job})


@login_required
def post_job(request):
    if request.method == "POST":
        form = JobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.status = "pending"
            job.posted_by = request.user
            job.save()
            return redirect('company_dashboard')
    else:
        form = JobForm()

    return render(request, 'jobs/post_job.html', {'form': form})


@login_required
def company_dashboard(request):
    jobs = Job.objects.filter(posted_by=request.user)

    applications = Application.objects.filter(
        job__posted_by=request.user
    )

    return render(request, 'jobs/company_dashboard.html', {
        'jobs': jobs,
        'applications': applications
    })
@login_required
def save_job(request, job_id):
    job = Job.objects.get(id=job_id)

    already_saved = SavedJob.objects.filter(
        user=request.user,
        job=job
    ).first()

    if not already_saved:
        SavedJob.objects.create(
            user=request.user,
            job=job
        )

    return redirect('job_detail', job_id=job.id)
@login_required
def saved_jobs(request):
    saved_jobs = SavedJob.objects.filter(user=request.user)

    return render(request, 'jobs/saved_jobs.html', {
        'saved_jobs': saved_jobs
    })