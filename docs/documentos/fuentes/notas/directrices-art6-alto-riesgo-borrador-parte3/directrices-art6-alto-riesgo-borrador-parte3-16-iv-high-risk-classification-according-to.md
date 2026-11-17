---
name: directrices-art6-alto-riesgo-borrador-parte3-16-iv-high-risk-classification-according-to
description: "Comisión Europea: directrices art6 alto riesgo borrador parte3, sección «IV. High-risk classification according to Article 6(2) and Annex III AI Act (parte 12)» (págs. 93-100). Documento de 2026-05-19, idioma en."
metadata:
  type: reference
  documento: directrices-art6-alto-riesgo-borrador-parte3
  emisor: Comisión Europea
  fecha: 2026-05-19
  idioma: en
  seccion: "IV. High-risk classification according to Article 6(2) and Annex III AI Act (parte 12)"
  paginas: 93-100
  origen: 2026-05-19-directrices-art6-alto-riesgo-borrador-parte3-en.pdf
  oficial: false
---
# IV. High-risk classification according to Article 6(2) and Annex III AI Act (parte 12)

processes data provided by the applicant, such as age, health status, family history, lifestyle habits and occupation and relies on mortality tables, that estimate the probability of death for each applicant within a given period. This processing guides whether the insurer accepts the application and what conditions apply.
-

An AI system intended to be used by an insurer to predict the expected annual medical cost for a risk group. The AI system may calculate and add expenses for administration and a profit margin. The final figure becomes the premium charged to members of that group.
b)

Practical examples of AI systems falling outside the high-risk use case of point
5(c)

Claims management
-

AI systems intended to be used for claims management in case of health insurance products in case the insured event happens. This is because these systems are intended to to verify whether a claim is valid under the policy terms or to determine the amount to be paid, they do not fall within the use case of point 5(c) of Annex III. These use cases are distinct from carrying out a risk assessment or pricing, even though their outcome might affect the enjoyment of the health insurance. In the same vein, those systems may fall outside the use case of point 5(c) of Annex
III if they are intended to be used in claims management to improve the quality of claims processing and decision-making by contributing to the accuracy, by inter alia the validation of claimant information against various databases.

Product design for life insurance
-

AI systems intended to be used in product design for life insurance fall outside the use case of point 5(c) of Annex III, if they are not intended to be used for risk assessment and pricing in individual cases. Those AI systems typically support a data-driven approach to product design by analysing large volumes of demographic, behavioural, and socio-economic data. By identifying emerging customer needs, risk patterns, and coverage gaps, the AI system enables insurers to create tailored life insurance products that are both relevant and competitively priced.
For example, these AI systems can detect underserved segments and recommend product features or pricing models suited to their profiles. Scenario simulations and predictive modelling may help to assess the potential impact of new product offerings before launch, reducing development time and market risk. Those AI systems usually represent a prior and separate stage in the value chain of insurance companies. The product design may set the framework on what insurance products are offered and within which pricing framework. However, there is no evaluation of a natural person’s risk profile involved to determine whether to offer, decline, revoke or deliver services related to health and life insurance.
3.5.5.

Interplay with other Union legislation: Article 144 of Regulation (EU)
No 575/2013 (Capital Requirements Regulation) and Article 120 of Directive
/2009/13/8 EC (Solvency II Directive)

(322) If an AI system intended to be used to evaluate the creditworthiness of natural persons or establish their credit score is also intended to be used for prudential purposes provided for by Union law to
92

