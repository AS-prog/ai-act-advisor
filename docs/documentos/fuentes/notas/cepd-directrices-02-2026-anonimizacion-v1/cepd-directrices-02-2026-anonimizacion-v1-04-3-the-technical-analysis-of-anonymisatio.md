---
name: cepd-directrices-02-2026-anonimizacion-v1-04-3-the-technical-analysis-of-anonymisatio
description: "CEPD: cepd directrices 02 2026 anonimizacion v1, sección «3  The technical analysis of anonymisation (parte 1)» (págs. 17-24). Documento de 2026-07-07, idioma en."
metadata:
  type: reference
  documento: cepd-directrices-02-2026-anonimizacion-v1
  emisor: CEPD
  fecha: 2026-07-07
  idioma: en
  seccion: "3  The technical analysis of anonymisation (parte 1)"
  paginas: 17-24
  origen: 2026-07-07-cepd-directrices-02-2026-anonimizacion-v1-en.pdf
  oficial: false
---
# 3  The technical analysis of anonymisation (parte 1)

reasonably likely to be used. Where this is the case, the entity which suffered the incident should then determine its role with respect to the processing and whether it needs to fulfil any obligations under Article 33 and 34 GDPR 35.

3 The technical analysis of anonymisation
3.1 Introduction
43

It will not always be immediately apparent whether information relates to an identified or identifiable individual. This is especially the case when the anonymising controller has deliberately tried to make it difficult to recognise that the information relates to an identified or identifiable individual. It is therefore necessary to apply a technical analysis that considers the state of the art of re-identification techniques and can be used to draw out whether or not the data is anonymous.

44

Given the broad scope of possible datasets and anonymisation techniques, as well as future developments in (re-)identification techniques, assessments will often require a case-by-case analysis and may require considerations not fully covered by this document. Nevertheless, this section will provide guidance on a framework which can be used to test the anonymity of data.

45

The framework in this section can be used in two ways. The first is a contextualised approach, which is based on the legal analysis set out above and uses information about all relevant entities’ means and the likelihood of their use. The second is through a simplified approach, which disregards differences between entities regarding the means they are reasonably likely to use. This simplified approach may lead the anonymising controller to treat the data as though it is not anonymous even if it would actually be so for the relevant entities. However, it can provide greater confidence and can be complemented with the contextualised approach to refine the findings.

46

Having set out these two approaches in detail, this section quickly discusses the simple cases, where the given data is clearly personal and use of the full framework is unnecessary. It then moves on to the main part of the framework itself, which is made up of three broad criteria: No
Record Isolation, No Linkage and No Inference. If all three of these criteria are met, the information may be regarded as anonymous; if one or more is violated, further analysis may be required. The section finishes by providing guidance on how the framework can be applied and assessed, and what this further analysis involves.

3.2 Approaches to the assessment
47

The legal standard for anonymisation can produce different results depending on the applicable perspectives. This contextual approach leads to a differentiated assessment, where the respective capabilities of the relevant entities should be individually assessed. In practice, this can be quite complex, especially where it is difficult to account for (or even know about)
all the possible contextual elements involved. This contextual approach therefore runs the risk of false positives, where the assessor may incorrectly conclude that data is anonymous because they are unaware of a particular entity’s means reasonably likely to be used for

35

For further guidance on this topic, see EDPB Guidelines 9/2022 on personal data breach notification under GDPR.

16 | Adopted

identification. However, if done properly, this approach allows for a comprehensive analysis of the dataset and allows controllers to be confident in whether the dataset falls within the scope of the GDPR.
48

For the sake of simplicity, then, some anonymising controllers may decide to use a simplified approach for the assessment. Under this approach, an anonymising controller can simply choose to ignore differences between entities regarding access to the given data, to additional information or to other resources that can contribute to re-identification. It must be emphasised that this simplified approach is not an alternative legal standard 36. Instead, this approach is a way to voluntarily shift the risk from false positives to false negatives, where the anonymising controller treats anonymous data as personal because they have (in effect) overestimated the likelihood that certain means will be used. In some cases, this approach would provide a more cautious level of protection than is strictly necessary, but in doing so it ensures that the legal standards set by the GDPR will always be met in cases of doubt.

49

