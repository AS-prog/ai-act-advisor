---
name: cepd-directrices-03-2026-web-scraping-ia-generativa-v1-03-2-definition-of-web-scraping
description: "CEPD: cepd directrices 03 2026 web scraping ia generativa v1, sección «2  Definition of web scraping» (págs. 6-7). Documento de 2026-07-07, idioma en."
metadata:
  type: reference
  documento: cepd-directrices-03-2026-web-scraping-ia-generativa-v1
  emisor: CEPD
  fecha: 2026-07-07
  idioma: en
  seccion: "2  Definition of web scraping"
  paginas: 6-7
  origen: 2026-07-07-cepd-directrices-03-2026-web-scraping-ia-generativa-v1-en.pdf
  oficial: false
---
# 2  Definition of web scraping

The European Data Protection Board
Having regard to [Article 70 (1)(e) of the Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive
95/46/EC, (hereinafter “GDPR”),
Having regard to the EEA Agreement and in particular to Annex XI and Protocol 37 thereof, as amended by the Decision of the EEA joint Committee No 154/2018 of 6 July 2018,
Having regard to Article 12 and Article 22 of its Rules of Procedure,
Has adopted the following Guidelines:

1 Introduction and scope
1

These guidelines aim to clarify the legal and technical implications of web scraping for generative artificial intelligence (AI) development under the GDPR. Generative AI is a technology aiming to create new content by learning patterns from existing data. It uses specialised machine learning models designed to produce a wide and general variety of outputs such as text, image or audio.

2

Generative AI models are built through different phases, including training and, where relevant, fine-tuning. Training generative AI models requires vast amounts of data from diverse sources. In the context of AI training, web scraping is used to collect large datasets from publicly accessible sources on the internet, which may be employed not only to train new generative AI models but also to fine-tune existing models for specific use cases.

3

The following are typical situations regarding data scraping for the purpose of training AI models.
-
-

An organisation scrapes data from the internet themselves or by contracting another party, in the context of the development of generative AI.
An organisation obtains and reuses a dataset that has already been scraped by another organisation (data broker).

4

These guidelines will focus on these scenarios. The guidelines will not address the role of data brokers who scrape data and just hold data sets available for other organisations, and whose intention is not to train AI models themselves.

5

Furthermore, these guidelines focus on situations in which personal data is acquired
(scraped) from sources external to the organisation and do not address processing of an organisation’s own personal data. This does not mean that the excluded situations are not subject to data protection legislations.

6

As web scraping for the development of generative AI is mainly performed by private sector bodies, these guidelines will also focus only on web scraping done by private entities.

2 Definition of web scraping
7

Web scraping is a commonly used technique that uses automated tools for extracting and storing information from publicly available web services, for example public registers, opendata portals, news outlets, social media, discussions’ forums, and personal websites
(‘blogs’). Many of these websites are likely to contain personal data.

5 | Adopted

Types of web scraping and content
8

An overarching distinction can be made between targeted scraping and untargeted scraping, depending on the specificity and restrictiveness, of the collection (and not the technical tools used):
Targeted scraping is performed according to collection criteria that can be more or less restrictive. The criteria could be, for example: all URLs ending in europa.eu, URLs with content written in a specific language or covering a specific topic.
Untargeted scraping (such as web crawling without collection criteria) is done on more unrestricted basis, where the software is allowed to explore and follow each discovered link and continue with its exploration. This can be performed by using a web crawler, which automatically updates the list of URLs to be visited and store the server replies. This is done with ‘spiders’, small software programs that receive their instructions (tasks) in advance. These tasks could be: “add all the URLs you encounter while crawling the listed URLs”. The task could also be limiting the list or URLs to visit, for example “follow all links as long as you stay within the domain www.edpb.europa.eu”. Depending on the instructions to the spiders, a relatively short list of URLs can expand significantly over time as the crawler continuously discovers and adds new
URLs to its queue of pages to be visited. This may result in the exploration of a large portion of the internet to be searched as a result of the constant addition of relevant URLs. This increases the risk that the controller has limited knowledge of what personal data are collected and processed.

9

An additional distinction can be made between static and dynamic content in websites. It is common practice to combine both static and dynamic content on the same site or webpage.
Static content does not change due to users’ actions (e.g. the text of a given post in a blog). When scraping static content from web pages, the target data resides directly in the HTML of a webpage, meaning it can be extracted simply by fetching and parsing the page. Most scrapers targeting static websites rely on the direct structure of HTML to locate the needed data.
Dynamic content can change to respond to users’ actions (e.g. loading more content when a user scrolls down a page). When scraping dynamic content from webpages, web crawlers need to render the page internally, mimicking a human users’ interaction with the page. These scrapers wait for the page to render the additional content and then read and extract the dynamically rendered data.

10 Websites change their structure frequently. Scrapers might need regular monitoring and updates to continue functioning correctly (e.g., when updated data is needed for the model to perform accurately).
The different steps in the process of web scraping
11 The process of web scraping can typically be sequenced into several separate steps.
The first step relates to defining data collection criteria. It involves defining the relevant sources which will be scraped depending e.g. on the purpose of

6 | Adopted
