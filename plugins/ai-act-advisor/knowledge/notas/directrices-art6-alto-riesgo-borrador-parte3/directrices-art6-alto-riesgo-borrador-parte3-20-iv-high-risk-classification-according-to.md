---
name: directrices-art6-alto-riesgo-borrador-parte3-20-iv-high-risk-classification-according-to
description: "Comisión Europea: directrices art6 alto riesgo borrador parte3, sección «IV. High-risk classification according to Article 6(2) and Annex III AI Act (parte 16)» (págs. 125-132). Documento de 2026-05-19, idioma en."
metadata:
  type: reference
  documento: directrices-art6-alto-riesgo-borrador-parte3
  emisor: Comisión Europea
  fecha: 2026-05-19
  idioma: en
  seccion: "IV. High-risk classification according to Article 6(2) and Annex III AI Act (parte 16)"
  paginas: 125-132
  origen: 2026-05-19-directrices-art6-alto-riesgo-borrador-parte3-en.pdf
  oficial: false
---
# IV. High-risk classification according to Article 6(2) and Annex III AI Act (parte 16)

5(1)(c) AI Act, by, for example, generating generalised trustworthiness ranking over time and across contexts treating the person detrimentally or (ii) it predicts criminal behaviour in a prohibited way within the meaning of Article 5(1)(d) AI Act.
These systems are intended to produce an evaluative output about an identified or identifiable person (for example, a score, a flag, or a rank) that is used to triage or channel that person for further checks or stricter treatment related to entry or stay in the Member State. Such outputs materially influence the substance of the assessment and are not tasks that qualify for the filter mechanism in Article 6(3) AI Act. Such tools may also be used to infer the risk to security that the individual intending to enter or who has entered the territory of a Member State may constitute.
Person-level health-risk flagging
–

An AI system intended to assess whether an individual presents an infectious disease risk based on biometric readings and recent travel history, and to flag them for additional medical checks. This is a substantive evaluation about an identified or identifiable person that directly steers treatment at the border; they are not tasks that could qualify for the exception listed in
Article 6(3) AI Act.

Object and itinerary signals mapped to person-level risk
–

An AI system intended to process licence-plate reads and travel-time data in order to generate an individual alert that a named traveller presents a heightened risk of irregular migration, because their journey between two points was abnormally long, and to refer that person to secondary screening. The alert is specified and used as a risk indicator about a natural person, even if a second AI system or a human performs the final assessment. Although the initial signal originates from a vehicle or a route, the intended use is to generate an alert for a specific person and refer that person to second line checks. Once the system outputs a person-specific risk indicator used for triage, it materially influences the assessment and is not eligible for the filter mechanism in Article 6(3) AI Act.

Group-level risk indicators applied to individuals
–

An AI system intended to derive group-level risk indicators from aggregate historical data
(for example, overstay rates by route and season) and to apply those indicators to the personal data of named travellers to generate individual irregular-migration risk flags that are used to refer the person for enhanced checks.

AI system consisting of several non-high-risk components
–

An AI system intended to derive group-level indicators from aggregate historical data (for example, overstay rates by route and season) is combined with a non-AI rule-based engine that applies those indicators to named travellers to generate per-person irregular-migration risk flags used to refer the travellers to secondary screening. Taken separately none of the modules is high-risk under point 7(b), the analytics module outputs only aggregate statistics and the rules engine is not an AI system. However, used together with the intended purpose of assessing a risk posed by a natural person, the combined set-up should be classified as high-risk; it is not eligible for the filter mechanism in Article 6(3) AI Act.
124

b) Practical examples of AI systems falling outside the use case of point 7(b) of Annex III
Aggregate or cohort-level analytics
–

An AI system intended to process and aggregate large amounts of data to detect trends and patterns in migration, anticipate flows, or identify possible irregular migration networks at an aggregate level, where no natural persons are identified or identifiable from the aggregated data. Since the outputs do not concern identified or identifiable natural persons the system is not covered by use case listed in point 7(b) of Annex III.

–

