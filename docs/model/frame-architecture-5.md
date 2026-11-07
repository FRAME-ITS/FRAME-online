---
version: 5.2
repository_url: ../uml_models/frame_repository/index.htm
metamodel_url: ../uml_models/frame_metamodel/index.htm
---

# FRAME Architecture version 5

!!! info "important"

    This is the current version of FRAME using enterprise architect.

## FRAME Tool

Following section contain versions of the FRAME Tool for download. The Tool is an Enterprise Architect Model, with the __FRAME repository__ (1), __FRAME Meta model__ (2), and selected __Reference Architectures__. 
{ .annotate }

1.	FRAME repository is a library of User Needs and functions, which are grouped into several Functional Areas covering whole ITS. The repository is used in first phases of creation of the specific architectures, when an architect selects based on the stakeholders aspirations a user needs fulfilling those aspirations and leading to a specific functionality.

2.	FRAME meta model defines objects used by updated FRAME. The meta-model has a different structuring than the final views of the architecture, it structures the FRAME artefacts into five sections. The first four sections develop from a high-level perspective down to more technical details of the service. The last layer contains artefacts, which are relevant for all sections. 

	The sections are __Motivational Layer__, __Business Layer__, __Application Layer__, __Data Layer__ and __External__

!!! note "Release 5.3 in preparation"

	Release 5.3 corrects the relationships of the FRAME Repository, includes the FRAME technology (toolbox) V1.3 in the model and comes with an updated User Guide and Installation Guide. Progress: [pull request #95](https://github.com/FRAME-ITS/FRAME/pull/95).

### FRAME_Architecture Tool V5.2 (rel. 21.01.2025)

??? notes "contents and changelog"

	FRAME_Architecture Tool V5.2 contains the FRAME Meta-model, the FRAME Repository and the NAP, National Body, eCall, Safe and Secure Truck Parking and C-ITS Reference Architectures.

	Changes to V5.2: NAP Reference Architecture extended with the results of NAPCORE; National Body Reference Architecture added; NAP data flows of the FRAME Repository aligned with it; definitions of the Meta-model revised; Safety & Security package (PASSPORT) added. Full list of changes: see the release.

#### Download

 - download [**full FRAME tool** in qea format](https://github.com/FRAME-ITS/FRAME/releases/download/v5.2.0/FRAME_Architecture_Tool_V5.2.qea.zip) (Enterprise Architect 16 or later) – [release v5.2.0](https://github.com/FRAME-ITS/FRAME/releases/tag/v5.2.0)

### FRAME_Architecture Tool V5.1.1 (rel. 05.10.2021)

??? notes "contents and changelog"

	FRAME_Architecture Tool V5.1.1 contains the following packages: FRAME Meta-model, FRAME Repository, NAP Reference Architecture and eCall Reference Architecture, Safe and Secure Truck parking Reference Architecture, and C-ITS Reference Architecture.

	Changes to V5.1.1 are: Addition of Safe and Secure Truck parking Reference Architecture, and C-ITS Reference Architecture.

#### Full tool downloads

 - all files of this version are attached to the [GitHub release v5.1.1](https://github.com/FRAME-ITS/FRAME/releases/tag/v5.1.1)
 - download [**full FRAME tool** in eapx format](https://github.com/FRAME-ITS/FRAME/releases/download/v5.1.1/FRAME_Architecture_Tool_V5.1.1.eapx.zip),  (enterprise architect <16), [quea format](https://github.com/FRAME-ITS/FRAME/releases/download/v5.1.1/FRAME_Architecture_Tool_V5.1.1.qea.zip) (enterprise architect >16) or in [xmi format](https://github.com/FRAME-ITS/FRAME/releases/download/v5.1.1/FRAME_Architecture_Tool_V5.1.1.xmi.zip) (exchange)
 
#### Partial downloads
 
 - the model packages (meta-model, repository, reference architectures) as separate XML files: [releases/5.1.1](https://github.com/FRAME-ITS/FRAME/tree/master/releases/5.1.1)

<div class="grid cards" markdown>

- :fontawesome-brands-markdown: Explore structure of __FRAME Meta model__ [:octicons-arrow-right-24:]({{page.meta.metamodel_url}})
- :material-format-font: Browse content of __FRAME Repository__ [:octicons-arrow-right-24:]({{page.meta.repository_url}})

</div>


## FRAME Toolbox

The Toolbox is an Enterprise Architect MDG technology, allowing modelling with FRAME specific objects. It contains the stereotypes, scripts, functionalities and objects which are used in FRAME. Releases 5.1.1 and 5.2 need Toolbox V1.0 for new projects; from release 5.3 the toolbox (V1.3) is included in the model and is also published with the release.

### FRAME Toolbox V1.0 (rel. 23.09.2020)

??? notes "contents and changelog"

	Contains xml files defining object types used for modelling architecture and reporting templates.
	
	Changes to V1.0: final version as of 2021 (end of project FRAME-NEXT).

#### Toolbox downloads

 - download [**FRAME toolbox** in xml format](https://github.com/FRAME-ITS/FRAME/releases/download/v5.1.1/FRAME_Toolbox_V1.0.zip)
 