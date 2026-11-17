---
name: cepd-directrices-02-2026-anonimizacion-v1-03-2-legal-analysis
description: "CEPD: cepd directrices 02 2026 anonimizacion v1, sección «2  Legal analysis» (págs. 6-16). Documento de 2026-07-07, idioma en."
metadata:
  type: reference
  documento: cepd-directrices-02-2026-anonimizacion-v1
  emisor: CEPD
  fecha: 2026-07-07
  idioma: en
  seccion: "2  Legal analysis"
  paginas: 6-16
  origen: 2026-07-07-cepd-directrices-02-2026-anonimizacion-v1-en.pdf
  oficial: false
---
# 2  Legal analysis

passed, under either the contextual or simplified approach, then the given data can be safely considered anonymous. If one of those criteria are violated, further analysis should be done:
the given data may be personal or it may nevertheless be considered anonymous. These guidelines end by providing guidance on that further analysis.
4

Much of the content in these guidelines sits in the space between anonymous and personal data – since the guidelines set out criteria for testing whether a dataset falls into one side or the other, they adopt some terminology specific for these guidelines. It is not possible, for example, to know if the person holding the data should be described as a controller or not, since that answer will depend on whether the data being tested is personal or not. Therefore, rather than, for example, constantly referring to “the person who may or may not be a controller”, these guidelines use a number of key terms for the sake of readability, all of which are set out in more detail in a glossary at the end of this document.

5

Particularly importantly, the guidelines use “individual” to refer to a natural person who may or may not be a data subject and “given data” to refer to data which is being tested and may or may not be personal data. The guidelines then use the word “record” to refer to all values
(including images etc.) within the given data that are known to relate to the same individual.
They also use the term “entity” to refer to a party whose role depends on the situation at hand.
For example, an entity could be a potential controller, a potential processor, or a potential third party with additional information necessary to identify the data subject. Each entity then has a
“perspective”, which depends on the circumstances of the case.

2 Legal analysis
2.1 Introduction
6

The core test for anonymity asks two questions:
a. Does the information “relate” to a natural person? If so, b. Is that natural person “identified or identifiable”?
If the answer to either of these questions is “no”, then the data should be considered anonymous. Importantly, these answers may vary from one entity to another. This means that information may be anonymous for some entities, but not for others 4.

7

For example, information may unambiguously relate to an individual, but only one organisation may be able to actually identify that individual. In this case, the answer to both questions would be “yes” from that organisation’s perspective, and so the information would be considered personal data for that organisation. At the same time, the answer to the second question would
– outside of particular circumstances that will be explained later 5 – be “no” from everyone else’s perspective, and so the information would be considered anonymous for everyone else.
It is, therefore, necessary to consider the different perspectives of the relevant entities when performing this test. This means that anonymisation can be done in a way that the data is anonymous for everyone, or in a way that is only anonymous for particular entities (which may or may not include the anonymising controller).

4
5

C-413/23 P EDPS v SRB.
See, e.g., paras 20, 21 and 29.

5 | Adopted

8

In many cases, the second question will receive a qualified response (“The individual might be identifiable, but only if…”). In particular, there may be several ways that an entity could identify an individual in theory but where the likelihood of this happening is insignificant in practice. This question therefore needs to be viewed as one of likelihood: rather than asking if the individual is identified or identifiable in an absolute sense, it should ask how likely it is that the individual will be identified or identifiable by some entity 6.

9

It should also be recognised that these questions assume that the entity in question has, or could have, some kind of access to, or control over, the data. If, taking into account the means that the entity is reasonably likely to use, an entity cannot actually access or process the data, is not meaningfully connected to any other entities (or chain of entities) with such access, and is not likely to receive the data from such other entities 7, then it should not be necessary to assess whether the information is anonymous for that entity.

10

Finally, these guidelines refer to the concept of “anonymisation” broadly, as any processing which successfully produces anonymous data under the GDPR, whether or not the original data is deleted. This includes anonymisation that does not lead to a deletion of the original data and so does not contribute to storage limitation. These guidelines do not, therefore, provide guidance for the interpretation of existing specific legal provisions that may mandate erasure of the original data.

2.2 Identifying the applicable perspective(s)
11

