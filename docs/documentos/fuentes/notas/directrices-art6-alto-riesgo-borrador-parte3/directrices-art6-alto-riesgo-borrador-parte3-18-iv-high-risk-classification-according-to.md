---
name: directrices-art6-alto-riesgo-borrador-parte3-18-iv-high-risk-classification-according-to
description: "Comisión Europea: directrices art6 alto riesgo borrador parte3, sección «IV. High-risk classification according to Article 6(2) and Annex III AI Act (parte 14)» (págs. 109-116). Documento de 2026-05-19, idioma en."
metadata:
  type: reference
  documento: directrices-art6-alto-riesgo-borrador-parte3
  emisor: Comisión Europea
  fecha: 2026-05-19
  idioma: en
  seccion: "IV. High-risk classification according to Article 6(2) and Annex III AI Act (parte 14)"
  paginas: 109-116
  origen: 2026-05-19-directrices-art6-alto-riesgo-borrador-parte3-en.pdf
  oficial: false
---
# IV. High-risk classification according to Article 6(2) and Annex III AI Act (parte 14)

–

AI systems that flag irregularities in how different polygraph examiners interpret similar cases, highlighting inconsistencies for law enforcement authorities. Such system is not a polygraph itself, but is intended to be used to interpret the work of polygraph examiners.
3.6.4.

Point 6(c): AI systems intended to be used to evaluate the reliability of evidence

(363) Point 6(c) of Annex III classifies as high risk AI systems intended to be used by or on behalf of law enforcement authorities, or by Union institutions, bodies, offices or agencies in support of law enforcement authorities, to evaluate the reliability of evidence in the course of the investigation or prosecution of criminal offences. The provision refers to ‘evaluation of reliability of evidence’ and as such focuses only on this specific task and only in the course of an open criminal investigation or prosecution.
(364) In the context of law enforcement activities, evaluating the reliability of evidence means assessing how trustworthy, accurate, and credible the evidence is in the case it is used in investigations, arrests, or prosecutions. This encompasses, in particular, the court-proof verification of the authenticity of evidence prior to conducting in-depth investigations or making arrests or other prosecussion action. The core function of AI systems covered by this use case is the evaluation of evidentiary reliability. This may include, for instance:
–

authenticity verification;

–

data integrity checks;

–

source reliability assessment;

–

evaluation whether the evidence aligns with other available information or is internally consistent.

(365) This does not include AI systems that are intended to be used for working with the information collected, but that are not intended to be used for the evaluation of reliability of evidence. Examples of such tasks that are not falling under the scope of ‘evaluation of reliability of evidence’ (and thus are outside of point 6 AI Act), include collecting, arranging and structuring of information, data extraction and linking, document clustering, timeline reconstruction, visualisation, indexing of documents, duplicate detection, search in its various forms (including, for example, keyword-based queries, similarity/fuzzy, knowledge‑graph search, and multimodal and semantic retrieval across text, audio, image or video, translation and transcription, as well as data structuring and standardisation.
a) Practical examples of AI systems falling within the use case of point 6(c)
Authenticity verification
–

AI-enabled digital forensics solutions for image, audio and video analysis intended to be used by law enforcement authorities to detect whether digital images, audio recordings or videos have been altered or manipulated (e.g. to confirm the authenticity of CCTV footage or

108

smartphone recordings that were presented as evidence; to verify if collected pictures are not deepfakes).
Data integrity checks and source reliability assessment
–

AI systems intended to be used by law enforcement authorities to determine and evaluate alterations of documents , or forged signatures.

–

AI systems intended to be used for evaluating the authenticity of digital evidence retrieved from mobile or other devices, including by analysing digital traces (e.g. metadata such as geolocation records, file creation and modification histories) and by flagging elements requiring closer human examination.

– AI systems intended to be used to assist competent law enforcement authorities in assessing the reliability of evidence, including from human sources, such as the credibility of informants or witnesses, by analysing factors such as the internal consistency of statements, their coherence with verified facts, and the accuracy of information provided by the same source in past cases.

109

b) Practical examples of AI systems falling outside the use case of point 6(c)
Image enhancement and data recovery
–

AI systems intended to be used for forensic reconstruction, image enhancement, or data recovery from devices. Such systems do not evaluate the reliability of evidence, but assist human experts by processing, restoring, or extracting data that can then be examined and relied upon.

AI systems reconstructing crime scenes
–

AI systems intended to be used to map or reconstruct crime scenes or to provide visualisations or models based on data collected (photos, measurements, etc.). Such systems help investigators better understand the spatial relationships and sequence of events at a crime scene without assessing evidence reliability.

Pattern detection
–

