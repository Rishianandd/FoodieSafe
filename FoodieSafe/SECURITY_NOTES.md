# FoodieSafe security status

## Implemented in this demo
- Explicit, separate opt-in toggles, default off; withdrawal/clear action.
- No real restaurant API, user accounts, persistent user profiles, or marketing integration.
- Disclosure preview gated on consent; only selected allergens and diet included.
- Session-only selections; no database writes or customer analytics tracking by app code.
- Synthetic dashboard shows aggregates, not raw records.
- Streamlit usage-statistics opt-out; CORS and XSRF protections enabled.
- Unit tests for consent gating, validation, allergen and dietary matching.

## NOT implemented / not proven
- Server authentication, authorization, audit trails, encrypted database, data retention workflows.
- HTTPS/TLS termination, security headers, reverse proxy, hosting isolation, incident response, backups.
- Verified real restaurant ingredients, cross-contact safeguards, production safety review.
- GDPR legal compliance, DPIA determination, processor agreements, privacy notice, consent records.

## Deployment requirements
- Do not expose directly to the internet without a properly configured HTTPS reverse proxy and access controls.
- Do not add real customer records to the synthetic CSV or commit secrets to source control.
- Deploy using least-privilege credentials and supported/patched dependencies.
- Conduct penetration testing, privacy impact assessment, security review, and legal review before handling real health data.
- Streamlit server may retain widget/session state until the session is cleared or expires; clearing the UI is not a verifiable server-wide erasure guarantee.
- Test accessibility and make clear allergen warnings are not a substitute for restaurant verification.
