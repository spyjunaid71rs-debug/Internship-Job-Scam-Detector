from utils.model_loader import model
from utils.input_processor import prepare_input


def predict_internship(data):

    df = prepare_input(data)

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0]

    confidence = round(max(probability) * 100, 2)

    reasons = []

    if data.payment_required:
        reasons.append("The internship requires payment from applicants.")

    if data.registration_fee > 0:
        reasons.append("A registration fee is being charged.")

    if not data.website.strip():
        reasons.append("No official company website was provided.")

    domain = data.recruiter_email.strip().split("@")[-1].lower()

    if domain in [
        "gmail.com",
        "yahoo.com",
        "hotmail.com",
        "outlook.com",
        "icloud.com"
    ]:
        reasons.append("The recruiter is using a free email service instead of a company domain.")

    if data.fake_certificate_offer:
        reasons.append("A certificate offer may be used to attract applicants.")

    if not data.linkedin_url.strip():
        reasons.append("No company LinkedIn profile was provided.")

    # If genuine and no suspicious reasons
    if prediction == 0 and len(reasons) == 0:
        reasons.append("No major warning signs were detected.")
        reasons.append("Official company website is available.")
        reasons.append("No registration fee is required.")
        reasons.append("Recruiter appears to use a professional email.")

    return {
        "prediction": "Fake Internship" if prediction else "Genuine Internship",
        "confidence": confidence,
        "risk_level": "High" if prediction else "Low",
        "reasons": reasons
    }