AI systems intended to be used to detect patterns in investigations and notify law enforcement authorities thereof (e.g. identifying similar break-in methods in recent thefts or notify of similar victim profile in recent homicides). Such systems do not evaluate the reliability of evidence, but find correlations or patterns that might otherwise go unnoticed and help law enforcement focus their investigations or spot potential links between cases.

Content flagging and searches
–

AI systems intended to be used to detect child sexual abuse material online, without evaluating the reliability of it as evidence. The primary function of such a system is to identify, flag and filter content that potentially violates the law.

–

AI-enabled solutions intended to be used by law enforcement authorities for screening child sexual abuse material online and the classifying thereof in the following groups for prioritisation: (i) new material; (ii) material already registered in the database; and (iii)
deepfake pictures. Such systems do not evaluate the reliability of evidence, but are designed to support investigative workflows by filtering or preselecting large volumes of incoming material. The application of Article 6(3) of the AI Act in this use-case is without prejudice to the potential qualification of the AI system at issue as high-risk system under other use cases listed in Annex III of the AI Act (e.g. point 6(a) of Annex III).

–

AI systems intended to be used by law enforcement authorities to analyse online advertisements in the sex industry and to flag those most likely to be linked to human trafficking. Such systems do not evaluate the reliability of evidence, but are designed to identify, flag and filter content that potentially violates the law.

–

AI systems intended to be used to match the ballistic markings on a bullet to markings registered in a reference database for the purposes of identifying whether a particular weapon was used for committing a crime. Such systems do not evaluate the reliability of evidence,

110

but constitute a means of file handling or of searching a database by evaluating the similarities between evidence material and a reference database.
c) Practical examples of AI systems falling within the use case but exempted by the filter mechanism in Article 6(3) AI Act
–

AI systems that are used in the course of evaluation of evidence but only classify documents, pictures, videos or other material selected to be analysed for authenticity into categories and thus structure the evaluation of evidence where that categorisation does not impact the assessment of the reliability of those documents as evidence. Such systems fall under the exception for AI systems intended to perform narrow procedural tasks in Article 6(3)(a) AI
Act.

–

An AI system that is used in the course of evaluation of evidence and is indexing and tagging financial documents collected to be evaluated for reliability of evidence (e.g. to be checked with bank account flows; or to be checked for existence of names or objects). Such system fall under the exceptions for AI systems intended to perform narrow procedural or preparatory tasks in Article 6(3)(a) and (d) AI Act.
3.6.5.

Point 6(d): AI systems assessing offending or reoffending of concrete person(s)

(366) Point 6(d) classifies as high-risk AI systems intended to be used by or on behalf of law enforcement authorities, or by Union institutions, bodies, offices or agencies in support of law enforcement authorities, to assess the risk of (a) concrete person(s) offending or reoffending, provided that assessment is not based solely on profiling or evaluating their personality traits, or by looking at their past criminal behaviour or the past criminal behaviour of the groups to which that person belongs. In other words, the use case in point 6(d) includes AI systems intended to be used to assess the risk of a person committing a crime or reoffending, without prejudice to the prohibition set out in Article 5(1)(d) AI Act. Each of the conditions of the use case listed in point 6(d) of the Annex
III AI Act shall be examined in the subsections below.
ii. The concept of ‘not solely on the basis of” (i) profiling, (ii) assessment of personality traits and characteristics, and (iii) assessment of the past criminal behaviour of natural persons or groups as alternatives
(367) The use case listed in point 6(d) of Annex III captures predictive and behavioural AI systems that are intended to be used to assess the risk of a natural person offending or re-offending. It explicitly excludes AI systems that are based solely (i) on profiling as per Article 3(4)LED, (ii) on the assessment of personality traits and characteristics, which are already prohibited under Article
5(1)(d) AI Act (see Section 5 of the Guidelines on prohibited artificial intelligence practices)77or
(iii) on the assessment of past criminal behaviour of natural persons or groups. Recital 59 AI Act clarifies that the use cases listed in point 6(d) of Annex III are to be interpreted as alternative. If at

77

Article 5(1)(d) AI Act prohibits AI systems assessing or predicting the risk of a natural person committing a criminal offence based solely on profiling or assessing personality traits and characteristics.

111