In practice, a combination of the two approaches may often be helpful. For example, an anonymising controller might wish to begin with the simplified approach, asking if re-identification is even possible in theory. If this is not possible, the data can be safely considered anonymous. If, however, the simplified approach identifies the existence of certain re-identification methods, the anonymising controller can then shift to the contextual approach and consider whether those methods are reasonably likely to be used from the relevant entities’ perspectives. Alternatively, the anonymising controller might perform an initial mapping of the given data and immediately realise that there are a huge range of re-identification methods that are possible in theory, but which can quickly be excluded as impossible to be applied to the given data in practice. That anonymising controller may, therefore, decide to go straight to the contextual approach, which allows these methods to be immediately discounted because, in reality, they are not means reasonably likely to be used by any entities.
Example 9: The controller wishes to anonymise a dataset containing a combination of demographic and medical information. They begin with the simplified analysis and discover that the demographic data alone could not allow for re-identification of the individuals in this case. However, they also discover that re-identification could be possible if the demographic information is combined with certain additional medical information. Under the simplified analysis, they would therefore conclude that the information is not anonymous. However, the controller decides to extend the analysis and pivots to a contextual analysis. They therefore begin identifying the applicable perspectives and testing if the respective entities could access that additional medical information with means reasonably likely to be used.

3.3 Simple cases and data mapping
50

In some cases, it may be immediately apparent that information is not anonymous. This includes, for example, a dataset which includes an individual’s name, email address, phone number or social security number; a dataset which contains pseudonyms that can easily be reverse engineered to discover an identifier, or which itself can be used to identify the individuals; a dataset which lacks direct identifiers but which clearly contains attributes that allow for identification of the individuals; or a dataset which is clearly being used for the
This means, in particular, that while the simplified approach may be quite useful for anonymising controllers to prove that the information is anonymous and falls outside of the scope of the GDPR, it cannot be used by third parties to definitively prove that the information is personal data and that the controller’s processing of that data is therefore in violation of the GDPR.

36

17 | Adopted

purposes of evaluating, treating or influencing the status or behaviour of a specific individual in a particular way.
51

To help catch these, and other simple cases, it is recommended to map out the data, as well as any additional information that may aid (re-)identification that is either held by other relevant entities or is accessible to them through means reasonably likely to be used. If the data is clearly not anonymous at this stage, it is unnecessary to apply the criteria set out below. This should be done as an early step in the assessment and, even if no such simple identification becomes apparent, can also help to streamline the next steps.

3.4 The three criteria
52

This sub-section sets out the three criteria: No Record Isolation, No Linkage and No Inference, with further guidance on their application then contained in sub-section 3.5. If all three of the criteria are met, the information may be regarded as anonymous. On the other hand, violating a criterion does not necessarily mean that the information must necessarily be considered as personal data; rather, if one or more of the criteria is violated, it is then necessary to continue the analysis, as set out in sub-section 3.5.3, to assess the impact of that violation and whether the data could still be considered anonymous.

53

The same criteria are used for both the contextual and simplified approaches. For the sake of explanation, the descriptions of these criteria in sub-sections 3.4.1–3.4.3 use the simplified approach, which allows this sub-section to focus on the methods themselves. The contextual matters will then be reintroduced sub-section 3.5.

3.4.1 No Record Isolation
54

A common method used to distinguish individuals from others in a given group is by singling them out by reference to one or more attributes 37. By its very nature, it is much easier to do this when a record – i.e. all of the values within the given data that relate to one single individual – is unique. As such, record isolation can then lead to the violation of anonymity for the given data. This leads to the No Record Isolation criterion.

55

The No Record Isolation criterion is met if the data does not contain a unique combination of attribute values that relate to a single individual.

56

The larger a record is, and the more attributes that it contains, the higher the likelihood that the record will be unique within the given data.

57

The No Record Isolation criterion can generally be tested by reference to the given data on its own. Since a record constitutes all information which is known to relate to a single individual, the No Record Isolation criterion may involve looking at, for example, multiple lines in a table or database table, depending on how the given data is structured.

37

The concept of singling out will be explained in detail in section 3.5.3.

18 | Adopted

Example 10: A research institute holds a dataset containing individual records of patients.
Each record contains information about the individual’s sex, date of birth, postcode, and the autoimmune disease affecting the patient. The data was verified before inclusion in the dataset and has not been modified.
Sex

Date of birth

Postcode

Disease

Female

28-09-1955

43221

celiac disease

Female

06-01-1955

43210

Crohn’s disease