As noted above, whether information is personal may vary from one entity to another. It is therefore important to determine the relevant entities for the assessment of the given data.
Typically, whether information is personal for a particular entity will be assessed by reference to their own perspective – although, as set out below, there are some cases where another entity’s perspective should be used instead. The goal of anonymisation should be to ensure that the resulting data is anonymous for all of the relevant entities concerned by the assessment.

12

It can sometimes be immediately apparent if a certain entity is relevant or not. The basic question is: for whom is the data intended to be anonymous? For example, if the intention is to anonymise data for an entity’s own use, that entity’s perspective will be relevant for the assessment. Likewise, if the intention is to anonymise the data for independent use by anyone who receives the data, anonymity should generally be assessed from the perspective of those who will have access to the data after it has been transferred. In some cases, there may only be one relevant perspective (e.g., if the data is kept securely by a single entity and nobody else will ever be able to gain access to it) while, in others, there may be many different relevant perspectives (e.g., if the data could be accessed by many entities).
Example 1: In OC v Commission 8, the CJEU considered whether a press release contained personal data. The Court noted that the press release was, by its very nature, intended for

See, e.g., C-413/23 P EDPS v SRB and C-582/14 Breyer v Bundesrepublik Deutschland.
This can, for example, be the case where there is collusion or cooperation between such entities, or where it is likely that the information may be (directly or indirectly) transferred from one entity to another. See, for example, C-582/14 Breyer v
Bundesrepublik Deutschland and C-319/22 Gesamtverband Autoteile-Handel eV v Scania CV AB. See also C-210/16
Unabhängiges Landeszentrum für Datenschutz Schleswig-Holstein v Wirtschaftsakademie Schleswig-Holstein GmbH, where the
CJEU found that a party who determines the purposes and means of the processing of personal data can still be considered a joint controller, and are still subject to EU data protection law, even if they do not have access to that data.
8
C-479/22 P OC v Commission.
6
7

6 | Adopted

distribution to journalists, including investigative journalists with research skills beyond those of an average person. When assessing if the publication contained personal data, it was therefore necessary to perform the assessment from (at least) those investigative journalists’ perspectives.
13

In other cases, several factors may be important for identifying the relevant perspectives. In particular, it is important to examine the specific nature and context of the processing, such as who has access to or control over the data, whether the data is being transmitted from one party to another, the relationship between those parties, and whether a receiver of the data might process it on behalf of another party.

14

The relevant perspective 9 may be affected by specific GDPR obligations – and may affect how a certain obligation is applied in practice, as was seen in EDPS v SRB.
Example 2: In EDPS v SRB, the CJEU examined the obligation to provide information when personal data is collected directly from the data subjects. This obligation required, among other things, that data subjects be informed about the recipients of any transfers of personal data. The SRB argued that, when deciding if this obligation was applicable, it was important to consider the receiving entity’s perspective. Following the SRB’s line of reasoning, if the information was anonymous from the receiving entity’s perspective, then sharing the data with that entity would not qualify as a transfer of personal data per se and this obligation would not apply.
The CJEU, however, rejected this argument. Rather, the Court noted that this obligation had to be fulfilled at the time when the data is collected, and that the obligation formed an important part of the legal relationship between the data subject and the controller. The Court held that, when deciding if this obligation was applicable, the personal nature of the data should only be assessed from the controller’s perspective at the time the data was collected. Since, at that time, the data was personal for the controller, any transfer of that information qualified as the transfer of personal data regardless of the receiving entity’s perspective. As a result, the controller was obliged to inform the data subjects about the recipients of the data 10.

15 Importantly, the applicable perspective used for a particular entity depends on whether they themselves determine the means and purposes of the processing 11. If an entity processes information on behalf of another, whether the given data is personal for that entity should be assessed by reference to the controlling entity’s perspective. In practice, this means that if an entity processes information on behalf of a controller (i.e. someone for whom the information is personal data, and who decides the purposes and means of the processing), that information should also be considered personal data for the processing entity. That entity should, therefore, be considered a processor under the GDPR and be subject to the obligations applicable to processors 12 . This follows from a teleological application of the
GDPR, noting that:
-

EU data protection law relies on the concept of processor to prevent controllers from avoiding GDPR protections by outsourcing their processing activities to third parties,