least one of these use cases is present, the AI system qualifies as high-risk, unless it falls under the prohibition set out in Article 5(1)(d) AI Act.
(368) The use of an AI system to assess the risk of a natural person offending or re-offending is not based solely on profiling where that system is used to support the human assessment of the involvement of a person in a criminal activity, which is already based on objective and verifiable facts directly linked to a criminal activity. As recital 42 AI Act clarifies, this will be the case where a reasonable suspicion already exists in respect of the natural person concerned. Paragraphs 199 to 206 of the
Guidelines on prohibited artificial intelligence practices contain further guidance on the notion of
‘solely” in relation to profiling under Article 5(1)(d).
a) Practical examples of AI systems falling within the use case of point 6(d)
AI systems used when processing detained persons to assess the risk of offending/reoffending
–

An AI system intended to be used during the initial processing of detained youth suspects by police to calculate a risk score that indicates the likelihood of reoffending, which is then used to make a decision on measures to be taken. The AI system does not autonomously make decisions; the outcome is considered alongside other information, and final decisions are made by the competent authorities. The AI system is intended to be used in support of law enforcement authorities for assessing the risk of a natural person re-offending and this assessment is done not solely on the basis of the profiling of natural persons as referred to in
Article 3(4) LED, or to assess personality traits and characteristics or past criminal behaviour of natural persons or groups, as there are verifiable facts directly linked to a criminal activity
(the assessment is performed post-detention).

AI systems used by probation officers
–

An AI system intended to be used by probation officers to support assessments informing decisions on parole or conditional release, by evaluating factors such as criminal record, behaviour and progress during the custodial sentence, and other case-relevant supervisionrelated information. Like the example above, there are verifiable facts directly linking a person to a criminal activity (the person having already been convicted of a criminal offence).

AI systems used by penitentiary institutions
–

An AI system used by a penitentiary institution to predict the likelihood of an offender reoffending based on prior criminal record, violence within the prison facilities, or socioeconomic data. Like the examples above, there are verifiable facts directly linking a person to criminal activity (the person having either already been convicted of a criminal offence or being detained on suspicion of having committed such an offence).

AI systems used by criminal courts to assess the risk of offending/reoffending
–

An AI-based risk assessment system intended to be used in criminal courts to estimate the likelihood of recidivism, violent reoffending, or the commission of further serious offences.
Since such a risk assessment system involves profiling, the exceptions of Article 6(3) AI Act do not apply.

112

b) Practical examples of AI systems falling outside the use case of point 6(d)
Location focused AI-systems

-

AI systems predicting locations and timeframes of likely crimes (e.g., burglary risk in a neighbourhood), without linking the prediction to identifiable individuals. The use case in point 6(d) concerns risk assessments of natural persons, not geospatial predictions.
c) Practical examples of AI systems falling within the use case but exempted by the filter mechanism in Article 6(3) AI Act
–

An AI system that checks whether all required fields are completed in a probation officer’s risk assessment form or flags inconsistencies in entered data (e.g., mismatched dates of offence or custody period). Such an AI system performs a preparatory task for the risk assessment and does not evaluate personal characteristics . It is also intended for a narrow procedural task (Article 6(3)(a) AI Act), since it only flags inconsistencies and would in any event fall under the exception for AI systems intended to perform a preparatory task listed in Article 6(3)(d) AI Act.

– An AI system that collects and pre-sorts prior convictions, probation reports, and other records to prepare a case file for human officers. Such a system performs a preparatory task for risk assessment and therefore qualifies for an exemption under Article 6(3)(d) AI
Act.

3.6.6.

Point 6(e): AI systems intended to be used for the profiling of natural persons in the course of the detection, investigation or prosecution of criminal offences

(369) Point 6(e) of Annex III classifies as high-risk AI systems intended to be used by or on behalf of law enforcement authorities, or by Union institutions, bodies, offices or agencies in support of law enforcement authorities, for the profiling of natural persons as referred to in Article 3(4) LED in the course of the detection, investigation or prosecution of criminal offences. The inclusion of this use case in point 6 of Annex III affirms that profiling itself, when carried out through an AI system inter alia by law enforcement authorities in the criminal justice context, warrants a high-risk regulatory response, due to its potential to undermine the rights of due process, data protection, and equal treatment.
(370) This provision applies to AI systems intended to be used by law enforcement authorities in identifying potential suspects or other persons of interest (e.g. victims) in various criminal contexts in the course of profiling of a natural person. Such systems typically analyse diverse types of data, such as geographic information, registry data, witness descriptions, or online activity, to generate profiles or flags that assist in crime detection, investigation or prosecution.

113

a) Practical examples of AI systems falling within the use case of point 6(e)
AI systems intended to be used in assisting the identification of potential suspects
–

