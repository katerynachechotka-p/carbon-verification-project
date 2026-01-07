
# Carbon Verification Project

This repository contains a group project developed as part of **The Knowledge Society (TKS)** program.  
The project explores the use of AI-assisted workflows to **support and accelerate the verification of carbon offset projects**, with a focus on alignment with established standards and methodologies.

This work was completed collaboratively by a **team of four contributors** and should be understood as a **team-based research and prototyping effort**, not an individual or commercial product.

---

## Project Motivation

Carbon offset verification is a resource-intensive process that relies on detailed documentation, methodological rigor, and expert review. As the volume of carbon projects grows, verification timelines can become a bottleneck.

The goal of this project was to investigate whether **AI-assisted tools** could help:
- streamline document review,
- support methodology compliance checks,
- and assist human verifiers by reducing repetitive manual work,

while remaining **fully grounded in existing verification frameworks** rather than attempting to replace them.

---

## Standards and Methodological Framework

This project is explicitly grounded in resources from **Verra**, including:

- **Verified Carbon Standard (VCS)**  
  The world’s most widely used greenhouse gas (GHG) crediting program.

- **VCS Program documentation and methodologies**, including:
  - VCS Standard
  - VCS Methodology Requirements
  - Project Description templates
  - Public Verra resources describing project validation and verification processes

These materials were used as **reference frameworks** to guide the structure, logic, and evaluation criteria implemented in the prototype.

Example context studied includes Verra-registered projects such as peatland restoration and conservation initiatives (e.g., projects in Indonesia), as described in public VCS documentation.

> This project does **not** issue, validate, or certify carbon credits and is **not affiliated with Verra**.  
> It is a technical exercise and proposed solution to posed challenge by The Knowledge Society program informed by publicly available Verra resources.

---

## What This Project Does

At a high level, the prototype explores:
- structuring carbon project documentation for automated review,
- extracting relevant information aligned with VCS requirements,
- assisting with consistency checks and timeline estimation,
- supporting human-led verification workflows through AI-assisted analysis.

The focus is on **decision support**, not autonomous verification.

---

## Collaboration and Authorship

This project was developed collaboratively by a **team of four students** as part of **The Knowledge Society** program.

All design decisions, modeling approaches, and implementation work were conducted as a **group effort**.  
This repository represents one contribution within that shared project and should not be interpreted as sole authorship.

---

## Repository Contents

- `app.py`, `verifier.py`, `developer.py`  
  Core prototype logic and supporting scripts

- `requirements.txt`  
  Python dependencies for running the prototype

- `VCS-Standard.pdf`, `VCS-Methodology-Requirements.pdf`, and related documents  
  Reference materials used to understand and align with Verra’s VCS framework

---

## Notes and Limitations

- This repository reflects an **prototype**, not a production-ready system.
- Some components are partial or experimental.
- Results are illustrative and intended for learning and research purposes.
- The project does not replace expert judgment or official verification processes.

---

## Acknowledgements

This project was completed as part of **The Knowledge Society (TKS)** in collaboration with three other team members.  
It draws upon publicly available resources from **Verra** and the **Verified Carbon Standard (VCS)** program.