An AI system intended to process aggregate data (e.g. country of origin, route characteristics, real-time epidemiology) to flag an incoming group as having an elevated health risk and to trigger public-health measures (testing or quarantine). Since the system does not assess the risk posed by an identified or identifiable natural person, and the same measure is applied to all members of the cohort (e.g. everyone on a specific flight is tested), it falls outside the use case listed in point 7(b) of Annex III. If the data used to estimate the group risk is personal, the GDPR applies, but the system remains outside the scope of the use case. If the system, or combined configuration that includes the system, is intended to select specific individuals within the group for different treatment based on their individual features, then it should be considered to assess the risk posed by natural persons and falls within the use case.

Vehicle-focused screening without mapping to a person
–

An AI system intended to process licence-plate reads and travel-time data in order to flag vehicles with unusually long journeys and route the vehicle to a general secondary lane for a technical inspection, without creating or implying a risk assessment about the driver or passengers. If the output is framed and used strictly as vehicle-level logistics, not as a personal risk indicator, it will not fall with the use case listed in point 7(b) of Annex III. If the border guards then also check the passengers as a standard operational consequence of a flagged vehicle, that does not convert the AI system’s output into a person-level risk assessment.

–

An AI system intended to monitor vehicles transiting a border crossing point to flag stolen vehicles for secondary checks does not assess risks posed by a natural person within the meaning of point 7(b) of Annex III.

Post-decision data cleaning
–

An AI system intended to harmonise terminology and detect duplicate entries in completed risk-assessment records, after human assessment has been concluded. Such an AI system does not produce, nor is it intended to produce, a person-level risk output used in entry or stay decisions.
3.7.4.

Point 7(c): AI systems intended to be used for assistance in examining asylum/visa/residence applications and associated complaints

(397) Point 7(c) of Annex III classifies as high-risk AI systems intended to be used by or on behalf of competent public authorities or by Union institutions, bodies, offices or agencies to assist competent
125

public authorities in the examination of applications for asylum, visa or residence permits and with associated complaints as regards the eligibility of the natural persons applying for a status, including related assessments of the reliability of evidence. Such systems are classified as high-risk because they have the potential to materially influence the decisions of public authorities that affect people who are often in a particularly vulnerable position and errors, bias, or opacity may lead to severe, and sometimes irreversible harm (e.g., due to refusal of status or exposure to removal).
(398) Point 7(c) covers AI systems intended to assist competent authorities in examining the eligibility of applicants for asylum, visa or residence permits and in examining associated complaints that relate to the eligibility determination. This includes complaints concerning elements capable of affecting either the substantive assessment of the application (such as facts, evidence, or credibility)
or the procedural fairness of the decision-making process (such as the right to be heard, interpretation, or reasoning). It does not cover complaints concerning general service quality, understood as complaints about organisational or logistical aspects of service delivery that do not affect the substance of the eligibility assessment or the procedural fairness of the decision-making process.
(399) The elements listed in point 7(c) of Annex III are alternative (asylum or visa or residence;
applications or associated complaints), not cumulative. The terms ‘including related assessment of the reliability of evidence’ clarifies that reliability-of-evidence checks are illustrative, not exhaustive. The concept of ‘assistance’ is not limited to the decisions e.g. on application for international protection. It also covers earlier stages of the examination (e.g. steps that analyse interview content, documents or country-of-origin information and are relevant for the decision on the merits. Where the AI system’s outputs materially influence the substance or outcome of eligibility determinations, such as by validating or challenging evidence, highlighting inconsistencies, prioritising issues, or pre-classifying status elements it should be classified as highrisk pursuant to point 7(c) of Annex III. For example, if an AI system derives its outputs from the substance of a live case (statements, documents, COI) and uses them to prioritise, flag, validate or challenge evidence, or to recommend next steps, it materially influences the examination and remains within point 7(c). While the filter mechanism in Article 6(3) may be relied upon for narrow procedural or purely preparatory tasks, the systems assessing reliability of evidence generally materially influence decision-making and should in principle be classified as high-risk (e.g. in case of detection of document morphing).
(400) Where a single integrated assistant is intended to assist in the examination of eligibility (and associated complaints) and its outputs can materially influence substance (e.g. by validating or challenging evidence, prioritising issues, or pre-classifying status elements), the overall AI system falls within the use case listed in point 7(c) of Annex III. If individual functionalities are truly separable and put into service independently (e.g. as stand-alone tools), each functionality may be assessed on its own for possible high-risk classification. Some modules can qualify for as the exceptions for AI systems intended to perform narrow procedural or purely preparatory listed in
Article 6(3)(a) and (d) AI Act, while others remain high-risk. However, low-risk modules inside a single assistant that steers eligibility analysis, cannot benefit from the filter mechanism. Nor does embedding low-risk modules inside a single assistant that steers eligibility analysis bring the overall system under the filter mechanism. For the exception in Article 6(3)(c) AI Act to apply, the system must be intended to perform ex-post detection of patterns or deviations.

126

a) Practical examples of AI systems falling within the use case of point 7(c) of Annex III
Evidence appraisal and consistency analysis
–

