const form = document.getElementById("predictionForm");

const loading = document.getElementById("loading");

const resultCard = document.getElementById("resultCard");

const prediction = document.getElementById("prediction");

const confidence = document.getElementById("confidence");

const risk = document.getElementById("risk");

const reasons = document.getElementById("reasons");

const progressBar = document.getElementById("progressBar");

form.addEventListener("submit", async function (e) {

    e.preventDefault();

    resultCard.style.display = "none";

    loading.style.display = "block";

    document.body.classList.remove("fake");
    document.body.classList.remove("genuine");

    const data = {

        internship_title: document.getElementById("internship_title").value,

        employment_type: document.getElementById("employment_type").value,

        work_mode: document.getElementById("work_mode").value,

        industry: document.getElementById("industry").value,

        location: document.getElementById("location").value,

        company_size: document.getElementById("company_size").value,

        stipend: Number(document.getElementById("stipend").value),

        registration_fee: Number(document.getElementById("registration_fee").value),

        payment_required: Number(document.getElementById("payment_required").value),

        fake_certificate_offer: Number(document.getElementById("fake_certificate_offer").value),

        website: document.getElementById("website").value,

        recruiter_email: document.getElementById("recruiter_email").value,

        linkedin_url: document.getElementById("linkedin_url").value

    };

    try {

        const response = await fetch("/predict", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(data)

        });

        const result = await response.json();

        loading.style.display = "none";

        resultCard.style.display = "block";

        prediction.innerHTML = result.prediction;

        confidence.innerHTML = "Confidence : " + result.confidence + "%";

        risk.innerHTML = "Risk Level : " + result.risk_level;

        progressBar.style.width = result.confidence + "%";

        reasons.innerHTML = "";

        result.reasons.forEach(reason => {

            const li = document.createElement("li");

            li.innerHTML = reason;

            reasons.appendChild(li);

        });

        if (result.prediction.includes("Fake")) {

            document.body.classList.add("fake");

        }

        else {

            document.body.classList.add("genuine");

        }

    }

    catch (err) {

        loading.style.display = "none";

        alert("Server Error!");

        console.log(err);

    }

});