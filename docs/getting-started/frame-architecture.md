# FRAME Architecture

The FRAME Architecture (originally called the European ITS Framework Architecture) was developed as a result of recommendations from the High Level Group on transport telematics, which were supported by a resolution of the Council of Ministers. It was created and first published by the EC funded project KAREN in October 2000. The underlying aim of this initiative was to promote the deployment of (mainly road-based) ITS in Europe by producing a framework which would provide a systematic basis for planning ITS implementations, facilitate their integration when multiple systems were to be deployed, and help to ensure inter-operability, including across European borders.

A distinctive feature of the FRAME Architecture is that it is designed to have sub-sets created from it, and is thus unlikely to be used in its entirety. Indeed, on occasions, it contains more than one way of performing a service and the user can select the most appropriate set of functionality to deliver it in that environment. Thus the FRAME Architecture is not so much a model of integrated ITS, as a framework from which specific models of integrated ITS can be created in a systematic and common manner.

## Framework principle

The FRAME Architecture achieves its aim by providing a model of almost all of ITS from which specific sub-sets of integrated ITS can be created in a systematic and common manner. It covers most ITS applications and services that are currently being used, or being considered for implementation, in Europe, and it does not impose any technical or organisational assumptions on the way things are done.

It therefore provides ITS engineers with a common approach, or “language”, for use throughout the EU.

Because the FRAME Architecture is intended for use within the European Union it conforms to the precepts of subsidiarity, and thus does not mandate any physical view or organisational structure on a Member State. It therefore consists of only a set of User Needs for ITS, and a Functional View that satisfies them; the remainder of the views are created when required. Thus the FRAME Architecture is “neutral” and makes no assumptions about the way things are done.

## Views of an ITS architecture

The FRAME Architecture is intended to be used within a top down approach to the planning and deployment of integrated ITS.  The overall concept may, or may not, be represented in a formal (reference) model.  Since the creation of a reference model requires a number of decisions or choices to have been taken by those implementing and/or regulating ITS, the FRAME Architecture does not provide one.

The overall concept and the system structure should be described in a technology independent way so that, as technology evolves, all the higher level requirements remain unchanged.  The information contained within the system structure enables the ITS industry to produce the equipment and systems that will provide the services wanted by the stakeholders, each with their own distinctive features, but conforming to the purposes expressed in the overall concept and system structure.  Thus integrated and/or inter-operable ITS services can be provided across the EU.

![image](../assets/img/Architecture-Layers-Stds-n-800x486-1.png)
![image](../assets/img/Example-Physical-Viewpoint-n-800x491-1.png)

An ITS architecture created with FRAME (version 5) describes the service in the following views. Each view builds on the previous ones; the FRAME Meta-model defines their building blocks and the relationships between them.

| View | What it describes | Main building blocks |
|---|---|---|
| **Motivation layer** | why the service is needed: the stakeholders, their expectations, the vision and mission, the added value of the ITS service | Stakeholder, Business Expectation, ITS Vision, Mission Statement, ITS Service, ITS Service Added Value, Requirement |
| **Functional view** | what the system has to do: chains of functions connected by data flows, with terminators at both ends; derived from the selected User Needs | User Need, Function, Data Flow, Data Store, Terminator |
| **Organisational view** | who is involved: actors, the roles they perform, the agreements between the roles, business processes | Actor, Role, Agreement, Business Process |
| **Physical view** | how the functions are allocated to sub-systems and modules, and which physical data flows connect them; always based on a consistent functional view | Sub-system, Module, Physical Data Flow, Interface |
| **Communications view** | how the sub-systems and modules exchange data: protocols, data formats, interfaces | Interface, Specification |
| **Safety and security view** | hazards that can cause physical harm, and threats to confidentiality, integrity and availability | Safety and security analysis (PASSPORT) |

The content of the physical and communications views can be used in calls for tender, so that the components and communications can be procured; the organisational view helps to put the right management structure, rules and agreements in place. How the views are built step by step is described in [Methodology](user-guide.md) and, for a complete example, in the [Reference Architectures](../model/reference-architectures.md).

## The FRAME model

The FRAME model used for the Functional View is based on hierarchical Data Flow Diagrams. At the highest level is the Context Diagram (see figure below) which shows all the functionality supported by the FRAME Architecture inside a box labelled “System” surrounded by a set of “Terminators”, which are outside the boundary of the system. Each Terminator represents some thing, or person, to which the system will send data and/or from which it will receive data. As there is a large amount of functionality in the FRAME Architecture (2-3000 elements in total), its size is managed using hierarchies of functions and terminators.

![FRAME Context Diagram](../assets/img/FRAME-Context-Diagram-n-1024x732.png)

The FRAME System in the figure above is divided into 9 Areas (see below). Each Area then has a number of hierarchical levels of functions as required, with each High-Level Function being decomposed into a number of lower-level Functions until the final Low-Level Functions are reached. Initially it was thought that the High-Level Functions would be used during the sub-set creation process, but it was quickly found that, whilst many of the corresponding Low-Level Functions were required in a given situation, not all them were. That, and the difficulty of following data flows through the hierarchy of functions, has resulted in the High-Level Functions being used solely for convenience when creating or looking at the entire FRAME Architecture. Thus the FRAME Architecture Functional View is now defined with its Low-Level Functions, and the creation of sub-sets is performed using only them.

The name “Terminator” derives from the fact that the data for, and produced by, the System starts/stops there. The FRAME Architecture sub-divides some of its Terminators into a number of Actors. Not only does this make the total architecture more manageable, especially the construction of the diagrams, but it is also useful for situations when some data goes to/from all Actors in the Terminator, e.g. all Drivers, and on other occasions data goes to/from a specific Actor, e.g. Public Transport Driver.

## Functional areas

The FRAME Architecture models road based ITS applications and services, and is divided into the following nine broad Areas:

 - Provide Electronic Payment Facilities
 - Provide Safety and Emergency Facilities – includes both in-vehicle and roadside “eCall” plus the management of the Emergency Services responses
 - Manage Traffic – includes urban and inter-urban traffic management, plus parking, incident and demand management
 - Manage Public Transport Operations – includes both regular and on-demand services, plus fare cards and vehicle sharing
 - Provide Advanced Driving Assistance Systems – includes support for in-vehicle services some of which are part of cooperative systems
 - Provide Traveller Journey Assistance – includes both pre- and on-trip planning, plus traveller information
 - Provide Support for Law Enforcement
 - Manage Freight and Fleet Operations
 - Provide Support for Cooperative Systems – includes support for cooperative systems not included elsewhere

Links to other modes of transport are made through the Terminator “Multi-Modal System”, which is used to provide travellers with multi-modal travel information, to manage multi-modal crossings and incidents that take place on other modes.

## Use of FRAME in Europe

![Use of FRAME in Europe](../assets/img/Rys.-12-01-1024x625-1.png)
![FRAME Use World Wide](../assets/img/mapa-world-new-1024x605-1.png)

The maps show the use of FRAME up to the end of the FRAME-NEXT project.