See the definition of the term in the Glossary.
C-413/23 P EDPS v SRB, paras 102 – 103 & 108 – 111.
11
For more guidance on the concept of processing data on behalf of another, see EDPB Guidelines 07/2020 on the concepts of controller and processor in the GDPR, paras 79 – 84.
12
This includes, in particular, compliance with Articles 27, 28, 29, 30(2), 31, 32, 33(2), 37, 38, 44, 46, 48, and 49(6) GDPR, and any orders made by supervisory authorities under Article 58 GDPR.
9

10

7 | Adopted

-
-

the GDPR further reinforces this by placing certain obligations directly on processors, and both contractual agreements (or other applicable legal acts) and GDPR obligations need to work together to ensure that the processor handles the information in an appropriate manner.

Example 3: An e-commerce retailer transmits excerpts from its customer records to a thirdparty agency for analysis. In this case, the retailer determines the purpose and means of the processing activity, while the agency is a separate entity which processes the records on their behalf. It is therefore necessary to use the retailer’s perspective for both parties when determining if the information is personal for them. In this case, the retailer is able to identify the customers from those records and the information should therefore be treated as personal data for both the retailer (as the controller) and the agency (as the processor).
Example 4: A hospital transmits excerpts from patient records, which in and by themselves do not allow identification of the individuals, to an independent institute for research purposes.
The data will never be returned to the hospital, and the institute is free to determine means and purposes of processing and is not acting on the instructions from the hospital. Since it is acting independently, whether the information is personal for the research institute should be assessed from its own perspective.

2.3 Whether the information “relates” to a natural person
16

Information relates to a natural person where, by reason of its content, purpose or effect, it is linked to that person. The link should be assessed in light of all the circumstances of the specific case: 13 a. Content. The information is about that person per se, e.g. it describes one or several of their characteristics or actions. For example, this could be an employee record, a patient’s medical record, or a picture or video of a person.
b. Purpose. The information is either about that person, or is primarily about something which, or someone else who, is directly or indirectly related to that person due to some relationship or interaction, and such information is used or likely to be used for the purpose of evaluating, treating or influencing the status or behaviour of the individual in a particular way. This can include information about an object (like a phone, car or house owned by the person), an organisational entity (like a company, department, association or club where that person is a member), or an associate or relative of the natural person (like their friend or family member). For example, this could be data on the value of a house used for the purpose of determining the owner’s taxes, or the service record of a car that could be used for the purpose of ascertaining the productivity of the responsible mechanic.
c. Effect. The information is primarily about an object (like a phone, car or house), an organisation (like a company, department, association or club), or another person, but

13
C-434/16 Nowak v Data Protection Commissioner, para 35 and C-413/23 P EDPS v SRB, paras. 55 and 56. See also Article
29 Data Protection Working Party, Opinion 4/2007 on the concept of personal data, adopted on 20 June 2007, p. 10, although that Opinion using the term “result” rather than “effect”.

8 | Adopted

its processing is liable to have an effect on the data subject’s rights and interests. For such a link to be present, there should be a concrete possibility that the individual can be treated differently from other persons as a result of processing of the information.
For example, this could be location data of taxis that is collected for the purpose of optimising itineraries, but which also allows for the monitoring of the taxi drivers’ performance and shows when they are taking a break.
17

Information may relate to a person even if it is not readily apparent that it does so, or if some additional processing is necessary to reveal that link. This is particularly true for aggregate data which, at first glance, only contains information about groups of people, not individuals.
For example, many techniques exist that can reveal information relating to one or several single individuals from aggregate data. When such a technique could be used, the aggregate data may relate to that individual (and to any other individual for which such a technique could be used).

2.4 Whether the natural person is “identified or identifiable”
18

It is not enough for information to simply relate to a natural person. For this information to be personal data, that natural person must also be identified or identifiable using means reasonably likely to be used. This is especially important where information is anonymised for research or analytical purposes, where the goal is often to have an anonymous dataset which lets you learn something about the people in question (i.e. information which is still related to those individuals) but does so in a way that keeps their identities private (i.e. they are not identified or identifiable).

19

To identify a natural person means to distinguish them from others within a given context, consequently making it possible to treat them differently from those other people. This can be done using direct identifiers (such as a name, ID number or reference code), or one or more attributes which relate to that person.

20

An entity can identify an individual either directly or indirectly. An individual is “directly” identifiable by a particular entity if that entity can, through its own means, identify the individual based on the information itself. An individual is “indirectly” identifiable from a particular entity’s perspective if, through means reasonably likely to be used, that entity could identify the individual by:
-
-
-

