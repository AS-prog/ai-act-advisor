---
name: directrices-art6-alto-riesgo-borrador-parte3-19-iv-high-risk-classification-according-to
description: "Comisión Europea: directrices art6 alto riesgo borrador parte3, sección «IV. High-risk classification according to Article 6(2) and Annex III AI Act (parte 15)» (págs. 117-124). Documento de 2026-05-19, idioma en."
metadata:
  type: reference
  documento: directrices-art6-alto-riesgo-borrador-parte3
  emisor: Comisión Europea
  fecha: 2026-05-19
  idioma: en
  seccion: "IV. High-risk classification according to Article 6(2) and Annex III AI Act (parte 15)"
  paginas: 117-124
  origen: 2026-05-19-directrices-art6-alto-riesgo-borrador-parte3-en.pdf
  oficial: false
---
# IV. High-risk classification according to Article 6(2) and Annex III AI Act (parte 15)

–

AI systems intended for the detection of objects (e.g. weapons, suspicious parcels, dangerous objects, stolen goods including cultural objects and fine art). Such AI systems do not fall within the use cases listed in point 6 of Annex III, nor do they constitute biometrics within the meaning of point 1 of Annex III.

–

AI systems intended for the detection of unusual behaviour or movements, such as running, raised arms, a fighting stance, a physical position that could indicate someone is holding a weapon, etc., real-time or in video feeds (not identifying a person, but whether a process or behaviour is potentially unlawful).

–

AI systems detecting gunshot sounds in real time. Such AI systems do not fall within the use cases listed in in point 6 of Annex III, since they function based on the detection of sounds and not people.

–

AI systems used by custom authorities to assess consignments (goods crossing the border).
Custom authorities checking consignments normally do not classify as law enforcement authorities within the context of point 6 of Annex III. In addition, those systems evaluate the compliance of goods with EU legislation based on verifiable data (e.g. container number, description of goods, routing, transport, payment method), not personal characteristics or behaviour or persons. In certain cases, such AI systems may also process information about the prior involvement of the importer or exporter in irregularities related to the import of goods, their affiliation to criminal organisations, or a criminal record for drug trafficking.
Such systems, as noted in the Guidelines on prohibited artificial intelligence practices (para.
214), fall outside the scope of the prohibition in Article 5(1)(d)AI Act because any prediction of the likelihood of a natural person being involved in the import or export of illicit goods is not solely based on profiling, but on objective and verifiable information related to the goods and the importer or exporter’s prior involvement in criminal activity and subject to a human review to determine whether the situation requires a customs control or risk mitigation action.

–

AI systems used by customs and/or law enforcement authorities to analyse data related to the movement of goods and transport operations, such as shipping routes, frequency and patterns of consignments, anomalies in declared cargo, transport modalities, etc., to detect misuse of commercial transport systems to transport trafficked goods. Such AI systems do not fall within the use cases listed in point 6 of Annex III, since they do not seek to predict the likelihood of a natural person committing an offence or to profile a natural person. Rather, they review objective and verifiable data relating to the commercial transportation of goods to determine an anomaly that may require further investigation.
3.7. Migration, asylum and border control management

(373) Point 7 of Annex III AI Act lists four high-risk use cases of AI systems intended to be used in the field of migration, asylum, and border control management. As explained in Recital 60 AI Act, AI systems used in these fields affect people who may be in a particularly vulnerable position and whose treatment can determine access to a territory, international protection, residence, detention or return. Such uses therefore carry significant implications for the entry and stay of individuals in the territory of the EU and their safety and fundamental rights. Any deployment of an AI system in this field must also comply with the applicable EU rules and procedures on asylum, visas, and border-management and fully respect the GDPR/EUDPR and the Charter, including the principle
116

