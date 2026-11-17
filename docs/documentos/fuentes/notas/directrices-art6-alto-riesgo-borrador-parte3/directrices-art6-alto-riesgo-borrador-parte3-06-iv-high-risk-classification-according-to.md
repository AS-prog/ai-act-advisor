---
name: directrices-art6-alto-riesgo-borrador-parte3-06-iv-high-risk-classification-according-to
description: "Comisión Europea: directrices art6 alto riesgo borrador parte3, sección «IV. High-risk classification according to Article 6(2) and Annex III AI Act (parte 2)» (págs. 13-20). Documento de 2026-05-19, idioma en."
metadata:
  type: reference
  documento: directrices-art6-alto-riesgo-borrador-parte3
  emisor: Comisión Europea
  fecha: 2026-05-19
  idioma: en
  seccion: "IV. High-risk classification according to Article 6(2) and Annex III AI Act (parte 2)"
  paginas: 13-20
  origen: 2026-05-19-directrices-art6-alto-riesgo-borrador-parte3-en.pdf
  oficial: false
---
# IV. High-risk classification according to Article 6(2) and Annex III AI Act (parte 2)

Example: An AI system intended to analyse past eligibility checks completed by public administrators in the public administration in order to detect decision-making patterns or deviations for quality-assurance and reporting, without proposing outcomes on live cases or evaluating the performance of staff members, e.g., in the context of the annual appraisal.
Assessment: If the system is intended to be used after the officials in the public administration have made their assessments, the system could be relevant for exemption pursuant to point (c) of Article
6(3) AI Act and does not constitute profiling. The comparison done by the system would allow the public administrator to detect divergences identified by the system from past decision-making patterns in similar cases, as well as all the elements and the evidence taken into consideration when the first assessment was made. The assessor or a quality assistance control will have the role to decide after proper human review whether the identified discrepancies are relevant or not for the completed assessment.
d) Preparatory task
(103) Point (d) of Article 6(3) AI Act lists the fourth condition under which the filter mechanism applies, which is that the AI system is intended to perform a preparatory task to an assessment relevant for the purposes of the use cases listed in Annex III.
(104) The notion ‘preparatory’ in point (d) of Article 6(3) AI Act refers to tasks that occur prior to the actual assessment process. This specification is important, since it differentiates the preparatory task exemption in point (d) from the narrow procedural task exemption in point (a) of Article 6(3)
AI Act, which can occur during the assessment process so long as it is clearly defined and limited in scope. At the same time, if the narrow procedural task occurs prior to the assessment and is preparatory in nature, both points in letters a) and d) may apply.
(105) As specified in Recital 53 AI Act, the preparatory nature of the task should be such that the ‘possible impact of the output of the system [is] very low in terms of representing a risk for the assessment to follow’. This aligns to the objectives of Article 6(3) AI Act, which sets out the conditions under which AI systems should not be considered to lead to a significant risk of harm, in particular because they do not materially influence the decision-making. Recital 53 AI Act specifies that an AI system that does not materially influence the outcome of decision-making should be understood as an AI system that does not have an impact on the substance, and thereby the outcome, of decision-making, whether human or automated.
(106) Recital 53 AI Act provides as examples AI systems performing preparatory tasks such as indexing, searching, processing, and linking. Such tasks add structure to the inputs that will be used in the later assessment producing an outcome, but they do not provide themselves an assessment leading to an outcome.
(107) The decisive factor in determining whether a task is ‘preparatory’ is the task’s role in the decisionmaking process and proximity to the final human decision. If a task is deemed preparatory, the filter mechanism in point (d) of Article 6(3) AI Act may be applicable, regardless of the specific field in which the system will be used.

12

