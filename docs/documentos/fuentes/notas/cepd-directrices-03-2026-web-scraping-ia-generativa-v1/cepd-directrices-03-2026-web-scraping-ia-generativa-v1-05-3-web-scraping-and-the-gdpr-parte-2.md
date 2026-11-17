---
name: cepd-directrices-03-2026-web-scraping-ia-generativa-v1-05-3-web-scraping-and-the-gdpr-parte-2
description: "CEPD: cepd directrices 03 2026 web scraping ia generativa v1, sección «3  Web scraping and the GDPR (parte 2)» (págs. 16-23). Documento de 2026-07-07, idioma en."
metadata:
  type: reference
  documento: cepd-directrices-03-2026-web-scraping-ia-generativa-v1
  emisor: CEPD
  fecha: 2026-07-07
  idioma: en
  seccion: "3  Web scraping and the GDPR (parte 2)"
  paginas: 16-23
  origen: 2026-07-07-cepd-directrices-03-2026-web-scraping-ia-generativa-v1-en.pdf
  oficial: false
---
# 3  Web scraping and the GDPR (parte 2)

assessment entails two elements 27: (i) whether the processing activity will allow the pursuit of the purpose; and (ii) whether there is an equally effective and less intrusive way of pursuing this purpose. 28
52 When personal data is necessary for training generative AI, narrowing the collection criteria to exclude unnecessary collection of personal data, rather than scraping a wide part of the internet may be crucial to ensure the necessity condition is met. Using pseudonymised personal data, or synthetic data, may be another less intrusive way of pursuing this purpose.
Condition 3: balancing test
53 The balancing test requires, inter alia, the identification and description of the different opposing rights and interests at stake, i.e., on the one side, the interests, fundamental rights and freedoms of the data subjects; on the other side, the legitimate interests of the controller or a third party. The impact on the data subjects as well as their reasonable expectations are also relevant elements of the balancing. 29
Data subjects’ interests, fundamental rights and freedoms
54 In the context of web scraping for training a generative AI model, data subjects’ interests may include, but are not limited to, the interest in self-determination and retaining control over their own personal data (i.e. the data that originally was published on a website for a certain purpose is then scraped and processed for generative AI training against the data subjects’ wishes or without their knowledge). 30 Also, large-scale and indiscriminate data collection in the AI development phase may create a sense of surveillance for data subjects
(‘chilling effect’). This may lead individuals to self-censor themselves and risks undermining their freedom of expression. The ‘chilling effect’ on freedom of expression may be due to the possible use of an AI model to identify data subjects who intended to express themselves anonymously, especially if the AI model is connected to a web search tool, as well as to the possible use of the AI model for profiling within the meaning of the GDPR. 31 The generation of deep-fakes (pictures, videos, speech) also adds to the possible impact on data subjects’ interests, rights and freedoms, as well as possibly on the right to dignity of the person concerned. 32
Impact of the processing on the data subjects
The nature of the data processed
55 When scraping data from the internet, it should be recalled that - in addition to special categories of personal data and data relating to criminal convictions and offences that enjoy special protection under Article 9 and 10 of the GDPR respectively - certain types of personal data revealing highly private information, such as location data or financial data, may also be scraped. Personal data about minors may also be collected. The processing of such personal data may lead to significant consequences for data subjects and should be

EDPB Opinion on certain data protection aspects related to the processing of personal data in the context of AI models 28/2024, adopted on 17 December 2024, paragraph 72.
28
EDPB Guidelines 1/2024 on processing of personal data based on Article 6(1)(f) GDPR, adopted on 8 October 2024, paragraph
29.
29
EDPB Guidelines 1/2024 on processing of personal data based on Article 6(1)(f) GDPR, adopted on 8 October 2024, paragraph
32.
30
EDPB Opinion on certain data protection aspects related to the processing of personal data in the context of AI models 28/2024, adopted on 17 December 2024, paragraph 77.
31
Article 4(4) GDPR.
32
See also the section on Consequences for data subjects, at paragraphs 59-61 of these Guidelines.
27

15 | Adopted