of non-refoulement and the right to international protection, as well as the Member States’ obligations under the 1951 Refugee Convention and its 1967 Protocol. In the AI Act, the EU legislature has emphasised that accuracy, non-discrimination, and transparency are particularly important to safeguard fundamental rights, maintain public trust, and ensure effective remedies. As explained in Section 2.6 above, the fact that an AI system is classified as a high-risk AI system under these use cases should not be understood to mean that the use of the system is lawful under other acts of Union law or under national law compatible with Union law.
3.7.1. Overview of use cases and horizontal issues
(374) Point 7 of Annex III lists four high-risk AI systems intended to be used by or on behalf of competent public authorities, or Union institutions, bodies, offices or agencies, in the field of migration, asylum, and border-control management, in so far as such use is permitted under relevant Union or national law. In particular, that provision classifies the following use cases as high-risk:
(a)

Polygraphs or similar tools;

(b)

AI systems intended to assess a risk posed by a natural person who intends to enter or who has entered into the territory of a Member State (e.g., security, irregular-migration, or health risk);

(c)

AI systems intended to assist a competent public authority in examining an asylum, visa, or residence application and associated complaints with regard to the eligibility of the natural persons applying for a status (including a related assessment of the reliability of evidence);
and

(d)

AI systems intended to detect, recognise, or identify natural persons in the migration, asylum or border-management context (with the exception of the verification of travel documents).
i. The concept of ‘competent authorities” and ‘on be

(375) The AI system use cases listed in point 7 of Annex III concern those systems intended to be used by or on behalf of competent public authorities or by Union institutions, bodies, offices or agencies in the migration, asylum and border-management fields. This covers the national authorities designated pursuant to the EU or national law governing the field, as well as Union institutions, bodies, offices or agencies acting within their mandates under that law.
(376) Without prejudice to the assessment on the compatibility of the use of an AI system with the Charter and EU secondary law in this context, these authorities may potentially include the following nonexhaustive examples:

-

Border-control authorities under Regulation (EU) 2016/399 (‘the Schengen Borders Code’)79 and Regulation (EU) 2019/1896 (‘the European Border and Coast Guard framework’)80.
These authorities perform checks at external borders and related tasks. The ‘European Border

79

Regulation (EU) 2016/399 of the European Parliament and of the Council of 9 March 2016 on a Union Code on the rules governing the movement of persons across borders (Schengen Borders Code) (codification) OJ L 77,
23.3.2016, pp. 1–52.
80
Regulation (EU) 2019/1896 of the European Parliament and of the Council of 13 November 2019 on the
European Border and Coast Guard OJ L 295, 14.11.2019, pp. 1–131.

117

and Coast Guard” is composed of the national authorities responsible for border management and Frontex;

-

Consular authorities and central visa authorities responsible for examining visa applications and taking visa decisions under Regulation (EC) No 810/200981 (‘the Visa Code’) and
Regulation (EU) 2021/113482(‘the VIS framework’);

-

Asylum authorities competent under Directive 2013/32/EU83, and, as of 12 June 2026,
Regulation (EU) 2024/1348 (‘the Asylum Procedures Regulation’)84 which will replace the
Directive; in particular ‘determining authorities” responsible for first-instance examination of applications for international protection;

-

Immigration/return/detention authorities acting under the Return Directive 2008/115/EC85 including authorities issuing and enforcing return decisions and operating return/detention procedures;

-

Competent authorities and other appeal or review bodies (including administrative appeal bodies and judicial authorities), where they examine appeals or associated complaints relating to asylum, visa or residence decisions under the applicable Union and national legal framework;

-

Union bodies, offices and agencies acting within their mandate in the aforementioned fields, notably Frontex when acting under Regulation (EU) 2019/1896 (‘the EBCG Regulation’)86, the European Agency for Asylum when acting under Regulation (EU) 2021/2303 87, and euLISA set up under Regulation (EU) 2018/1726 for the management/operation of large-scale
IT systems (VIS, SIS, Eurodac) established under Regulation (EU) No 603/201388, as a Union system supporting asylum and migration management through biometric data processing, and as of 12 June 2026 under Regulation (EU) 2024/135889, which will replace Regulation (EU)
No 603/2013.

81

