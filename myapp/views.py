from django.shortcuts import render


# Home page
def home(request):
    return render(
        request,
        "myapp/home.html"
    )


# Plastic Surgery → Subspecialties
def subspecialties(request, specialty_slug):

    if specialty_slug == "plastic":

        return render(
            request,
            "myapp/subspecialties.html",
            {
                "specialty_name": "Plastic Surgery",
                "specialty_slug": specialty_slug,
            }
        )

    return render(
        request,
        "myapp/subspecialties.html",
        {
            "specialty_name": "Specialty Not Found",
            "specialty_slug": specialty_slug,
        }
    )


# Hand Surgery → Surgeries
def surgeries(request, subspecialty_slug):

    if subspecialty_slug == "hand":

        return render(
            request,
            "myapp/surgeries.html",
            {
                "subspecialty_name": "Hand Surgery",
                "subspecialty_slug": subspecialty_slug,
            }
        )

    return render(
        request,
        "myapp/surgeries.html",
        {
            "subspecialty_name": "Subspecialty Not Found",
            "subspecialty_slug": subspecialty_slug,
        }
    )


# Individual Surgery → Patient Journey
def surgery_detail(request, surgery_slug):

    if surgery_slug == "flexor-tendon-zone-5":

        return render(
            request,
            "myapp/surgery_detail.html",
            {
                "surgery_name": "Flexor Tendon Injury — Zone 5",
                "surgery_slug": surgery_slug,
            }
        )

    return render(
        request,
        "myapp/surgery_detail.html",
        {
            "surgery_name": "Surgery Not Found",
            "surgery_slug": surgery_slug,
        }
    )