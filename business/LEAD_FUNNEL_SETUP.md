# Agentic AI Enterprise Lead Funnel Setup

The public website now contains a complete assessment inquiry funnel:

```text
Visitor
  -> Interactive Readiness Scorecard
  -> Readiness Score and Maturity Band
  -> Request Assessment CTA
  -> Qualified Enterprise Inquiry Form
  -> Private Form Ingestion Endpoint
  -> Founder / Sales Workflow
```

## Current state

The front-end funnel is implemented and privacy-safe, but **live transmission is intentionally disabled until a private form-ingestion endpoint is selected**.

The endpoint is configured in:

```text
docs/lead-config.js
```

with:

```javascript
window.AGENTIC_LEAD_ENDPOINT = "";
```

When this value is empty, the website does not transmit the inquiry anywhere. It attempts to copy the prepared inquiry to the visitor's clipboard and clearly states that nothing was submitted.

## Why GitHub Issues are not used

Enterprise inquiries may contain commercially sensitive information. Public GitHub issues are therefore not an appropriate default lead destination.

The public intake form explicitly tells visitors not to submit:

- passwords or credentials
- API keys or secrets
- protected health information
- personal customer records
- confidential source code
- trade secrets
- classified information
- sensitive architecture evidence

Detailed evidence should move to an approved private channel only after discovery.

## Recommended production choices

Choose a service that provides a **public browser-safe form endpoint** while keeping authentication and downstream systems private.

### Option A: Managed form endpoint

Best for the fastest launch.

Typical workflow:

```text
GitHub Pages
  -> Managed form endpoint
  -> Email notification
  -> Private lead dashboard / CRM
```

Requirements:

- HTTPS endpoint
- spam protection
- rate limiting or abuse controls
- configurable recipient or destination
- data-retention controls
- privacy terms appropriate for enterprise leads
- no secret token embedded in front-end JavaScript

### Option B: Serverless intake API

Best for a more scalable proprietary funnel.

Typical workflow:

```text
GitHub Pages
  -> Serverless POST endpoint
  -> Input validation
  -> Rate limiting / bot filtering
  -> Private database or CRM
  -> Notification / sales automation
```

The serverless endpoint should validate every field again on the server. Client-side validation is a usability feature, not a security boundary.

### Option C: CRM-native form endpoint

Best when a CRM has already been selected.

Typical workflow:

```text
GitHub Pages
  -> CRM form endpoint
  -> Lead enrichment
  -> Qualification pipeline
  -> Discovery scheduling
```

Use only the CRM's documented public form submission mechanism. Never expose a private CRM API key in `docs/lead-config.js`.

## Activating live submission

Once a browser-safe form endpoint exists, edit:

```text
docs/lead-config.js
```

and set:

```javascript
window.AGENTIC_LEAD_ENDPOINT = "https://YOUR_PUBLIC_FORM_ENDPOINT";
```

No other website code needs to change if the endpoint accepts JSON POST requests.

The website currently sends a JSON object containing:

```text
name
email
company
role
company_size
industry
stage
timeline
agents
tools_count
system_description
tools_description
primary_concern
readiness_score
readiness_band
source
submitted_at
```

## Qualification model

Not every inquiry needs the same sales response. A simple initial qualification model can prioritize leads using:

### High-priority signals

- production or pre-production system
- multiple agents with external tools
- consequential external actions
- regulated or safety-sensitive industry
- explicit security, governance, evaluation, or authority concern
- timeline within 90 days
- engineering, product, risk, compliance, security, founder, or executive buyer

### Lower-priority signals

- purely exploratory interest
- no existing system
- educational use only
- no expected implementation timeline

Lower-priority leads can still receive the open Gold Standard and library resources while preserving founder time for likely enterprise engagements.

## Suggested pipeline stages

```text
New Inquiry
  -> Qualified
  -> Discovery Scheduled
  -> Evidence Scope Defined
  -> Proposal Sent
  -> Assessment Active
  -> Executive Readout
  -> Remediation / Architecture Opportunity
  -> Ongoing Advisory or Closed
```

## Discovery call objective

A 30-minute discovery call should determine:

1. what the system does
2. why the workflow matters
3. what agents and tools exist
4. which actions have real-world consequences
5. what evidence is already available
6. what the buyer is worried about
7. who owns engineering and deployment decisions
8. whether legal, security, risk, clinical, or other domain reviewers are involved
9. desired timeline
10. whether a paid readiness assessment is the appropriate next step

## Do not request confidential evidence too early

The public inquiry form intentionally collects only high-level information. After qualification, use an approved private file-transfer or collaboration process and agree on scope, confidentiality, access, retention, and deletion expectations before accepting architecture documents or sensitive evidence.

## Conversion metrics to track

Once the funnel is active, measure:

```text
website visitors
scorecards started
scorecards completed
assessment CTA clicks
forms started
forms submitted
qualified leads
calls booked
proposals sent
assessments sold
average assessment value
assessment-to-implementation conversion
```

Avoid optimizing only for form volume. The more meaningful metric is the number and quality of organizations with a real agentic AI production problem.

## Security requirements

The production endpoint should implement, as appropriate:

- server-side schema validation
- field-length limits
- rate limiting
- spam/bot filtering
- request size limits
- origin/CORS policy appropriate to the deployment
- secure logging without unnecessary personal data
- retention and deletion controls
- encrypted transport
- least-privilege access to lead data
- monitoring for abuse

## Current front-end protections

The website already includes:

- required-field validation
- email validation
- field length limits
- numeric bounds
- consent checkbox
- hidden honeypot field
- sensitive-data warning
- no file upload field
- no public GitHub issue fallback
- score and maturity prefill
- explicit status messages
- fail-safe behavior when the endpoint is unavailable

## Next commercial evolution

After the first real assessments, the funnel can evolve into:

```text
Free Readiness Scorecard
  -> Enterprise Inquiry
  -> Paid Evidence-Based Assessment
  -> Gold Standard Remediation
  -> Architecture / Governance Program
  -> Continuous Agentic AI Control Plane
```

The open library remains the credibility and distribution layer. The assessment becomes the first paid diagnostic. Repeated remediation work becomes the evidence for what the future software platform should automate.

---

**Agentic AI Gold Standard and Agentic AI Library by Mahsa Keikha.**
