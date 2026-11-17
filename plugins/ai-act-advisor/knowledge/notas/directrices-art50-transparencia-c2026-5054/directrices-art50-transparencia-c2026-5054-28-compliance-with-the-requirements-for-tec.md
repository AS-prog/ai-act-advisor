---
name: directrices-art50-transparencia-c2026-5054-28-compliance-with-the-requirements-for-tec
description: "Comisión Europea: directrices art50 transparencia c2026 5054, sección «Compliance with the requirements for technical solutions: effective, interoperable, robust and reliable» (págs. 26-28). Documento de 2026-07-20, idioma en."
metadata:
  type: reference
  documento: directrices-art50-transparencia-c2026-5054
  emisor: Comisión Europea
  fecha: 2026-07-20
  idioma: en
  seccion: "Compliance with the requirements for technical solutions: effective, interoperable, robust and reliable"
  paginas: 26-28
  origen: 2026-07-20-directrices-art50-transparencia-c2026-5054-en.pdf
  oficial: false
---
# Compliance with the requirements for technical solutions: effective, interoperable, robust and reliable

level of the underlying AI model or integrated in the AI system’s inference process).
They may rely on the marking solution implemented by an upstream model provider or a third party providing the solution (e.g. as an open standard or a specialised service) to the extent that the marking solution is compliant with Article 50(2) AI Act. Such reliance is without prejudice to the responsibility of the provider of the AI system to demonstrate compliance with Article 50(2) AI Act.
4.2.2. The detection obligation
(75) Providers of AI systems falling within scope of Article 50(2) AI Act must ensure that the output of their systems are detectable as AI-generated or manipulated content. This means that the provider is obliged to ensure that the means of detection are available to the persons potentially exposed to the content. Furthermore, pursuant to Article 50(5)
AI Act, such detection solutions should be able to produce human-readable results indicating whether the content has been AI-generated or manipulated.
(76) A detection tool is a mechanism that detects whether content has been AI-generated or manipulated, typically identifying technical markers or signatures that verify its origin.
To ensure full interoperability, providers must rely on publicly-available industry standard detection solutions that allow any third party to implement detection that is ideally locally executable on the digital device and allow seamless integration into selfcontained, isolated networks. Where such standards are not available, in particular at the initial stage of the implementation of Article 50(2) AI Act for watermarking technologies, the provider may rely on its own detection solution or on a third party or shared detection solution, so long as those solutions ensure interoperability with the detection solutions used by other providers (see Section 4.2.3.). That possibility should be limited in time until harmonised standards and a standardised provider-agnostic interoperable detection solution emerge that is secure, privacy-preserving and locally executable.
(77) Article 50(5) AI Act further specifies that the information referred to under Article 50(2)
AI Act should be provided to the natural persons exposed to the content in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. This information is notably the result of the detection, which indicates whether content is AIgenerated or manipulated and not the AI-generated or manipulated content itself. ‘At the time of first exposure’ should be understood as the moment at which natural persons are willing to verify the origin of a specific piece of content and access the detection solution to obtain the detection results.
(78) If the provider of the AI system depends on another actor for the provision or access to a detection solution, it must ensure that the detection solution complies with Article 50(2)
and (5) AI Act and that those actors display the detection results in compliance with
Article 50(5) AI Act (see Section 7).
4.2.3. Compliance with the requirements for technical solutions: effective, interoperable, robust and reliable
(79) The second sentence of Article 50(2) AI Act provides that the technical solutions for marking and detection must be effective, interoperable, robust and reliable. These requirements should be understood as follows:
25

-

Effectiveness refers to the capability of the technical solution implemented by providers to detect their marks and enable natural persons to distinguish artificially generated or manipulated content produced by their AI system, and thus contribute to the trust and integrity of the information ecosystem.

-

Reliability refers to the capability of the technical solution to accurately identify and distinguish AI-generated or manipulated content from other content in nominal conditions across the variety of content generated or manipulated by the provider´s
AI system.

-

Robustness refers to the capability of the technical solution to accurately identify and distinguish AI-generated or manipulated content produced by the provider’s AI system from other content under varying conditions, covering both common alterations and adversarial attacks.

-