Regulation (EC) No 810/2009 of the European Parliament and of the Council of 13 July 2009 establishing a
Community Code on Visas (Visa Code) OJ L 243, 15.9.2009, pp. 1–58.
82
Regulation (EU) 2021/1134 of the European Parliament and of the Council of 7 July 2021 for the purpose of reforming the Visa Information System OJ L 248, 13.7.2021, pp. 11–87.
83
Directive 2013/32/EU of the European Parliament and of the Council of 26 June 2013 on common procedures for granting and withdrawing international protection (recast) OJ L 180, 29.6.2013, pp. 60–95.
84
Regulation (EU) 2024/1348 of the European Parliament and of the Council of 14 May 2024 establishing a common procedure for international protection in the Union OJ L, 2024/1348, 22.5.2024.
85
Directive 2008/115/EC of the European Parliament and of the Council of 16 December 2008 on common standards and procedures in Member States for returning illegally staying third-country nationals OJ L 348,
24.12.2008, pp. 98–107.
86
Regulation (EU) 2019/1896 of the European Parliament and of the Council of 13 November 2019 on the
European Border and Coast Guard OJ L 295, 14.11.2019, pp. 1–131.
87
Regulation (EU) 2021/2303 of the European Parliament and of the Council of 15 December 2021 on the
European Union Agency for Asylum OJ L 468, 30.12.2021, pp. 1–54.
88
Regulation (EU) No 603/2013 of the European Parliament and of the Council of 26 June 2013 on the establishment of 'Eurodac' for the comparison of fingerprints (recast) OJ L 180, 29.6.2013, pp. 1–30.
89
Regulation (EU) 2024/1358 of the European Parliament and of the Council of 14 May 2024 on the establishment of 'Eurodac' for the comparison of biometric data OJ L, 2024/1358, 22.5.2024.

118

(377) Depending on the field, the following instruments may be relevant to determine the competent authority, including the competent EU institution, body or agency: Regulation 2024/135690 (‘the
Screening Regulation’) as regards pre-entry screening and referral; the Asylum Procedures
Regulation91 as regards asylum procedures; Regulation 2024/134992 (‘the Return Border
Procedure’) as regards return border procedures; and Regulation 2024/135193 (‘the Asylum and
Migration Management Regulation’).
ii. Interplay with other Union rules
(378) The high-risk rules of the AI Act apply to AI systems classified as high-risk pursuant to point 7 of
Annex III in addition to the rules on EU asylum, visa and border-management procedures. The intended use of an AI system must comply with those rules, and must therefore respect the applicable guarantees, including the principle of non-refoulement and effective access to the asylum procedure, as well as the Member States’ obligations under the 1951 Refugee Convention and its
1967 Protocol Where an AI system, if deployed as a component and authorised within the infrastructure of systems such as the Visa Information System (VIS), the Schengen Information
System (SIS), the European Dactyloscopy database (Eurodac), the Entry/Exit System (EES), the
European Travel Information and Authorisation System (ETIAS), the European Criminal Records
Information System – Third Country Nationals (ECRIS-TCN), the Central Repository for
Reporting and Statistics (CRRS) or EU Interoperability components, is designed to use data from those systems it must respect those instruments’ purpose limits, access conditions and fundamental rights’ safeguards.
iii. Interplay with biometric high-risk systems
(379) Where the functionality of an AI system falling within one of the use cases listed in point 7 of
Annex III involves the processing of biometric data or techniques (e.g. face, fingerprints, gait), the system will also be classified as high-risk pursuant to point 1 of Annex III (Biometrics), if it falls in one of the use cases listed in point 1 (a),(b) or (c) and the considerations set out in section 2.3.1 apply. As a consequence, the system will be subject to a third-party conformity assessment, since it is classified as high-risk pursuant to point 1 of Annex III.
(380) AI systems intended to be used to verify travel or identity documents, including checking for morphing, unusual inks, copied signatures, or chip or Public Key Infrastructure (PKI) validity, fall outside the scope of the use case listed in point 7(d) of Annex III. By contrast, AI systems intended to be used to perform presentation-attack checks, including on-person liveness checks, used within person detection and recognition flows are not document-verification features and will generally be classified as high-risk under the use case listed in point 7(d) of Annex III, unless the system is used for RBI, in which case it will be classified as high-risk pursuant to point 1(a) of Annex III. In seamless border procedures, where travellers actively present themselves for one-to-one verification against their travel document, presentation-attack detection used solely as an anti90

