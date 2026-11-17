---
name: cepd-directrices-03-2026-web-scraping-ia-generativa-v1-04-3-web-scraping-and-the-gdpr-parte-1
description: "CEPD: cepd directrices 03 2026 web scraping ia generativa v1, sección «3  Web scraping and the GDPR (parte 1)» (págs. 8-15). Documento de 2026-07-07, idioma en."
metadata:
  type: reference
  documento: cepd-directrices-03-2026-web-scraping-ia-generativa-v1
  emisor: CEPD
  fecha: 2026-07-07
  idioma: en
  seccion: "3  Web scraping and the GDPR (parte 1)"
  paginas: 8-15
  origen: 2026-07-07-cepd-directrices-03-2026-web-scraping-ia-generativa-v1-en.pdf
  oficial: false
---
# 3  Web scraping and the GDPR (parte 1)

the following AI-development, as well as other criteria to exclude the collection of unnecessary personal data for the processing. If instructed to do so in line with the selection criteria, the scraper might update its list of URLs to be visited with links found at the source. This step also implies implementing measures to exclude certain sources from the collection (e.g. websites which oppose web scraping with measures such as robots.txt or CAPTCHA). For more details, see part 3.2.2 on data minimisation.
The second step relates to “extraction”, during which data from the selected sources is transferred to the designated storage location.
The third step is the “cleaning”, as the raw data transferred by the automated process will often need to be cleaned to improve data quality (e.g. avoiding duplicated data, removing irrelevant HTML tags or code and normalizing formats (e.g. dates, numbers), delete unnecessary data).
The fourth step is the “structuring and storing”, during which the organisation building the training dataset might apply some further rules to refine the data by excluding low quality Internet content. After this refinement step, the remaining data will be structured into a usable format.

3 Web scraping and the GDPR
3.1 General observations
12 The GDPR will apply to web scraping when it includes processing operations, such as extraction, cleaning, structuring and storing of personal data, e.g., data that directly identifies an individual (e.g. names, pictures or contact details) or data that indirectly identifies an individual (i.e. information that can be linked to an identifiable individual considering all the means reasonably likely to be used).
13 Compliance with certain GDPR requirements can be challenging when web scraping is used to collect personal data, such as identifying a lawful basis for processing under Article 6
GDPR, meeting the obligations for processing of special categories of personal data under
Article 9 GDPR, complying with the obligation to ensure transparency towards data subjects
(under Article 5(1)(a), 12-14 GDPR), and complying with, but not limited to, principles such as purpose limitation (Article 5(1)(b) GDPR), data minimisation (Article 5(1)(c) GDPR), fairness (Article 5(1)(a) GDPR), and accuracy (Article 5(1)(d) GDPR). The EDPB recalls that in case of ‘mixed’ datasets (including both personal and non-personal data), GDPR applies to the processing of personal data. Organisations must carefully consider these requirements. They should conduct their scraping activities in a way that enables them to ensure compliance with these principles and requirements, and include safeguards that protect personal data to facilitate compliance with the GDPR and avoid infringing individuals' rights.
14 Collecting vast amounts of personal and potentially sensitive data 1, which usually happens without the data subjects' knowledge, could provide the controller with very detailed information about data subjects, irrespective of whether it is intentional or not. Considering

On “sensitive” data see Article 29 Working Party Guidelines on Data Protection Impact Assessment (DPIA) and determining whether processing is “likely to result in a high risk” for the purposes of Regulation 2016/679, wp248rev.01, endorsed by the
EDPB, p. 9-10.

1

7 | Adopted

the technical aspects and goals of web scraping, it might be challenging for the organisation carrying out the scraping, and an organisation obtaining the scraped data, to determine exactly what personal data, and related to which data subjects, are included in the data set.
It is thus not obvious how to meet the principle of accountability laid down in Article 5(2)
GDPR when processing such data sets for AI development. Nonetheless, compliance with regard to Article 5(2) GDPR must be met by the controller. Furthermore, if an AI model memorizes and reproduces data included in a training data set, it poses additional risks to the privacy of individuals and the data subjects’ rights. The information memorised by the AI model could be used directly for arbitrary purposes. Other risks include the fact that AI models could infer additional information about individuals by using the training data about the data subjects as well as additional information about other data subjects. The reasoning capability of the model based on the training data can also pose an additional risk to individuals.
15 In summary, web scraping can be a powerful tool for generative AI development, but it poses significant data protection risks. These guidelines are intended to assist controllers in navigating the requirements of the GDPR when using web scraping for generative AI training.

