from pydantic import BaseModel


class InternshipInput(BaseModel):

    internship_title: str
    employment_type: str
    work_mode: str
    industry: str
    location: str
    company_size: str

    stipend: float
    registration_fee: float

    payment_required: int
    fake_certificate_offer: int

    linkedin_url: str

    website: str
    recruiter_email: str