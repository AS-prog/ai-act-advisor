---
name: cepd-directrices-02-2026-anonimizacion-v1-05-3-the-technical-analysis-of-anonymisatio
description: "CEPD: cepd directrices 02 2026 anonimizacion v1, sección «3  The technical analysis of anonymisation (parte 2)» (págs. 25-31). Documento de 2026-07-07, idioma en."
metadata:
  type: reference
  documento: cepd-directrices-02-2026-anonimizacion-v1
  emisor: CEPD
  fecha: 2026-07-07
  idioma: en
  seccion: "3  The technical analysis of anonymisation (parte 2)"
  paginas: 25-31
  origen: 2026-07-07-cepd-directrices-02-2026-anonimizacion-v1-en.pdf
  oficial: false
---
# 3  The technical analysis of anonymisation (parte 2)

every weekday, a single user is present in a particular residential building from 0:00 to 08:00 and 20:00 to 24:00, and at a particular commercial building from 09:00 to 17:00. This information allows a meaningful and specific inference of the user’s home and work addresses, which could then be added to that user’s record.
75

Simply because you might be able to add inferred information to a record does not necessarily mean that the No Inference criterion is violated. It will almost always be possible to find inferred information that can be added, either by analysing the data or simply by applying general facts to it. It is, therefore, important to consider the nature of the inferred information and whether it is meaningful and specific, as set out above.
Producing record-level data from aggregate data

76

It may be possible to infer record-level data by analysing and/or combining aggregate data.
This is particularly true for outlier data, where this kind of inference is often more likely.
Example 16: A company decides to publish information about the total salaries that it pays to each category of employees. The information states that engineers in the company receive an aggregate of €550,000 a year but does not specify how much is paid to each engineer.
However, the company’s internal reporting also states that the company employs a total of six engineers, that the Product Engineering team is made up of five engineers (and does not contain any other employees) and that the Product Engineering team has an annual salary expense of €480,000. Although both reports are limited to aggregate data, an entity with all of this information can infer that the sixth engineer is paid €70,000 a year.

77

This form of inference can also be significantly more sophisticated. It may, for example, start from large sets of aggregate statistics accessible in bulk, or from data query systems. Often, this kind of inference will use multiple aggregated datasets, especially if those sets were all produced from the same original data. This is particularly true for advanced de-aggregation techniques, including attacks which can extract data from supposedly-anonymous AI models 45. Nevertheless, a single dataset which contains a sufficiently large quantity of data may allow for the inference of information relating to a single individual, without the need for other sources.

78

Inferences can also be drawn from the absence of a value.
Example 17: A company organises a survey where each team can “anonymously” provide their views on the line manager. The survey includes questions like: “From 1 to 5, to what extent does the company culture encourage you to make and learn from mistakes?” The individual responses are not shared with the line managers, who are only told the total number of their team members that selected each answer. However, if a line manager is told that all of their team members took part in in the survey and none of the answers gave a score higher than 3, that manager can infer that all team members have a critical view of the company culture. Although it is aggregated, this information still relates to each member of the team individually.

See also EDPB: Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models.

45

24 | Adopted

Membership inference
79

It may be possible to infer that an individual’s data was included in the original dataset which was then used to produce the given data. This type of membership inference may be the first step for other types of inferences or may itself reveal information about the individual.
Example 18: A supposedly anonymous dataset is generated from information about members of a rowing club. However, by analysing certain attributes contained in the given data, it is possible to infer that Alex was included in the original dataset and so is a member of that club.
Inferred linkage to additional information

80

Linkage with other data, such as that discussed in section 3.4.2, can also be seen as a form of inference. By linking the given data to additional information, it is possible to infer that information contained in the given data can be applied to the additional information and vice versa. This kind of inference can also go beyond the type of linkage described in the No
Linkage criterion. For example, if information cannot be matched on a 1:1 basis between datasets, but the additional information could be matched to several possible entries in the given data, it may still be possible to draw relevant inferences. This is particularly the case where one attribute value occurs in an overwhelming number of matching records.

81

Further, while the No Linkage criterion referred to record-level data in particular, this kind of inference also applies to aggregate data.
Example 19: The data from Example 12 is aggregated to create a histogram of diagnoses grouped by combination of sex, year of birth and abbreviated postcode. Despite the aggregation, it is still possible to infer an individual’s diagnosis by linking this histogram to (a)
data about the individual’s sex, year of birth, and generalised postcode; and (b) data that the individual’s record was included in the dataset.