calculate credit institutions’ and insurance undertakings’ capital requirements, it will still be classified as high-risk under points 5(b) and (c) of Annex III. This follows from the clear specification in that provision that AI systems intended to be used for the use case listed therein shall only be exempted from high-risk classification if they are intended to be used for the purpose of detecting financial fraud.
(323) The statement in Recital 58 AI Act that AI systems provided for by Union law for prudential purposes to calculate credit institutions’ and insurance undertakings’ capital requirements should not be considered to be high-risk under the AI Act clarifies that AI systems used for those purposes fall outside the use case of point 5(b) of Annex III if they are not intended also to be used for the assessment of creditworthiness of and the establishment of a credit score for natural persons. An example of such a system falling outside the use case of point 5(b) of Annex III is an AI system intended to be used by a financial institution to calculate solely the risk-weighted exposure of portfolios of loans to natural persons under the internal ratings-based approach (IRB) pursuant to
Article 143 of Regulation (EU) No 575/2013, but the same system is not intended to be used for credit scoring or the evaluation of creditworthiness of natural persons. Such (normally) internal AI systems are not high-risk in and of themselves as a result of the use test mentioned in Article
144(1)(b) of Regulation (EU) No 575/201365 and in Article 120 of the Solvency II Directive.
(324) In this light, it should be recalled that it is not relevant what the main purpose of an AI system is for high-risk classification purposes. Provided one of the purposes of the system is the use case listed in point 5(b) of Annex III, the AI system should be classified as high-risk, regardless of the fact that the same AI system is also used for internal ratings and default and loss estimates under the IRB approach for the purpose of calculating own funds requirements.
(325) If, however, financial institutions use different AI systems for both operations (e.g. a bank uses an
AI system for credit-scoring that takes the IRB system as an input or uses an IRB system that takes the credit scoring as an input, but deviates in some elements from the IRB system), the AI system used for IRB purposes should not be classified as high-risk, since it is only the credit-scoring system that is intended to be used for the use case listed in point 5(b) of Annex III, AI Act. The same principles apply to insurance undertakings that widely use internal models and where those models play an important role in their system of governance in accordance with Article 120 of the Solvency
II Directive.
(326) Whether there are one or two underlying AI systems within the meaning of the use cases listed in
Annex III requires a case-by-case assessment. Market surveillance authorities and providers must identify the underlying AI system(s) and their boundaries based on the definition of an AI system under Article 3(1) AI Act, drawing inspiration from the Guidelines on the definition of an artificial intelligence system66. This may require, inter alia, describing the hardware and software components of the AI system, as well as its objectives and its functionalities with a view to inputs and outputs, and its interface with other AI systems or its environment.

65

Regulation (EU) No 575/2013 of the European Parliament and of the Council of 26 June 2013 on prudential requirements for credit institutions and amending Regulation (EU) No 648/2012.
66
Commission Guidelines on the definition of an artificial intelligence system established by Regulation (EU)
2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence and amending Regulations (EC) No 300/2008, (EU) No 167/2013, (EU) No 168/2013, (EU)
2018/858, (EU) 2018/1139 and (EU) 2019/2144 and Directives 2014/90/EU, (EU) 2016/797 and (EU) 2020/1828
(Artificial Intelligence Act) (Text with EEA relevance) (OJ L, 2024/1689).

93

(327) Where financial institutions, as a provider of a high-risk AI system falling within the use case of points 5(b) of Annex III, implement model changes of already approved IRB systems in a non-live production environment, this should not be considered as putting the AI system into service pursuant to Article 3(11) AI Act until approval is granted, since until then there is no intention, in practice, to deploy the AI system as implemented in the non-live environment.
(328) In any case, high-risk AI systems placed on the market or put into service by financial institutions before the date of application of the high-risk rules are grandfathered and do not need to comply with the requirements and obligations, unless as from that date those systems are subject to significant changes in their design (see Article 111(2) AI Act and Section V below, as well as the relevant Union legislation on prudential requirements). For this purpose, the definition of material change to the credit-scoring within the IRB Approach as set out in the relevant Union legislation will be relevant in the context of the assessment of whether a high-risk AI system in point 5(b) of
Annex III is subject to a significant change in design under Article 111(2) AI Act.

3.5.6.

Point 5(d): Evaluation and classification of emergency calls or the dispatching or establishing prioritisation of emergency first response services

(329) Point 5(d) of Annex III classifies as high-risk AI systems intended to evaluate or classify emergency calls by natural persons or to be used to dispatch or to establish priority in the dispatching of emergency first response services, including by police, firefighters and medical aid, as well as of emergency healthcare patient triage systems. If not developed or used correctly, the use of such systems can have risks concerning very critical situations for the life and health of persons and their property. To address those risks, such systems are classified as high-risk and subjected to safeguards to ensure they work as intended and are accurate, safe and do not discriminate.
(330) Five types of AI systems fall within the uses cases listed in point 5(d) Annex III:
(i)

AI systems intended to be used to evaluate and classify emergency calls by natural persons;

(ii)

AI systems intended to be used to dispatch emergency first response services;