Male

08-07-1959

89127

Vitiligo

Male

10-06-1959

89127

multiple sclerosis

Male

27-09-1959

89127

Diabetes mellitus type 1

In this case, all of the records are unique. The No Record Isolation criterion is violated because of the unique combinations of the attributes.
58

Notably, aggregate data will usually satisfy the No Record Isolation criterion – if the aggregation was done correctly, it should result in information that relates to groups of individuals and, therefore, should not actually contain any individual records which could be isolated.

3.4.2 No Linkage
59

Another common method of identifying an individual is by linking information from one dataset to another, or multiple other, dataset(s). By establishing that a record in Dataset A relates to the same individual as a record in Dataset B (and, if relevant, Datasets C, D and E etc.), the linkage increases the amount of information about that individual, which in turn makes it more likely that the individual can then actually be identified. Linkages can then lead to the violation of anonymity for the given data. This leads to the No Linkage criterion.

60

The No Linkage criterion is met if the data does not contain an individual’s record which could be linked to another record which (a) also relates (with certainty or high likelihood) to that same individual, and (b) comes from a different dataset.

61

Unlike the No Record Isolation criterion, which was assessed by reference to the given data alone, this criterion requires knowledge and understanding of other datasets that could be linked to the given data with means reasonably likely to be used 38.

62

Linkage may often be possible by reference to a common identifier (e.g., an internal customer number) which is used in both datasets, or by matching records based on certain combinations of attributes.
Example 11: A board game shop keeps a record of every purchase made by every customer.
This is clearly personal data, since each purchase is linked to a specific user. The shop wishes

As noted in para. 53 above, this section will explain the criteria following the simplified approach, to focus the explanation on the core parts of the criterion. It will not, therefore, consider whether the relevant entities could access those other datasets with means reasonably likely to be used. Under the contextual approach, however, it would also be necessary to ask whether such links are actually possible with means reasonably likely to be used from the relevant perspective, as explained in sub-sections
2.2 and 2.4 and discussed in sub-sections 3.5.2 and 3.5.3 below. This is true for all three of the criteria, but can be especially helpful to emphasise for the sake of the examples set out in this sub-section.
38

19 | Adopted

to anonymise the data and so decides to test if simply erasing the direct identifiers would be enough to do so.
The shop immediately notices that many of the records in the given data are unique, and that the given data therefore fails the No Record Isolation criterion. However, since failing a criterion does not necessarily mean that the given data is personal, the shop continues to test the other criteria before starting its assessment of the results.
To test the No Linkage criterion, the shop checks for other datasets which might contain matching records based on certain combinations of attributes (in this case, the specific combinations of purchased board games). This leads to a very popular website where users create lists of the games which they own and mark how often they play each of those games.
The shop finds that several records on the website match those in the given data, where customers have purchased games from the shop and then entered that information onto the website. These matching records mean that the datasets can be linked, and the shop therefore concludes that the given data also violates the No Linkage criterion.
63

In practice, data which satisfies the No Record Isolation criterion will often also satisfy the No
Linkage criterion. However, the two criteria should still be assessed separately, as there are ways to link non-unique data.
Example 12: A research institute processes a dataset containing individual records of some patients. In the dataset, the date of birth and postcode attributes have been generalised as follows:
Sex

Date of birth

Postcode

Disease

Male

**-**-1946

54***

sclerosis

Male

**-**-1946

54***

sclerosis

Female

**-**-1951

32***

lung cancer

Female

**-**-1951

32***

lung cancer

Female

**-**-1951

32***

lung cancer

The data satisfies the No Record Isolation criterion since no record is unique in the dataset.
However, looking at the first two records, this dataset reveals that all individuals born in 1946 and living in any postcode starting with 54 (and whose record was included in the dataset)
have sclerosis.
Therefore, the data could be linked to information in other datasets which contain the same individual’s sex, year of birth and generalised postcode. The fact that the datasets contain information about the same individual could, for example, be established through prior knowledge that two datasets contained information about the same individual, from information contained in either dataset which makes this link clear, or though information in a third dataset which acts as a bridging link. If this link can be established, the No Linkage criterion is violated.
64

It may still be possible to achieve linkage on records that are not fully accurate (including where records are intentionally modified, e.g., by adding noise to the data). This can often be done to a high degree of accuracy and with a likelihood of success by, for example, using

20 | Adopted

