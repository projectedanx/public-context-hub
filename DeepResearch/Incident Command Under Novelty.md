# **Cognitive Infrastructure Under Fire: Incident Command Decision-Making Under Novelty**

## **Executive Synthesis**

**\[Inference\]** The modern Incident Command System (ICS), alongside its international variants such as the Australasian Inter-Service Incident Management System (AIIMS), represents more than a bureaucratic standard for emergency management; it functions as a sophisticated, distributed cognitive architecture. These systems are engineered to metabolize the chaotic, high-velocity data of a disaster and convert it into structured operational objectives, effectively serving as a "cognitive prosthetic" for human commanders whose individual processing capacities would otherwise be overwhelmed. By routing decision rights, strictly managing spans of control, and externalizing memory through rigid planning cycles, ICS acts to stabilize the environment, imposing order upon entropy.

However, the efficacy of this cognitive infrastructure faces catastrophic deformation when subjected to "Novelty." In the context of this report, novelty is not merely a function of scale—a larger fire is not necessarily a novel one—but of unfamiliar coupling between hazards, the cascading failure of critical support infrastructures, and the violation of the fundamental mental models held by command staff. \*\*\*\* Drawing on High-Reliability Organizing (HRO) theory and Resilience Engineering, we argue that standard ICS architectures are "Robust" (designed to resist known stressors) rather than "Adaptive" (designed to reconfigure for unknown stressors). When faced with "Black Swan" events or "Cosmology Episodes"—where the physics of the hazard or the behavior of the populace defies established prototypes—the structural rigidity intended to ensure safety can paradoxically accelerate sensemaking collapse.1

**\[Case Evidence\]** Forensic analysis of the Yarnell Hill Fire (2013) and the Lahaina Fire (2023) exposes a recurring failure mode: the **Plan-Tempo Mismatch**. In both instances, the update rate of the hazard (e.g., thunderstorm outflow winds, hurricane-driven embers) fundamentally outpaced the update rate of the organization’s planning cycle. The "shared mind" of the command structure became decoupled from the "ground truth" of the operation, leading to a state where the Incident Action Plan (IAP) functioned as a historical document rather than a tactical guide. \*\*\*\* While ICS doctrine emphasizes "flexibility," in practice, the heavy administrative inertia of the "Planning P" often traps command staffs in a cycle of feeding the system rather than observing the fire.3

This report delivers an exhaustive analysis of these failure modes. It contrasts the US-centric ICS model with the AIIMS model, noting specifically how AIIMS's elevation of "Intelligence" to a Command Section offers superior capacity for anticipating hazard novelty, albeit with increased coordination friction.5 **\[Inference\]** We conclude that upgrading this infrastructure requires moving beyond better compliance; it requires structural interventions such as "Shadow Command" (Red Teaming) to institutionalize the challenge function, and the deployment of mesh-networked Common Operating Pictures (COP) to maintain shared consciousness when centralized infrastructure fails.

## ---

**1\. The Doctrinal Baseline: Architecture of Distributed Cognition**

To understand how decision-making fails under extreme novelty, one must first map the "cognitive circuitry" of the baseline system. We analyze ICS and AIIMS not as management hierarchies, but as information processing systems designed to route attention and authority.

### **1.1 The Incident Command System (ICS): The Modular Mind**

\*\*\*\* The National Incident Management System (NIMS) codifies ICS as a modular, scalable system designed to enable disparate agencies to operate under a unified structure.7 Its primary cognitive function is the reduction of load on individual decision-makers through the **Manageable Span of Control**, typically maintained at a ratio of 1:3 to 1:7.9 This is not merely a management rule; it is a cognitive safety valve designed to prevent "node saturation," where a supervisor loses the mental model of their subordinates' locations and status.

#### **1.1.1 Role and Authority Routing (The Cognitive Circuit)**

ICS divides the cognitive labor of incident management into five functional areas, effectively creating a "distributed brain" where no single individual must hold the entire complexity of the event.7

* **Command (The Executive Function):** This node holds the ultimate decision rights for strategy and risk acceptance. The Incident Commander (IC) sets the **Command Intent**, a high-level heuristic that guides subordinate decision-making when communications fail. The Command Staff (Safety, Liaison, Public Information) acts as sensory filters, monitoring specific domains (risk, politics, media) to protect the IC’s attention.10  
* **Operations (The Motor Cortex):** Responsible for tactical execution. Crucially, Operations acts as an information filter. A Division Supervisor does not report every shovel strike to the IC; they aggregate data into "Situation Reports" (SITREPS), passing up only actionable deviations from the plan. This filtering prevents upward information overload.10  
* **Planning (The Hippocampus):** The Planning Section is the center of "Shared Memory Externalization." It is responsible for collecting, evaluating, and displaying incident information. Its primary output, the **Incident Action Plan (IAP)**, serves as the collective memory of the organization, ensuring that the operational plan exists independently of any single person's mind.4

**\[Inference\]** The rigidity of these roles creates a "Cognitive Contract." A firefighter on the line trusts that "Planning" is tracking the weather so they don't have to. When novelty breaks this contract—when Planning fails to predict a weather shift—the firefighter is left exposed, having offloaded that cognitive task to a failed system.

#### **1.1.2 Safety Invariants and Heuristics**

