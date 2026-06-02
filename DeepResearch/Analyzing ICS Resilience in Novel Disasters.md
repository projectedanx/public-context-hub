# **Cognitive Decision Structures in Fireground Command: Black Swan Diagnostics & Emergency Control Resilience**

The architecture of modern emergency management is fundamentally rooted in the Incident Command System (ICS), a modular and scalable hierarchy designed to provide order, predictability, and resource efficiency during high-stakes events.1 Originally developed to manage the complexity of wildland firefighting, the ICS has evolved into an "all-risk" framework adopted by federal, state, and local agencies to manage everything from hazardous material spills to terrorist attacks.2 However, as the global disaster landscape shifts toward "Black Swan" events—novel, high-impact, and cascading scenarios that defy historical precedent—the cognitive underpinnings of the ICS face unprecedented strain.4 This report evaluates the latent failure modes in decision pathways when the rigid doctrine of the ICS meets the fluid uncertainty of compound disasters, leveraging insights from Naturalistic Decision Making (NDM), Complexity Theory, and Cognitive Systems Engineering (CSE).

## **Modular Hierarchies and the Illusion of Scalability**

The fundamental premise of the Incident Command System is its modularity.2 By dividing the management of an incident into five functional areas—Command, Operations, Planning, Logistics, and Finance/Administration—the system allows for a "plug-and-play" expansion of personnel and equipment.2 This bureaucratic structure is designed to overcome the tendencies toward inertia found in traditional government agencies by establishing a temporary, highly reliable organization.1

While the ICS is lauded for its ability to manage "known" classes of emergencies, its reliance on a top-down flow of authority assumes that the Incident Commander (IC) at the top of the hierarchy maintains a clear and accurate mental model of the entire event.2 In a routine structure fire or a localized hazardous materials incident, this assumption holds. However, in compound disasters like the wildland-urban interface (WUI) fires seen in Paradise (2018) and Maui (2023), the speed and complexity of the event can lead to "node overload," where the central command node is saturated with more information than a human or a small team can process.4

| ICS Decision Module | Primary Function | Potential Brittleness Factor |
| :---- | :---- | :---- |
| **Command** | Strategic direction and goal setting | Reliance on a single "mental model" |
| **Operations** | Tactical execution of objectives | Disconnect from high-level strategy |
| **Planning** | Information collection and modeling | Lag between data entry and output |
| **Logistics** | Resource acquisition and tracking | Single-point dependencies |
| **Finance** | Administrative and legal compliance | Procedural lock-in during crises |

The reliability of the ICS is predicated on "structuring mechanisms" and "cognition management".2 Structuring mechanisms involve the formal rules and specialized training that allow responders from different agencies to work together seamlessly.2 Cognition management refers to the methods used to ensure that all members of the organization share the same understanding of the incident's status and objectives.2 In a Black Swan event, these mechanisms can become liabilities if they favor adherence to protocol over the need for adaptive improvisation.1

## **Naturalistic Decision Making: Recognition-Primed Decisions under Pressure**

Fireground commanders do not make decisions by generating a list of options and weighing them against one another; the time pressure and high stakes of the environment preclude such rational choice models.7 Instead, they rely on Naturalistic Decision Making (NDM), specifically the Recognition-Primed Decision (RPD) model.7 RPD suggests that experts use their experience to recognize patterns in a situation and then mentally simulate a single course of action to see if it will work.7

### **The Role of Expertise and "Thin Slicing"**

The difference between a veteran Incident Commander and a novice lies in the richness of their "mental bank" of past experiences.7 Experienced ICs are capable of "thin slicing"—filtering a massive amount of environmental data down to the few variables that actually matter.7 For example, a veteran IC might look at the color of smoke and the speed of its movement and instinctively know that a structure is about to collapse, even before any physical signs are visible to the untrained eye.7

According to research, fireground commanders make approximately 80% of their decisions in less than one minute.7 This rapid-fire decision-making is enabled by the brain's ability to match the current problem against similar problems solved in the past.7 However, the RPD model is inherently retrospective. It assumes that the future will resemble the past. When a fireground commander encounters a "novel event"—one for which they have no prior mental template—the RPD model can lead to "recognition errors" or decision paralysis as the commander attempts to find a match that does not exist.7

### **The Threshold of Unfamiliarity**

