# FoodieSafe — Allergen Alerts and Dietary Preferences in Restaurant Tech

## 1. Executive summary
FoodieSafe is an educational Streamlit prototype that lets diners select declared allergies and dietary preferences, view illustrative menu conflict warnings, and explore privacy controls. Its accompanying dataset is **synthetic** and contains 500 fictional customer records across 12 fields. This project demonstrates privacy-by-design concepts; it is not a certified food-safety system.

## 2. Problem and objectives
Restaurants need to communicate ingredient information while limiting unnecessary collection and disclosure of sensitive dietary and allergy data. The project objectives are to (1) demonstrate ingredient/allergen conflict flags, (2) give users privacy choices, (3) analyze synthetic preference and privacy fields, and (4) recommend risk controls consistent with GDPR principles.

## 3. Dataset and methodology
Source: locally generated `FoodieSafe_app_data.csv`, **not an original supplied course dataset**. Fields include customer ID, age group, restaurant, allergen, dietary preference, allergy severity, privacy consent, restaurant data sharing, marketing opt-in, privacy concern, recent visits, and satisfaction. Analysis uses Pandas and Matplotlib. Missing `allergen` and `allergy_severity` values appear in 163 records; these are not assumed to indicate medically confirmed absence of allergies.

## 4. Results (synthetic records only)
- 500 records, 12 columns.
- 372 (74.4%) have `privacy_consent=Yes`; 128 (25.6%) have `No`.
- Non-null allergen entries: peanuts 59, milk 55, wheat 47, soy 41, eggs 40, tree nuts 29, fish 28, shellfish 26, sesame 12.
- Four figures are generated in `outputs/`: allergens, dietary preferences, privacy concerns, and privacy consent.
- These numbers illustrate application behavior and **must not** be generalized to actual diners or restaurants.

## 5. Privacy risk assessment
| Risk | Impact | Proposed mitigation |
|---|---|---|
| Unnecessary collection of health-related allergy information | High | Data minimization; purpose limitation; optional profiles |
| Disclosure to unauthorized staff | High | Role-based access, least privilege, access logging |
| Third-party marketing reuse | High | Separate marketing choice; do not repurpose health data without lawful basis |
| Account or database compromise | High | Encryption in transit and at rest, secure authentication, patching |
| Data retained indefinitely | Medium | Defined retention schedule and deletion workflow |
| Incorrect or outdated menu data | Critical for food safety | Restaurant verification, ingredient update process, cross-contact warnings |

## 6. GDPR considerations
Where GDPR applies, identify a valid Article 6 lawful basis and address Article 9 conditions for processing health-related information, potentially explicit consent where appropriate. Provide clear privacy notices, rights-request workflows, access controls, retention policies, and data protection impact assessment screening. A checkbox alone does not establish full compliance. Local legal review is needed before real deployment.

## 7. Proposed system
- Streamlit prototype: menu alerts, privacy controls, dataset dashboard.
- Allergy input is compared only with **declared illustrative menu allergens**; it cannot evaluate unknown ingredients or cross-contact.
- Privacy design for a production system: default-minimal data collection, separate optional sharing and marketing choices, staff access restrictions, encrypted storage, and deletion workflows.

## 8. Testing and limitations
The menu alert, privacy controls, and dashboard were manually tested in a local browser. No automated tests, penetration testing, clinical validation, restaurant integration, or production security audit has been demonstrated. The synthetic dataset is not evidence of customer behavior. **Never use this prototype to decide whether a food is safe to eat; verify with restaurant staff.**

## 9. Conclusion
FoodieSafe illustrates how an allergen-awareness interface can be combined with privacy-by-design recommendations. Further work before real use would require verified menu data, robust consent and access-control implementation, security testing, and food-safety validation.
