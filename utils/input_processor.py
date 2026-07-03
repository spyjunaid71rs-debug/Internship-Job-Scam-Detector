import pandas as pd
from utils.model_loader import model


def prepare_input(data):

    # Create all model features with 0
    sample = {feature: 0 for feature in model.feature_names_in_}

    # -------------------------
    # Numerical Features
    # -------------------------

    sample["linkedin_presence"] = int(bool(data.linkedin_url.strip()))
    sample["stipend"] = data.stipend
    sample["payment_required"] = data.payment_required
    sample["registration_fee"] = data.registration_fee
    sample["fake_certificate_offer"] = data.fake_certificate_offer

    # -------------------------
    # Website
    # -------------------------

    sample["website_available"] = int(bool(data.website.strip()))

    # -------------------------
    # Email
    # -------------------------

    free_domains = [
        "gmail.com",
        "yahoo.com",
        "hotmail.com",
        "outlook.com",
        "icloud.com"
    ]

    domain = data.recruiter_email.strip().split("@")[-1].lower()

    if domain in free_domains:
        sample["recruiter_email_type_Free"] = 1
        sample["suspicious_email_domain"] = 1

    # -------------------------
    # One Hot Encoding
    # -------------------------

    mappings = {
        "internship_title": data.internship_title,
        "employment_type": data.employment_type,
        "work_mode": data.work_mode,
        "industry": data.industry,
        "location": data.location,
        "company_size": data.company_size
    }

    for prefix, value in mappings.items():

        column = f"{prefix}_{value}"

        if column in sample:
            sample[column] = 1

    df = pd.DataFrame([sample])

    return df