\*\*\*\* To stabilize decision-making under uncertainty, ICS integrates "invariants"—rules that function as "hard stops" in the decision loop.

* **The Safety Officer:** Armed with the authority to bypass the chain of command to stop unsafe acts, the Safety Officer represents an "institutionalized override".10  
* **LCES (Lookouts, Communications, Escape Routes, Safety Zones):** This acronym is a continuous, looping heuristic required for all tactical engagements. It forces a recurrent check of the environment.12  
* **10 Standard Firefighting Orders & 18 Watch Out Situations:** These operate as "Pattern Recognition Triggers." They serve to alert the firefighter that the current situation matches a known "disaster prototype" (e.g., "Unfamiliar with weather and local factors").13

### **1.2 The AIIMS Contrast: Elevating Intelligence**

\*\*\*\* The Australasian Inter-Service Incident Management System (AIIMS) shares the DNA of ICS but introduces a critical architectural variation: the elevation of **Intelligence**.5

#### **1.2.1 The Intelligence Section**

In standard FEMA ICS, "Intelligence/Investigations" is typically nested within the Planning Section or formed only for law enforcement needs.15 In AIIMS, **Intelligence** is frequently a standalone Section, peer to Operations and Planning.6

* **Cognitive Implication \[Inference\]:** By separating Intelligence (understanding the hazard) from Planning (managing resources and writing the IAP), AIIMS explicitly allocates cognitive bandwidth to Sensemaking. In ICS, the Planning Section Chief can become consumed by the administrative burden of the "Planning P" (resource tracking, form completion), potentially neglecting the dynamic analysis of the fire itself. The AIIMS structure theoretically safeguards the "Hazard Analysis" function from being cannibalized by the "Logistical Planning" function.6

### **1.3 Comparative Analysis: Attention Allocation**

| Feature | FEMA ICS (NIMS) | AIIMS (AFAC) | Cognitive Impact & Trade-off |
| :---- | :---- | :---- | :---- |
| **Hazard Analysis** | Embedded in Planning Section (Situation Unit).10 | Elevated to Intelligence Section (in many configurations).6 | **AIIMS** reduces the risk of the "Planning Fallacy" (focusing on the plan, not the fire) but increases coordination costs between Intel and Ops. |
| **Span of Control** | Strict 1:3–1:7 ratio.9 | Guidance (1:5 ideal); emphasizes "functional management".5 | Both prioritize preventing cognitive saturation of supervisors. |
| **Command Logic** | **Unity of Command:** One supervisor per person.9 | **Unity of Effort:** Emphasizes coordination across agencies.17 | **ICS** optimizes for speed and clarity of authority; **AIIMS** optimizes for multi-agency consensus and hazard awareness. |

## ---

**2\. Cognitive Mechanisms: How Decisions Are Actually Made**

**\[Inference\]** A profound gap exists between how doctrine says decisions are made (The Planning Cycle) and how human beings actually make decisions under fire (Recognition-Primed). This gap is the location of "Friction."

### **2.1 The Two Tempos of Command**

We must model the incident as two interacting loops: the **Hazard Loop** (the physical reality) and the **Decision Loop** (the organization).

#### **2.1.1 Tempo 1: Recognition-Primed Decision Making (RPD)**

\*\*\*\* Research by Klein on fireground commanders reveals that experts do not engage in analytical option comparison. Instead, they use **Recognition-Primed Decision Making (RPD)**.

* **Mechanism:** The commander scans the environment for **Cues** (smoke column angle, fuel moisture, crew demeanor). These cues are matched against a mental **Library of Prototypes** built from years of experience. Once a match is found (e.g., "This is a wind-driven run in continuous fuel"), the commander mentally simulates a single course of action. If the simulation succeeds, they act.18  
* **Speed:** Near-instantaneous.  
* **Vulnerability:** **Pattern Mismatch.** In a novel event (Black Swan), the commander lacks a valid prototype. The brain, abhorring a vacuum, often forces a "nearest neighbor" match, treating a novel threat (e.g., a fire tornado) as a standard threat (e.g., a whirlwind), leading to catastrophic under-reaction.20

#### **2.1.2 Tempo 2: The Planning Cycle (The "P")**

\*\*\*\* ICS mandates a formal "Planning P"—a cyclical, linear process involving strategy meetings, tactic meetings, and IAP preparation, typically running on a 12 or 24-hour Operational Period.4

* **Mechanism:** Data Collection ![][image1] Analysis ![][image1] Strategy ![][image1] Resource Assignment ![][image1] IAP Production.  
* **Vulnerability:** **Plan-Tempo Mismatch.** This cycle assumes the hazard is relatively stable during the planning period. If the fire changes state every 30 minutes (e.g., Yarnell Hill thunderstorm outflow), the IAP becomes obsolete before it is distributed. The cognitive infrastructure forces the team to focus on "feeding the beast" (completing the ICS-204 forms) rather than observing the changing reality, creating a "bureaucratic blindness".3

### **2.2 Operational Uncertainty and Information Gaps**

**\[Inference\]** Uncertainty on the fireground manifests in distinct forms that degrade RPD and Planning differently:

