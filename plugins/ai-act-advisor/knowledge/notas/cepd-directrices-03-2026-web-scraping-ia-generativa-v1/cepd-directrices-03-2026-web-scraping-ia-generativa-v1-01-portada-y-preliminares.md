---
name: cepd-directrices-03-2026-web-scraping-ia-generativa-v1-01-portada-y-preliminares
description: "CEPD: cepd directrices 03 2026 web scraping ia generativa v1, sección «Portada y preliminares» (págs. 1-5). Documento de 2026-07-07, idioma en."
metadata:
  type: reference
  documento: cepd-directrices-03-2026-web-scraping-ia-generativa-v1
  emisor: CEPD
  fecha: 2026-07-07
  idioma: en
  seccion: "Portada y preliminares"
  paginas: 1-5
  origen: 2026-07-07-cepd-directrices-03-2026-web-scraping-ia-generativa-v1-en.pdf
  oficial: false
---
# Portada y preliminares

Guidelines 03/2026 on web scraping in the context of generative AI
Version 1.0
Adopted on 07 July 2026

Version history
Version

Date

Adoption information

Version 1.0

07 July 2026

adoption of the guidelines for public consultation

1 | Adopted

Executive summary
Web scraping is a commonly used technique for extracting large amounts of data from publicly available web services. It is a large-scale processing activity and often occurs without data subjects being aware of it. This poses particular risks to individual’s rights and freedoms, and in particular their right to protection of personal data.
These guidelines focus on situations where data is scraped from internet sources, in the context of training generative AI. They cover situations were an organisation either scrapes data from internet sources external to the organisation themselves, or by contracting another party. They are limited to web scraping done by private entities.
The GDPR applies to web scraping when it includes personal data processing operations, such as collection, storage, organisation and retrieval. Compliance with certain GDPR requirements can be challenging when web scraping collects data that include personal data.
Different organisations may be involved in the data collection process for the creation of an AI training dataset, with varying degrees of involvement. The qualification of the organisations involved in each processing as controllers, joint controllers or processors should be analysed on a case-by-case basis.
The controller must comply with the purpose limitation principle, as well as the transparency principle. For the latter, this includes the obligation to inform the data subject about the processing of their personal data. Depending on how the data processing is precisely designed, the controller might not have to inform data subjects individually about the web scraping if the provision of the information proves impossible or would require disproportionate effort.
To comply with the principle of data minimisation, the controller should implement measures to ensure that only information necessary for the intended purpose is collected. Such measures could be: before the collection of data, considering using synthetic data instead of personal data; defining precise collection criteria; undertaking a data mapping and inventory process; apply filters to exclude the collection of certain categories of data; exclude from the collection websites that structurally contain certain types of data and websites which clearly oppose the scraping. After the collection of data, the controller could apply syntax-based filtering mechanisms and, where feasible, replace some or all real data with synthetic data, or anonymise or pseudonymise the data.
To ensure the accuracy of the personal data, it is recommended that the controller scrape from reliable sources, timestamp the data and validate the data before using them in AI training.
The legal basis of legitimate interest (Article 6(1)(f) GDPR) is often used by private entities for scraping for generative AI training purposes. In order for the application of Article 6(1)(f) to be lawful, three cumulative conditions must be fulfilled: the pursuit of a legitimate interest by the controller or by a third party; the necessity to process personal data for the purposes of the legitimate interests pursued; and that the interests or fundamental rights of the person concerned by the data protection do not take precedence over the legitimate interest of the controller or a third party (the so-called “balancing test”). As a part of the balancing test, controllers can implement technical or organisational measures to mitigate any identified risks in the context of web scraping for generative AI.
Such mitigating measures could include, among others: ensuring that certain data categories are not collected or that certain sources are excluded by default from data collection; limiting
2 | Adopted

the collection to freely accessible data; establishing safeguards that contribute to increased transparency; facilitating the exercise of individuals’ rights; deleting or anonymising personal data as soon as possible and pseudonymise personal data. Other additional measures relating to the subsequent stages of the AI development phase, such as including measures to limit the risks of memorisation, regurgitation or attack of AI models or systems are also relevant.
Processing of special categories of data is in principle prohibited. For the web scraping entailing the processing of special categories of personal data, a derogation in Article 9(2)
GDPR is required, in addition to a lawful basis in Article 6 GDPR. The EDPB considers that the Court’s ruling GC & Others (C-136/17) can be relevant for the incidental and residual collection by a controller of special categories of personal data in the context of web scraping for the training of an AI model, ‘within the framework of his responsibilities, powers and capabilities,’ if the controller implements technical and organisational measures to prevent the collection and the dissemination of data. The EDPB recalls that the controller should carry out a case-by case analysis of whether the reasoning of the Court’s ruling can be applied to a specific processing activity.

3 | Adopted

Table of Contents
1 Introduction and scope.................................................................................................... 5
2 Definition of web scraping .............................................................................................. 5
3 Web scraping and the GDPR ........................................................................................... 7
3.1 General observations ............................................................................................. 7
3.2 Guidance on specific provisions in the GDPR ........................................................ 8
3.2.1 Controller/joint controllers/processor ............................................................... 8
3.2.2 Principles relating to processing of personal data ............................................ 9
3.2.3 Legal basis for the processing of personal data ............................................. 13
3.2.4 Special categories of personal data ............................................................... 19

4 | Adopted