An AI system intended to assess the authenticity and consistency of documents or the plausibility of personal narratives and to provide credibility signals that the examiner relies on when determining eligibility of migrants to entry the country or asylum-seekers. These outputs validate or challenge evidence relied upon by the examiner and therefore assist the examination.

–

An AI system intended to analyse phone data lawfully obtained from a device to validate routes, timelines or contacts and to produce signals used in an eligibility appraisal. This assists the authority’s appraisal of evidence in the file.

–

An AI system intended to detect document morphing, non-conforming inks, copied signatures or chip and public-key infrastructure validity as part of document verification as a step in the examination procedure for assessing eligibility for a visa, a residence permit or international protection.

Automated comparison of discrepancies against prior submissions
–

An AI system intended to identify substantive or credibility-relevant discrepancies against prior submissions in order to assist the authority’s subsequent examination of the application for asylum, a visa, a residence permit, or an associated complaint. Such an AI system assists the examination.

Origin inference used in the examination
–

An AI system intended to analyse recorded speech to indicate a likely country or region of origin for use in the authority’s eligibility reasoning and selection of country-of-origin information. The output assists the examiner when deciding whether information is treated as proven, contested, prioritised or further investigated in a specific person’s file.
b) Practical examples of an AI system falling outside the use case of point 7(c) of Annex
III

– An AI system intended to provide applicants with answers to frequently asked questions, to guide users to the correct forms, to schedule appointments, or to deliver application status notifications. Such an AI system does not assist the authority in examining eligibility or associated complaints, but its intended purpose is service delivery to migrant applicants.
c) Practical examples of AI systems falling within the use case but exempted under the filter mechanism of Article 6(3)
Narrow procedural tasks (Article 6(3)(a) AI Act)

127

–

An AI system intended only to organise a case file by applying pre-defined categories for storage and retrieval (for example, ‘identity documents”, ‘medical records”, ‘interview notes”), without ranking materials by importance or omitting any items. Applying fixed, predefined labels for storage and retrieval is a narrow procedural operation. The system does not evaluate evidence, set priorities, or influence the assessment.

–

An AI system intended to check the completeness and formatting of visa applications, to sort or assign files for administrative handling based on public and objective criteria, while performing only technical and non-interpretative operations and without assessing the content of the application, determining the applicable procedural track, or otherwise steering the substance of the examination.

–

An AI system intended to highlight verbatim differences between current and previous statements (for example, string-level contrasts), without generating any credibility assessment or recommending follow-up questions; where the system evaluates the significance of the differences or labels them as credibility concerns, the exception no longer applies.

–

A pre-check tool that, under strict, objective rules (e.g., a visa facilitation agreement fixes the fee for applicants from a specific country), routes an applicant to payment of a fixed fee.

–

AI system intended to check the completeness or format of travel authorisation or visa
(ETIAS/VIS) files (e.g. required fields, document presence), without producing any risk score, flag or triage of individuals. Such a system performs narrow procedural tasks, rather than preparatory tasks, since it does not prepare or structure substantive content for the examination.