obtaining additional information 14, applying methods (such as decryption of encrypted parts of the data) that are controlled by other parties, and/or putting the data at the disposal of other entities who themselves have means reasonably likely to be used to identify the individual 15.

Consequently, an individual can still be identified even if some of the necessary information
– or some of the means of identification – are spread across different entities and require effort to obtain, provided that these elements can be combined through means reasonable likely to be used by the respective entities 16.

C-604/22 IAB Europe v Gegevensbeschermingsautoriteit, para 39.
C-319/22 Gesamtverband Autoteile-Handel eV v Scania CV AB, paras 45 – 49.
16
Recital 26 GDPR. See also C-582/14 Breyer v Bundesrepublik Deutschland, para 43 and C-319/22 Gesamtverband AutoteileHandel eV v Scania CV AB, paras 45 – 49.
14
15

9 | Adopted

21

In this regard, the EDPB emphasises that if (a) it is reasonably likely that an entity can transfer the data to a third party, and (b) it cannot be ruled out that this receiving entity has the means to identify the individual through means reasonably likely to be used, the data should be considered personal for both that transfer and for any subsequent processing of the data by that recipient 17 . Further, this transfer means that the transferred information would also indirectly become personal for the transferring entity, even if that entity would not otherwise have means reasonably likely to be used to identify the individuals in question 18.

22

Importantly, for information to be anonymous, the likelihood of the individual being successfully distinguished from others within the given context does not need to be zero; instead, that likelihood should be insignificant in reality 19. This likelihood may vary dramatically from one perspective to another and the fact that an individual has been, or could be, identified from one perspective does not necessarily mean that the same is true from another.

2.4.1 Identifiers and other attributes
23

In many cases, identification is done by reference to an identifier that is unique within a given context. In the simplest cases, this could, for example, be a single piece of unique data, such as a name, IP address, social security number or e-mail address.

24

In other cases, identification may rely on one or more attributes which, when put together, are unique for a particular individual, even if each of the individual values would not in itself be unique. The type of attribute(s) involved could be extremely broad and may include, among other things, physical, genetic, psychological, behavioural, economic, or cultural attributes.
For example, someone could be identified as “the one with the northern accent” or “the one who lives underground”.
Example 5: When looking at live CCTV of people on a street, many people are wearing black suits, and many people are walking dogs. Within the context of that street, “the person in a black suit” is not, therefore, unique and that description does not allow for the identification of a particular individual. The same is true of “the person with a dog”. However, only one individual on the street is both wearing a suit and walking a dog. Within the context of that street, the combination of those attributes is therefore unique to that individual and the description “the person in a black suit who is also walking a dog” allows for them to be identified.

25

Importantly, the identifiers or attributes do not necessarily have to be about the individual per se but can also be about other individuals, groups or objects which are otherwise linked to them. For example, a user’s device may have a hardware identifier – such as a MAC address
– that can identify the device and, in turn, the individual using the device. Equally, a website may “fingerprint” its visitors based on their unique combination of web browser, operating system, screen resolution, time zone etc., and use this fingerprint to then identify them as they move from page to page and across different visits.

C-413/23 P EDPS v SRB, para 85.
C-413/23 P EDPS v SRB, para 84, referencing C-319/22 Gesamtverband Autoteile-Handel eV v Scania CV AB, paras 45 &
49.
19
C-413/23 P EDPS v SRB, para 82.
17
18

10 | Adopted

Example 6: Several websites use the same third-party provider for targeted advertising. The websites do not share any names, IP addresses, or emails etc. with the third party; instead, they provide information about the pages visited together with a pseudonym which is based on fingerprints from the users’ devices. The third party then uses these pseudonyms to link the data about users across the various sites, profile those users, and decide which adverts should be shown to them.
In this situation, both the raw fingerprint data (as a combination of attributes) and the pseudonym which is derived from that data (as an identifier) allow for the identification of the individual. This is true for both the websites and the third party: even though it does not interact with them directly, the third-party can (and, indeed, does) still use the pseudonyms to distinguish the individual and treat them differently from others, and those individuals are therefore identified or identifiable from its perspective.

2.4.2 Means reasonably likely to be used
26