1. **Missing Information:** "Where is the fire front?" (Yarnell Hill gap).21 This prevents RPD cue uptake.  
2. **Ambiguity:** "The siren is sounding." (Lahaina). Is it a Tsunami (run uphill) or Fire (stay out of smoke)?.22 This causes prototype confusion.  
3. **Equivocality:** "We need to clear the roads." Police define this as "block traffic to prevent looting/entry," while Fire defines this as "remove cars to allow egress.".23 This breaks the "Shared Mind" required for distributed cognition.

## ---

**3\. Taxonomy of Novelty Stressors**

**\[Inference\]** To understand "Black Swan" failure, we must move beyond the "Probability vs Consequence" matrix used in standard risk assessment. Instead, we propose a **"Novelty vs Coupling"** matrix. A true Black Swan in incident command is defined by the **unfamiliar coupling** of system components.

### **3.1 The Novelty Stressor Matrix**

| Stressor Type | Definition | Target of Cognitive Deformation | Case Example |
| :---- | :---- | :---- | :---- |
| **Hazard Novelty** | The physical threat behaves in a way that violates the commander's mental model of physics or historical precedence. | **Intelligence / Sensemaking:** RPD fails; prototypes do not match cues; "Stalling" or "Denial" occurs. | Pyro-cumulonimbus (fire clouds) generating their own lightning and erratic winds (Carr Fire, Black Summer). |
| **Scale Novelty** | The event exceeds resource capacity and span of control by orders of magnitude (10x, not 2x). | **Logistics / Span of Control:** Cognitive overload; "Span Breakers" fail; tracking systems collapse; "Task Shedding" at command level. | 2019/20 Black Summer Fires (AUS) burning 17M hectares simultaneously.24 |
| **Coupling Novelty** | Two distinct systems interact in unforeseen ways (e.g., Hurricane winds \+ Fire \+ Power Grid). | **Command / Planning:** Cross-domain expertise is missing; "stovepiped" mental models fail to predict cascades. | Lahaina 2023 (Hurricane Dora winds \+ Grass Fire \+ Power Failure).25 |
| **Infrastructure Failure** | The tools of cognition (radios, software, power) fail during the event. | **Ops / Comms:** Loss of "Shared Mind"; reversion to local, isolated sensemaking; disintegration of the IAP. | Portugal 2017 (SIRESP failure) 26; Lahaina Cell/Siren failure.23 |
| **Adversarial / Malicious** | Active interference or misinformation (cyberattack, terrorism) during response. | **Public Info / Intel:** Distrust of data inputs; paralysis of decision-making; "Verification Loops" slow down tempo. | Hypothetical Cyber-physical attack on water infrastructure during fire.27 |

### **3.2 Compound and Cascading Risks**

\*\*\*\* Pescaroli and Alexander distinguish between **"Compound Risks"** (coinciding events, e.g., Hurricane \+ Fire) and **"Cascading Disasters"** (causal chains).28

* **The Planning Blindspot:** The ICS Planning Section is typically linear and domain-specific ("Resources for Division A"). It is rarely staffed to model complex dependencies: "If Division A fails, does the water treatment plant lose power? If power is lost, does the water pressure drop for Division B?"  
* **Escalation Points:** These are the nodes where a secondary impact becomes larger than the trigger. Identifying these requires **System 2 thinking** (slow, analytical), which is often unavailable during the fast-paced "fog of war".30

## ---

**4\. Deformation and Failure Modes: The Catalog**

When the stressors of Section 3 impact the architecture of Section 1, the system does not just "break"; it deforms in specific, predictable patterns.

### **4.1 Sensemaking Collapse (The Mann Gulch Pattern)**

\*\*\*\* Defined by Karl Weick in his seminal analysis of the Mann Gulch fire, this occurs when the "Cosmology" (the deep understanding of how the universe works) breaks.

* **Early Signal:** "Vu jádé"—the feeling of "I’ve never been here before, I have no idea where I am, and I have no idea who can help me".2  
* **Mechanism:** The environment acts in a way that makes no sense (e.g., "The fire is acting like a fluid, not a fuel consumer"). The "Role System" (Leader, Subordinate) is the only thing holding the group together.  
* **Symptom:** Disintegration of the role system. When the leader orders an improvisation (e.g., lighting an escape fire), the crew views it as madness because it fits no prototype. "Drop your tools" (abandoning the identity of a firefighter) becomes the only survival option, yet many refuse because their identity is their only anchor.1

### **4.2 Plan-Tempo Mismatch (The Obsolete Map)**

**\[Inference\]** This is the bureaucratic failure mode. The organization persists in "feeding the Planning P" despite the cycle time being slower than the hazard's rate of change.

* **Mechanism:** The 12-hour operational period is too long. The IAP is published at 0600 based on data from 2000 the previous night. The fire changed direction at 0200\.  
* **Symptom:** Field operations ignore the IAP ("The paper plan"). A **"Shadow Plan"** emerges on the radio, undocumented and unvetted for safety.  
* **Safety Consequence:** The Safety Officer reviews the *paper plan* for risks, not the *shadow plan*. Hazards in the real plan go unmitigated.3

### **4.3 Comms as Incident (The Noise Bottleneck)**

**\[Case Evidence\]** In Yarnell Hill, radio communications were "brief, informal, and vague," leading to confusion about the crew's location.32