considered when assessing the level of intrusiveness, notably in case of personal data relating to minors.
56 As a rule, the more sensitive or private the nature of the data to be processed, the more likely it is that the processing of such data will have a negative impact on the data subject, and the more weight should be attributed to it in the balancing test.
The context of the processing
57 The context of the processing and the specific data processing methods may influence the impact that the processing may have on the rights and interests of the data subject. The
EDPB has previously stated that the use of web scraping in the development phase may lead - in the absence of sufficient safeguards - to significant impacts on individuals, due to the large volume of data collected, the large number of data subjects, and the indiscriminate collection of personal data. 33
58 Since information published on the internet are rarely deleted, the scraped data may have been published during a long period of time. Scraping a larger amount of websites means the interference with the fundamental rights to privacy and to the protection of personal data increases.
Consequences for data subjects
59 The rights, freedoms and interests of the data subjects may be impacted by the envisaged processing. The greater the impact on the data subjects is, the less probable it is that the controller can rely on legitimate interest.
60 In practice, it might be difficult for data subjects to exercise their rights under the GDPR and to oppose the scraping of their data, notably when data are scraped by third parties. This means that, even if the data subjects are aware that their personal data will be scraped, it is difficult for them to make these data unreachable to scrapers. One of the main consequences of scraping in the context of generative AI is that given the current technical state of the art, once the model is trained, personal data cannot be easily deleted from a model.
61 The analysis of the possible further consequences of the processing should also consider the likelihood of these further consequences materializing. The assessment of such likelihood should be made taking into consideration the technical and organizational measures in place and the specific circumstances of the case. 34
Expectations of data subjects
62 The data subjects’ reasonable expectations play an important role when weighing their legitimate interest(s) and the interests or fundamental rights and freedoms of data subjects.
63 Reasonable expectations do not necessarily depend on the information provided to data subjects, as the mere fulfilment of the information obligations set out in Articles 12, 13 and
14 GDPR is not sufficient in itself to consider that the data subjects can reasonably expect a specific processing. 35 However, the information provided to data subjects may be

EDPB Opinion on certain data protection aspects related to the processing of personal data in the context of AI models 28/2024, adopted on 17 December 2024, paragraph 86.
34
EDPB Opinion on certain data protection aspects related to the processing of personal data in the context of AI models 28/2024, adopted on 17 December 2024, paragraph 90.
35
EDPB Guidelines 1/2024 on processing of personal data based on Article 6(1)(f) GDPR, adopted on 8 October 2024, paragraph
53.
33

16 | Adopted

considered when assessing whether data subjects can reasonably expect their personal data to be processed. 36
64 Given the technological developments of recent years on generative AI, people may be aware that the data they publish online may be accessed, collected and reused by third parties. However, it cannot be considered that they can always expect such processing to take place in all situations, for all purposes, for all controllers’ interests and for all types of data accessible online concerning them. Moreover, the impact of generative AI models, depending on the capability of the model, may also change in time. In particular, the controller should consider:
-
-

-

-

-

the nature of the source websites (social networks, online forums, dataset dissemination sites, etc.)
the type of publication and the publicly accessible nature of the data (for example, an article published on a freely accessible blog has a more public character compared to a post on a social network published with access restrictions). As a ‘rule of thumb’, when the data has been made public and visible to everyone by the data subject themselves, the data subjects are more likely to reasonably expect that their personal data may be processed by others.
the restrictions imposed by the scraped website, for example through the implementation of technical measures such as the use of robots authentication to view content, robots.txt or ai.txt files, or the implementation of CAPTCHA, which are intended to impose an action that can only be carried out by a human being, and aim to prohibit access to the pages by robots. If data subjects are aware that a website implements these measures and a website is nevertheless scraped, it is less likely that they can expect the processing of their personal data by a scraping entity.
the nature and characteristics of the relationship between the data subject and the controller: even though there is often no direct relationship between the data subject and the entity carrying out the web scraping or using scraped data, people may be aware that the data published online may be accessed, collected and reused by third parties; 37 the characteristics of the data subjects (minor, public figure, position of the data subject, etc.)
Example 4: A person uploads their data to a content sharing platform that is freely accessible and does not contain any prohibitions against web scraping, and the platform communicates the possibility of the content being scraped to its users.
In this instance, data subjects can reasonably expect third parties to scrape that data to develop AI models.

Example 5: If a person uploads their data to a content sharing platform that prohibits scraping through the use of robots.txt files and the implementation of CAPTCHA, and expressly states on their site that they do not allow the use of their users' data for the development of AI models, they cannot reasonably expect third parties to scrape that data for that purpose.

EDPB Opinion on certain data protection aspects related to the processing of personal data in the context of AI models 28/2024, adopted on 17 December 2024, paragraph 92.
37
EDPB Guidelines 1/2024 on processing of personal data based on Article 6(1)(f) GDPR, paragraph 54.
36

17 | Adopted