(108) If an AI system’s output is intended to inform a human operator’s assessment, it may be considered to perform a preparatory task only if the system’s output is a general input or factor, for example supplementary information that supports an operator’s decision-making process. Where the AI system is intended to produce a specific recommendation or evaluation of the case, it plays a decisive role in the assessment or the decision and can therefore not be considered to perform a preparatory task within the meaning of point (d) of Article 6(3) AI Act.
Example: An AI system is intended to be used for assessing data relevant to a decision (e.g. in relation to public benefits) and provides a human operator with references to the relevant legal provisions, information on jurisdiction, and possibly existing internal guidelines relevant to the decision-making process.
Assessment: The tasks performed by the system could be considered as preparatory within the meaning of point (d) of Article 6(3) AI Act, since they neither analyse nor evaluate the concrete cases at hand and do not produce an output that materially influences the decision. Rather, the system references general information as a supplementary information for the human assessor to consider in his or her decision.
2.7.2. Exception for profiling
(109) Article 6(3) AI Act provides that the filter mechanism may not be applied where an AI system performs profiling of natural persons. Article 3(52) AI Act defines the notion of profiling by crossreferring to Article 4(4) GDPR.
(110) Pursuant to that provision, profiling is to be understood as any automated form of processing, which is carried out on personal data with the objective to ‘evaluate certain personal aspects’ relating to a natural person5. That definition consists of three cumulative elements:
(i) there must be an automated form of processing;
(ii) which is carried out on personal data; and
(iii) the objective of which must be to evaluate personal aspects relating to a natural person.
(111) It is only if all three conditions are fulfilled that an AI system classified as high-risk pursuant to
Article 6(2) AI Act does not benefit from the exemptions listed in Article 6(3) AI Act. While the element of automated processing will always be fulfilled with regard to AI systems, providers must determine whether the data input of the system includes personal data and whether the system is intended to be used to evaluate personal aspects relating to a natural person. Such an evaluation is normally conducted with the purpose of analysing or predicting personal aspects, for instance concerning that natural person’s performance at work, economic situation, health, personal preferences, interests, reliability, behaviour, location or movements. In other words, profiling means the use of information about an individual (or group of individuals) and evaluating their characteristics or behaviour patterns in order to place them into a certain category or group, in

5

See also Article 29, Data Protection Working Party, Guidelines on Automated individual decision-making and
Profiling for the purposes of Regulation 2016/679, WP251 rev.01, 6.2.2018, p. 6 and 7, endorsed by the European
Data Protection Board (EDPB).

13

particular to analyse, infer or make predictions about, for example, their ability to perform a task, interests, or likely behaviour6.
For example, AI system used by customs authorities to assess the risk of goods entering the EU for not complying with legislation applicable at the border on the basis of information about the economic operators related to goods (e.g. container number, description of goods, routing, transport, payment method). The processing is not evaluating personal aspects of a natural person, but assesses the risk of non-compliant consignments, hence such evaluation would not amount to profiling.
(112) Where the personal data are not used to perform an evaluation of personal characteristics (which must always include a form of prediction, assessment or judgement) that evaluation will not constitute profiling7. For instance, a simple classification of individuals based on personal characteristics such as their age, sex, and height does not necessarily lead to profiling. Whether an evaluation includes predictions or the drawing of conclusions will depend on the purpose of the classification8.
Example: An AI system is intended to be used in the context offor th recruitment of employees. The system is used to identify deviations from previous recruitment decision-making patterns before recruitment is completed (to detect potential inconsistencies and deviations from corporate recruitment policies), while evaluating the personal characteristics of the recruiters conducting the job interviews.
Assessment: The evaluation of the recruiter’s decisions and their personal characteristics to analyse possible deviations from previous decision-making patterns constitutes profiling. While the use of the system could fall under point (c) of Article 6(3) AI Act, the fact that the system also involves the processing of personal data to profile recruiters means that the filter mechanism listed in that provision is not applicable.
2.7.3. Self-assessment by the provider, registration and monitoring of systems benefitting from the filter mechanism
(113) Whether an AI system may benefit from the filter mechanisms in Article 6(3) AI Act depends on a self-assessment by the provider.
(114) The consequence of applying the filter mechanism is that the AI system should not be classified as high-risk and therefore that neither the obligations for providers nor for deployers set out in Chapter
III of the AI Act apply in relation to that system. However, Article 6(4) AI Act sets out specific obligations for providers of such AI systems, which are:

6