* **Mechanism:** Cognitive channel capacity is exceeded, or technical infrastructure fails (Portugal SIRESP).26  
* **Symptom:** "Frequency congestion." Critical safety traffic (Mayday) competes with logistical traffic (ordering lunch).  
* **Compensatory Behavior:** Crews stop transmitting to avoid the noise. "Silence" is misinterpreted by Command as "All is well," creating a **Common Operating Picture (COP) Illusion**.

### **4.4 Span Overload (The Saturation Point)**

\*\*\*\* NIMS sets span of control to protect attention.9

* **Mechanism:** A sudden expansion of the incident (Novelty of Scale) forces the IC to manage 15 divisions directly because the "Order" for a Type 1 Team hasn't been filled yet.  
* **Symptom:** **"Task Shedding."** The IC ignores long-term planning to focus on immediate tactical requests (tunnel vision). They regress from "Strategic" to "Tactical".33  
* **Safety Consequence:** No one is looking at the "Big Picture" (e.g., the weather front approaching in 2 hours).

### **4.5 Unified Command Friction (The Jurisdictional Seam)**

**\[Inference\]** Unified Command (UC) is the ICS solution to multi-agency events. However, it introduces negotiation costs.

* **Mechanism:** Different agencies bring different risk tolerances and cognitive models (e.g., Police: "Evacuate everyone now"; Fire: "Keep roads clear for engines").  
* **Symptom:** Delays in **"Command Intent."** The UC acts by committee, slowing the OODA loop (Observe-Orient-Decide-Act).  
* **Case Evidence:** In the 2003 Cedar Fire, resource orders were delayed due to jurisdictional confusion.34 In Lahaina, the lack of coordination between sirens (Emergency Management), police (traffic), and fire (suppression) created a fatal bottleneck.22

### **4.6 Cascading Failures (The Infrastructure Trap)**

\*\*\*\* This is the physical manifestation of "Coupling Novelty."

* **Mechanism:** Fire destroys the control mechanism for the fire (e.g., burns the repeater tower, melts the water pumps).  
* **Symptom:** The IC attempts to pull a lever (e.g., "Sound the sirens," "Call for air support") and the lever is disconnected.  
* **Cognitive Effect:** Confusion and Denial. "Why aren't they answering?" The commander wastes precious cognitive cycles debugging the tool rather than fighting the fire.

## ---

**5\. Case Anchors: Evidence of Deformation**

### **5.1 Deep Case: Yarnell Hill Fire (2013)**

**\[Case Evidence\]** The loss of 19 Granite Mountain Hotshots serves as a tragic exemplar of **Plan-Tempo Mismatch** and **Sensemaking Collapse** driven by **Hazard Novelty** (Thunderstorm Outflow).

* **Context:** The fire was burning in "doughnut hole" terrain with extreme drought conditions. A thunderstorm was approaching from the north, creating a gravity current.32  
* **Tempo Synchronization:** The fire transitioned from "fuel-driven" (topography dominant) to "wind-driven" (outflow dominant) in minutes. The crew's mental model (RPD) likely predicted a flank fire they could traverse to reach a safety zone. The **novelty** was the speed and direction shift caused by the outflow boundary. Their RPD library contained "thunderstorm," but likely lacked a prototype for "outflow boundary intersecting a box canyon with this specific fuel loading".35  
* **Shared Memory Externalization:** There was a critical 30-minute "gap" in communications. The "Shared Mind" of the Incident Command did not know where the crew was. The crew had left "the black" (safety) to move to a ranch (safety zone). This movement was not externalized on a map or confirmed via radio, meaning the IC had a **"Ghost Crew"** on their mental map—located where they *used* to be, not where they *were*.21  
* **Safety Invariants (LCES):**  
  * **L:** Lookouts were present but arguably compromised by the rapid smoke obscuration.  
  * **C:** Communications were vague/informal, failing to convey the urgency of the movement.  
  * **E:** Escape Route was cut off by the fire acceleration (Tempo mismatch).  
  * **S:** Safety Zone was never reached.

### **5.2 Light Case: Mann Gulch (1949)**

\*\*\*\* Weick’s analysis anchors the concept of **Sensemaking Collapse**.

* **The Novelty:** A blow-up in a "10:00 AM fire" (a fire expected to be contained by morning).  
* **The Collapse:** When Foreman Wagner Dodge lit an "escape fire" (a survival fire to burn out fuel), the crew did not recognize this innovation. It fell outside their RPD library. To them, the boss was "lighting a fire in the middle of a fire."  
* **Deformation:** The order "Drop your tools" was a violation of identity. Tools \= Firefighter. No Tools \= Runner. The organizational structure dissolved into panic.  
* **Insight:** Resilience (Dodge survived) came from **improvisation** (bricolage)—using the fire itself as a shield. The organization failed because it could not process the improvisation in real-time.1

### **5.3 Light Case: Lahaina / Maui (2023)**

**\[Case Evidence\]** An exemplar of **Coupling Novelty** and **Cascading Failure**.