robust record linkage attacks 39 . It is therefore typically difficult to determine whether inaccuracies are sufficiently large to prevent linkage, since noisy data may leak information in unexpected ways. In addition, the effectiveness of the attack depends heavily on the availability of additional information.
65

The No Linkage criterion is likely to be met if the information has not been recorded elsewhere and is not correlated to similar information about the same individual recorded in other contexts. This criterion may be met, for example, in the case of answers given to an opinion survey, provided that they do not contain, among other things, demographic data which might be traced back to an individual. Another example of this could be records of patients’ particular physiological states, provided that, among other things, similar attribute values are collected for many patients and that the said state is likely to vary over time.

3.4.3 No Inference
66

Generally speaking, “inference” is the process of reaching a conclusion by deduction from evidence and reasoning 40 . Using this process, a relevant entity can effectively obtain information from the given data. Inferences can be drawn from both record-level and aggregate data. Inferences can also “add to” the data in a way which then reveals it as personal, even if the inferred information was not obviously contained in the dataset before the inference was made 41. Such inferences can violate the anonymity of the given data. This leads to the No Inference criterion.

67

The No Inference criterion is met if no specific and meaningful inference can be drawn from the given data. Inferences may be based on the given data and/or on additional information, including information about the anonymisation process. In particular:
-
-

An inference is specific if the inferred information relates to a single identified or identifiable individual (i.e. it is personal data); and
An inference is both specific and meaningful if the processing of the inferred information is also liable to have an effect on the data subject’s rights and interests, relies on the given data and could not be obtained from general knowledge or from data about the population at large 42.

68

This criterion should be assessed by reference to the given data, together with any external information that might be used in conjunction with the given data to infer information – including the context in which the given data was produced, and any external datasets which might be brought together with it.

69

It may often be possible to infer some personal data from given data in some way, even if the given data itself is not personal. In such cases, the inferred personal data would certainly

See, e.g., Arvind Narayanan & Vitaly Shmatikov, “Robust De-anonymization of Large Sparse Datasets” (2008) 2008 IEEE
Symposium on Security and Privacy 111, https://doi.org/10.1109/SP.2008.33; and Julien Freudiger, Reza Shokri & Jean-Pierre
Hubaux, “Evaluating the privacy risk of location-based services” in George Danezis (ed.) Financial Cryptography and Data
Security: 15th International Conference, FC 2011, Gros Islet, St Lucia, February 28 – March 4, 2011, Revised Selected Papers
(Springer 2012), https://doi.org/10.1007/978-3-642-27576-0_3.
40
See the entries “infer” and “inference” in Catherine Soanes & Angus Stevenson (eds.) Concise Oxford English Dictionary (11th edition Revised, OUP 2009).
41
In this regard, it is important to recall that, as discussed in sub-sections 2.3 and 2.4, information may be considered personal data, even if its link to an individual is not immediately apparent or if the information does not itself contain everything necessary to identify the individual to whom it relates.
42
Here, “information about the population at large” means any large group of people about whom information is not collected individually, but extrapolated from a sample, with any connection to the individuals left behind. In technical terms, such inferences can be seen as part of the “prior belief”.
39

21 | Adopted

relate to an identified or identifiable individual, but this does not then mean that the same is true for the given data. For example, when dealing with record-level data, it may be possible to infer information about an entirely new individual who was not included in the original dataset, but who has similar attributes to people that were. In such a case, the inferred information certainly relates to this new individual, but this does not itself mean that the given data does so.
70

It is, therefore, important to distinguish between two situations. In the first situation, personal data is inferred from the given data, but is not actually connected to the original dataset (i.e., the information that was used to generate the given data). This kind of inference would not lead to a violation of the No Inference criterion because the inference is not meaningful: it is obtained from information contained in the given data that is general knowledge or is about the population at large – a result of a generalisation from the original dataset represented by the given data. In the second situation, the inferred personal data is actually connected to the original dataset and is reasonably likely to have an effect on the rights and interests of the data subject. The inference, then, is meaningful because the connection to the original dataset shows that it is not obtained from general knowledge or from generalised data about the population at large, but from information about the data subject of the inferred information represented by the given data and coming from the original dataset. This kind of inference would lead to a violation of the No Inference criterion.

71