The role of mitigating measures
65 When for a specific processing the data subjects’ interests, rights and freedoms override the legitimate interest(s) being pursued by the controller or a third party, the controller may consider introducing mitigating measures to limit the impact of the processing on data subjects. Mitigating measures are safeguards that should be tailored to the circumstances of the case. These additional measures should not be confused with measures that the controller is legally required to adopt anyway to ensure compliance with the GDPR. 38 If the data subject’s interests, rights and freedoms override the legitimate interests being pursued, and sufficient mitigating measures are not taken, the processing cannot be based on Article
6(1)(f) GDPR.
66 Measures may include technical or organisational measures, such as:
a. Excluding data content from publications which might include personal data entailing risks for particular persons or groups of persons (e.g. individuals who might be subject to abuse, prejudice or even physical harm if information was released publicly).
b. Ensuring that certain data categories are not collected or that certain sources are excluded by default from data collection is important to comply with the principle of data minimization, but also to limit the impact of the scraping on data subject. This could include, for instance, certain websites that are particularly intrusive due to the sensitivity of their subject matter.
c. Limiting the collection by excluding scraping of certain personal data, such as:


personal data on sites, which are only accessible when logged into the site or service and are therefore not freely accessible, for example personal data published on a social network that requires login before getting access to that data;



personal data on sites that are freely accessible but in relation to which data subjects cannot be considered reasonably aware of the accessibility. For example, where a social network returns different outputs when the user agent of the scraping service is used and when the user agent of the web browser from the social media user is used, particularly where the scraping service receives more data (e.g. meta data such as timestamps or access statistics by using a technical API)
than the regular user. 39 This could also be the case for an online directory or register in which anyone can freely look up an individual's name, address and contact details;

d. Imposing other relevant limits on collection, possibly including criteria based on time periods.
e. Establishing safeguards that contribute to increased transparency. For example, the controller can publish and make available, as widely as possible, information about data collection and data subjects’ rights (e.g. through online articles), ensuring that an updated list of scraped websites is published.

EDPB Guidelines 1/2024 on processing of personal data based on Article 6(1)(f) GDPR, adopted on 8 October 2024, paragraph
57.
39
For information about the term ‘user agent’, see for example User agent - Wikipedia, or RFC 9110 - HTTP Semantics.
38

18 | Adopted

f. Facilitating the exercise of individuals’ rights, including putting in place a discretionary and prior right to object to strengthen individuals' control over their data. The controller can also create an opt-out list, which allows data subjects to object to the collection of their data on certain websites or online platforms by providing information that identifies them on those websites, including before the data collection occurs.
g. Deleting or anonymising the unnecessary personal data as soon as possible.
h. As referred to in the EDPB guidelines on pseudonymisation, pseudonymisation could be a measure to limit the direct identification of personal data. This could, in some cases, be done by replacing direct identifiers with placeholders and use these during the AI training.
i.

Other additional measures that are relevant to protect personal data concerned by the further stages of the AI development phase, including measures to limit the risks of memorisation, regurgitation or attack of AI models or systems (e.g.
deduplication).
These measures do not constitute an exhaustive list. The controller should make a case-by-case assessment to determine which measures are appropriate.

Example 6: An organisation that collects numerous publicly available online voice recordings, in order to develop and market a voice generation tool, without taking any additional measures to protect the training data or limit the risks of unlawful or malicious reuse, cannot rely on the legal basis of legitimate interest.

Example 7: An organisation aims to develop a generative AI system for text. It exclusively uses data from freely and publicly accessible online sources, where the data subjects have manifestly made the content public. It also excludes any content protected by copyright (i.e., using only content in the public domain or for which rights holders have not objected to text and data mining as permitted under
Directive 2019/790 on copyright and related rights in the Digital Single Market).
In addition, it implements a range of safeguards to limit data memorization and regurgitation, restricts problematic content generation through technical or contractual measures, facilitates the exercise of data subjects’ rights when reidentification is possible, and clearly indicates data sources in a publicly available privacy policy. In such a case, the balancing test may generally be considered as met.

3.2.4 Special categories of personal data
67 Processing of special categories of data, such as data revealing racial or ethnic origin or political opinion, and concerning health or sexual orientation, is prohibited. 40 For the intended scraping of such data a derogation in Article 9(2) GDPR is required, in addition to a lawful basis under Article 6 GDPR.

40

Article 9(1) GDPR.

19 | Adopted