Rather than describing which means are reasonably likely to be used per se, the CJEU has defined this concept by reference to things which would stop means from being reasonably likely to be used by a particular entity. In particular, means may not be reasonably likely to be used if the likelihood of identification appears, in reality, to be insignificant because it would be impossible to do; because it would involve disproportionate effort in terms of time, cost and labour; or because of a legal prohibition 20. This sub-section provides further guidance on this concept and on how to assess whether a means can be considered reasonably likely to be used or not.

27

As a starting point, the “means reasonably likely to be used” test only relates to possible, future identification (i.e. is the individual “identifiable”?). If the individual to whom the information relates has already been identified, then the information is not anonymous.

28

The concept of “means” should be understood broadly, covering anything from simply reading a document to making a web search to running incredibly complex analyses and inferences.
Further, an entity’s means can also include taking advantage of means that are available to another entity; where this is possible, it is important to assess the likelihood that this overall
“chain” of means 21 comes together.
Example 7: A controller wants to share certain information with its business partner. They try to anonymise data but, when testing the strength of the anonymisation, quickly realise that the data subjects could be re-identified through a certain re-identification technique. The controller knows that their business partner would not itself be able to perform this re-identification technique. However, they could easily hire a third party to do it. That technique therefore still qualifies as a means reasonably likely to be used by the business partner.

29

Whether an entity is likely to use certain means to identify an individual should be assessed in light of all objective factors that might influence the availability of such means and the likelihood of their actual use, including:

C-413/23 P EDPS v SRB, paras 82 – 83.
The chain of means includes any transfer of the given data to (or access by) an entity that is involved in the respective identification process. The likelihood of such transfers (or access) needs to be considered starting from the reception of the given data by an entity for whom it is supposed to be anonymous.

20
21

11 | Adopted

a. the properties of the data itself – including whether the data is aggregated, the uniqueness of the records, as well as the accuracy and precision of the information – and how these affect the data’s vulnerability to the different possible means of (re-)
identification;
b. the context in which the data are released and/or processed 22, including whether there are any effective and permanent restrictions on access to the data;
c. any additional information that would allow for the identification of individuals, and how likely it is that such information can be obtained;
d. the costs and the amount of time that the entity would need to obtain such additional information (in case it is not already available to them); and e. the available technology at the time of the processing, as well as reasonably foreseeable technological developments.
Notably, if the law provides means to access additional information, it is objectively clear that such access constitutes a means reasonably likely to be used 23.
30

The GDPR does not lay down any conditions regarding the entities who are able to identify the individual 24 . Relevant entities may, therefore, include anybody directly or indirectly receiving the data, including unauthorised and malicious actors. Depending on the circumstances at hand, these may include (among others) 25:
-
-
-
-

-
-

-

-

-

The controller of the data which is intended to be anonymised;
Any receiving entities;
Rogue employees;
The individual’s partners, friends, colleagues, neighbours, etc. These entities will often have limited access to the given data (especially if appropriate security measures are deployed), but may have access to additional information which can then be used to
(re-)identify the individual(s) in the given data;
Investigative journalists. This is particularly relevant for data relating to individuals who are, or who are expected to soon be, in the public eye;
Domestic law enforcement or intelligence agencies. These bodies often have extensive legal powers to investigate and gather data, as well as large access to financial means, high computational power and technical experts;
Foreign intelligence agencies. The same considerations that apply to domestic law enforcement agencies also apply to foreign intelligence agencies. Further, foreign intelligence agencies may not be limited by the same laws which limit the actions of domestic law enforcement agencies;
Unethical companies. These entities may have access to large datasets and may exploit legal loopholes or grey areas to gain access to data that would otherwise be inaccessible; and
Cybercriminals. These entities may simply break the law to gain access to data not available from a law-abiding entities’ perspective.

Different entities may be relevant in different capacities. For example, an individual’s friends and family might be able to supply additional information that could aid re-identification, but

See para 148 of Binding decision 1/2021: "[T]he EDPB stresses that the whole context of the processing needs to be considered, as ‘all objective factors’ affect ‘whether means are reasonably likely to be used to identify the natural person’”.
23
This includes, e.g., the ability for a private entity to obtain additional information through legal channels, as referenced in C582/14 Breyer v Bundesrepublik Deutschland, para 47 & 49.
24
C-479/22 P OC v European Commission, para 56.
25
Not all of these perspectives would need to be considered systematically in each case but this depends on the circumstances of each specific case and the entities directly or indirectly receiving the data.
22

12 | Adopted

