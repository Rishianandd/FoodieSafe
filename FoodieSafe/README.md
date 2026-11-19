# FoodieSafe — Allergen Alerts and Privacy

## Dataset
`FoodieSafe_app_data.csv` contains **500 fictional, synthetically generated** customer records. It is not the professor's original dataset and cannot support claims about real customers or market trends.

## Run
```bash
pip install pandas matplotlib
python analyze_foodiesafe.py
```
The script creates four charts and a summary CSV in `outputs/`.

## Project objective
Study how a restaurant platform can communicate dietary restrictions while reducing unnecessary exposure of sensitive allergy information.

## Privacy recommendations
- Collect allergy data only when necessary and explain its purpose.
- Obtain an appropriate GDPR legal basis; health-related data may require an Article 9 exception, such as explicit consent.
- Allow users to review, correct, and delete their information where applicable.
- Share only the minimum information needed with authorized restaurant staff.
- Use encryption, role-based access, audit logs, and retention limits.
- Do not use allergy data for marketing without a separate valid legal basis.

## Important safety limitation
An allergen warning must not be treated as proof that a dish is safe. Ingredient changes, cross-contact, and restaurant verification are essential. This dataset has no ingredient or menu records and does not support actual dish safety predictions.

## Suggested report sections
1. Problem and audience
2. Dataset description and limitations
3. Exploratory data analysis and charts
4. Privacy risk assessment
5. GDPR considerations
6. Proposed privacy-first system
7. Conclusion

## Step 2: Run the interactive application
From the `FoodieSafe` directory:
```bash
pip install -r requirements.txt
streamlit run app.py
```
Open the local address printed by Streamlit (usually http://localhost:8501).
The fictional menu's declared ingredients are intentionally incomplete as a food-safety source. The app never labels a dish safe; confirm all ingredients and cross-contact risks with restaurant staff.

## Project report
See `PROJECT_REPORT.md` for the dataset findings, risk matrix, GDPR considerations, and limitations.