68 Even though the controller should implement measures to prevent the collection of such personal data, it is not always possible to assess with reasonable certainty whether the scraping leads to the collection of special categories of personal data as defined in Article 9
GDPR until after the data has been scraped, thus when the processing activity has already been carried out.
69 It remains likely that, despite the organisational and technical measures, the controller residually processes special categories of personal data that it did not intend to collect and subsequently process. If such processing cannot be justified under EU data protection law, it will be unlawful for controllers to scrape such personal data in the context of AI development (subject to the considerations made below)
The case GC & Others, C-136/17
70 For the processing of personal data in the context of the activity of a search engine, the Court of Justice of the European Union (‘the Court’) has emphasized that the processing and dissemination of special categories of data, constitutes a particularly serious interference with the fundamental rights to privacy and the protection of personal data, and that there is no exemption from the prohibitions or restrictions contained in Article 9 or 10 GDPR for the activity of a search engine. However, the Court recognised that the specific features of the processing carried out by the operator of a search engine may have an effect on the extent of the operator’s responsibility and obligations under those provisions, 41 and that the prohibition in Article 9(1) GDPR applies ‘within the framework of his responsibilities, powers and capabilities’. 42
71 Against this background, the Court considered the prohibitions and restrictions of Articles 9 and 10 GDPR apply to the operator of a search engine only by reason of referencing (on a page with search results following a search on the basis of an individual’s name) and via verification on the basis of a request by the data subject. 43
The responsibilities, powers and capability test
72 The EDPB considers that the Court’s ruling can be relevant for the incidental and residual collection of special categories of personal data in the context of web scraping for the training of an AI model. 44 The Court’s ruling can be relevant only for processing activities similar to those in the judgement, and under similar circumstances, and should not be seen as a general exemption from the requirements in Articles 9 and 10 GDPR.
73 The controller should make a case-by case analysis to assess if the following conditions are met:
a. the processing activity has relevant similarities with the processing activity of a search engine, as referred to in the Court’s judgement, b. the processing includes only the incidental and residual processing of special categories of personal data, and no intentional processing,

CJEU, Grand Chamber, Judgment of 24 September 2019, GC and Others C-136/17, paragraph 45.
C-136/17, paragraph 48.
43
C-136/17, paragraph 47.
44
Incidental and residual collection of data should be understood as a processing of data that the controller has no intention of carrying out, but which will occur to some extent despite the implementation of measures to prevent such collection.
41
42

20 | Adopted

c. it is difficult/impossible to assess whether and to what extent the processing includes special categories of personal data, and therefore prevent the collection if such data, and d. the controller implements measures ‘within the framework of his responsibilities, powers and capabilities’, as mentioned in the Court’s judgement, to prevent the dissemination of special categories of personal data.
The responsibilities, powers and capabilities when web scraping in the context of the development of generative AI models
74 If the conditions a-c are relevant for the specific processing activity, and the controller implements measures ‘within the framework of his responsibilities, powers and capabilities’ to prevent the dissemination of special categories of personal data, the prohibition laid down in Article 9(1) GDPR will apply to a controller only within this framework of his responsibilities, powers and capabilities (condition d). These responsibilities, powers and capabilities will include at least the following measures:
i. Before the collection of the data the controller should define precise criteria and apply filters to prevent the collection of special categories of personal data. The controller should also exclude certain categories of websites (e.g. sites or social networks mainly used by minors) which structurally contain these data (e.g. data concerning vulnerable such as minors or certain sensitive data).
ii. After the collection of the data, the controller should ensure that special categories of personal data that may have been collected despite the application of these measures is deleted from datasets immediately after the collection or as soon as it is identified. In particular, the controller should delete special categories of personal data upon request from the data subject if the request constitutes a plausible indication that the concerned data indeed fall under the prohibition laid down in Article 9(1) GDPR.
iii. During the development of the AI model, the controller should prevent extraction of special categories of personal data from the model and provide assurance regarding state-of-the-art resistance to privacy attacks. The controller should train and perform testing of the model and apply content (output) filters to the AI system to prevent the system from producing results and giving information to users that reveals special categories of personal data.
iv. After the development of the AI model, the controller using the model as part of an AI system should implement a process to constantly monitor the output generated by the AI system. When, despite the organisational and technical measures already implemented, special categories of personal data is included in the output, the controller should immediately take measures to prevent the production of such data (e.g. through updated or reinforced output filters, restricting certain prompts or functionalities). In the longer term, model unlearning or other processes with equal effect that might become available through technological progress should also be considered is necessary. If,
21 | Adopted

through technological progress, machine unlearning algorithms can guarantee deletion of specific data from a model this may provide an alternative to output filters or retraining the model.
75 The controller should be able to demonstrate, in line with the accountability principle, that the conditions a-c are relevant for the specific processing activity, and that the measures adopted within the framework of his responsibilities, powers and capabilities’ (condition d)
are relevant and effective to prevent the collection and the dissemination of special categories of personal data.
76 The implementation of these measures should be accompanied by regular verification and assessment - having regard to the development as well as to the use of the AI model - of the effectiveness of the measures implemented when performing web scraping activities. As a result of such verification and assessment, it is possible that additional or different organisational and technical measures should be implemented by the controller when the measures adopted are not effective.
77 The measures to be implemented should be in line with the state-of-the-art techniques available to limit the collection and other processing of special categories of personal data.
It is however possible that in the future better privacy enhancing techniques to limit or even exclude the processing of special categories of personal data become available. Controllers should therefore constantly monitor technological developments to ensure that the state-ofthe-art measures remain appropriate.

For the European Data Protection Board
The Chair
Anu Talus

22 | Adopted