3.2 Guidance on specific provisions in the GDPR
3.2.1 Controller/joint controllers/processor
16 Different organisations may be involved in the data collection process for the creation of an
AI training dataset, with varying degrees of involvement. The qualification of the organisations involved in each processing (i.e. controllers and processors), within the meaning of the GDPR, should be analysed on a case-by-case basis. It should stem from an analysis of the factual elements or circumstances of the case, including the way in which the data processing at hand is organized. 2 However, some general considerations can be provided:
17 The organisation performing the scraping is not necessarily the controller under the GDPR.
18 There might be cases where an organisation (AI developer) that is planning to train an AI model contracts another party to perform the scraping (scraper). If the scraper creates a training data set on behalf of the AI developer, according to its documented instructions (in particular on how the data set should be constituted with regard to data sources and categories), the scraper may be regarded as a processor. The AI developer will generally determine the instructions given in regard to the purposes and essential means of the scraping, and therefore be considered the controller.
19 In situations where an AI developer trains an AI model using a data set which has already been scraped by another entity (scraper) it is necessary to distinguish between the responsibility for the different data processing. The scraper and AI developer are, in principle, responsible for their own, separate, processing activities, since each of them determines the objectives and the essential means of its own processing. The scraper is not, in principle, responsible for the re-use of the data.

EDPB Guidelines 7/2020 on the concept of controller, joint controllers and processor in the GDPR, adopted on 7 July 2021, paragraph 52: “The assessment of joint controllership should be carried out on a factual, rather than a formal, analysis of the actual influence on the purposes and means of the processing. All existing or envisaged arrangements should be checked against the factual circumstances regarding the relationship between the parties.”

2

8 | Adopted

20 It is also possible that the scraper and the AI developer are jointly responsible for the processing instead. This could be the case when the scraper and the AI developer determine the purposes and means of the processing together (jointly).
Example 1: Two organisations make a joint decision to develop an AI model, and agree that one of the organisations will perform the task to scrape data from the web to and create data sets for the development of the AI model, while the other organisation perform the development of the model, using the data sets created by the scraper. The collection criteria for the scraping of personal data are determined jointly by both parties. Even though they perform separate processing activities they determine the purposes and means of the processing
(the web scraping and the development of the model) together and are jointly responsible for the processings of personal data.

3.2.2 Principles relating to processing of personal data
Lawfulness
21 Personal data should be processed lawfully, fairly and in a transparent manner in relation to the data subject. 3 When assessing whether the processing of personal data is lawful, the developer of the generative AI model as controller must consider the datasets (containing the scraped data) it intends to use, and/or the types of websites it would like to scrape data from.
22 Moreover, the purpose of the web scraping of personal data should be lawful. 4
Purpose limitation
23 Personal data should be collected for specified, explicit and legitimate purposes, and not further processed in a manner that is incompatible with those purposes. The EDPB has provided further considerations on the purpose limitation principle in the context of the development of AI models in the Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models. 5
Transparency
24 Personal data should be processed in a transparent manner in relation to the data subject. 6
This includes the obligation to inform the data subject about the processing of their personal data. However, when scraping large amounts of data from the internet, it is often difficult, impracticable or, even, objectively impossible to identify and inform the data subjects in an effective way. This makes compliance with the principle of transparency challenging.
25 Depending on how the data processing is precisely designed, it is possible that the controller of the web scraping might not have to inform data subjects individually about the web scraping, if providing the information proves impossible or requires disproportionate effort
(Article 14 (5)(b) GDPR).

Article 5(1)(a) GDPR.
See Joint Statement on AI-Generated Imagery and the Protection of Privacy, issued on 23 February 2026, on the creation of non-consensual intimate imagery, defamatory depictions, and other harmful content featuring real individuals.
5
EDPB Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models, adopted on 17 December 2024, p. 64.
6
Article 5(1)(a) GDPR.
3
4

9 | Adopted

26 Impossibility or disproportionate effort typically arises in circumstances where the personal data were not obtained from the data subject. 7
27 Informing the data subjects individually may be impossible or require disproportionate effort in particular for processing “for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes”, subject to the safeguards referred to in Article
89(1) GDPR. 8 While the word “in particular” clarifies that there may be other cases where it would be impossible or require disproportionate effort to inform data subjects, 9 this exception should not be routinely relied upon by controllers who are not processing personal data for the purposes of archiving in the public interest, for scientific or historical research purposes or statistical purposes. 10
28 Where a controller seeks to rely on the exception in Article 14(5)(b) GDPR, it should assess the effort involved for the controller to provide the information to the data subject against the impact and effects on the data subject if they were not provided with the information. 11 The balancing exercise should be carried out with regard to the dataset as a whole and not on every single piece of personal data, and should take into account:
-