Para. 154 of the Commission Guidelines on prohibited artificial intelligence practices established by Regulation
(EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence and amending Regulations (EC) No 300/2008, (EU) No 167/2013, (EU) No 168/2013,
(EU) 2018/858, (EU) 2018/1139 and (EU) 2019/2144 and Directives 2014/90/EU, (EU) 2016/797 and (EU)
2020/1828 (Artificial Intelligence Act), Text with EEA relevance (OJ L, 2024/1689).
7
See also Article 29 Data Protection Working Party, Guidelines on Automated individual decision-making and
Profiling for the purposes of Regulation 2016/679, p. 6-7, endorsed by the EDPB.
8
Article 29 Data Protection Working Party, Guidelines on Automated individual decision-making and Profiling for the purposes of Regulation 2016/679, p. 6-7, endorsed by the EDPB.

14

(i)
(ii)

to document the assessment before the AI system is placed on the market or put into service, and to register the AI system in the EU database established pursuant to Article 71 AI Act, which is intended to ensure the traceability of exempted AI systems.

(115) The assessment should contain:
(i)
(ii)
(iii)
(iv)

a description of the intended purpose of the AI system;
a description why the system qualifies as high-risk pursuant to Article 6(2) AI Act;
a description which condition or conditions listed under Article 6(3) AI Act are considered to apply and why;
a description why the system does not perform profiling, in which case the filter mechanism of Article 6(3) AI Act should not be applied.

(116) The assessment should be recorded in a way that it can be made available at any time upon the request of a market surveillance authority. Deployers procuring AI systems are encouraged to verify the use of the exception in the EU database under Article 71 for their due diligence purposes.
2.7.4. Protection against circumvention
(117) The AI Act sets out several safeguards against the misapplication of the filter mechanism in Article
6(3) AI Act. According to Article 80 AI Act, market surveillance authorities may carry out evaluations of AI systems in respect of their classification as high-risk, request the provider of the system to bring that system into compliance with the high-risk requirements of the AI Act, and request the provider of the system to take corrective actions. Where the market surveillance authority finds that an AI system was misclassified as non-high risk to circumvent the application of the high-risk requirements and obligations in the AI Act, it is also empowered to impose penalties on the provider pursuant to Article 99 AI Act.
3. High-risk AI systems in the areas listed in Annex III
(118) This Section examines all high-risk use cases under each of the eight areas listed in Annex III AI
Act and provides examples of AI systems that fall within or outside the scope of those use cases or that may be exempted under the filter mechanism of Article 6(3) AI Act, even if they fall within one of those use cases.
3.1. Biometrics
(119) Point 1 of Annex III AI Act lists three high-risk use cases covering AI systems intended to be used in the field of biometrics, in so far as such use is permitted under relevant Union or national law.
3.1.1.

Overview of use cases and horizontal issues

(120) Point 1 of Annex III AI Act includes the following use cases:
(a) Remote biometric identification (RBI) systems;
(b) AI systems intended to be used for biometric categorisation, according to sensitive or protected attributes or characteristics based on the inference of those attributes or characteristics; and
15

(c) AI systems intended to be used for emotion recognition.
(121) The aforementioned use cases are classified as high-risk given their potential intrusiveness on the rights and freedoms of the persons concerned by the systems, including because of the systems’ reliance on biometric data and their sensitive nature. As explained in Section 2.6 above, the fact that an AI system is classified as a high-risk AI system under these use cases should not be understood to mean that the use of the system is lawful under other acts of Union law or under national law compatible with Union law.

i.

Biometric data

(122) RBI systems involve the processing of ‘biometric data’. Article 3(34) AI Act defines ‘biometric data’ as ‘personal data resulting from specific technical processing relating to the physical, physiological or behavioural characteristics of a natural person, such as facial images or dactyloscopic data’.
(123) Personal characteristics from which biometric data may be extracted are physical, physiological or behavioural attributes of a natural person. Physiological and physical biometrics employ bodily, structural, and relatively static attributes of a person, such as their fingerprints, the pattern of their iris, contours of their face, or the geometry of veins in their hands. Some attributes are microscopic in nature, but still exhibit biological and chemical structures that can be acquired and identified e.g.,
DNA and odour9. Behavioural biometrics monitor the distinctive characteristics of movements, gestures, and motor-skills of natural persons as they perform a task or series of tasks. This means that human movements, such as walking (gait analysis) or finger contact with a keyboard
(keystrokes), are captured and analysed. Behavioural biometrics encompass a variety of attributes that exhibit both voluntary and involuntary repeated motions and associated rhythmic timings or pressures of body features ranging from signatures, gait, voice, click patterns, and keystrokes, through to eye tracking and heartbeats10, electroencephalography (EEG)11, or electrocardiograms
(ECG)12. The biometric input may relate to one attribute (e.g., facial images) or multiple attributes
(e.g., facial information combined with electroencephalogram (EEG)). Biometric data referring to characteristics of natural persons cannot, as such, concern deceased individuals, dead bodies, human remains of deceased people or traces thereof.
For example, the following AI systems do not fall within the use case of point 1 of Annex III:
–

an AI system comparing DNA samples from a corpse;

–

an AI system comparing facial image from human remains;

9

Physiological and Behavioural Biometrics – Biometrics Institute, available online:
https://www.biometricsinstitute.org/physiological-and-behavioural-biometrics/.
10
Physiological and Behavioural Biometrics – Biometrics Institute; available online:
https://www.biometricsinstitute.org/physiological-and-behavioural-biometrics/.
11
See EDPS, TechDispatch 1/2024 – Neurodata, 3.6.2024, in which the use of brain data and related technology is discussed, as well as the legal implication, including the proposition of new ‘neurorights’, including mental privacy and integrity, In S. O’Sullivan, H. Chneiweiss, A. Pierucci and K. Rommelfanger, Neurotechnologies and
Human Rights Framework: Do we need new Human Rights?, available online: https://rm.coe.int/rapporteurreport-neurotechnology-final-e-2758-7638-0166-1/1680a90ae0 Report, OECD and CoE, 9.11.2021, p.33 , a state of the art and legal aspects of neurotech is discussed.
12
See Hasnul et al., 2021, Electrocardiogram-Based Emotion Recognition Systems and Their Applications in
Healthcare, available online: https://www.mdpi.com/1424-8220/21/15/5015.

16

–

an AI system comparing facial images, DNA, or fingerprints from a known deceased individual, coming from official register, including police records.

(124) AI systems intended to be used to search for objects that do not make use of biometric data to track the movement of a suspect, e.g. searches based on number plates, specific clothes, weapons, background, etc., will not be classified as high-risk pursuant to point 1(a) of Annex III AI Act.
Examples with regard to the element of biometric data:
–

An AI system inferring emotions of an individual from key stroke (way of typing), facial expressions, body postures or movements is based on biometric data.

–

An AI system following a person with a red scarf or a blue jacket is not based on biometric data.

–

An AI system used in supermarkets to detect whether a product is being put into a basket, cart or into a bag is not based on biometric data when it only performs object recognition.
The same is true for a system used at train stations or airports that detects suspicious objects.

–

An AI system inferring emotions from typed text (content, sentiment analyses or stylometry)
to define the style or the tone of a certain article is not based on biometric data.

(125) The AI Act’s definition of biometric data is broad and includes any biometric data used for biometric identification, biometric categorisation, emotion recognition or other purposes. Contrary to the definition of biometric data in the EU data protection law, including Regulation (EU)
2016/679 (‘GDPR’), Directive (EU) 2016/680 (‘LED’) and Regulation (EU) 2018/1725
(‘EUDPR’), the definition of biometric data in the AI Act does not include the wording ‘which allow or confirm the unique identification’ (the functional use of biometric data), since it aims to cover AI systems that use biometric data not only in cases where the AI system identifies an individual or confirms its identity as specified in Recital 14 AI Act.

ii.

Interplay with prohibited practices

(126) The use cases listed in point 1 of Annex III should be considered in the light of the AI practices prohibited by Article 5(1)(f), (g), (h) and (2) to (5) AI Act. That is because, in specific instances where all the conditions for one or more prohibited practices under Article 5 AI Act are met, the placing on the market, putting into service and use of the AI system is prohibited. It will then be unnecessary to consider whether those systems should be classified as high-risk. Most AI systems that fall under an exception from the prohibitions provided in Article 5 AI Act will qualify as highrisk.
For example, emotion recognition systems, where they do not fulfil the conditions for the prohibition of Article 5(1)(f) AI Act, will fall within the use case of point 1(c) of Annex III AI Act and be classified as high-risk pursuant to Article 6(2), insofar as the conditions under Article 6(3) AI Act do not apply. In particular, emotion recognition systems outside the areas of workplace and education institutions, as well as such systems used in the areas of workplace and education institutions, when used for medical or safety reasons, are not prohibited, but qualify as high-risk.
17

Similarly, biometric categorisation systems that do not fulfil the conditions for the prohibition of
Article 5(1)(g) AI Act will fall within the use case of point 1(b) of Annex III and be classified as high-risk pursuant to Article 6(2) AI Act, where they are intended to be used for biometric categorisation according to sensitive attributes or characteristics protected under Article 9(1) GDPR
(insofar as the conditions of Article 6(3) AI Act do not apply).
In contrast, RBI systems that fall within the use case of point 1(a) of Annex III AI Act may in some cases be prohibited if they fulfil the conditions for the prohibition under Article 5(1)(h) AI Act, i.e.
they are being used in real-time, at publicly accessible places, for law enforcement purposes, and without one of the exceptions applying. Conversely, RBI systems that fall under one of the exceptions of Article 5(1)(h) AI Act13 will be classified as high-risk under Article 6(2) AI Act, as will RBI systems that are not used for law enforcement purposes or not in real time.
3.1.2.

Point 1(a): Remote biometric identification systems

(127) Point 1(a) of Annex III classifies RBI systems as high-risk. Such systems are deemed worthy of high-risk classification, since technical inaccuracies in the system may lead to biased results and entail discriminatory effects (especially on the grounds of age, ethnicity, race, religion or belief, gender, sexual orientation or disabilities) and RBI may lead to the feeling of surveillance and have a chilling effect on the exercise of fundamental rights, such as the freedom of expression and the freedom of assembly and association.
(128) The two subsections below describe (i) the scope of the high-risk use case point 1(a) of Annex III and (ii) the requirements for authorisation of certain law enforcement uses of post RBI systems under Article 26(10) AI Act.
3.1.2.1. Remote biometric identification system
(129) Article 3(41) AI Act defines an RBI system as ‘an AI system for the purpose of identifying natural persons, without their active involvement, typically at a distance through the comparison of a person’s biometric data with the biometric data contained in a reference database’. An AI system must therefore fulfil three conditions to be classified as an RBI system: (i) its purpose must be biometric identification; (ii) that identification must occur without the active involvement of the person concerned, typically at a distance; and (iii) the system must perform a comparison between that person’s biometric data and biometric data contained in a reference database. Each of these conditions is described in more detail in subsections below.
i.

Biometric identification system

(130) Biometric recognition systems can be used for verification (authentication) and identification purposes14. Such systems always rely on biometric data to perform such verification and identification. They detect, capture, and transform measurable physiological and physical
13

The exceptions set out in Article 5(1)(h)(i)-(iii) AI Act aim to allow the use of certain AI and investigative tools for law enforcement purposes: (i) the targeted search of victims of three specific serious crimes and missing persons [protection]; (ii) the prevention of imminent threats to life or physical safety or a genuine threat of terrorist attacks [prevention]; and (iii) the localisation or identification of suspects and offenders of certain serious crimes as listed in Annex II AI Act [prosecution/investigation].
14
As defined in Article 3(36) AI Act, and agreed by the biometrics community in ISO/IEC Standard 238237:2022 Information Technology - Vocabulary, Biometric recognition, Term 37.01.03.

18

characteristics (such as eye distance and size, nose length, etc.) or behavioural characteristics (such as gait or voice) into machine-readable biometric data (see Section 3.1.1.i) above). Those data are available in different forms (images or templates), which are a mathematical representation of the salient features of an individual, used for verification and identification purposes.
(131) Article 3(35) AI Act defines ‘biometric identification’ as ‘the automated recognition of physical, physiological and behavioural or psychological human features for the purpose of establishing the identity of a natural person by comparing biometric data of that individual to biometric data of individuals stored in a database.’ Such identification can be done for a variety of private or public sector purposes. Regarding law enforcement, such identification is typically done in view of an action or decision to be taken by either administrative, law enforcement or judicial authorities.
(132) This definition excludes systems whose intended purpose is not to establish the identity of a natural person and systems which do not compare the biometric data of a natural person to biometric data stored in a database. Processing of biometric data that is not done for the purpose of identifying persons do not constitute biometric identification (e.g. collecting additional information or establishing links between criminal cases based on biometric samples).
(133) AI systems may be used for biometric identification in all stages of activities. For example, biometric identification includes ‘initial identification’ as used in Article 26(10) AI Act (see Section
3.1.2.2. below). Biometric identification can also cover establishing the identity (including, but not limited to, the civil identity) of a natural person whose identity is already known or previously verified by a human.
(134) An AI system that locates an individual does not necessarily constitute an RBI system. Where the system does not rely on biometric features to locate a person (or there is no comparison of the biometric data of that person with biometric data stored in a reference database), that system will not be classified as high-risk pursuant to point 1(a) of Annex III AI Act.

For example, the following AI systems are not considered biometric identification systems:
–

AI systems automatically searching for non-biometric identifiers (including logos on clothing, specific items).

–

Automated number plate recognition (ANPR) systems when used for locating a motorised vehicle by the means of the car number plate, by the shape, the make or the colour of the vehicle, related to a person of interest (e.g. missing persons, persons suspected of having committed a crime, subject to a European arrest warrant).

–

AI systems automatically searching occurrences of the validation of the individual’s transport tickets (e.g., to establish the movements of the suspect). The ‘tracking’ is done based on the individual’s validations of a ticket/subscription and not based on biometric data.

–

AI systems used to geolocate a picture involving criminal activities (such as CSAM)
based on background or unique identifiers in the picture excluding biometric data.

19