Preparatory tasks (Article 6(3)(d) AI Act)
–

An AI system intended to transcribe interviews, translate interview transcripts or produce neutral summaries for the file, without advising on next steps or suggesting outcomes. A system that goes beyond these functions, for example by introducing elements not contained in the applicant’s statements, making credibility assessments, or linking the applicant’s statements to the applicable legal framework, will not benefit from the exception.

–

An AI system that carries out large data scanning on electronic devices to extract metadata on the travel route taken by an individual. The system sets out a neutral output from the search providing all pieces of metadata relating to geolocation without preferring one piece of information over another. As such, it could be considered to carry out a preparatory task.

Improving a completed human activity (Article 6(3)(b))
–

An AI system intended to harmonise terminology and correct grammar in a decision after the human assessment has been concluded, without introducing additional reasoning or altering the outcome. A system that infers or formulates legal or factual grounds not explicitly stated or re-evaluates credibility is not covered by the exception.

128

Ex-post pattern detection (Article 6(3)(c))
–

An AI system intended to analyse past, completed eligibility files in order to detect decision-making patterns or deviations for quality-assurance reporting, without proposing outcomes in actual cases.
3.7.5.

Point 7(d): AI systems intended to be used for detecting, recognising or identifying natural persons in migration, asylum or border control management contexts (excluding travel-document verification)

(401) Point 7(d) of Annex III classifies as high-risk AI systems intended to be used by or on behalf of competent public authorities, or by Union institutions, bodies, offices or agencies, in the context of migration, asylum or border control management, for the purpose of detecting, recognising or identifying natural persons, with the exception of the verification of travel documents. Such systems are classified as high-risk because they often apply biometric or identity recognition, where outputs can immediately trigger intrusive measures (extra screening, refusal of entry, restriction of movement, or detention) with limited time and a limited ability to contest. The combination of error rates, demographic bias, and opaque decision logic can therefore translate into wrongful identification and discriminatory treatment.
(402) High-risk classification under point 7(d) of Annex III is determined by the intended purpose; the place of deployment and the sensor modality are not decisive. Verification of travel documents is excluded from the use case listed in point 7(d) of Annex III. On-person checks used within person detection or identification, such as liveness or presentation-attack detection, may fall under that use case and, where biometric identification or categorisation is involved, under the use case listed in point (1) of Annex III.
(403) AI systems used exclusively for search and rescue are not border-control uses and therefore fall outside the the use case listed in point 7(d) of Annex III. Only functions that neither detect, recognise, or identify persons and that do not influence operational decision making may benefit from the exceptions listed in Article 6(3) AI Act.
a) Practical examples of AI systems falling within the use case of point 7(d) of Annex III
Identification of persons at border-crossing points
–

An AI system using live facial recognition for identity checks at border-crossing points, comparing live camera feeds with biometric templates in connected systems and returning identity hits for operator action. Such a system is in scope because the intended purpose is to identify natural persons for border-control purposes, which falls under the terms ‘detect, recognise or identify’.

Detection that cues operational action at land or sea borders
–

AI-combined satellite imagery services, surveillance towers or unmanned platforms that flag human presence for response for a border-control response acting on the persons detected.

129

Such a system is in scope because the intended purpose to detect people approaching a land border and to generate alerts that trigger patrol dispatch, apprehension or second-line checks.
–

An AI system used for maritime surveillance that detects and tracks persons for migration management or border-control operations, including cueing interception or boarding. Such a system is in scope because the intended purpose is to detect and track natural persons for these operations, irrespective of whether the platform operates in territorial waters, the contiguous zone or on the high seas. What matters is the intended purpose, not its location.
By contrast, if an AI system is tasked exclusively for safety of navigation or lifesaving, with its outputs not cueing a border control unit, but sent to a SAR (search and rescue)
coordination, used only to prevent collisions or to coordinate search and rescue, not to initiate or support border-control actions, the system will be out of scope.

–