To consider that the given data actually relates to an individual, the inference should be specific and meaningful. This means that the inference will result in personal data whose processing is liable to have an effect on the data subject’s rights and interests, relies on the given data and could not be obtained from general knowledge or from data about the population at large. This can typically be shown in one of three ways:
a. Ideally, this can be done by tracing the way in which the inference is drawn.
b. If this is not possible, e.g. due to the opacity of automated processing that led to the inferred information, a lack of reliance could also be shown by comparing the outcome of inference with two versions of the given data – one which was produced from the original dataset, and one which was produced from a modified version of the original dataset and which excludes the record(s) relating to the individual. If the inference can only be drawn from the first version of the given data, it is clear that the inference relies on the records relating to the individual, and consequently that the given data relates to the individual 43.
c. If neither of these can be done, e.g. because the information has been aggregated and the original dataset has been deleted, it is also possible to rely on a rebuttal presumption that an inference did not rely on the given data by demonstrating that it

In more technical terms, the argument presented in this paragraph is as follows: Inferring means making a prediction on a property S having observed the given data A(D) and additional information, where A(D) was produced by running the anonymisation process A to the original data D and the additional information serves as a conditioning factor. Suppose that S is a property about a person named John Smith and that data relating to that person is included in D. We denote by D' a copy of the dataset D, with the only difference that all data relating to John Smith have been removed. Therefore, D' does not contain any data relating to John Smith. It may still be possible to make some inference on John Smith based on A(D'), including on property S. For example, this may be possible if the other records in D' relate to persons that are "similar" to John Smith (e.g.
because they live in the same city). However, this inference cannot depend on John Smith's data, as there is no data relating to
John Smith in D'. Therefore, if the inference on John Smith works in the same way for A(D) and A(D'), it is not an inference drawn from his data but from data relating to the population at large, for which D’ is representative.

43

22 | Adopted

could have been drawn from general knowledge or from information about the population at large 44.
Example 13: The unqualified statement “Green is a popular colour” is anonymous data since it does not relate to any identified or identifiable natural person. We could infer from this information that Connor likes the colour green. The inferred statement “Connor likes green” is clearly information related to an identified natural person and should therefore be treated as personal data. However, this inference does not mean that “Green is a popular colour” is also personal data.
While the inferred information “Connor likes green” is specific (since it relates to a single identified individual), it is not meaningful because it can (and, indeed, was) obtained from information about the population at large. This inference does not, therefore, lead to a violation of the No Inference criterion for the given data “Green is a popular colour”.
Example 14: An anonymised record-level dataset of a bank’s historical loan information shows that individuals with a particular combination of attributes are likely to fail to repay the loan. The bank uses this insight to a new loan applicant, who was never part of the dataset, and infers that this applicant has a high risk not to honour the loan obligations. This, however, is not a meaningful inference in the sense defined above, and hence the dataset could still satisfy the No Inference criterion.
72

Importantly, inferences which, on first review, do not appear to be specific and meaningful may still be helpful for (re-) identification and should be further analysed in conjunction with the given data. It may, for example, be that the given data, together with the inferred information, can lead to further inferences that would actually be specific and meaningful, and therefore violate the No Inference criterion.

73

There is a wide spectrum of processes that can lead to relevant inferences. On one end are conclusions reached by simply thinking logically about the data, on the other are those reached by elaborate analyses or the use of automated processing which follows sophisticated algorithms. Some forms of inference may be easier, or more relevant, for record-level data, while others may be particularly good at extracting information from aggregate data. The following sub-sections will discuss and provide examples for some of these processes.
However, any given inference may aid re-identification in more than one way and the below should not be taken as an exhaustive list.
Adding an inferred attribute to a given record

74

It may be possible to add inferred information to record-level data in a way which then leads to a violation of the No Inference criterion. This inferred information does not have to be appended to the record– it is enough that it is possible to attach it to the record.
Example 15: A controller receives precise location data about users of a mobile app, removes all direct identifiers and collates them into 24-hour tracks for each user. The controller would like to assess whether those tracks constitute anonymous data. The tracks show that,

In such a case, “Prior belief” (see footnote 40) could include knowledge coming from an alternative version of the given data which has been produced without the record of the persons that are being identified – A(D’) in footnote 41 – but which still applies to them and other persons by way of extrapolation. Inferences from the given data should yield a significantly different “posterior belief” (on which an action could turn) to be considered related to the individual in a way that classifies the given data as personal.

44

23 | Adopted