(iii)

AI systems intended to establish priority in the dispatching of emergency first response services;

(iv)

AI systems intended to be used to dispatch emergency healthcare patient triage systems;

(v)

AI systems intended to be used to be used to establish priority in the dispatching of emergency healthcare triage systems.

(331) AI systems that fall within the use cases of point 5(d) of Annex III AI Act and that qualify as a medical device pursuant to Article 2(1) of Regulation (EU) 2017/745 (the Medical Devices
Regulation) or as radio equipment pursuant to Article 2(1)(1) of the Radio Equipment Directive fall within the scope of Annex I AI Act and shall also be classified as high-risk pursuant to Article 6(1)
AI Act if they meet the conditions of this provisions (See Section III above). If Article 6(1) AI Act is not applicable, AI systems within the scope of the use cases in point 5(d) are classified as highrisk pursuant to Article 6(2) and Annex III of the AI Act.

94

i.

The meaning of ‘emergency calls’

(332) The AI Act does not define the notion of ‘emergency calls’. Inspiration may be drawn from Article
2(31), (36) and (38) of Directive (EU) 2018/1972 (the European Electronic Communications
Code)67. Those provisions define the notions of ‘call’, ‘public safety answering point’ (‘PSAP’), and ‘emergency communication’. As regards the latter, emergency communication is classified as
‘communication by means of interpersonal communications services between an end-user and the
PSAP with the goal to request and receive emergency relief from emergency services’, which is not limited to only calls but can also include text messaging and video. A PSAP is ‘a physical location where an emergency communication is first received under the responsibility of a public authority or a private organisation recognised by the Member State’68.

ii.

The meaning of ‘emergency first response services’

(333) The AI Act does not define the notion of ‘emergency first response services’. Such services are generally a Member State competence69 and Member State legislation designates the organisations and types of services that should be considered emergency first response services. In addition, inspiration may be drawn from Article 2(39) of the European Electronic Communications Code, which defines ‘emergency service’ as those services ‘recognised as such by the Member State, that provide immediate and rapid assistance in situations where there is, in particular, a direct risk to life or limb, to individual or public health or safety, to private or public property, or to the environment, in accordance with national law’. Point 5(d) of Annex III and Recital 59 AI Act provide as examples of such services police, firefighters and medical aid. Such services may also include ambulance services, operation centres for information management relating to, for example, disaster risk management and forecasting, and organisations providing search, rescue, and evacuations.

iii.

The meaning of ‘emergency healthcare patient triage systems’

(334) Emergency healthcare patient triage systems may qualify as medical devices in so far as they fulfil the definition of a medical device in Article 2(1) of the Medical Devices Regulation. If such systems meet the conditions in Article 6(1) AI Act, they will be classified as high-risk pursuant to that provision and Annex I AI Act and require streamlined and consistent compliance with sectoral laws
(see Section III above).
(335) Emergency healthcare patient triage systems that do not constitute medical devices shall be classified as high-risk pursuant to Article 6(2) and point 5(d) of Annex III AI Act.

iv.

The meaning of ‘forecasting’ and ‘disaster monitoring’

(336) AI systems can also be used for forecasting or predicting situations where emergency first response services will be needed in the absence of emergency calls from natural persons, e.g. systems alerting
67

Directive (EU) 2018/1972 of the European Parliament and of the Council of 11 December 2018 establishing the European Electronic Communications Code (Recast). This Directive is currently being revised, with a proposal from the Commission expected in Q1 2026.
68
Directive (EU) 2014/53/EU of the European Parliament and of the Council of 16 April 2014 on the harmonisation of the laws of the Member States relating to the making available on the market of radio equipment and repealing Directive 1999/5/EC.
69
Article 196 of the Treaty on the Functioning of the European Union.

95

to a situation where emergency first response services are needed. Such systems will only fall within the scope of point 5(d) of Annex III where they are specifically intended to be used to decide when or where to dispatch emergency first response services.
a)

Practical examples of AI systems falling within the high-risk use case of point
5(d)

Analysing calls and prioritising interventions
-

An AI system intended to be used in emergency response centres where 112 calls are classified to assign the level of urgency and to route responders, using natural language processing. Such an AI system is high-risk, since the system is intended to evaluate and classify the calls, and to establish prioritisation in the dispatching of emergency first response services, including the actual dispatching of the services.