the number of data subjects,

-

the age of the data,

-

any appropriate safeguards adopted. 12

29 In the case of processing of personal data that do not require the identification of a data subject by the controller, the controller is not obliged to maintain, acquire or process additional information in order to identify the data subject for the sole purpose of complying with the requirements in the GDPR. In such cases, the controller is not required to comply with the rights of the data subject in Articles 15 to 20, unless the data subject provides additional information enabling their identification. 13
30 In cases where informing data subjects individually proves impossible or would require disproportionate effort, the controller must take appropriate measures to protect the data subject’s rights, freedoms and legitimate interests. One appropriate measure that controllers must always take, as specified in Article 14(5)(b), is to make the information publicly available. 14 This can be done for instance by publishing a privacy policy and/ or specific notice on the controller’s website. This policy should include the information that is required by Article 14(1)-(2) GDPR, including the categories of personal data concerned, the purposes of the legal basis of the processing as well as a precise indication of the source(s)
of the data. The information should indicate in particular whether the sources are publicly accessible or non-publicly available sources and, if the data is crawled and scraped from online sources, the information should include crawler’s characteristics. In situations where it would be impossible or require disproportionate effort to provide a complete list of the

Article 29 Working Party, WP260 rev.01, 29 November 2017, Guidelines on transparency under Regulation 2016/679 - endorsed by the EDPB, paragraph 62.
8
Recital 62 GDPR.
9
Recital 62 GDPR.
10
Article 29 Working Party, WP260 rev.01, 29 November 2017, Guidelines on transparency under Regulation 2016/679 endorsed by the EDPB, paragraph 61.
11
Article 29 Working Party, WP260 rev.01, 29 November 2017, Guidelines on transparency under Regulation 2016/679 endorsed by the EDPB, paragraph 64.
12
Recital 62 GDPR.
13
Article 11 GDPR.
14
Article 29 Working Party, WP260 rev.01, 29 November 2017, Guidelines on transparency under Regulation 2016/679 endorsed by the EDPB, paragraph 64.
7

10 | Adopted

sources, the sources should be included in the list to the greatest extent possible, and the list should be accompanied with an indication of the types of sources not included in the list, and the reasons for not including those sources.
31 Where possible, it is good practice to include information on the domain names and URLs of the scraped web pages, to provide them in a searchable format, and to include the date or period of collection.
32 In situations where an organisation obtains already scraped datasets to develop AI models, it is recommended to also provide the means to contact the controller from whom the data was obtained. A good practice is to link directly to the website of the controller for the web scraping, and to accompany the information with a clear, concise explanation of the conditions under which the personal data was collected. This information should be provided in clear and plain language.
33 Data subjects should also be informed about their rights under the GDPR, and on how they can exercise them. Information should be easy for users to find and understand. By doing this, the controller will not only meet GDPR requirements but also build trust with data subjects whose data were scraped.
34 Other appropriate measures to protect the data subject’s rights, freedoms and interests, in addition to making the information publicly available, depending on the circumstances of the processing, may include: undertaking a data protection impact assessment and making it publicly available; applying anonymisation or pseudonymisation techniques to the personal data; minimising the data collected and the storage period; and implementing technical and organisational measures to ensure a high level of security. 15
Example 2: In order to train the AI model, the AI developer collects a very large volume of data about data subjects from a variety of sources that extend back to
20 years ago, such as social media pages and discussion forums where no direct identifiers are included in the data. As the webpages might contain personal data of thousands or millions of individuals, the provider does not necessarily have the means to contact them. Given the fact that there is no direct link between the scraper and the data subject that enables the communications, that the publication dates of the data extend back to 20 years ago and that a very large dataset is collected, it would involve disproportionate effort on the part of the controller to provide all persons with the information required under Article 14
GDPR. The controller makes the required information publicly available on its web site that is easily accessible, in clear and plain language. The controller also applies appropriate measures, e.g. the exclusion of data from web pages where the data subjects are directly identifiable.