82

This kind of inference could also be drawn from data that has been aggregated to represent correlations between elements of the original information, rather than that information itself.
This would, in particular, be the case for AI models or synthetic data. Specific inferences can be made by querying (or, in the case of AI models, prompting) the given data with additional information to elicit new information about a particular individual. Where such an inference is also meaningful, this would be a violation of the No Inference criterion.

3.5 Applying the criteria
3.5.1 Assessing the effectiveness of (re-)identification techniques
83

The three criteria set out above should be used to evaluate the effectiveness of (re-)
identification techniques that can be deployed against the given data. These techniques range from the very simple, like using a basic search in other datasets for matching attributes, to the very complex, like using special-purpose AI agents to deploy a sophisticated combination of probabilistic techniques. Depending on the technique, these could be used intentionally or unintentionally, and may be tailored to exploit potential vulnerabilities that arise from specific contexts or specific flaws in the applied anonymisation methods.

25 | Adopted

84

The state of the art for such techniques is always evolving and should be considered during this assessment. The EDPB therefore encourages the development, dissemination and application of scientifically grounded expertise on this topic. Such expertise will become increasingly important as the complexity of the (re-) identification methods grows and/or the risk of their successful deployment rises.

85

Although a comprehensive list is not possible, several key factors will typically be relevant when assessing the effectiveness of these techniques:
-
-
-
-
-
-

Whether the data is aggregated or at record-level;
The dimensionality of the data. This refers to the amount of information that is available on each individual (e.g. the number of columns in a table for each individual record);
The resolution of the data. This refers to the level of detail in the recorded attributes
(e.g. a full date of birth has a higher resolution than the year of birth alone);
The diversity of the data. This refers to the amount of differences between the data
(e.g. if many individuals share the same attribute values, the data has a low diversity);
The number of individuals whose data is included in the record; and
The amount of additional information that is available for combination with the data.

86

As a rule of thumb, (re-) identification techniques are more likely to be effective against recordlevel data with high dimensionality and high resolution. By contrast, many (re-)identification techniques are less likely to be effective against data which is aggregated through mathematical functions into statistical indicators (e.g. averages), although this can depend on the amount of data which is aggregated. These key factors are also typically interdependent.
For example, the amount of additional information which is necessary for a (re-)identification technique to be effective may be much lower for record-level data than it would be for aggregate data.

87

The effectiveness of a (re-) identification technique should be assessed on its ability to generate accurate results. This does not necessarily require perfect accuracy or absolute certainty; rather, the result should be at least sufficiently close, and provide at least a sufficiently high confidence in the circumstances at hand, to allow the data subjects to be distinguished and treated differently. Further, a (re-)identification technique can be successful even if it only succeeds against a single individual in a larger dataset 46.
Example 20: An entity uses a dataset with information about all of the employees in a big organisation to infer, with reasonable precision, the salary of the employees. However, the inference is only successful for one employee with a significant confidence and the entity has no way, other than guessing, to tell whose salary was correctly inferred. Since this technique cannot, with sufficiently high confidence, lead to the identification of the individual, it is not sufficiently effective and its use does not violate the No Inference criterion.

3.5.2 Assessing the criteria under the contextual approach
88

When using the contextual approach, it is important to recognise that the capabilities of different entities may vary over time. For example, a data leak could provide certain entities with access to new datasets which were previously unavailable to them. This would, in turn, allow those entities to link information with means which were, at least from that entity’s perspective, previously unavailable but are now reasonably likely to be used, leading to a
46

See paragraph 36.

26 | Adopted

violation of the No Linkage criterion. To ensure the proper protection of data subjects, the
EDPB therefore recommends that analyses carried out under the contextual approach should incorporate, as much as possible, adequate safety margins ensuring that the assessment remains robust as the entities’ capabilities evolve.
89

Another important consideration under the contextual approach is the accessibility of data. If data is publicly available, anybody may be able to access it with means reasonably likely to be used. If the data is subject to appropriate security controls (particularly regarding the confidentiality of the data), access to the data will constitute a mean reasonably likely to be used only for the authorised users (and not for unauthorised actors).This is relevant for both the given data itself and for any necessary additional information that might be used as part of linkage or inference.
Example 21: Returning to Example 16, the company’s internal report is a necessary part of inferring the sixth engineer’s salary. When applying the contextual approach, it is therefore important to test if each relevant entity has access to that report with means reasonably likely to be used. If that internal reporting is public, it should be assumed that everyone can access it and that the No Inference criterion is violated from everyone’s perspective. If, however, access to that internal report is limited, and assuming that there is no other way to get this extra information, the No Inference criterion will only be violated from those perspectives who actually have access to it.