unable to access the given data itself or actually run the necessary re-identification technique.
These different capacities can, therefore, affect the means that each entity might have on their own, how each entity might slot into a possible chain of means, and whether those means (or chains of means) are actually reasonably likely to be used.
31

The EDPB cautions against using “lack of motivation” as a factor in this analysis. As a starting point, the motivation of individuals can be difficult to assess or demonstrate objectively, and may change over time. Moreover, an entity’s actions may not be consistent with their motivations. It may be, for example, that identification occurs due to an accident or negligence.
This could also happen if an entity is forced by outside circumstances to identify an individual, or to transfer information which allows for such identification 26. When assessing the means reasonably likely to be used, the potential value of the re-identified data to the re-identifying entity (which is not limited to monetary value) 27 should be taken into account to the extent that it offsets the costs and effort involved in re-identification. Equally, the risks that re-identification entails for the re-identifying entity should be considered in the context of this assessment.

32

The CJEU has stated that means do not need to be considered if, in reality, the likelihood of their use is insignificant because they are prohibited by law 28. It should be noted that these cases involved actors who were properly limited by the rule of law, so that the law effectively prevented the use of the means in question. Indeed, we can generally assume that people will follow the law. However, there may also be cases where illegality does not provide any meaningful barrier to identification, because the entities involved will not actually be restricted by this prohibition.

33

The general assumption that people will follow the law can, therefore, be rebutted if there is sufficient evidence of a concrete risk that unlawful means are nevertheless reasonably likely to be used. The assessment of this risk should consider, in particular, evidence that the prohibition in question is not respected by the entities involved. Relevant factors may include, but are not limited to:
-
-
-

-

evidence that the legal prohibition is not effectively monitored, enforced and sufficiently dissuasive;
evidence that the gains from breaking the legal prohibition might outweigh costs, effort and potential risks of doing so;
evidence of a situation where data relevant for re-identification (i.e. both the given and, potentially, the additional data useful for re-identification) is especially vulnerable to illegal access using the prohibited means, due to a lack of protection; and evidence that the prohibition has previously been breached or circumvented in comparable situations.

Example 8: A media company wants to share certain information with a local public authority, provided that they can anonymise it before doing so. The media company is the only entity with access to this information, and they are confident that it is not available through any other sources. The media company, however, does not want to delete the original sources which was used to generate that information, and wants to use an anonymisation technique that

See, e.g., the ability for a private entity to obtain additional information through legal channels, as referenced in C-582/14
Breyer v Bundesrepublik Deutschland, para 47.
27
The potential value of personal data lies in the benefit that an entity may gain from re-identification and should be distinguished from the sensitivity of the personal data. For example, information about a person's hobby may be non-sensitive but economically valuable for targeted marketing purposes.
28
See, e.g., C-582/14 Breyer v Bundesrepublik Deutschland, para 46; C-479/22 P OC v European Commission, para 51; and C413/23 P EDPS v SRB, para 82.
26

13 | Adopted

prevents identification in practice unless the (otherwise-anonymous) data is combined with privileged information that only the media company possesses. In its assessment, the media company notes that that privileged information is stored on their servers, and that, while their network security is starting to be out of date, third-party access to those servers is prohibited by law. Since the public authority is properly limited by the rule of law, the media company concludes that the risk of identification is insignificant from the public authority’s perspective and that the information is anonymous for that authority.
However, the media company also recognises that there is a risk of the shared data being unlawfully intercepted by unintended third parties. These third parties include entities located outside the scope of applicable Union and Member State law, not effectively bound by such laws prohibiting unauthorised access. Moreover, there have been several incidents of illegal access affecting this and other media company’s IT systems storing personal data.
Since the media company’s out-of-date security measures mean that those third parties could also likely hack into the media company’s servers, these unintended receivers of the data would be able to access the privileged information and therefore re-identify the individuals through means reasonably likely to be used. The shared information would not, therefore, be considered anonymous from their perspective. The media company therefore decides that it will upgrade its network security before re-testing the anonymity of the data.
34

A prohibition set out in a contract (even if it is legally binding upon its parties) should not be treated as a prohibition by law. While contractual terms may have an effect on the means reasonably likely to be used, they should only be used to complement technical measures and it is important to carefully consider the actual strength of their effect. Among other things, the measures should be reliable, verifiable and enforceable 29, bearing in mind that contractual measures can typically be subject to revision, or may even be disregarded entirely by the parties.