An AI system intended to analyse sensor data to detect the presence or number of persons in vehicles (including hidden persons) and to generate alerts that prompt second-line checks.
The system is in scope, since it concerns the detection of natural persons for border-control purposes, even without identification. The filter mechanism cannot apply because the alerts generated by the system drive operational action, which is neither a narrow procedural nor preparatory task.

Person-level monitoring in controlled facilities
–

An AI system intended to monitor reception or detention areas, detect or track identified persons, and alert staff for intervention. The system detects or tracks natural persons in a migration-management setting and is therefore in scope. If the system only estimates scenelevel anomalies (for example, a crowd surge or a loud-disturbance spike), without detecting or tracking persons and without person-specific alerts, it is out of scope.
b) Practical examples of AI systems falling outside the use case of point 7(d) of Annex III

AI systems that are not border-control or person-detection functions
–

An AI system intended to detect persons in distress at sea exclusively to coordinate searchand-rescue operations, with no link to migration-management or border-control tasks. Such a system is out of scope because the intended purpose is lifesaving, not border control.

–

An AI system intended to verify travel or identity documents (for example, chip or PKI validity, morphing or ink anomalies, copied signatures). Verification of travel or identity documents is excluded from this use case.

–

An AI system embedded in a maritime or unmanned platform used by border authorities, where it is intended and technically limited to collision avoidance (for example detecting obstacles, including persons, only to prevent impacts and without generating alerts for interception, tracking, triage or any border-control response). Such a system is out of scope because its outputs are used exclusively for safety of navigation, not for migration, asylum or border-control management. Where an AI system with the same sensing or detection capability is intended to be used to cue or support border-control actions regarding persons, it will be in scope.
130

Analytics that do not detect, recognise or identify persons
–

An AI system intended to analyse historical data to identify patterns of document fraud and to inform general indicators or staffing, without person detection. Such a system is out of scope, since its output does not detect, recognise or identify natural persons. If the patterns identified by the system are later applied to named individuals to triage them, the system would be in scope since it performs a person-level risk assessment.

–

An AI system intended to estimate crowd size or gate occupancy to balance lanes and reduce queues. Such a system is out of scope, provided it is designed so that it does not detect, recognise or identify persons and does not generate person-level alerts.
c) Practical example of AI systems falling within the use case but exempted under the filter mechanism of Article 6(3)

–

An AI system intended to stabilise, denoise or enhance video feeds without performing any detection, recognition or identification of persons and without producing cues for operational response. Such a system falls within the exception for AI systems intended to perform a preparatory task listed in Article 6(3)(d) AI Act.
3.8. Administration of justice and democratic processes

(404) Point 8 of Annex III AI Act identifies the administration of justice and democratic processes as one of the areas in which certain use cases of AI systems can pose significant risks to the health, safety and fundamental rights of natural persons. Recital 61 AI Act justifies the classification of such systems as high-risk due to their potentially significant impact on democracy, the rule of law and fundamental rights and freedoms, including the right to an effective remedy and to a fair trial.
3.8.1.

Point 8(a): AI systems intended to be used to assist judicial authorities or in alternative dispute resolution

(405) Point 8(a) of Annex III classifies as high-risk AI systems intended to be used by judicial authorities or on their behalf to assist a judicial authority in researching and interpreting facts and the law and in applying the law to a concrete set of facts, or to be used in a similar way in alternative dispute resolution. Point 8(a) of Annex III therefore contains two distinct use cases: first, AI systems intended to be used by judicial authorities or on their behalf to assist a judicial authority in researching and interpreting facts and the law and in applying the law to concrete set of facts; and, second, AI systems intended to be used in alternative dispute resolution (for example intended for arbitration procedures) in researching and interpreting facts and the law and in applying the law to a concrete set of facts.
First use case: AI systems intended to be used to assist judicial authorities i. Overview of use cases and horizontal issues
(406) The first high-risk use case listed in point 8(a) of Annex III concerns AI systems intended to be used by a judicial authority or on its behalf to assist that authority in researching and interpreting facts and the law and in applying the law to a concrete set of facts. The classification of such AI
131
