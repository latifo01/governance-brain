Under **Article 14 of the [[EU AI Act]]**, **human oversight** is a mandatory requirement designed to ensure that **high-risk AI systems can be effectively supervised by real people (natural persons) during their operation**.

Its core goal is to prevent or minimize risks to **health, safety, and fundamental rights** by keeping humans in control of automated decision-making processes rather than treating AI outputs as unquestionable commands.

## 5 Core Capabilities Required for Human Overseers

Under Article 14(4), an AI system must be built so that the humans overseeing it are enabled to:
1. **Understand System Limitations:** Fully grasp the system's capabilities, limitations, and operational boundaries (detecting anomalies or performance degradation).
2. **Resist "Automation Bias":** Remain conscious of the human tendency to over-rely on automated outputs and actively question AI suggestions rather than rubber-stamping them.
3. **Correctly Interpret Outputs:** Accurately analyze the AI’s generated results, confidence metrics, or explanations using provided operational tools.
4. **Override or Disregard Decisions:** Possess both the technical ability and the organizational authority to disregard, reverse, or reject the AI's recommendations.
5. **Safely Halt the System:** Intervene at any point to stop system execution safely (e.g., triggering a emergency "stop" button or safe-state shutdown).

## Technical vs. Operational Implementation

Human oversight is a **shared responsibility** divided between system developers and system users:
- **Built-in by Design (Providers):** AI developers must design systems with appropriate **Human-Machine Interface (HMI)** tools. This includes building explainable AI (XAI) dashboards, confidence scoring displays, real-time alert systems, and override mechanisms into the product software before release.
- **Executed in Operation (Deployers):** Organizations using the high-risk AI system must assign oversight tasks to **qualified, trained individuals** who have the necessary competence, authority, and organizational backing to intervene when necessary.
    

## Common Oversight Models

Depending on the context and autonomy level of the AI, oversight usually falls into one of three design patterns:
- **Human-in-the-Loop (HITL):** The AI presents a recommendation, but a human **must review and approve** it before any final action or decision takes effect (e.g., an AI medical diagnostic tool recommending a treatment plan).
- **Human-on-the-Loop (HOTL):** The AI acts autonomously, but a human **monitors the operation in real-time** and holds the power to intervene or hit the stop button if errors occur (e.g., an automated industrial quality control line).
- **Human-in-Command (HIC):** A human oversees the broader strategic deployment, assessing systemic risks and deciding whether to deploy, pause, or decommission the AI system altogether.

> **Special Safeguard (Biometric Verification):** For certain critical use cases—such as post-remote biometric identification—Article 14(5) mandates enhanced oversight where **at least two independent natural persons** must separately verify the AI's identification result before any action can be taken.