-

An AI system is used to analyse emergency calls received by the police and to prioritise interventions according to the urgency and seriousness of the situation through the extraction of relevant information, such as relevant key words. The system assesses the urgency of the situation and the response to be given. Such an AI system is as high-risk, since it is directly involved in the evaluation, prioritisation and dispatching of incoming calls made by natural persons, and the system assesses which response should be given.

Supportive tools for human review
-

An AI system intended to provide real-time decision support for emergency first response services call-talkers, effectively enhances human decision-making skills by acting as an assistant to the call-taker, listening for signs or signals of life-threatening emergencies in what the caller is describing. The AI system uses real-time automatic speech recognition technology, creating high-quality transcripts and during the call, the data is analysed and compared with historical data collected from previous emergency calls. Such an AI system is high-risk, since it evaluates the call made by a natural person by assisting the emergency first response services call-taker by helping to classify the call on the basis of the severity of the situation through the listening for keywords that might indicate a medical emergency.

-

AI systems intended to determine the nature and severity of emergency situations in incoming calls that are put in a queue before they are picked up. The AI system’s role is to identify the emergency as life-threatening and alert the human call-taker if the waiting incoming call needs to be prioritized, while the decision to perform an automated triage or prioritise dispatch remains with the human call-taker. Such an AI system is high-risk, since it evaluates and classifies emergency calls into those that are life-threatening and those that are not.

Emergency triage systems
-

AI systems used in emergency departments that are intended to prioritise patients, without performing clinical assessment medical acts or diagnostic functions . Such an AI system is highrisk, since it is intended to be used to establish priority in the dispatching of emergency healthcare patient triage systems.

96

-

AI systems intended to be used as chatbots to trigger emergency medical emergency services in medical institutions without performing clinical assessment medical acts or diagnostic functions.

Rapid alert systems
-

An AI system intended to be used to support decisions on allocating resources and prepositioning assets to combat wildfires, where the system not only predicts the likelihood and the direction of wildfire evolution across an area’s protected forests, but also automatically triggers the dispatching of emergency first response services or provides clear recommendation of staff allocation in order to contain the wildfire. The system does not replace human decision-making but supports staff. Such an AI system is high-risk, since it is specifically intended to trigger emergency first response services, as well as to decide when and/or where to dispatch emergency first response services. The impact of such system is related to its decisive role for the dispatching of resources and to locations, which are decisions made in critical situations for the life and health of persons and the protection of their property.

Language tools
-

AI systems intended to be used as a mental health crisis triage chatbot, which uses natural language processing to assess severity and urgency of chat-based contacts with emergency mental health services without performing clinical assessment or diagnostic functions. Such an
AI system is high-risk, since it directs mental health intervention responses, carries a risk of misclassification and provides a first emergency triage function.
b)

Practical examples of AI systems falling outside the high-risk use case of point
5(d)

Transcribing emergency calls
-

An AI system intended to transcribe poor-quality emergency calls, or calls where callers may be panicked or unable to communicate, identifying relevant keywords and transcribing them automatically, thereby saving time that the call-taker would otherwise spend asking the caller to repeat themselves. Such an AI system falls outside the use case listed in point 5(d), since it aids the emergency first response services call-taker in the evaluation of a call made by a natural person by focusing on specific keywords related to emergency first response services, but does not evaluate or classify the call.

Forecasting
-

AI systems that analyse various sets of data for fast indications of potential disasters before emergency first response services are made aware through emergency communications. These systems can for example identify flood-prone regions and suggest mitigation strategies, model potential wildfire spread patterns based on wind, temperature and vegetation density, process social media feeds to detect when a new topic is trending and monitor weather conditions and seismic activity. Such an AI system falls outside the use case listed in point 5(d), since it is not intended to decide when and/or where to dispatch emergency first response services, but rather resembles systems that are intended for the general forecasting of potential disasters, without a link to dispatching emergency first response services.
97

Enhanced learning and training
-