90

Limits to access should be assessed holistically, taking into account the capabilities of the different entities and any contextual elements which may have a greater or lesser effect on the means they are likely to use. Technical, organisational and contractual measures can help to restrict access, but are not by themselves sufficient to make data anonymous; while controllers are encouraged to adopt these measures wherever appropriate, they should still examine the (re-)identification capabilities of anyone who might be able to access the data with means reasonably likely to be used.

91

Appropriately implemented encryption may be used to limit access to data (or, at least, limits access to a form of the data which is intelligible) and, in this way, can help to support successful anonymisation. Nevertheless, encryption is, by its very nature, intended to be reversible and differs from anonymisation. It is, therefore, important to assess if entities with access to the data could still decrypt it with means reasonably likely to be used, even if they do not currently have the decryption key (e.g. through cryptanalysis).

92

Most currently documented (re-) identification techniques are becoming increasingly accessible, require limited resources and can be performed within a reasonable timeframe, even on commodity hardware. This is especially the case for the re-identification of recordlevel data. Some techniques which work on aggregate data may require larger computational resources, but access to such resources is still possible as a service, at relatively accessible costs. Time and cost would not generally be prohibitive for running these existing techniques, although they may pose challenges for (e.g.) obtaining the additional information necessary to use that technique successfully. The EDPB also notes that developments in AI, and especially agentic AI, will likely further reduce the time and costs necessary to access and deploy these techniques.

93

The effect of time and cost on the means reasonably likely to be used may, therefore, be particular seen where additional information which is necessary for (re-) identification is spread across multiple places or entities, or is hard to locate or access. However, the EDPB again notes that developments in AI may also reduce the time associated with gathering and

27 | Adopted

combining information from multiple sources (at least in cases where those sources are publicly available), which may lead to significant increases in the means reasonably likely to be used.
94

The following example is a high-level illustration of how one might assess the No Linkage criterion using the contextual approach.
Example 22: The research institute described in Example 12 decides to use the contextual approach to evaluate the anonymity of the data contained in the table after deleting the original personal data.
The research institute starts by identifying anybody who might, through means reasonably likely to be used, be able to access the table itself. The table has not been publicly released, and the research institute currently employs strong state-of-the-art cybersecurity measures, as well as other technical means to restrict unauthorised access to this dataset and prevent its members from creating any copies. Out of caution, the research institute considers that, especially over a long period of time, it is possible that the data will nevertheless leak. This could include, among other things, leaks due to human error or hacking attempts from external actors. The research institute therefore concludes that the table is accessible, through means reasonably likely to be used, by, at least:
1.

members of the research institute who have been granted access to the table,

2.

individuals who might accidentally receive the data due to human error,

3.

individuals who might hack into the system and steal and distribute the data,

4.

government or judicial authorities that might access the data in the course of the fulfilment of their public duties, and

5.

other entities who might obtain the given data from someone in one of the above four groups.

However, the research institution concludes that it is extremely unlikely that people who are familiar with the data subjects’ personal lives would receive the data in the aftermath of a leak, which already is not very likely to occur. The same conclusion applies to all other people who would know about an individual’s participation in activities that lead to the inclusion of data relating to them in the given data. Therefore, the research institution concludes that these people would not qualify as relevant entity.
The research institution then considers whether the means available to each relevant entity are reasonably likely to be used, using objective factors as set out in paragraph 29 above.
It has already been concluded that the data can be linked to other data relating to the same individuals by any entity who knows (a) the individual’s sex, year of birth and generalised postcode, and (b) that the individual was included in the given data. While this information may be known by, for example, the individuals’ close friends and family members, nobody who knows about the inclusion of an individual in the given data are among the relevant entities. This includes the members of the research institute, since its members had no direct interaction with the patients and were not involved in their treatment, and there is no record of which patients were included in the dataset.
In conclusion, no relevant entity would know that a certain individual’s data was included in the dataset. Moreover, it is not possible to derive from the dataset itself that a certain individual’s data was included in the dataset. These considerations depend on the specific context of the given case and need to be underpinned by careful reasoning. However, in this