Interoperability refers to the capability of the different technical solutions for marking and detection to operate seamlessly across multiple systems, actors, contexts and technical implementations to enable detection of AI-generated or manipulated content, regardless of the marking technique(s) deployed by providers of different AI systems.

(80) Providers must ensure that the combination of the technical solutions for marking and detection holistically meet all aforementioned requirements to the legally required degree, taking into account the limitations and the complementarities of the various solutions deployed. The technical solutions must comply with all requirements insofar as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation, and the generally acknowledged state of the art, as may be reflected in relevant technical standards.
(81) ‘Technically feasible’ solutions within the meaning of Article 50(2) AI Act are solutions that are capable of being implemented for the modalities covered in the scope of the provision, using currently available technology, methods, and engineering practices, within the specific technical architecture and operational environment concerned. The provider is not obliged to make use of a technical solution that is not yet developed or available on the market, or that is technically unfeasible for implementation. Technical feasibility is an objective notion that is not dependent on the specific resources and capabilities of individual providers.
(82) Article 50(2) AI Act requires providers to implement technically feasible solution(s) that align with the generally acknowledged state of the art, in order to meet the four quality requirements of effectiveness, robustness, reliability and interoperability.
(83) The ‘state of the art’ is to be understood as a developed stage of technical capability at a given time as regards products, processes and services, based on the relevant consolidated findings of science, technology and experience and which is accepted as good practice in technology (28). The state of the art does not necessarily imply the latest scientific research still in an experimental stage or with insufficient technological

(28) See Annex II of Commission Implementing Decision C(2025) 3871 final on a standardisation request to the
European Committee for Standardisation and the European Committee for Electrotechnical Standardisation as regards high-risk AI system in support of Regulation (EU) 2024/1689 of the European Parliament and of the Council and repealing Implementing Decision C(2023)3215 final.
26

maturity. Providers must continuously adapt their marking and detection solutions in a timely and proportionate manner as the technology and state of the art evolves.
(84) In light of Article 50(7) AI Act, providers may rely on a code of practice, assessed as adequate pursuant to that provision to demonstrate compliance with the marking and detection obligations in Article 50(2) and (5) AI Act, which is aligned with the state of the art. For further information regarding the effects of adherence to such a code and the supervision of other providers who do not adhere to a code, see Section 8.1 below.
(85) The costs of implementation of certain technical solutions for marking and detection can also be taken into account. In certain cases, as described in the following points, the costs may be disproportionate to marginal gains with more limited value for enabling humans to distinguish AI-generated or manipulated content, and ensuring the integrity and trust in the information ecosystem.
(86) There may therefore be narrowly defined cases where a technical solution based on less robust metadata markings is sufficient for the purpose of complying with Article 50(2)
AI Act, taking into account the specificities of the AI system’s outputs if they pose inherently lower risks of deception, manipulation or negative effects on the information ecosystem. This is specifically the case where a generative AI system is embedded in physical products generating outputs in a technically controlled and closed environment that is mainly instructive in nature (e.g., an AI system embedded in navigation systems in vehicles) to the extent effective technical measures are embedded in the product to prevent the output from leaving the product environment, for example by being captured or exported and disseminated externally.
(87) There may also be limited cases of “industrial AI applications” or “business to business applications” (excluding public and consumer-facing AI systems) where the proportionality principle and the limited benefits for the transparency objectives means that no marking and detection of AI-generated or manipulated outputs is required. This applies only if the following requirements are met cumulatively:
i. The AI system’s generated output is strictly technical in nature, for example engineering designs, industrial production workflows, technical instructions, output generated as a result of predictive system maintenance processes in industrial settings, internal documentation processes or production steps and workflows before the output is finalised and made available to other external persons or the public.
ii. The AI system’s generated output is only intended to be perceived and processed by a limited pre-defined number of natural persons acting in a professional capacity within the organisation of the provider and the deployer.
iii. The AI system’s generated output must not be intended to be shared outside the company or to be usable by external persons, with appropriate safeguards in place to avoid reasonably foreseeable misuse (e.g. cloud isolation, role-based controls).
(88) Real-time content generation that is ephemeral and consumed immediately, without being recorded, stored or disseminated further (e.g. in video games, virtual reality applications), may also be exempted when marking is not technically feasible and the persons exposed to the content are made aware that the content is AI-generated or manipulated (e.g. inexperience disclosure, session-level notifications).

27