Example 3: A provider of an AI model intends to fine tune an LLM model that can produce coherent text completion based on a short input. To do so the provider collects personal data from a closed user group of 5 000 individuals, discussing in the last two years a specific topic and using a specific business or social jargon.
The data subjects are directly identifiable through their full names, email addresses, and unique participant IDs. Given the fact that there are means to

Article 29 Working Party, WP260 rev.01, 29 November 2017, Guidelines on transparency under Regulation 2016/679 endorsed by the EDPB, paragraph 62.

15

11 | Adopted

contact the data subjects and that the data has been published or collected in the recent years, it would not involve disproportionate effort on the part of the controller to provide all persons with the information required under Article 14
GDPR. The controller should inform the data subjects individually about the scraping.
Data minimisation
35 The principle of data minimisation provides that personal data must be adequate, relevant and limited to what is necessary for the purposes for which they are processed. 16
36 This means that the controller must only collect personal data necessary for the purpose of the processing. While there is a major challenge in scraping large amounts of data while limiting personal data to only what is necessary for the intended purpose of processing, the principle of data minimisation does not prohibit training an AI model or AI system with large volumes of data. Instead, the principle of data minimisation requires not to process personal data that would not be necessary, relevant or adequate. To comply with this, the controller should make an assessment before the scraping begins, so as not to collect personal data that is not necessary for the development of the model.
37 The controller should, before the collection of the data:
-
-
-
-

-

-

consider using synthetic data instead of personal data, define precise collection criteria, undertake a data mapping and inventory process, apply filters to exclude the collection of certain categories of data where they are not necessary (e.g. bank transaction data, location/geolocation data, etc.) if they can be sorted out (e.g. if they rest in specific directories within file servers);
exclude from the collection certain categories of websites (e.g. sites or social networks used mainly by minors) which structurally contain these personal data (e.g.
data concerning vulnerable persons such as minors or certain sensitive data 17, such as financial information or location information);
exclude from the collection websites which clearly oppose the scraping of their content, through the use of technical measures, such as the use of robots authentication to view content, robots.txt or ai.txt files, or CAPTCHA, which impose an action that can only be carried out by a human being and aim to prohibit access to pages by robots.

38 The controller should, during and after the collection of the data:
-

-
-

apply syntax-based filtering mechanisms (e.g. regular expressions) during the collection to filter out personal data identifiable by their format (such as social security number, telephone number, etc);
where feasible, replace some or all real data with synthetic data generated for testing, analysis, or training purposes, in order to reduce exposure to personal data;
where feasible, anonymise or alternatively pseudonymise 18 personal data.

Article 5(1)(c) GDPR.
This term refers to data of a particularly sensitive nature and is distinct from special categories of data within the meaning of
Article 9 GDPR. See also Article 29 Working Party Guidelines on Data Protection Impact Assessment (DPIA) and determining whether processing is “likely to result in a high risk” for the purposes of Regulation 2016/679, wp248rev.01, endorsed by the
EDPB, p. 9-10.
18
EDPB Guidelines 01/2025 on Pseudonymisation, version for public consultation, adopted on 16 January 2025.
16
17

12 | Adopted

Accuracy
39 The principle of accuracy means that the personal data processed must be accurate and updated with regard to the specific purpose for which they are processed. 19 If scraping is used to process data obtained from different and/or unreliable sources, it will be difficult or even impossible to ensure the accuracy of the personal data. Complying with the principle of accuracy can also be challenging if the scraped personal data is stored for a long time and no longer up to date.
40 The principle of accuracy does not only apply to the collection and processing of personal data as such but also means that the controller should consider the final result of the AI training in order to minimize the risk of incorrect output. When the AI model, once it is placed on the market, is expected to produce (as output) data that constitute personal data, it should be compliant with the principle of accuracy.
41 Limiting the collection of personal data to what is necessary, it is crucial not only to comply with the principle of data minimisation, but also to make it easier for the controller to conduct the mapping of the personal data and to keep them updated and accurate.
42 To the greatest extent possible, it is recommended that the controller:
-

-
-

Scrape from reliable sources: when possible, choose sources that are official, trustworthy, and maintained (e.g. a government registry, verified company profile) and avoid secondary or outdated aggregators.
Timestamp the data: record when the data was scraped, to allow to show how up to date the data is.
Validate the data before using them in AI training: correct formats (emails, phone numbers), spot-check random samples for factual accuracy.