Regulation (EU) 2024/1356 of the European Parliament and of the Council of 14 May 2024 introducing the screening of third-country nationals at the external borders OJ L, 2024/1356, 22.5.2024.
91
Regulation (EU) 2024/1348 of the European Parliament and of the Council of 14 May 2024 establishing a common procedure for international protection in the Union OJ L, 2024/1348, 22.5.2024.
92
Regulation (EU) 2024/1349 of the European Parliament and of the Council of 14 May 2024 establishing a return border procedure OJ L, 2024/1349, 22.5.2024.
93
Regulation (EU) 2024/1351 of the European Parliament and of the Council of 14 May 2024 on asylum and migration management OJ L, 2024/1351, 22.5.2024.

119

spoofing safeguard remains part of that verification function and does not, on its own, classify the system as high-risk pursuant to point 7 of Annex III. Where the same functionality is used to support operational person detection, tracking or identification beyond verification, the system will be classified as high-risk pursuant to point 7 of Annex III, unless the conditions for classification pursuant to point 1 of Annex III are met, in which case that classification will apply.
(381) Classification as high-risk follows the intended use of the systems. AI systems intended to be used exclusively for search-and-rescue (lifesaving) do not fall within the border control use case and therefore will not be classified as high-risk pursuant to point 7 of Annex III. The same system intended to be used for migration or border control may be classified as high-risk pursuant to point
7 of Annex III, provided the system meets the other conditions of that point. Many AI systems can be used for both border control and search-and-rescue or navigation safety. Where a system’s intended use includes both, the system will fall within the scope of the use cases listed in point 7 of
Annex III because of its intended border-control use.
iv. Interplay with AI prohibited practices
(382) Where an AI system used by or on behalf of competent public authorities in the field of migration, asylum, and border-control management falls under one of the practices listed in Article 5 AI Act, its use should be prohibited. Where not all of the conditions of that provisions are met for a prohibition to apply, the system should be classified as high-risk, provided it falls within one of the use cases listed in point 1 or point 7 of Annex III AI Act.
(383) Article 5(1)(b) AI Act prohibits AI systems that exploit a natural person’s vulnerabilities (age, disability, specific social or economic situation) with the objective or effect of materially distorting that person’s behaviour in a manner likely to cause significant harm. Behaviour-analysis tools (e.g., those assessing voice-stress, micro-expressions, or gaze patterns) are not, in themselves, prohibited merely because they misinterpret stress or cultural expressions. Such misinterpretations may affect the assessment of evidence, but do not necessarily have the object or effect of distorting a natural person’s behaviour.
(384) AI systems that, over a period of time, evaluate or rank migrants based on physiological reactions, behaviour (including online activity), or other personal data to derive a generalised trustworthiness or risk score, especially where used across contexts or to produce detrimental treatment, may amount to social scoring prohibited by Article 5(1)(c) AI Act.. Providers and deployers must also ensure that the use does not amount to prohibited social-scoring practice under Article 5(1)(c) AI
Act.
(385) Tools that predict future criminal behaviour of persons at borders (e.g., ‘criminal intent” from gaze/speech patterns) may fall within the prohibition listed in Article 5(1)(d) AI Act. Where the conditions of that provision are met, the prohibition applies. Where not all conditions of Article
5(1)(d) AI Act are met, the same tool may be classified as high-risk under point 7(b) of Annex III where its intended purpose is the assessment of a migration risk. Providers and deployers must ensure that the use does not amount to prohibited individualised crime risk assessments under
Article 5(1)(d) AI Act.
(386) Deception or credibility analysis AI tools (e.g. micro-expression/voice-stress) used at borders are not considered RBI systems covered by the prohibition in Article 5(1)(h) AI Act, because they do

120