The "threshold of unfamiliarity" is the cognitive point where the incident transcends the responder's experience and training.14 Crossing this threshold requires a shift from recognition-primed action to explicit sensemaking.16 In the initial stages of the 2018 Camp Fire in Paradise, many commanders were initially operating within the bounds of their training for a standard brush fire.8 However, as the fire accelerated to a speed of 7.8 miles in 45 minutes, they breached the threshold of unfamiliarity.8 At this point, the standard scripts for fire suppression became obsolete, and the mission had to pivot entirely to mass evacuation and life safety.9

## **The Collapse of Sensemaking: Lessons from Mann Gulch and Maui**

Sensemaking is the process of turning a chaotic and ambiguous situation into a coherent narrative that supports action.16 In organizations, sensemaking is not just a cognitive task; it is a social one.16 When the formal role structure of an organization collapses, the ability of its members to make sense of the situation often collapses with it.16

### **The Disintegration of the Smokejumper Team**

The 1949 Mann Gulch fire disaster remains the definitive case study for the collapse of sensemaking.16 When a 15-man smokejumper crew was confronted with a "blowup" fire that they had no experience with, their role structure disintegrated.19 The crew’s radio had been destroyed upon landing, cutting them off from external intelligence.19 When their leader, "Wag" Dodge, recognized that they could not outrun the fire and ordered them to enter his "escape fire," the crew failed to follow him.16 To the crew, Dodge’s actions made no sense; they saw a man lighting a fire in front of them when they were already running from one.17

Thirteen men died in Mann Gulch because they could not make sense of a novel command in a high-stress, low-information environment.18 Karl Weick’s analysis identifies four sources of resilience that can prevent this type of collapse 16:

1. **Improvisation**: The ability to create new, effective actions on the fly.1  
2. **Virtual Role Systems**: Maintaining a mental map of who is supposed to do what, even when the actual people are missing or out of contact.16  
3. **The Attitude of Wisdom**: Maintaining a balance between confidence in one's skills and a healthy skepticism of one's interpretation of the situation.16  
4. **Norms of Respectful Interaction**: Ensuring that signals from any level of the organization can be heard and believed by others.16

### **Fragmented Mental Models in the Maui 2023 Fire**

The 2023 Maui wildfires, which claimed over 100 lives, demonstrated a modern failure of sensemaking across multiple agencies.21 After-action reports indicate that the Maui Police Department (MPD) and the Maui Fire Department (MFD) never established a unified command post.22 This lack of co-location meant that the two departments operated with fragmented mental models.22

Police officers, tasked with evacuations, were often unaware of fire progression or water supply failures, while firefighters were unaware of which evacuation routes were blocked by downed trees or utility poles.22 The "common ground"—the shared understanding of the problem space—was never established.4 When cell service and radio repeaters failed, the organization was plunged into a "silent node" syndrome, where individual units were left to improvise survival strategies in complete isolation from the command node.23

## **Cognitive Systems Engineering: Graceful Extensibility vs. Decompensation**

Cognitive Systems Engineering (CSE) provides a framework for evaluating how joint human-machine systems adapt to complexity.4 David Woods, a pioneer in the field, argues that the most important property of a resilient system is "graceful extensibility"—the ability to stretch its capacity to handle surprises that were not anticipated in its design.4

### **The Limits of Adaptive Capacity**

Every system has a finite amount of adaptive capacity.4 As an Incident Command System is pushed toward its limits, it begins to "decompensate"—performance starts to degrade, and the system becomes increasingly brittle.4 This often manifests as "getting stuck in outdated behaviors," where the IC continues to issue orders based on a fire's previous location because they lack the "visual momentum" to track its current trajectory.4

Woods identifies three recurring failure patterns in complex systems 4:

1. **Decompensation**: The system is overwhelmed and breaks down rather than stretching.4  
2. **Working at Cross-Purposes**: Different parts of the system optimize for their own goals but inadvertently sabotage the overall mission.4  
3. **Brittleness at the Boundaries**: The system performs well within its "designed" envelope but fails catastrophically the moment it is pushed outside of it.4

### **Managing Cognitive Load and the Information Firehose**

In a modern Emergency Operations Center (EOC), the problem is often not a lack of information, but an "information firehose"—a massive influx of data that has not been triaged or synthesized.7 Incident Commanders can experience "bounded rationality," where their ability to make optimal decisions is limited by the amount of information they can process in the time available.7