* **Coupling:** Hurricane Dora (wind) \+ Drought (fuel) \+ Power Lines (ignition). This is a "Compound Risk".25  
* **Cascading Infrastructure Failure:** The winds knocked out power ![][image1] de-energized water pumps (loss of suppression pressure) ![][image1] knocked out cell towers (loss of public alert/comms).23  
* **Decision Deformation:** The decision *not* to sound sirens (fear of people running *mauka* into the fire) was an RPD error. The Administrator used a "Tsunami Prototype" for the sirens, fearing a wrong response, rather than an "All-Hazard Prototype." This illustrates how rigid mental models ("Sirens \= Tsunami") can be fatal in novel contexts.22

## ---

**6\. Resilience Upgrade Proposals**

To upgrade the cognitive infrastructure for novelty, we must move from "Hardening" (robustness) to "Flexibility" (resilience).

### **6.1 Organizational Design: The "Shadow Command" / Red Team**

**\[Inference\]** The primary failure in Yarnell and Lahaina was the lack of a "Challenge Function." The IC becomes locked into a single narrative.

* **Proposal:** Institutionalize a **"Red Team" Safety Officer** or "Strategic Advisor" (distinct from the operational Safety Officer).  
* **Function:** This role does *not* manage safety compliance (PPE, slips/trips). Instead, they are tasked with **"Pre-Mortem" thinking**. They continually ask: "If the wind shifts 90 degrees right now, does our plan kill someone?" "What information are we missing?".38  
* **Mapping:** *Monitor/Anticipate*. This introduces "Preoccupation with Failure" (HRO principle) into the org chart.40

### **6.2 Tech/Information: The Resilient COP (ATAK)**

**\[Inference\]** The "Ghost Crew" problem in Yarnell and the "Siloed Agencies" in Lahaina stem from disjointed mental maps.