not establish the identity of natural persons via a database comparison. Such AI tools will generally be classified as high-risk pursuant to point 7 of Annex III.
(387) The deployment of an AI system for real-time RBI for law enforcement purposes in the vicinity of a border is only permitted if strictly necessary for the objectives listed in Article 5(1)(h)(i)-(iii) AI
Act and if all the requirements of Article 5(2)-(5) AI Act are fulfilled. However, as explained in the
Commission Guidelines on prohibited artificial intelligence practices, a border crossing point is not considered a publicly accessible space, so that the prohibition does not apply in that context, whereas the street leading to a border crossing point or a forest in the vicinity normally is such a space. Some spaces may have a dual function. For example, an airport is generally considered a publicly accessible space as regards its common areas, but the area dedicated to border control
(where the customs officials stand, and passports or ID checks are carried out) is not and therefore the deployment of real-time RBI systems in such areas is excluded from the scope of the prohibition, but likely to be classified as high-risk pursuant to either point 1 or point 7 of Annex III AI Act.
3.7.2.

Point 7(a): AI systems intended to be used as polygraphs or similar tools

(388) Point 7(a) of Annex III classifies as high-risk AI systems intended to be used in the field of migration, asylum and border control management as polygraphs or similar tools. Such AI systems are generally designed to analyse physiological, behavioural or biometric signals with the purpose of inferring deception by natural persons in migration, asylum or border-control settings. Where such systems are intended to be used by or on behalf of law enforcement authorities in those settings, they will be classified as high-risk pursuant to point 6(b) of Annex III.
(389) The high-risk classification under point 7(a) of Annex III reflects the serious consequences that such systems may have for decisions on entry, stay or protection, combined with documented risks of inaccuracy and bias. Such systems are considered high-risk when intended to be used in the migration, asylum and border control contexts even if the competent authorities may not take the final decision on entry, stay or protection. Even where a human makes the final decision, the output of the system may significantly influence that decision due to overreliance and automation bias.
(390) Polygraphs or similar tools cover a range of modalities, including analysis of voice patterns (voicestress analysis), micro-expressions or facial muscle activity, gaze, posture, or body movements, thermal imaging of physiological responses, multimodal interview platforms combining these signals (see chapter 3.6.3 Point 6(b): Polygraphs and or similar tools). If any of the modalities are used by the AI system for purposes other than to infer or detect deception (e.g. for language or dialect detection), the system is unlikely to be classified as high-risk under point 7(a) of Annex III.
a) Practical example of an AI system falling within the use case of point 7(a) of Annex
III
–

Border guards deploy an AI system in secondary inspection at an external airport. During an officer-led interview, the system analyses the traveller's verbal and non-verbal responses and provides the officer with a supplementary credibility indicator.

– A consular authority uses an AI system that analyses an applicant's voice patterns and verbal responses during visa interviews conducted by consular officers, providing the officer with supplementary indicators relating to the veracity of the statements made.
121

(391) Such systems fall within point 7(a) because they function as polygraph-type tools used in migration, asylum or border-control procedures to assess truthfulness. The filter mechanism of Article 6(3) AI
Act does not apply to the systems described in the example above, since the system generates evaluative outputs that directly influence the substance of an individual examination and cannot be considered a narrow procedural, preparatory or post-decision task under the exceptions listed in that provision.
(392) Additionally, such AI systems are not prohibited per se under Article 5(1)(b) AI Act, unless designed or used to materially distort behaviour of vulnerable persons in a significantly harmful manner. Additionally, such AI systems are not prohibited under Article 5(1)(h) AI Act, nor are they classified as high-risk under point 1(a) of Annex III because they are not RBI systems: they operate with the person’s active involvement in a face-to-face interview (so not ‘remote”), they do not perform one-to-many identity matching against a reference database (they infer credibility, not identity), and their processing is not aimed at establishing identity (in real time).
b) Practical examples of AI systems falling outside of the use case of point 7(a) of Annex
III
–

AI system that processes interview audio (as lie-detection tools do) but does not infer deception. Instead, it automatically transcribes the interview or translates responses into another EU language for the case file.