35

Finally, the likelihood of re-identification typically increases over time due to advances in the technology and techniques used for re-identification, as well as the increased availability of additional information. If the likelihood of identification increases to a level that is no longer insignificant, the previously anonymous data should again be considered personal and the controller will be accountable for any processing of that personal data 30. It is, therefore, good practice for entities processing anonymised data, wherever possible and as appropriate, to periodically reassess the likelihood of re-identification.

2.5 Additional considerations
2.5.1 Datasets containing a mix of anonymous and personal data
36

Some anonymisation techniques might only make the likelihood of identification insignificant for some individuals in a dataset. In such cases, it is important to distinguish between the anonymity of particular records and the anonymity of the dataset per se. In particular, the dataset as a whole should only be considered anonymous if the anonymisation is effective for all of the included individuals – this does not necessarily require an equal level of protection for all individuals, but does require the likelihood of re-identification to be insignificant for all of
European Commission and EDPB, Joint Guidelines on the Interplay between the Digital Markets Act and the General Data
Protection Regulation (version for public consultation), para 181.
30
For general conditions on the liability of controllers for infringing behaviour, see C-807/21 Deutsche Wohnen SE v
Staatsanwaltschaft Berlin, paras 76 & 78.
29

14 | Adopted

these individuals. Where this is not the case, and so a dataset contains a mix of personal and anonymous data, the entire dataset should be treated as containing personal data (and therefore within the scope of the GDPR) in any situation where the separate parts of the dataset are not treated separately 31.

2.5.2 GDPR compliance and the anonymisation process
37

The EDPB emphasises that when making information anonymous from some perspectives but not others, it is important to consider the possible implications for GDPR compliance. For example, when information is anonymised for the entity which receives the given data, but not for the anonymising controller, that controller will still have to treat the given data as personal data and comply with all of their GDPR obligations in regard to it 32.

38

The principles of data protection apply whenever personal data is processed, which includes processing operations carried out to obtain anonymous information. This means, amongst other things, that anonymisation must have a legal basis under Article 6 GDPR, and that one of the exemptions under Article 9(2) GDPR should apply if the dataset contains special category personal data. Legal basis and, when applicable, the relevant Article 9(2) exemption should be presumed to coincide with the legal basis and exemption of the processing preceding anonymisation if the anonymisation is part of the same processing activity, and that the controller pursues the same purposes with it 33.

39

Anonymisation (at least when combined with the deletion of the original data) may also be helpful for controllers who wish to rely on legitimate interest for any preceding processing activities. In particular, the immediate anonymisation of the given data, and immediate deletion of the original data, can limit the overall impact of the processing activities for data subjects, and so act as a positive factor in the legitimate interest balancing test 34.

40

Controllers should also comply with their transparency obligations under Articles 5(1)(a) and
12 – 15 GDPR regarding the anonymisation processing. Among other things, controllers should clearly state that personal data will be processed to produce anonymous data which then falls outside of the scope of the GDPR, and should avoid any ambiguous or misleading statements. In particular, controllers should not use descriptions like “anonymous”, “deidentified” or “de-personalised” if individuals are actually still identifiable.

41

Equally, controllers should ensure adequate documentation of the anonymisation processing.
This documentation of the anonymisation process (including for the testing of the supposedly anonymous datasets) makes it possible to demonstrate both the GDPR-compliance of the anonymisation process, and the effectiveness of the anonymisation itself. This documentation should then be retained after the completion of the anonymisation process.

42

In some cases, a security incident may lead to a reassessment of anonymity. This is particularly the case if the assessment of anonymity relied on certain information being kept confidential, but the incident means that the individuals can now be identified with means

See, by comparison, the fact that a dataset containing a mix of special category and non-special category personal data must be collectively treated as special category personal data whenever the different parts cannot be processed separately: C-252/21
Meta v Bundeskartellamt, para 89.
32
See, e.g., C-413/23 P EDPS v SRB and the effects of anonymisation (or lack thereof) on certain aspects of the information obligation as discussed in Example 2.
33
See also EDPB Guidelines 1/2026 on processing of personal data for scientific research purposes, adopted on 15 April 2026, version for public consultation, section 3.1.
34
For more information on the legitimate interest balancing test, see EDPB Guidelines 1/2024 on processing of personal data based on Article 6(1)(f) GDPR.
31

15 | Adopted