28 | Adopted

instance, the research institute is able to conclude that no relevant entity is likely to have access to the additional information that can be linked to the given data and that the No
Linkage criterion has been met.

3.5.3 Compiling the results
95

If the given data fulfil all three criteria under either the simplified or contextual approaches, they can be presumed anonymous. If, however, one or more criteria is violated, further analysis may be needed to see if the information should be considered as personal data.

96

If the data is found to be personal under the simplified approach, it is also possible to perform a further assessment through the contextual approach. If none of the three criteria are violated from the relevant perspective, then the information can still be considered anonymous from that perspective. In some cases, this finding of anonymity may be limited to the perspective of only one entity, while in others it may extend to all of the relevant entities. As previously stated, the goal of anonymisation should be to ensure that the resulting data is anonymous for all of the relevant entities.

97

This is shown in the following table:

No Record
Isolation

No Linkage

No
Inference

98

Criterion is satisfied under either approach

Criterion is violated under simplified approach

Criterion is violated under contextual approach

The data can be considered anonymous if the other two criteria are also passed.

The data may not be anonymous. See paras.
98 to 00 below.

The data may not be anonymous from at least one of the relevant perspectives.
See paras. 98 to 100 below.

The data can be considered anonymous if the other two criteria are also passed.

The data may not be anonymous. See paras.
101 to 103 below.

The data can be considered anonymous if the other two criteria are also passed.

The data should not be considered anonymous under the simplified approach, consider continuing to the contextual approach.

To reach a conclusive result, consider continuing to the contextual approach.

To reach a conclusive result, consider continuing to the contextual approach.

The data may not be anonymous from at least one of the relevant perspectives.
See paras. 101 to 103 below.

The data should not be considered anonymous from at least one of the relevant perspectives.

If the data violates the No Record Isolation criterion, it should be checked if the isolated records allow for singling out, so that individuals are distinguished from others by matching those records with the individual’s corresponding attributes. These corresponding attributes could,
29 | Adopted

for example, become apparent to the relevant entity in the course of their interactions with the individual, or may be available through additional information that allows for the individual to be identified 47. The larger the isolated record and the more attributes it contains, the easier the singling out of the individuals becomes. If the individual can be singled out in this way, then they should be considered identifiable.
Example 23: Returning to the dataset from Example 10 although the dataset violated the No
Record Isolation criterion in several places, this does not necessarily mean that the individuals can be identified by isolating their records. However, in this case it is very likely: The records are unique, and their values are likely to be unique for most individuals in this population.
Further, the information needed to identify the individuals by reference to the demographic attributes may be available through means reasonably likely to be used (e.g. through public registers). If this is possible, the given data would be personal.
99

If this singling out cannot be done – and the other two criteria have been successfully met – then the given data can still be considered anonymous, despite failing the No Record Isolation criterion. This could happen if, among other things, the record is unique (and so the No Record
Isolation criterion is failed) but the attributes cannot be matched to any other data available to the relevant entity or if the unique record is not intelligible.
Example 24: A cinema decides to run a study to better understand its clients’ preferences.
The survey is answered by a very large number of customers, and only contains questions related to the movie itself, that were written specifically for this survey and that do not reveal anything that can be reasonably linked back to the respondent. The responses are then collected in a secret ballot, and later turned into a dataset:
Survey Question 1 number

Question 2

...

Question 30

1

D

C

…

B

2

C

A

...

A

3

…

…

…

...

Because of the large number of questions, it is very likely that at least some (if not all) records are unique in the dataset, violating the No Record Isolation criterion. However, this does not mean that participants can be identified. In fact, given the circumstances, there is no way to link the answers to their identity or to other information relating to them using means reasonably likely to be used, nor to treat any respondent differently based on their individual answers. If the data passes the other two criteria, it is, therefore, anonymous, despite failing the No Records Isolation criterion.
100 If this singling out can be done, the information should not be considered anonymous.
However, if the analysis has progressed under the simplified approach (i.e. testing whether an entity can single out an individual on the basis of the given data, while assuming that if means reasonably likely to be used exist then at least someone will be able to use them), this

See, for example, C-479/22 P OC v European Commission, paras. 60 & 63, where the CJEU looked at a unique combination of attribute values which could then be compared against the corresponding attributes available online.

47

30 | Adopted