* **Proposal:** Universal adoption of mesh-networked Common Operating Pictures like **ATAK (Android Team Awareness Kit)**.  
* **Function:** Real-time location tracking (blue force tracking) that functions peer-to-peer even when cell towers fail (using localized mesh or satellite links).41  
* **Cognitive Benefit:** Externalizes "Location" from verbal radio traffic to a visual display. Reduces cognitive load on the IC (don't have to ask "Where are you?"); reduces bandwidth congestion.  
* **Mapping:** *Respond/Monitor*.

### **6.3 Training: Decision-Making Under Novelty (Sand Tables)**

**\[Inference\]** You cannot RPD a situation you have never seen. We must expand the "Library of Prototypes."

* **Proposal:** Shift from "Procedural Training" (how to fill out an ICS-204) to **"Tactical Decision Games" (TDGS)** using Sand Tables.43  
* **Mechanism:** Present students with "impossible" novel scenarios (e.g., "The fire is now a hazmat incident and your radio is dead"). Force them to make decisions, then critique the *sensemaking process*, not just the tactic.  
* **Mapping:** *Learn/Anticipate*.

### **6.4 Governance: Cross-Agency "Meta-Scripting"**

**\[Inference\]** The friction in Lahaina (Police vs Fire) was a failure of inter-agency heuristics.

* **Proposal:** Establish **"Trigger-Point Governance."** Pre-agreed operational triggers that automatically shift authority. E.g., "If Wind \> 60mph AND Fire Detected, Evacuation Authority delegates immediately to On-Scene Police Commander, bypassing EOC."  
* **Mechanism:** Removes the negotiation latency of Unified Command during fast-moving cascades.  
* **Mapping:** *Anticipate/Respond*.

## ---

**Friction Log (Unresolved Tensions)**

* **Standardization vs. Improvisation:** The report advocates for "Standardization" (ICS structure) to reduce load, yet "Improvisation" (Mann Gulch bricolage) to survive novelty. These are fundamentally opposing forces. A system optimized for one is usually weak at the other. The "Red Team" proposal attempts to bridge this, but finding personnel capable of this high-level cognitive dissonance is a resource constraint.  
* **Unity of Command vs. Multi-Agency Reality:** Doctrine demands Unity of Command. Reality (Lahaina, Yarnell) demands multi-agency coordination where no single person *actually* has total authority. The friction of "Influence vs Authority" is unresolved in strict ICS doctrine.  
* **Tech Reliance vs. Tech Fragility:** We propose ATAK/Tech solutions, yet identifying "Infrastructure Failure" as a key stressor. There is a risk that reliance on ATAK makes the "analog fallback" skills atrophy, leading to a worse collapse if the mesh network fails.

## ---

**7\. Conclusions**

The cognitive infrastructure of ICS/AIIMS is a marvel of 20th-century organizational engineering, designed to tame the chaos of "Standard Disasters." However, under the pressure of **Novelty**—specifically the compound, cascading, and high-velocity events characteristic of the 21st-century climate—this infrastructure shows signs of metal fatigue.

The analysis of Yarnell Hill and Lahaina demonstrates that failure often stems not from "breaking the rules," but from **following rules that no longer map to the territory**. The **"Plan-Tempo Mismatch"** and the collapse of **"Sensemaking"** are the defining failure modes of our time.

To adapt, we must not discard ICS, but rather **upgrade its cognitive software**. We must move from a culture of "Compliance" (Did you fill out the form?) to a culture of "Sensemaking" (Does the form match the fire?). By integrating Red Teams, resilient sensing tech, and novelty-based training, we can build an Incident Command System that doesn't just manage the disaster, but learns faster than the disaster can evolve.

## ---

**Reflexive Check (Drift Score Analysis)**

* **Evidence Grounding (3/3):** High. Doctrinal sources (NIMS, AIIMS, IRPG) and investigation reports (Yarnell, Lahaina) are cited throughout.  
* **Novelty Sensitivity (3/3):** High. The definition of novelty moves beyond scale to include "Coupling" and "Infrastructure Failure," directly addressing the "Black Swan" requirement.  
* **Causal Humility (3/3):** High. The report acknowledges that single-cause explanations (e.g., "bad decision") are insufficient, highlighting system-level mismatches (Tempo, Plan).  
* **Cross-System Comparison (3/3):** High. Detailed contrast between ICS Planning and AIIMS Intelligence sections.  
* **Drift Score:** **0.5 (Low Drift)**. The report remains tightly focused on "Cognitive Infrastructure" and "Decision Making," avoiding generic "Firefighting tactics" or "Climate Change" platitudes.

#### **Works cited**

1. The Collapse of Sensemaking in Organizations: The Mann Gulch Disaster \- USDA Forest Service, accessed on February 3, 2026, [https://www.fs.usda.gov/t-d/pubs/htmlpubs/htm95512855/page18.htm](https://www.fs.usda.gov/t-d/pubs/htmlpubs/htm95512855/page18.htm)  
2. The Mann Gulch Disaster \- Louisiana Civil Service, accessed on February 3, 2026, [https://www.civilservice.louisiana.gov/files/divisions/training/Weick%20Collapse%20of%20Sensemaking.pdf](https://www.civilservice.louisiana.gov/files/divisions/training/Weick%20Collapse%20of%20Sensemaking.pdf)  
3. ICS and How it's Being Applied \- \#17 by IMT\_Geek \- General Discussion \- Wildfire Intel, accessed on February 3, 2026, [https://forums.wildfireintel.org/t/ics-and-how-its-being-applied/20277/17](https://forums.wildfireintel.org/t/ics-and-how-its-being-applied/20277/17)  
4. Incident Action Planning \- A Step-by-Step Process \- Domestic Preparedness, accessed on February 3, 2026, [https://www.domesticpreparedness.com/communication-interoperability/incident-action-planning-a-step-by-step-process/](https://www.domesticpreparedness.com/communication-interoperability/incident-action-planning-a-step-by-step-process/)  
5. An assessment of the opportunities to improve strategic decision-making in emergency and disaster management, accessed on February 3, 2026, [https://knowledge.aidr.org.au/resources/ajem-oct-2016-an-assessment-of-the-opportunities-to-improve-strategic-decision-making-in-emergency-and-disaster-management/](https://knowledge.aidr.org.au/resources/ajem-oct-2016-an-assessment-of-the-opportunities-to-improve-strategic-decision-making-in-emergency-and-disaster-management/)  
6. Professional Standard: Registered Intelligence Officer \- AFAC EMPS, accessed on February 3, 2026, [https://www.emps.org.au/wp-content/uploads/2022/03/EMPSProfStandard\_Registered\_Intelligence\_Officer\_2022.pdf](https://www.emps.org.au/wp-content/uploads/2022/03/EMPSProfStandard_Registered_Intelligence_Officer_2022.pdf)  
7. NIMS Components \- Guidance and Tools | FEMA.gov, accessed on February 3, 2026, [https://www.fema.gov/emergency-managers/nims/components](https://www.fema.gov/emergency-managers/nims/components)  
8. National Incident Management System \- FEMA Training, accessed on February 3, 2026, [https://training.fema.gov/emiweb/is/is700b/handouts/national\_incident\_management%20system\_third%20edition\_october\_2017.pdf](https://training.fema.gov/emiweb/is/is700b/handouts/national_incident_management%20system_third%20edition_october_2017.pdf)  
9. ICS Review Document | FEMA Training, accessed on February 3, 2026, [https://training.fema.gov/emiweb/is/icsresource/assets/ics%20review%20document.pdf](https://training.fema.gov/emiweb/is/icsresource/assets/ics%20review%20document.pdf)  
10. ICS Organizational Structure and Elements | FEMA Training, accessed on February 3, 2026, [https://training.fema.gov/emiweb/is/icsresource/assets/ics%20organizational%20structure%20and%20elements.pdf](https://training.fema.gov/emiweb/is/icsresource/assets/ics%20organizational%20structure%20and%20elements.pdf)  
11. Safety Officer, Field \- NWCG, accessed on February 3, 2026, [https://www.nwcg.gov/positions/safety-officer-field](https://www.nwcg.gov/positions/safety-officer-field)  
12. Hazard Mitigation Through Risk Management | NWCG, accessed on February 3, 2026, [https://www.nwcg.gov/6mfs/operational-engagement/hazard-mitigation-through-risk-management](https://www.nwcg.gov/6mfs/operational-engagement/hazard-mitigation-through-risk-management)  
13. 18 Watch Out Situations, PMS 118 \- NWCG, accessed on February 3, 2026, [https://www.nwcg.gov/publications/18-watch-out-situations-pms-118](https://www.nwcg.gov/publications/18-watch-out-situations-pms-118)  
14. 10 Standard Firefighting Orders, PMS 110 \- NWCG, accessed on February 3, 2026, [https://www.nwcg.gov/publications/pms110/10-standard-firefighting-orders-pms-110](https://www.nwcg.gov/publications/pms110/10-standard-firefighting-orders-pms-110)  
15. Summary of Changes to 2017 NIMS \- EMSI, accessed on February 3, 2026, [https://www.emsics.com/summary-changes-2017-nims/](https://www.emsics.com/summary-changes-2017-nims/)  
16. The Australasian Inter-service Incident Management System™ \- NatCORR, accessed on February 3, 2026, [https://natcorr.org.au/wp-content/uploads/2023/05/AIIMS-Manual-compressed.pdf](https://natcorr.org.au/wp-content/uploads/2023/05/AIIMS-Manual-compressed.pdf)  
17. National Incident Management System and Incident Command System | Division of Homeland Security and Emergency Services, accessed on February 3, 2026, [https://www.dhses.ny.gov/national-incident-management-system-and-incident-command-system](https://www.dhses.ny.gov/national-incident-management-system-and-incident-command-system)  
18. Recognition-Primed Decision Strategies: First-Year Interim Report \- DTIC, accessed on February 3, 2026, [https://apps.dtic.mil/sti/tr/pdf/ADA226887.pdf](https://apps.dtic.mil/sti/tr/pdf/ADA226887.pdf)  
19. Large-Scale Incident Decision Making for Incident Commanders in the Springfield Fire Department, accessed on February 3, 2026, [https://www.hsdl.org/c/view?docid=689926](https://www.hsdl.org/c/view?docid=689926)  
20. Applying the Principles of Command and Control to the Employment of Emergency Services in the Air Force \- National Fire Academy, accessed on February 3, 2026, [https://apps.usfa.fema.gov/pdf/efop/efo30298.pdf](https://apps.usfa.fema.gov/pdf/efop/efo30298.pdf)  
21. Interpreting the Yarnell Hill Report, accessed on February 3, 2026, [https://www.outsideonline.com/outdoor-adventure/environment/interpreting-yarnell-hill-report/](https://www.outsideonline.com/outdoor-adventure/environment/interpreting-yarnell-hill-report/)  
22. Maui emergency services head, who met criticism for not using sirens during wildfire, resigns \- PBS, accessed on February 3, 2026, [https://www.pbs.org/newshour/nation/maui-emergency-services-head-who-met-criticism-for-not-using-sirens-during-wildfire-resigns](https://www.pbs.org/newshour/nation/maui-emergency-services-head-who-met-criticism-for-not-using-sirens-during-wildfire-resigns)  
23. LAHAINA FIRE: The failure of fire, law enforcement, and other agencies at the 2023 Maui fires \- Wildfire Today, accessed on February 3, 2026, [https://wildfiretoday.com/lahaina-fire-the-failure-of-fire-law-enforcement-and-other-agencies-at-the-2023-maui-fires/](https://wildfiretoday.com/lahaina-fire-the-failure-of-fire-law-enforcement-and-other-agencies-at-the-2023-maui-fires/)  
24. Australia: Black Summer Bushfires 2019-2020 | IRP \- Recovery Collection, accessed on February 3, 2026, [https://recovery.preventionweb.net/collections/recovery-collection-australia-black-summer-bushfires-2019-2020](https://recovery.preventionweb.net/collections/recovery-collection-australia-black-summer-bushfires-2019-2020)  
25. Narrative analysis of wildfire disasters: A case study of Hawai'i's 2018 and 2023 fires, accessed on February 3, 2026, [https://www.preventionweb.net/news/narrative-analysis-wildfire-disasters-case-study-hawaiis-2018-and-2023-fires](https://www.preventionweb.net/news/narrative-analysis-wildfire-disasters-case-study-hawaiis-2018-and-2023-fires)  
26. The Impact on Structures of the Pedrógão Grande Fire Complex in June 2017 (Portugal), accessed on February 3, 2026, [https://www.mdpi.com/2571-6255/3/4/57](https://www.mdpi.com/2571-6255/3/4/57)  
27. Sensing and Sensemaking of Early Warning Signs of Cyber Disasters in the Information, accessed on February 3, 2026, [https://www.researchgate.net/publication/378436624\_Sensing\_and\_Sensemaking\_of\_Early\_Warning\_Signs\_of\_Cyber\_Disasters\_in\_the\_Information](https://www.researchgate.net/publication/378436624_Sensing_and_Sensemaking_of_Early_Warning_Signs_of_Cyber_Disasters_in_the_Information)  
28. Understanding Compound, Interconnected, Interacting and Cascading Risks: A Holistic Framework \- UCL Discovery, accessed on February 3, 2026, [https://discovery.ucl.ac.uk/10042515/1/Understanding%20Compound,%20Interconnected,%20Interacting%20Risk.pdf](https://discovery.ucl.ac.uk/10042515/1/Understanding%20Compound,%20Interconnected,%20Interacting%20Risk.pdf)  
29. Understanding and Managing Cascading Disasters A Framework for Analysis, accessed on February 3, 2026, [https://preparecenter.org/wp-content/uploads/2021/04/cascading-events-ppt-Alexander-David.pdf](https://preparecenter.org/wp-content/uploads/2021/04/cascading-events-ppt-Alexander-David.pdf)  
30. What are cascading disasters? | UCL Open Environment, accessed on February 3, 2026, [https://journals.uclpress.co.uk/ucloe/article/id/1994/](https://journals.uclpress.co.uk/ucloe/article/id/1994/)  
31. NWCG Incident Response Pocket Guide (IRPG), PMS 461 \- dnr.wa.gov, accessed on February 3, 2026, [https://dnr.wa.gov/sites/default/files/2025-05/rp\_cb\_incident\_response\_pocket\_guide.pdf](https://dnr.wa.gov/sites/default/files/2025-05/rp_cb_incident_response_pocket_guide.pdf)  
32. Yarnell Hill Fire: Serious Accident Investigation Report \- Homeland Security Digital Library, accessed on February 3, 2026, [https://www.hsdl.org/c/yarnell-hill-fire-serious-accident-investigation-report/](https://www.hsdl.org/c/yarnell-hill-fire-serious-accident-investigation-report/)  
33. Cognitive Overload: The Hidden Killer in Combat Systems \- Ambush, accessed on February 3, 2026, [https://www.getambush.com/article/cognitive-load-optimization-in-combat-systems/](https://www.getambush.com/article/cognitive-load-optimization-in-combat-systems/)  
34. From Forest Fires to Hurricane Katrina: Case Studies of Incident Command Systems \- IBM Center for The Business of Government |, accessed on February 3, 2026, [https://www.businessofgovernment.org/sites/default/files/MoynihanKatrina.pdf](https://www.businessofgovernment.org/sites/default/files/MoynihanKatrina.pdf)  
35. The Yarnell Hill Fire: A review of lessons learned, accessed on February 3, 2026, [https://www.iawfonline.org/article/the-yarnell-hill-fire-a-review-of-lessons-learned/](https://www.iawfonline.org/article/the-yarnell-hill-fire-a-review-of-lessons-learned/)  
36. Granite Mountain Hotshots: The firefighting team that died battling the Yarnell Hill Fire, accessed on February 3, 2026, [https://www.firerescue1.com/yarnell-hill/articles/granite-mountain-hotshots-the-firefighting-team-that-died-battling-the-yarnell-hill-fire-Ot1BJ3uUG8US1wkI/](https://www.firerescue1.com/yarnell-hill/articles/granite-mountain-hotshots-the-firefighting-team-that-died-battling-the-yarnell-hill-fire-Ot1BJ3uUG8US1wkI/)  
37. The Collapse of Sensemaking in Organizations: The Mann Gulch Disaster \- AWS, accessed on February 3, 2026, [https://lessonslearned-prod-media-bucket.s3.us-gov-west-1.amazonaws.com/s3fs-public/2023-02/TheCollapseofSensemakinginOrganizations.pdf](https://lessonslearned-prod-media-bucket.s3.us-gov-west-1.amazonaws.com/s3fs-public/2023-02/TheCollapseofSensemakinginOrganizations.pdf)  
38. How to Run Pre-Mortem Exercises \[Templates Included\] | Atlassian, accessed on February 3, 2026, [https://www.atlassian.com/team-playbook/plays/pre-mortem](https://www.atlassian.com/team-playbook/plays/pre-mortem)  
39. Enhancing Incident Management Team Participation and Effectiveness: Lessons from a Premortem Analysis of a Failed Future State \- Cogplexiti, accessed on February 3, 2026, [https://www.cogplexiti.com/enhancing-incident-management-team-participation-and-effectiveness-lessons-from-a-premortem-analysis-of-a-failed-future-state/](https://www.cogplexiti.com/enhancing-incident-management-team-participation-and-effectiveness-lessons-from-a-premortem-analysis-of-a-failed-future-state/)  
40. High Reliability Organizing: What It Is, Why It Works, How to Lead It \- National Interagency Fire Center, accessed on February 3, 2026, [https://www.nifc.gov/sites/default/files/blm/training/HRO\_2010training.pdf](https://www.nifc.gov/sites/default/files/blm/training/HRO_2010training.pdf)  
41. Wildland Fire \- Somewear Labs, accessed on February 3, 2026, [https://somewearlabs.com/wildland-fire/](https://somewearlabs.com/wildland-fire/)  
42. Hands-on ATAK, WinTAK, WebTAK, and iTAK \- CritComm Insights, accessed on February 3, 2026, [https://www.critcomminsights.com/analysis/2023/8/22/hands-on-tak](https://www.critcomminsights.com/analysis/2023/8/22/hands-on-tak)  
43. Delivering Tactical Decision Games Using Sand Table Exercises, PMS 468 | NWCG, accessed on February 3, 2026, [https://www.nwcg.gov/publications/pms468/delivering-tactical-decision-games-using-sand-table-exercises-pms-468](https://www.nwcg.gov/publications/pms468/delivering-tactical-decision-games-using-sand-table-exercises-pms-468)  
44. S 131 Unit 5 Decision Making \- NWCG, accessed on February 3, 2026, [https://www.nwcg.gov/training/courses/s-131-unit-5-decision-making](https://www.nwcg.gov/training/courses/s-131-unit-5-decision-making)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAARCAYAAAACCvahAAAAJ0lEQVR4XmNgGAWDE/xHFyAFUKQZBLAaABIkBZMF6K8RBCjSPFwAAL4GEe+FOvHOAAAAAElFTkSuQmCC>