NIST Special Publication 1024, which addresses human factors in ICS, emphasizes the need for systems that reduce cognitive load through effective interface design and information prioritization.28 (Note: While SP 1024's technical subject in the snippets is optical fiber, in the context of this "Cognitive Architect" report, we apply the principles of human systems integration (HSI) and human engineering standards found in NISTIR 7889 to the domain of fireground command 29). Effective "joint cognitive systems" involve the use of technology to augment human pattern recognition, providing "perceptual landmarks" that help an IC orient themselves within a virtual data space of maps, camera feeds, and radio traffic.4

## **Diagnostic Analysis: The 2018 Camp Fire (Paradise)**

The 2018 Camp Fire provides a stark example of how a "Black Swan" fire can outpace the decision-making cycle of even an experienced command structure.8 The fire was ignited by a failure of a 100-year-old "C-hook" on a PG\&E transmission tower during a Red Flag warning.31 Within minutes, the fire was being driven by "Jarbo Winds" that were so strong responders could barely stand upright.31

### **Timeline of Decision Failure and Node Overload**

The spatiotemporal gap between fire progression and command action in the Paradise fire was catastrophic.8 By the time the first evacuation orders were issued, the fire had already impacted several mountain communities.9

| Time (Nov 8, 2018\) | Fire Location / Impact | Command Action / Decision | Cognitive Failure Mode |
| :---- | :---- | :---- | :---- |
| **06:30** | Ignition at Poe Dam | Initial dispatch (Class C fire) | Scripted Response |
| **07:00** | Enters Pulga / Concow | Mutual aid requests | Recognition of Novelty |
| **07:45** | Reaches Paradise outskirts | Evacuation zone alerts | Node Overload; Latency |
| **08:30** | Mass structure loss | Emergency hospital evac | Collapse of Sensemaking |
| **11:00** | Fire crosses town | Search and Rescue (SAR) pivot | Extreme Improvisation |

The after-action report noted that "communication from the field to the EOC needs improvement to ensure proper information flow".30 Specifically, the EOC was unaware of the location of fire-blocked roads, leading to public messaging that directed residents into "burnover" events.9 This is an example of "lost common ground," where the strategic command layer is making decisions based on data that is 30 to 60 minutes old, while the tactical layer is literally fighting for survival in a different reality.4

### **NETTRA: A Database of Resilience**

A detailed case study by NIST (specifically the NETTRA analysis—Notification, Evacuation, Traffic, Temporary Refuge Areas, and Rescues) integrated 2,600 observations into a spatiotemporal database to understand how decisions were made on the ground.9 The analysis found that 31 Temporary Refuge Areas (TRAs) were used by over 1,200 civilians.9 These TRAs were not part of any pre-fire plan; they were emergent decisions made by firefighters and police officers who recognized that the evacuation routes were failed and that they had to find "islands" of safety in parking lots and cleared fields.9

This illustrates the "inverted command flow," where the most critical life-saving decisions were made by subordinates who had "backfed" the signal of evacuation failure upward, even if the formal hierarchy was not yet ready to process it.1 Chief David Hawks of the CAL FIRE Butte Unit was recognized for his "command presence" during such a rescue at a hospital, where his ability to provide clear, improvisational direction to nurses and patients shifted their minds into "survival mode," ultimately saving lives despite the collapse of the formal evacuation route.33

## **Diagnostic Analysis: The 2023 Maui Wildfire (Lahaina)**

The 2023 Maui fire serves as a diagnostic anchor for the "silent node" syndrome and the failure of multi-agency coordination under extreme environmental stress.22 The fire in Lahaina was not a "pure wildfire" but an "urban conflagration" fueled by extreme winds and a landscape susceptible to fire.23

### **Infrastructure Collapse and the Comms Void**

The Lahaina fire was characterized by a massive breakdown in communication.24 Five days before the fire, meteorologists had warned of extreme risk, yet there was "minimal upstaffing and pre-positioning of resources".23 When the fires intensified on August 8, the head of the Maui Emergency Management Agency (MEMA) was off-island, and the agency "dragged its heels" about returning.24

As the fire moved into the town, power lines were toppled, cutting cell service and internet.22 Residents and tourists did not receive emergency alerts.24 Even the responders were in the dark; police and firefighters had to communicate on closed channels, and without cellular service, they could not check on the safety of their own families or coordinates with the EOC.24 This created a "fragility point" where the doctrine of a central command node became an obstacle, as the EOC was essentially blind to the unfolding tragedy in Lahaina.4

| Maui Response Gap | Evidence from AAR | Cognitive / Systemic Risk |
| :---- | :---- | :---- |
| **Preparedness** | "No evidence" of pre-event plans produced by MFD | Normalcy Bias |
| **Unity of Command** | MFD and MPD used separate command centers | Working at Cross-Purposes |
| **Tactical Tools** | Hydrant pressure failed due to infrastructure damage | Saturation of Adaptive Capacity |
| **Information Flow** | Relying on WhatsApp chains for callback | Comms Entropy |

The Western Fire Chiefs Association after-action report highlighted 111 recommendations, many of which focused on the need for "coordinated evacuation plans" and "firefighters and police operating out of the same command center".23 The failure in Maui was not a failure of individual courage—officers risked their lives to pile people into cars—but a failure of the "cognitive scaffolding" that should have allowed those individual acts to be part of a larger, coordinated survival strategy.22

## **Redesigning for Resilience: Meta-Commands and Elastic Hierarchies**

A resilient Incident Command System for Black Swan events must move beyond a static, modular hierarchy toward an "elastic hierarchy" that can reconfigure itself in real-time.1 This requires the implementation of "Meta-Command" layers and "Double-Loop Learning" processes.1

### **The Meta-Command Layer**

A Meta-Command layer is a specialized decision module that does not focus on the tactics of fire suppression, but rather on the "health" and "flow" of the command system itself.1 Its task is to monitor for signs of node overload, comms entropy, and doctrine lock-in.1 If the Meta-Command node detects that the Operations Section is being overwhelmed by novelty, it has the authority to "re-authorize" new roles in real-time—for example, converting all logistics units into ad-hoc evacuation squads without waiting for the standard ICS planning cycle.1

### **Double-Loop Learning and Adaptive Reframing**

Most ICS training focuses on "Single-Loop Learning"—following the rules more efficiently.27 Black Swan resilience requires "Double-Loop Learning," which involves questioning the rules and the underlying mental models themselves.5 David Woods describes this as "Reframing"—the ability to update one's mental model to match a changing reality even when that reality contradicts years of experience.5

In the 2018 Paradise fire, the transition from "fire suppression" to "mass evacuation" was a form of reframing.9 However, it happened too slowly in many command nodes. A resilient system would have pre-set "threshold markers" that trigger an automatic reframing. For example, if a fire crosses a certain geographical boundary at a certain speed, the "Fire Suppression" script is automatically archived and the "Survival and Rescue" script is activated, flattening the hierarchy and authorizing extreme improvisation at the tactical edge.1

## **AI Augmentation and the Joint Cognitive System**

The integration of Artificial Intelligence (AI) into the Incident Command System offers a potential solution to the "information firehose," but it also introduces new risks of "misalignment" and "automation bias".5

### **Swarm-Based AI Assistants (DRP-COG-SWARM-ICS)**

One promising area for resilient cognitive scaffolding is the use of "swarm-based" AI assistants.1 These are not central "supercomputers" but distributed machine agents that reside with individual tactical units.26 These agents can monitor local environment signals (heat, wind, radio chatter) and "backfeed" novel signals upward, bypassing the traditional chain of command if a critical danger is detected.1

Woods' theory of "Joint Human-Machine Cognitive Systems" suggests that AI should be designed as a "teammate" that helps the IC with "mental simulation".4 For example, an AI could run thousands of fire-spread simulations in seconds, presenting the IC with "perceptual landmarks" on their digital display that indicate where a fire is likely to be in 30 minutes, helping to overcome the "visual momentum" issues seen in Paradise and Maui.4

### **The Risk of AI-Diagnosis Misalignment**

A significant failure mode in human-AI teaming occurs when the AI misreads the human's uncertainty.27 If a commander is hesitant because they are seeing a "Black Swan" signal that the AI's training data does not include, the AI might push for a "scripted" solution that is actually lethal.26 Cognitive Systems Engineering must prioritize "explainable AI" that allows the commander to see *why* the machine is suggesting a particular course of action, maintaining the human's role as the final arbiter of decision-making under uncertainty.5

## **Failure Atlas: Mapping Latent Failure Modes in Fireground Command**

To enable better decision-making for EOC planners and system researchers, we can synthesize the findings from after-action reports into a "Black Swan ICS Failure Atlas." This library of patterns identifies the "fragility points" in the current command doctrine.

| Failure Mode | Mechanism | Marker / Signal | Resilience Fix |
| :---- | :---- | :---- | :---- |
| **Doctrine Lock-in** | Overtrusting SOPs despite evidence of novelty | IC ignores "unusual" reports from the field | "Threshold of Unfamiliarity" training |
| **Information Firehose** | Signal overload without triage or synthesis | EOC log becomes a "dumping ground" for raw data | AI-mediated signal triage |
| **Silent Node Syndrome** | Disengagement due to comms failure or ambiguity | Tactical units stop reporting back; "radio silence" | Decentralized comms (LoRaWAN, mesh) |
| **Role Boundary Collapse** | Non-standard roles acting without coordination | Logistics trucks acting as ambulances without a medic | "Virtual Role" cross-training |
| **Cognitive Decompensation** | Performance drop as saturation limit is reached | IC starts making "rational choice" lists instead of RPD | Meta-Command layer intervention |

The "silent node" syndrome is particularly dangerous, as it often leads to a false sense of security in the EOC.4 If a tactical unit stops reporting, the EOC may assume they are simply busy, when in fact they may be trapped or overwhelmed.24 Resilient ICS requires "active heartbeat" protocols where the absence of a signal is treated as a critical "emergency signal" in itself.1

## **Recommendations for Resilient Cognitive Scaffolding**

For municipal fire departments and incident commanders, the transition from a brittle hierarchy to an adaptive system requires a fundamental shift in both technology and culture.

### **1\. Implementation of Real-Time Operations Centers (RTOC)**

As seen in the final Maui Police Department recommendations, the creation of a Real-Time Operations Center (RTOC) that serves as an intelligence and coordination hub is essential.36 The RTOC should be staffed by cross-trained personnel (police, fire, EMS, utility, and meteorology) to ensure that the "common ground" is established before a crisis begins.22 This center should utilize "visual momentum" tools to integrate data from diverse sources, providing a single "truth" for all responding agencies.4

### **2\. Adoption of Elastic Communication Protocols**

The failure of cell networks in Maui and Paradise highlights the need for "comms-agnostic" command structures.24 Departments should invest in "Real-time Operations" platforms that can switch seamlessly between cellular, satellite, and mesh radio networks.34 Furthermore, the "phone tree" and "WhatsApp" notification systems should be replaced by automated, redundant mass-alert systems that can reach all personnel instantly.23

### **3\. Red-Teaming for Novelty and Complexity**

Training exercises should focus on "Red Team inversion," where simulators introduce rogue or failed nodes into a scenario.1 Instead of practicing for a fire that follows the script, commanders should be forced to manage "compound" events—for example, a wildfire occurring during a cyber outage at the regional dispatch center while a hospital is being evacuated.5 These exercises should not be graded on how well the IC followed the SOP, but on how quickly they recognized that the SOP was failing and authorized an effective improvisation.1

### **4\. Human-Centered AI Design (HCAI)**

When designing AI for fireground command, the focus must be on augmenting human capability rather than substituting for it.26 AI agents should be tasked with "low-level" cognition—tracking hose lengths, monitor engine fuel levels, and synthesizing weather updates—to free up the Incident Commander’s "high-level" cognitive resources for strategic sensemaking and role reconfiguration.1

## **Future Outlook: Swarm Intelligence and Crisis Resilience**

The evolution of emergency response cognition is moving toward "Swarm ICS," where the rigid hierarchy is replaced by a decentralized network of autonomous but "aligned" units.1 In this model, the role of the Incident Commander shifts from "controlling the response" to "stewarding the intent".2 By providing a clear strategic intent and a set of "simple rules" for interaction, the IC can allow the swarm of responders to self-organize in the face of novelty, much like how the Temporary Refuge Areas were created in Paradise.1

This shift toward complexity-aware command structures is the only way to meet the challenges of the Black Swan era.5 As disasters become more compound and cascading, the "source of power" for the Incident Commander will not be their authority to give orders, but their ability to foster a "team mind" that can make sense of the unthinkable.12

## **Conclusion: Diagnosing and Defeating Brittleness**

The diagnostic analysis of cognitive decision structures in fireground command reveals that our most sophisticated Incident Command Systems are often at their most brittle when faced with the "unscripted" event.4 The failures in Paradise and Maui were not failures of bravery, but of "cognitive infrastructure"—the pathways of information and authority that became clogged or severed under the pressure of extreme uncertainty.22

To build a resilient future, we must embrace the "paradoxical tensions" of high-reliability organizing: the need for both hierarchy and flexibility, both protocol and improvisation.1 By implementing Meta-Command layers, elastic communication networks, and joint human-AI cognitive systems, we can ensure that our command nodes do not just scale to the size of the fire, but stretch to the scale of the surprise.1 The "Black Swan" will continue to appear on the fireground; our task is to ensure that when it does, our decision structures are prepared to recognize it, make sense of it, and act with the wisdom and agility required to save lives.7

#### **Works cited**

1. The incident command system: High-reliability organizing for ..., accessed on February 3, 2026, [https://www.researchgate.net/publication/274913449\_The\_incident\_command\_system\_High-reliability\_organizing\_for\_complex\_and\_volatile\_task\_environments](https://www.researchgate.net/publication/274913449_The_incident_command_system_High-reliability_organizing_for_complex_and_volatile_task_environments)  
2. The Incident Command System: High-Reliability Organizing for Complex and Volatile Task Environments, accessed on February 3, 2026, [https://ahimta.org/resources/Documents/The%20ICS%20High%20Reliability%20Organizing%20for%20complex%20and%20volitile%20Task%20Environments.pdf](https://ahimta.org/resources/Documents/The%20ICS%20High%20Reliability%20Organizing%20for%20complex%20and%20volitile%20Task%20Environments.pdf)  
3. Bigley, G.A. and Roberts, K.H. (2001) The Incident Command System High Reliability Organizing for Complex and Volatile Task Environment. The Academy of Management Journal, 44, 1281-1299. \- References \- Scientific Research Publishing, accessed on February 3, 2026, [https://www.scirp.org/reference/referencespapers?referenceid=3493514](https://www.scirp.org/reference/referencespapers?referenceid=3493514)  
4. David Woods (safety researcher) \- Wikipedia, accessed on February 3, 2026, [https://en.wikipedia.org/wiki/David\_Woods\_(safety\_researcher)](https://en.wikipedia.org/wiki/David_Woods_\(safety_researcher\))  
5. Outmaneuver Complexity: AI Gold Rush 2.0 & Adaptive Capacity with David Woods, PhD, accessed on February 3, 2026, [https://nowayout.buzzsprout.com/2109174/episodes/17577468-outmaneuver-complexity-ai-gold-rush-2-0-adaptive-capacity-with-david-woods-phd](https://nowayout.buzzsprout.com/2109174/episodes/17577468-outmaneuver-complexity-ai-gold-rush-2-0-adaptive-capacity-with-david-woods-phd)  
6. The incident command system : high-reliability organizing for complex and volatile task management | ALNAP, accessed on February 3, 2026, [https://alnap.org/help-library/resources/the-incident-command-system-high-reliability-organizing-for-complex-and-volatile-task/](https://alnap.org/help-library/resources/the-incident-command-system-high-reliability-organizing-for-complex-and-volatile-task/)  
7. Fireground Command Decisions \- Fire Engineering, accessed on February 3, 2026, [https://www.fireengineering.com/firefighting/fireground-command-decisions/](https://www.fireengineering.com/firefighting/fireground-command-decisions/)  
8. November 2018 Camp Fire \- National Weather Service, accessed on February 3, 2026, [https://www.weather.gov/media/publications/assessments/sa1162SignedReport.pdf](https://www.weather.gov/media/publications/assessments/sa1162SignedReport.pdf)  
9. A Case Study of the Camp Fire—Notification, Evacuation, Traffic ..., accessed on February 3, 2026, [https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.2252.pdf](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.2252.pdf)  
10. The Incident Command System: High-Reliability Organizing for Complex and Volatile Task Environments (2001) | Gregory A. Bigley | 947 Citations \- SciSpace, accessed on February 3, 2026, [https://scispace.com/papers/the-incident-command-system-high-reliability-organizing-for-3e8altv9rz](https://scispace.com/papers/the-incident-command-system-high-reliability-organizing-for-3e8altv9rz)  
11. Sources of Power Free Summary by Gary Klein \- getAbstract, accessed on February 3, 2026, [https://www.getabstract.com/en/summary/sources-of-power/10481](https://www.getabstract.com/en/summary/sources-of-power/10481)  
12. Sources of power : how people make decisions / Gary Klein \- National Library of Australia, accessed on February 3, 2026, [https://catalogue.nla.gov.au/catalog/244831](https://catalogue.nla.gov.au/catalog/244831)  
13. Sources of Power by Gary Klein: 6 Minute Summary \- YouTube, accessed on February 3, 2026, [https://www.youtube.com/watch?v=RVdYWVBi3Ao](https://www.youtube.com/watch?v=RVdYWVBi3Ao)  
14. This Is a Classic: Translators on Making Writers Global 9781501376917, 9781501376900, 9781501376948, 9781501376931 \- DOKUMEN.PUB, accessed on February 3, 2026, [https://dokumen.pub/this-is-a-classic-translators-on-making-writers-global-9781501376917-9781501376900-9781501376948-9781501376931.html](https://dokumen.pub/this-is-a-classic-translators-on-making-writers-global-9781501376917-9781501376900-9781501376948-9781501376931.html)  
15. THE EXPERIENCES OF BIOLOGY INSTRUCTORS AT A COMMUNITY COLLEGE WITH THE INVERTED CLASSROOM \- TXST Digital Repository, accessed on February 3, 2026, [https://digital.library.txst.edu/bitstreams/f5022305-87c2-44b1-8625-b91112db3791/download](https://digital.library.txst.edu/bitstreams/f5022305-87c2-44b1-8625-b91112db3791/download)  
16. The collapse of sensemaking in organizations: the Mann Gulch disaster, accessed on February 3, 2026, [https://nrfirescience.org/resource/15592](https://nrfirescience.org/resource/15592)  
17. The collapse of sensemaking in organizations: the Mann Gulch disaster., accessed on February 3, 2026, [https://psnet.ahrq.gov/node/33923/psn-pdf](https://psnet.ahrq.gov/node/33923/psn-pdf)  
18. The collapse of sensemaking in organizations: The Mann Gulch disaster \- ALNAP, accessed on February 3, 2026, [https://alnap.org/help-library/resources/the-collapse-of-sensemaking-in-organizations-the-mann-gulch-disaster/](https://alnap.org/help-library/resources/the-collapse-of-sensemaking-in-organizations-the-mann-gulch-disaster/)  
19. The Collapse of Sensemaking in Organizations: The Mann Gulch Disaster \- AWS, accessed on February 3, 2026, [https://lessonslearned-prod-media-bucket.s3.us-gov-west-1.amazonaws.com/s3fs-public/2023-02/TheCollapseofSensemakinginOrganizations.pdf](https://lessonslearned-prod-media-bucket.s3.us-gov-west-1.amazonaws.com/s3fs-public/2023-02/TheCollapseofSensemakinginOrganizations.pdf)  
20. The Collapse of Sensemaking in Organizations: The Mann Gulch Disaster \- USDA Forest Service, accessed on February 3, 2026, [https://www.fs.usda.gov/t-d/pubs/htmlpubs/htm95512855/page18.htm](https://www.fs.usda.gov/t-d/pubs/htmlpubs/htm95512855/page18.htm)  
21. Lahaina Fire Incident Analysis Phase Two Report | Fire Safety ..., accessed on February 3, 2026, [https://fsri.org/research-update/lahaina-fire-incident-analysis-report-released-attorney-general-hawaii](https://fsri.org/research-update/lahaina-fire-incident-analysis-report-released-attorney-general-hawaii)  
22. Report finds 'no evidence' Hawaii officials prepared for wildfire that killed 102 despite warnings \- Victoria Times Colonist, accessed on February 3, 2026, [https://www.timescolonist.com/world-news/report-finds-no-evidence-hawaii-officials-prepared-for-wildfire-that-killed-102-despite-warnings-9519259](https://www.timescolonist.com/world-news/report-finds-no-evidence-hawaii-officials-prepared-for-wildfire-that-killed-102-despite-warnings-9519259)  
23. Better Evacuation Plans Needed, Maui Report Finds \- GovTech, accessed on February 3, 2026, [https://www.govtech.com/em/disaster/better-evacuation-plans-needed-maui-report-finds](https://www.govtech.com/em/disaster/better-evacuation-plans-needed-maui-report-finds)  
24. Communications breakdown left authorities in the dark and residents without alerts amid Maui fire \- MooseJawToday.com, accessed on February 3, 2026, [https://www.moosejawtoday.com/environment-news/communications-breakdown-left-authorities-in-the-dark-and-residents-without-alerts-amid-maui-fire-8611605](https://www.moosejawtoday.com/environment-news/communications-breakdown-left-authorities-in-the-dark-and-residents-without-alerts-amid-maui-fire-8611605)  
25. Integrated Preparedness Plan (IPP) \- Record of Changes \- Maui County, accessed on February 3, 2026, [https://www.mauicounty.gov/DocumentCenter/View/151888/Integrated-Preparedness-Plan](https://www.mauicounty.gov/DocumentCenter/View/151888/Integrated-Preparedness-Plan)  
26. The Design of Joint Human-Machine Cognitive Systems, accessed on February 3, 2026, [https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/511/447](https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/511/447)  
27. Cognitive Work in Future Manufacturing Systems: Human-centered AI for Joint Work with Models, accessed on February 3, 2026, [https://tsapps.nist.gov/publication/get\_pdf.cfm?pub\_id=933309](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=933309)  
28. Technical digest: symposium on optical fiber measurements, 2004 \- GovInfo, accessed on February 3, 2026, [https://www.govinfo.gov/content/pkg/GOVPUB-C13-c09a852154028fff0fecd9d884ce822c/pdf/GOVPUB-C13-c09a852154028fff0fecd9d884ce822c.pdf](https://www.govinfo.gov/content/pkg/GOVPUB-C13-c09a852154028fff0fecd9d884ce822c/pdf/GOVPUB-C13-c09a852154028fff0fecd9d884ce822c.pdf)  
29. Human Engineering Design Criteria Standards Part 1: Project Introduction and Existing Standards | NIST, accessed on February 3, 2026, [https://www.nist.gov/publications/human-engineering-design-criteria-standards-part-1-project-introduction-and-existing](https://www.nist.gov/publications/human-engineering-design-criteria-standards-part-1-project-introduction-and-existing)  
30. 2018 CAMP FIRE AFTER ACTION REPORT, accessed on February 3, 2026, [https://www.caloes.ca.gov/wp-content/uploads/Preparedness/Documents/FINAL-AAR-2018-Camp-Fire-508-Clean-Copy-11.17.25.pdf](https://www.caloes.ca.gov/wp-content/uploads/Preparedness/Documents/FINAL-AAR-2018-Camp-Fire-508-Clean-Copy-11.17.25.pdf)  
31. THE CAMP FIRE PUBLIC REPORT \- Butte County, accessed on February 3, 2026, [https://www.buttecounty.net/DocumentCenter/View/1881/Camp-Fire-Public-Report---Summary-of-the-Camp-Fire-Investigation-PDF](https://www.buttecounty.net/DocumentCenter/View/1881/Camp-Fire-Public-Report---Summary-of-the-Camp-Fire-Investigation-PDF)  
32. Supplement to A Case Study of the Camp Fire—Notification, Evacuation, Traffic, and Temporary Refuge Areas (NETTRA), accessed on February 3, 2026, [https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.2252sup.pdf](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.2252sup.pdf)  
33. California Fire Chief David Hawks Honored For Rescue Mission, accessed on February 3, 2026, [https://www.iafc.org/about-iafc/press-releases/press-release/california-fire-chief-david-hawks-honored-for-rescue-mission](https://www.iafc.org/about-iafc/press-releases/press-release/california-fire-chief-david-hawks-honored-for-rescue-mission)  
34. Preliminary After-Action Report: 2023 Maui Wildfire \- USFA.FEMA.gov, accessed on February 3, 2026, [https://www.usfa.fema.gov/blog/preliminary-after-action-report-2023-maui-wildfire/](https://www.usfa.fema.gov/blog/preliminary-after-action-report-2023-maui-wildfire/)  
35. Lahaina Fire Forward-Looking Report \- Cloudfront.net, accessed on February 3, 2026, [https://d1gi3fvbl0xj2a.cloudfront.net/2025-01/Lahaina\_Fire\_Forward\_Looking\_Report\_010924\_Final.pdf](https://d1gi3fvbl0xj2a.cloudfront.net/2025-01/Lahaina_Fire_Forward_Looking_Report_010924_Final.pdf)  
36. Maui Police Department releases Final After-Action Report on Aug. 8, 2023 wildfires, accessed on February 3, 2026, [https://mauinow.com/2025/08/01/maui-police-department-releases-final-after-action-report-on-aug-8-2023-wildfires/](https://mauinow.com/2025/08/01/maui-police-department-releases-final-after-action-report-on-aug-8-2023-wildfires/)