–

AI system intended only to create neutral, non-prioritised summaries of interviews for the file, without credibility scoring or recommendations. This system falls outside point 7(a) of
Annex III because the system does not assess deception.
c) Practical examples of AI systems falling within the use case but exempted under the filter mechanism of Article 6(3)

–

An AI system intended to normalise audio/video signals (e.g. denoising, adjusting lighting, extracting facial landmarks) so that caseworkers can review recordings more easily. If the system does not produce or imply deception inferences, it could benefit from the exception for AI systems intended to perform a preparatory task listed in Article6(3)(d) AI Act.
3.7.3.

Point 7(b): AI systems intended to be used for risk assessment of persons seeking to enter or stay

(393) Point 7(b) of Annex III classifies as high-risk AI systems intended to be used by or on behalf of competent public authorities or by Union institutions, bodies, offices or agencies to assess a risk, including a security risk, a risk of irregular migration, or a health risk, posed by a natural person who intends to enter or who has entered into the territory of a Member State.
(394) The most important element in determining whether an AI system should be classified as high-risk pursuant to point 7(b) of Annex III is the intended purpose of the system to produce an individual risk score, category or flag that can influence decisions on entry, stay, detention, return or related measures. By contrast, AI systems that combine data streams into a higher-level summary (for example, by summing, averaging, or grouping data) to produce aggregate flow or staffing analytics,
122

where outputs are not linked to identified individuals, should not be classified as high-risk pursuant to point 7(b) of Annex III.
(395) AI systems that fall within the scope of the use case listed in point 7(b) of Annex III often amount to profiling because they assess a risk posed by a natural person. What matters is whether the system processes personal data in that context. In such a case, the system cannot benefit from the filtering mechanism in Article 6(3) AI Act. For example, AI systems that output a per-person risk flag or risk score, by using or inferring information about that person, conduct automated processing of personal data to evaluate or predict that person’s behaviour or movements and thus perform profiling. In contrast, if anonymised data are processed by the system so that no individual is identified or identifiable, the system should not be considered to perform profiling. Low-level aggregation or linkability with other datasets can still make aggregated data (i.e. combined statistics on means, counts, rates) fall under the definition of personal data. AI systems that produce aggregate-only outputs that are never applied to identified or identifiable persons should be considered to fall outside the use case listed in point 7(b) of Annex III. However, if the system applies an aggregate indicator to a named or identifiable traveller to generate a risk flag or triage, its use involves personal data and constitutes profiling and therefore should be classified as highrisk pursuant to that provision.
(396) An AI system falling with the use case listed in point 7(b) of Annex III may only benefit from the filter mechanism in Article 6(3) AI Act where it performs a narrow procedural or purely preparatory function that does not itself amount to profiling and does not materially influence the substance or outcome of an individual risk assessment. However, combined configurations are assessed as a whole, not individually (see Section 2.3. above).
a) Practical examples of AI systems falling within the use case of point 7(b) of Annex III
Person-level migration or security risk scoring
–

Risk scoring for entry checks: An AI system intended to analyse a traveller’s personal history, travel patterns and watch-list matches to produce a ‘risk score” used by border guards to decide whether to refer the person to second line checks.

–

Automated security risk flagging: An AI system intended to compute per-person risk flags
(security, irregular-migration, or health) during travel authorisation or visa processing, using indicators based on certain trends and screening rules, and to refer named travellers for further checks.

–

Visa risk scoring (case pattern): An AI system intended to rank visa applicants by predicted overstay risk using nationality and similar proxies, leading to intensive tracks for specific groups. Such an AI system may fall under the prohibition listed in Article 5(1)(c) AI Act only if it amounts to generalised social behaviour scoring over time across contexts treating the person detrimentally.

–

Online search-based migration intent flagging: An AI system intended to infer a named traveller’s likelihood of irregular migration from their recent online search behaviour and to generate a risk flag for individual persons used at entry control. Such an AI system is not prohibited under the AI Act unless (i) it performs social scoring within the meaning of Article
123