3.2.3 Legal basis for the processing of personal data
43 Before carrying out scraping operations involving the collection of personal data or re-use of scraped data, the controller must identify a lawful basis to the processing. 20 The legal basis of legitimate interest is often relied on for scraping in the context of development of generative AI by private bodies. The other grounds referred to in Article 6(1) GDPR will generally be less likely to apply to web scraping in the context of development of generative
AI by private bodies.
Consent
44 Consent would most probably not be an applicable legal basis, since it is often difficult to obtain the consent of individuals when personal data are collected indirectly and at large scale. Organisations scraping data (as ‘third party data’) 21 from the internet do not have a direct relationship with the data subject and are most probably not able to identify and obtain consent from each and every data subject before scraping data.
45 Sometimes data subjects are not even aware of the fact that their data are publicly available online. When data subjects make their personal data available online, for example on a web page accessible to everyone, this does not mean that the data subjects gave their consent to the scraping of their personal data for a specific purpose. In particular, the absence or
Article 5(1)(d) GDPR.
Article 6(1) GDPR.
21
EDPB Guidelines 1/2024 on processing of personal data based on Article 6(1)(f) GDPR, adopted on 8 October 2024;
paragraph 7.
19
20

13 | Adopted

non-applicability of a robots.txt file on a web site does not amount to consent within the meaning of the GDPR.
Legitimate interest
46 Article 6(1)(f) GDPR provides a lawful basis for the processing of personal data where such a processing is necessary for the purposes of the legitimate interests pursued by the controller or by a third party, except where such interests are overridden by the interests or fundamental rights and freedoms of the data subject, in particular where the data subject is a child.
47 In order for the application of Article 6(1)(f) to be lawful, three cumulative conditions must be fulfilled: the pursuit of a legitimate interest by the controller or by a third party; the need to process personal data for the purposes of the legitimate interests pursued; and that the interests or fundamental rights of the person concerned by the data protection do not take precedence over the legitimate interest of the controller or a third party (the so-called
“balancing test”). 22
Condition 1: legitimate interest
48 The concept of interest is closely related to, but distinct from, the concept of the purpose of the processing.23 An interest is the broader stake or benefit that a controller or third party may have in engaging in a specific processing activity. While the GDPR and the CJEU recognized several interests as being legitimate, 24 the assessment of the legitimacy of a given interest should be the result of a case-by-case analysis.
49 As recalled by the EDPB in its Guidelines on legitimate interest, an interest may be regarded as legitimate if it is lawful, clearly and precisely articulated and real and present, not speculative. 25
50 The EDPB has previously stated that the following examples may constitute a legitimate interest in the context of AI models: (i) developing the service of a conversational agent to assist users; (ii) developing an AI system to detect fraudulent content or behaviour; and (iii)
improving threat detection in an information system. 26 With regard to the development and improvement of a general-purpose AI model, even when the precise use of the model has not yet been decided, it is recommended to refer to the objective pursued by the development of the model (indicating in particular whether it is commercial, public, scientific research, and whether it is internal or external to the organisation).
Condition 2: necessity
51 The second step of the assessment consists in determining whether the processing of personal data is necessary for the purpose of the legitimate interest(s) pursued. The
EDPB Guidelines 1/2024 on processing of personal data based on Article 6(1)(f) GDPR, adopted on 8 October 2024; Judgment of 17 June 2021, M.I.C.M, C-597/19, EU:C:2021:492, paragraph 106; Judgment of 4 May 2017, Rīgas satiksme, C-13/16,
EU:C:2017:336, paragraph 28; Bundeskartellamt, paragraph 106. Koninklijke Nederlandse Lawn Tennisbond vs Autoriteit
Persoonsgegevens, C-621/22 , EU:C:2024:858, paragraph 37; Mousse v Commission nationale de l’informatique et des libertés,
SNCF Connect, C-394/23 ; HTB, Joined Cases C-17/22 and C-18/22, EU:C:2024:738, paragraph 49.
23
EDPB Guidelines 1/2024 on processing of personal data based on Article 6(1)(f) GDPR, version 1.0, 8 October 2024, paragraph
14.
24
EDPB Guidelines 1/2024 on processing of personal data based on Article 6(1)(f) GDPR, version 1.0, 8 October 2024, paragraph
16.
25
EDPB Guidelines 1/2024 on processing of personal data based on Article 6(1)(f) GDPR, adopted on 8 October 2024, paragraph
17.
26
EDPB Opinion on certain data protection aspects related to the processing of personal data in the context of AI models 28/2024, adopted on 17 December 2024, paragraph 69.
22

14 | Adopted
