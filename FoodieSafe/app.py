"""FoodieSafe privacy-hardened educational prototype; NOT certified for food safety."""
from pathlib import Path
import pandas as pd
import streamlit as st
from privacy_core import ALLOWED_ALLERGENS, assess_dish, build_minimal_disclosure

st.set_page_config(page_title='FoodieSafe | Privacy-first demo', page_icon='🥗', layout='wide')

MENU = [
    {'dish':'Garden Salad','ingredients':'Lettuce, tomato, cucumber, olive oil','allergens':set(),'diet':['Vegan','Vegetarian','No restriction']},
    {'dish':'Peanut Noodles','ingredients':'Wheat noodles, peanuts, soy sauce, sesame oil','allergens':{'Peanuts','Wheat','Soy','Sesame'},'diet':['Vegan','Vegetarian','No restriction']},
    {'dish':'Cheese Pasta','ingredients':'Wheat pasta, milk cheese, tomato','allergens':{'Wheat','Milk'},'diet':['Vegetarian','No restriction']},
    {'dish':'Grilled Fish','ingredients':'Fish, lemon, olive oil','allergens':{'Fish'},'diet':['No restriction']},
    {'dish':'Egg Sandwich','ingredients':'Wheat bread, egg, mayonnaise (egg)','allergens':{'Eggs','Wheat'},'diet':['Vegetarian','No restriction']},
    {'dish':'Sesame Rice Bowl','ingredients':'Rice, sesame, vegetables, soy sauce','allergens':{'Sesame','Soy'},'diet':['Vegan','Vegetarian','No restriction']},
]

for key, default in {'allergies': [], 'diet': 'No restriction', 'share_consent': False, 'marketing_consent': False}.items():
    if key not in st.session_state:
        st.session_state[key] = default


def clear_private_preferences():
    """Clear session values and widget selections, including consent."""
    st.session_state['allergies'] = []
    st.session_state['diet'] = 'No restriction'
    st.session_state['share_consent'] = False
    st.session_state['marketing_consent'] = False

st.title('🥗 FoodieSafe')
st.caption('Privacy-first demonstration • fictional menu • no customer database or restaurant integration')
st.error('Food allergy safety warning: Ingredient lists are fictional and incomplete. Cross-contact is not assessed. NEVER rely on this app to decide whether food is safe. Confirm directly with trained restaurant staff.')

page = st.sidebar.radio('Navigate', ['Menu alerts', 'Privacy controls', 'Dataset dashboard'])
st.sidebar.button('Clear my session preferences', on_click=clear_private_preferences, use_container_width=True)
st.sidebar.caption('Selections remain in the current Streamlit session; they are not written to the project dataset or sent to restaurants.')

if page == 'Menu alerts':
    st.subheader('Choose restrictions (session-only)')
    st.multiselect('Known food allergies', sorted(ALLOWED_ALLERGENS), key='allergies')
    st.selectbox('Dietary preference', ['No restriction','Vegetarian','Vegan'], key='diet')
    st.info('Allergy matching uses only listed ingredients. A missing match does not mean a dish is safe.')
    for item in MENU:
        overlap, mismatch = assess_dish(item, st.session_state['allergies'], st.session_state['diet'])
        with st.container(border=True):
            st.markdown(f"**{item['dish']}**")
            st.write('Listed ingredients:', item['ingredients'])
            st.write('Declared allergens:', ', '.join(sorted(item['allergens'])) or 'None declared')
            if overlap:
                st.error('⚠️ Listed allergen conflict: ' + ', '.join(overlap))
            if mismatch:
                st.warning('Does not match your selected dietary preference.')
            if not overlap and not mismatch:
                st.info('No listed conflict detected. Safety remains unverified; ask restaurant staff.')

elif page == 'Privacy controls':
    st.subheader('Privacy and consent')
    st.write('No login, customer profile, database, analytics tracker, or restaurant transmission is implemented in this demo.')
    st.checkbox('I explicitly consent to prepare my selected allergies and diet for restaurant sharing (preview only).', key='share_consent')
    st.checkbox('I separately opt in to marketing (demo only; no messages are sent).', key='marketing_consent')
    st.caption('Marketing consent is optional and does not affect menu alerts. Both consents default to off and can be withdrawn anytime.')
    payload = build_minimal_disclosure(st.session_state['allergies'], st.session_state['diet'], st.session_state['share_consent'])
    if payload is None:
        st.warning('Restaurant sharing disabled. No disclosure preview is generated.')
    else:
        st.success('Consent enabled: minimal sharing preview only. Nothing has been transmitted.')
        st.json(payload, expanded=True)
        st.caption('No name, email, customer ID, visit history, or marketing preference is included.')
    st.button('Withdraw consent and erase session selections', on_click=clear_private_preferences)
    st.info('This demo does not persist user profiles. Closing a browser tab does not guarantee immediate server-side session deletion; use the clear button. Production use needs authentication, retention policies, audited access controls, and legal review.')

else:
    st.subheader('Synthetic dataset dashboard — aggregated statistics only')
    csv_path = Path(__file__).parent / 'FoodieSafe_app_data.csv'
    if not csv_path.is_file():
        st.error('Synthetic dataset missing.'); st.stop()
    try:
        df = pd.read_csv(csv_path)
        expected = {'allergen','dietary_preference','privacy_concern','restaurant_data_sharing'}
        if not expected.issubset(df.columns):
            st.error('Dataset has unexpected columns.'); st.stop()
    except (OSError, ValueError, pd.errors.ParserError):
        st.error('Unable to read synthetic dataset.'); st.stop()
    st.metric('Synthetic customer records', len(df))
    a, b = st.columns(2)
    with a:
        st.write('Allergen distribution'); st.bar_chart(df['allergen'].value_counts())
        st.write('Privacy concerns'); st.bar_chart(df['privacy_concern'].value_counts())
    with b:
        st.write('Dietary preferences'); st.bar_chart(df['dietary_preference'].value_counts())
        st.write('Data-sharing preferences'); st.bar_chart(df['restaurant_data_sharing'].value_counts())
    st.caption('Generated records only; no individual customer rows or identifiers are displayed.')