An AI driven simulation platform used to provide realistic training environments. The system creates among others scenario-based training for first responders, allowing them to practice responses to floods, wildfires and cyberattacks, followed by automated debriefings and response recommendations. Such an AI system falls outside the use case listed in point 5(d), since it is intended to provide a learning environment with realistic scenarios. In practice, such systems are not used to evaluate and classify incoming real-time calls from natural persons, nor do they actually dispatch or prioritise emergency first response services. The experience and information gained within this environment is valuable for the development of an AI system which is to be used for the intended purposes listed in point 5(d) of Annex III of the AI Act, but is not considered high-risk for learning purposes.

Identification of patients
-

AI systems intended to be used to securely identify patients undergoing medical procedures, using biometric parameters. Such an AI system falls outside the use case listed in point 5(d), since the system is not intended to be use for one of the intended purposes listed therein.

AI systems related to the connectivity of the service
-

AI systems intended to convey traffic on the network of received emergency calls or the lack of connectivity. Such an AI system falls outside the use case listed in point 5(d), since it is not inherently responsible for triggering harmful outcomes, even if it may affect the availability of services.

Estimated healing time
-

AI systems intended to estimate the healing time for room- and bed-management in a hospital.
Such an AI system falls outside the use case listed in point 5(d), since it is not intended to be use for one of the intended purposes lists therein.

Medical appointments
-

AI systems intended to schedule medical appointments. Such an AI system falls outside the use case listed in point 5(d), since it is not intended to be use for one of the intended purposes listed therein and it does not relate to life-threatening emergencies.
c)

Practical examples of AI systems falling within the use case but exempted under the filter mechanism of Article 6(3)

Preparatory tools for prioritization

-

An AI system intended to interpret weather risk data, such as of wildfire or flood, in advance of a probable emergency and to provide preparatory intelligence for the prioritisation of resources, such as pre-positioned firefighters or flood prevention devices, and their allocation preemptively. Such an AI system falls within the use case listed in point 5(d), since it is intended to be used for establishing priority in the dispatching of emergency services. However, since the
98

system performs a preparatory task to an assessment relevant for the prioritisation that will be evaluated and confirmed by human analysts and the competent commander, it falls under the exception in Article 6(3)(d) AI Act.
Supportive tools for human review
-

AI systems intended to provide situational awareness of an emergency site to first responders, such as of where patients and casualties are located and what is e.g., their body temperature. This could be a system held by the on-site commander that gathers and combines the respective data from human first responders, from autonomous rescue robots or drones, and other sensor data
(e.g., radioactivity or toxins). Such an AI system falls within the use case of point 5(d) of Annex
III, since it is linked to emergency healthcare patient triage systems. However, since the system merely provides existing and factual information in a structured manner, without evaluating this information for the prioritisation or triage of the patients and casualties, it falls under the exceptions for AI systems intended to perform narrow procedural and preparatory tasks in Article
6(3)(a) and (d) AI Act.
3.6. Law enforcement

(337) As explained in Recital 59 AI Act, given their role and responsibility, actions by law enforcement authorities involving certain uses of AI systems are characterised by a significant degree of power imbalance and may lead to surveillance, arrest or deprivation of a natural person’s liberty, as well as other adverse impacts on fundamental rights guaranteed in the EU Charter of Fundamental
Rights. Therefore, the AI Act designates law enforcement as one of the areas in which specific applications of AI systems may entail considerable risks to the health, safety, and fundamental rights of natural and legal persons.
(338) Point 6 of Annex III AI Act lists five high-risk use cases in which AI systems intended to be used in the area of law enforcement are classified as high-risk. These use cases were considered by the
Union legislature as situations in which accuracy, reliability and transparency are particularly important to avoid adverse impacts, retain public trust and ensure accountability and effective redress (Recital 59). As explained in Section 2.6 above, the fact that an AI system is classified as a high-risk AI system under these use cases should not be understood to mean that the use of the system is lawful under other acts of Union law or under national law compatible with Union law.
3.6.1. Overview of use cases and horizontal issues
(339) Point 6 of Annex III AI Act covers AI systems intended to be used by or on behalf of law enforcement authorities or by Union institutions, bodies, offices, or agencies in support of law enforcement authorities, in so far as such use is permitted under relevant Union or national law.
The following use cases are classified as high-risk:

(a)

AI systems intended to be used to assess the risk of a natural person becoming the victim of criminal offences;

(b)

AI systems intended to be used as polygraphs and similar tools;

(c)

AI systems intended to be used to evaluate the reliability of evidence in the course of the investigation or prosecution of criminal offences;
99