AI systems assisting in identifying potential suspects where a child is reported missing that analyse the neighbourhood, persons living in the neighbourhood that are on the sex offenders’ registry and their movements, as well as types of children they have abused earlier.
The purpose of the AI system is to generate individualised risk inferences from behavioural patterns, thereby filtering persons as potential suspects. Such a system would involve profiling, since it performs the automated processing of personal data to evaluate and predict aspects of natural persons’ behaviour. Where the assessment of potential involvement in criminal activities is supported bypast criminal behaviour and other verifiable facts, the system would not be solely based on profiling and assessing personal characteristics. It therefore falls within the use case of point 6(e) of Annex III AI Act, rather than the prohibition on predictive policing laid down in Article 5(1)(d) AI Act.

–

AI systems assisting in identifying potential suspects based on descriptions of witnesses and other personal data. Such an AI system processes personal data to infer identity-linked traits and other personal aspects based on patterns, and to single out individuals as potential suspects.

AI systems intended to be used for targeted online monitoring
–

An AI system that monitors online posts to classify users based on sentiment analysis, posting patterns, and networks, and assigning flags for potential extremist affiliation. The system automatically analyses communication patterns, language use, and behavioural indicators to classify persons as potential radicalised subjects. The system performs profiling, since it evaluates and predicts natural persons’ characteristics and likely future behaviour for law enforcement purposes. This does not amount to social scoring as prohibited by Article 5(1)(c)
AI Act, since the system is limited to targeted radicalisation monitoring within specific spheres or contexts.
b) Practical examples of AI systems falling outside the use case of point 6(e)

–

AI systems analysing neighbourhoods and assigning criminality scores (predictive crime mapping systems) where they do not include profiling of individuals as per points 6(d) and
(e) of Annex III.

–

AI systems detecting suspicious transaction patterns that indicate money laundering or terrorist financing, even though that allows linking such transaction to personal profiles.
However, borderline cases may arise where, in addition to focusing on transactions only (the structural, quantitative, or behavioural transactions data, e.g., transaction amounts, frequencies, intervals, geographic routing), such systems are combined with, or enriched by, personal data, thereby enabling the construction of individual profiles (e.g., names, account numbers).If the system assesses such personal characteristics, it should be classified as highrisk.

114

–

An AI-enabled crime-linkage system analysing police crime reports and case files containing variables, such as time, place, modus operandi, suspect/victim descriptions, physical traits, clothing, vehicles, and socio-demographic indicators, with the purpose to identify patterns and similarities across different incidents, linking them into possible ‘series’ committed by the same offender(s). Its main outputs are alerts, crime link hypotheses, and forecasts of likely future offences (not linked to a particular individual).
3.6.7.

Other AI systems falling outside the use cases of point 6 of Annex III

(371) The use cases listed in point 6 (and point 1) of Annex III, which are particularly relevant for law enforcement, do not encompass all AI systems used for law enforcement purposes. These use cases primarily address situations where AI systems are applied directly to natural persons or have the capacity to materially influence decision-making. Consequently, many AI applications employed by law enforcement that do not meet these criteria may fall outside the use cases covered by point
6 (and point 1).
(372) Below are some examples of AI systems used by law enforcement authorities that would not generally be classified as high-risk pursuant to Article 6(2) AI Act and point 6 of Annex III78. This list is provided for orientation purposes only and is not exhaustive, since there are many other AI systems used in law enforcement beyond those mentioned below.
–

AI systems used for automating administrative tasks (e.g., administration and accounting, case management, equipment management, AI systems scheduling patrol shifts). Such AI systems are intended for purely ancillary administrative activities and therefore do not fall within the use cases listed in point 6 of Annex III.

–

Chatbots on police websites providing general information, guiding users through the website. Such AI systems are intended for purely ancillary administrative activities and therefore do not fall within the use cases listed in.

–

Automated number plate readers seeking to identify concrete vehicles. Such AI systems are not considered as biometrics within the meaning of point 1 and do not involve profiling withing the meaning of point 6 of Annex III, since the technology itself is vehicle-focused, not person-focused. However, how the data is used, stored, and interpreted can, at a later stage, create risks of surveillance overreach or privacy violations (e.g. if enabling the reconstruction of individuals’ travel patterns).

–

AI systems checking whether road safety rules are broken (e.g. speeding cars, running red lights, motorbike riders failing to wear a helmet, smartphone use while driving). Such AI systems do not fall within the use cases listed in in point 6 of Annex III, nor do they constitute biometrics within the meaning of point 1 of Annex III.

78

As stated in Recital 52, for high-risk AI systems other than those that are safety components of products, or that are themselves products, it is appropriate to classify them as high-risk if, in light of their intended purpose, they pose a high risk of harm to the health and safety or the fundamental rights of persons, taking into account both the severity of the possible harm and its probability of occurrence and they are used in a number of specifically predefined areas specified in this Regulation.

115
